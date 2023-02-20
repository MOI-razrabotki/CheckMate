DEV = False

##### start: RPi development
if DEV:
    import sys
    import fake_rpi
    from fake_rpi import toggle_print
    toggle_print(False)

    sys.modules['RPi'] = fake_rpi.RPi # type: ignore
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # type: ignore
##### end: RPi development

import multiprocessing as mp
from time import (sleep as wait, time, perf_counter)
from typing import (Tuple, List, Union, Callable, Dict, Any, Optional)

from Mech.MechContainer import (MechContainer, StepMotor, Fan, Magnet, LED, Button, Switch)
from Mech.MechMotorPool import MechMotorPool
from Mech.MechDatatypes import *
from Mech.MechExceptions import *


class CM_Main_Pool_Controller(object):
    def __init__(self) -> None:
        c_pipe_remote, self.c_pipe = mp.Pipe()
        self.r_pipe, r_pipe_remote = mp.Pipe()
        self.run_lock = mp.Lock()

        self.mech_container = MechContainer(
                motors = (StepMotor(24, 23, (14, 15)), StepMotor(12, 25, (16, 20))),
                fan = Fan(19),
                magnet = Magnet(4),
                leds = (LED(17), LED(22), LED(27)),
                button = Button(13),
                switches = (Switch(5), Switch(6))
            )

        self.mech_pool = MechMotorPool(
                command_pipe = c_pipe_remote,
                results_pipe = r_pipe_remote,
                mech_container = self.mech_container,
                run_lock = self.run_lock
            )

        self.mech_pool.start()

        ping: float = self.ping()
        print(f"Ping: {perf_counter()-ping}")

        self.__wait_for_idle()

    def __del__(self) -> None:
        if self.mech_pool.is_alive():
            self.close()

    def get_value(self, val: MotorPool_Command_Val, c_id: Optional[str] = None) -> MotorPool_Command_Result:
        self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.GET_VALUE, val, c_id))

        self.r_pipe.poll(1)
        res: MotorPool_Command_Result = self.r_pipe.recv()
        return res

    def current_coords(self, c_id: Optional[str] = None) -> Tuple[Optional[int], Optional[int]]:
        res = self.get_value(MotorPool_Command_Val.COORDS, c_id)
        return res.arg

    def ping(self, c_id: Optional[str] = None) -> float:
        res = self.get_value(MotorPool_Command_Val.PING, c_id)
        return res.arg

    def pool_change_direction(self, direction: MotorPoolDirection, c_id: Optional[str] = None) -> None:
        self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.CHANGE_DIRECTION, direction, c_id))

    def pool_change_step_count(self, count: int, c_id: Optional[str] = None) -> None:
        self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.CHANGE_STEPS_SEQUENCE, count, c_id))

    def pool_change_step_type(self, step_type: MotorStepType, c_id: Optional[str] = None) -> None:
        self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.CHANGE_STEP_TYPE, step_type, c_id))

    def pool_change_step_delay(self, step_delay: float, c_id: Optional[str] = None) -> None:
        self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.CHANGE_STEP_DELAY, step_delay, c_id))

    def pool_run(self, c_id: Optional[str] = None) -> None:
        self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.RUN, command_id=c_id))

    def pool_stop(self, c_id: Optional[str] = None) -> None:
        self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.STOP, command_id=c_id))

    def pool_init(self, c_id: Optional[str] = None) -> None:
        self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.INIT, command_id=c_id))

    def magnet_turn(self, state: bool) -> None:
        self.mech_container.get_magnet.switch(state)

    def __send_cmd(self, cmd: MotorPool_Command_Sequence) -> None:
        self.c_pipe.send(cmd)

        ack = self.c_pipe.poll(1)
        try:
            if ack:
                res: MotorPool_Command_Response = self.c_pipe.recv()

                res_status: MotorPool_Command_Response_Type = res.status
                res_c_id: Optional[str] = res.command_id

                if res_status == MotorPool_Command_Response_Type.SUCCESS: pass
                elif res_status == MotorPool_Command_Response_Type.GOING_OUT_OF_BOUNDS: raise GoingOutOfBoundsException
                elif res_status == MotorPool_Command_Response_Type.POOL_INIT_IN_PROGRESS: raise PoolInitInProgressException
                elif res_status == MotorPool_Command_Response_Type.SEQUENCE_IS_RUNNING: raise PoolIsAlreadyRunningException
                elif res_status == MotorPool_Command_Response_Type.WRONG_DATA_EXCEPTION: raise PoolWrongDataPassed
                elif res_status == MotorPool_Command_Response_Type.UNKNOWN_COMMAND_EXCEPTION: raise PoolUnknownCommandPassed
                elif res_status == MotorPool_Command_Response_Type.UNKNOWN_VAL_EXCEPTION: raise PoolWrongValPassed
            else:
                raise NoResponseFromPool("Command not acknowledged after 1 second")
        except Exception as e:
            self.mech_container.get_magnet.switch(False)
            self.close()
            raise e

    def __wait_for_idle(self) -> None:
        __start = perf_counter()
        print(f"Frontend: Waiting for idle")
        self.run_lock.acquire()
        self.run_lock.release()
        print(f"Frontend: Idle received in {perf_counter() - __start}")

    def close(self) -> None:
        try:
            self.__send_cmd(MotorPool_Command_Sequence(MotorPool_Command_Body.QUIT_PROCESS))
            self.c_pipe.close()
            self.r_pipe.close()
            self.mech_pool.join()
        except (EOFError, OSError, BrokenPipeError):
            pass

    def yield_until_stopped(self, c_id: Optional[str] = None) -> None:
        while not self.get_value(MotorPool_Command_Val.VAL_STATE, c_id).arg == MotorPoolState.STOPPED: pass

    def yield_until_initted(self, c_id: Optional[str] = None) -> None:
        while not self.get_value(MotorPool_Command_Val.VAL_INITED, c_id).arg == PoolInitStatus.INITED: pass
