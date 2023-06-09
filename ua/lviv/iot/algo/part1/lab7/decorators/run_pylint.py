"""
Module for running pylint
"""
import os
import subprocess


def run_pylint(file_name):
    """
    Decorator for running pylint
    :type file_name: str
    :param file_name: The name of the file to run pylint on.
    :return: The decorated function.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            runner = f"pylint {os.path.abspath(file_name)}"
            subprocess.run(runner, shell=True, check=True)
            return func(*args, **kwargs)

        return wrapper

    return decorator
