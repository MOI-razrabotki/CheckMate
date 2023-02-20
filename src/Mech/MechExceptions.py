class NoResponseFromPool(Exception):
    """Exception when pool doesnt response"""
    pass


class GoingOutOfBoundsException(Exception):
    """Exception when motor is trying to get out of bounds"""
    pass


class PoolIsAlreadyRunningException(Exception):
    """Exception when pool is already running"""
    pass


class PoolInitInProgressException(Exception):
    """Exception when pool init is in progress"""
    pass


class PoolWrongDataPassed(Exception):
    """Exception when wrong data is passed to command sequence"""
    pass


class PoolWrongValPassed(Exception):
    """Exception when wrong val is passed to command sequence"""
    pass


class PoolUnknownCommandPassed(Exception):
    """Exception when unknown command is passed to command sequence"""
    pass
