"""
Module for logging exception
"""

import logging


def logged(exception, mode):
    """
    Decorator function that logs exceptions.

    Args:
        exception (Exception): The exception class to be caught.
        mode (str): The mode in which to log the exception. Either "file" or "console".

    Returns:
        function: The decorated function.

    Raises:
        Exception: If an invalid mode is provided.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "file":
                    logging.basicConfig(
                        filename="exception.log",
                        level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
                    logging.error(str(e))

                elif mode == "console":
                    logging.basicConfig(
                        level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
                    logging.error(str(e))
                else:
                    raise Exception("Wrong mode")
            return None

        return wrapper

    return decorator
