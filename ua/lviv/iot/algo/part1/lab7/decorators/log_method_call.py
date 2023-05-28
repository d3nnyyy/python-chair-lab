"""
Module contains decorator for logging method call.
"""


def log_method_call(func):
    """
    Decorator for logging method call.
    :type func: function
    :param func: The function to decorate.
    :return: The decorated function.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
