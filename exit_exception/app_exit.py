"""Custom exception to call sys.exit from main"""


class AppExitError(Exception):
    """Class AppExitError
    Custom exception to call sys.exit from all menus exit points
    """
