"""
    User input handling.
"""
import sys, time


def get_input(string: str, valid_options: list) -> str:
    """
        Deals with error checking for inputs
    """

    # This is just a bit cleaner
    user_input = input(string)

    while user_input not in valid_options:
        user_input = input(string)
    
    return user_input


def print_text(text: str, sleep_time: float = 0.0) -> None:
    """
        Prints the text to the console character by character. RPG style.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.021)
    if sleep_time != 0.0:
        time.sleep(sleep_time)