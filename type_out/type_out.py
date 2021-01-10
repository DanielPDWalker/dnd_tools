import sys
import time


class KeyboardDisable():
    """Makes an object with which you can disable keyboard input."""

    def __init__(self):
        self.on = False
        import msvcrt

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self):
        while self.on:
            msvcrt.getwch()


def type_out(text):
    """First disables keyboard input then prints out the passed
    text's characters over time in the console/terminal window.
    """
    disable_typing.start()
    text = text + "\n"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    disable_typing.stop()


def check_input(saved_input):
    """Checks for yes and no awnsers from the user."""
    if saved_input.lower() == "!yes" or "!y":
        return True
    if saved_input.lower() == "!no" or "!n":
        return False


def restart_or_quit(saved_input):
    """Check if the user has input the restart or quit command."""
    if saved_input.lower() == "!restart":
        menu()
    if saved_input.lower() == "!quit":
        exit()
    return True


DISABLE_TYPING = KeyboardDisable()
