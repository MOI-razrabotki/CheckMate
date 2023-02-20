from dataclasses import dataclass
from enum import (Enum, auto)
from typing import (Tuple, List, Union, Callable, Dict, Any, Optional)


class MotorStepType(Enum):
    #// _1_1 = 1.0
    _1_2 = .5
    _1_4 = .25
    _1_8 = .125
    _1_16 = .0625


class MotorId(Enum):
    LEFT = ("left")
    RIGHT = ("right")
    BOTH = ("left", "right")


class MotorDirection(Enum):
    CLOCKWISE = True
    ANTICLOCKWISE = False


class MotorPoolDirection(Enum):
    """ As clock: x+ goes at 3, y+ goes at 12 """
    _12 = auto()
    """ y+ """
    _1_2 = auto()

    _3 = auto()
    """ x+ """
    _4_5 = auto()
    
    _6 = auto()
    """ y- """
    _7_8 = auto()

    _9 = auto()
    """ x- """
    _10_11 = auto()


class MotorState(Enum):
    RUNNING = True
    STOPPED = False


@dataclass
class MotorData:
    motor_id: MotorId
    state: MotorState = MotorState.STOPPED
    """ Current motor state"""
    direction: MotorDirection = MotorDirection.CLOCKWISE
    """ Motor's direction"""


class MotorPoolState(Enum):
    RUNNING = True
    STOPPED = False


@dataclass
class MotorPoolData:
    step_type: MotorStepType = MotorStepType._1_2
    """ Motor's step type"""
    steps_sequence: int = 0
    """ Number of steps sequence to execute"""
    step_delay: float = 0.001
    """ Delay until the next step"""
    direction: MotorPoolDirection = MotorPoolDirection._6
    """ Motor pool direction"""


class MotorPool_Command_Body(Enum):
    CHANGE_DIRECTION = auto()
    CHANGE_STEP_TYPE = auto()
    CHANGE_STEPS_SEQUENCE = auto()
    CHANGE_STEP_DELAY = auto()
    GET_VALUE = auto()

    RUN = auto()
    STOP = auto()

    INIT = auto()

    QUIT_PROCESS = auto()


class MotorPool_Command_Val(Enum):
    VAL_STATE = auto()
    VAL_INITED = auto()
    VAL_DIRECTION = auto()
    VAL_STEP_TYPE = auto()
    VAL_STEPS_SEQUENCE = auto()
    VAL_STEP_DELAY = auto()
    
    COORDS = auto()
    PING = auto()


class PoolInitStatus(Enum):
    NOT_INITED = auto()
    INIT_IN_PROGRESS = auto()
    INITED = auto()


class MotorPool_Command_Response_Type(Enum):
    """ Enum passed from pool to controller to resolve command pass status"""
    SUCCESS = auto()

    WRONG_DATA_EXCEPTION = auto()
    UNKNOWN_COMMAND_EXCEPTION = auto()
    UNKNOWN_VAL_EXCEPTION = auto() 

    SEQUENCE_IS_RUNNING = auto()
    GOING_OUT_OF_BOUNDS = auto()
    POOL_INIT_IN_PROGRESS = auto()


@dataclass
class MotorPool_Command_Sequence(object):
    """ Object passed from controller to pool"""
    body: MotorPool_Command_Body
    arg: Any = None
    #// motor_id: Optional[MotorId] = None

    command_id: Optional[str] = None
    """ For debugging purposes"""


@dataclass
class MotorPool_Command_Response(object):
    """ Object passed from pool to controller to indicate command execution status"""
    status: MotorPool_Command_Response_Type

    command_id: Optional[str] = None
    """ For debugging purposes"""


@dataclass
class MotorPool_Command_Result(object):
    """ Object passed from pool to controller to indicate command execution result"""
    arg: Any
    #// motor_id: Optional[MotorId] = None

    command_id: Optional[str] = None
    """ For debugging purposes"""
