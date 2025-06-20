import ctypes
from tools.keyLangList import *

def get_keyboard_language():
    """
    Gets the keyboard language in use by the current
    active window process.
    """

    languages = getLangList()

    user32 = ctypes.WinDLL('user32', use_last_error=True)

    handle = user32.GetForegroundWindow()

    threadid = user32.GetWindowThreadProcessId(handle, 0)

    layout_id = user32.GetKeyboardLayout(threadid)

    language_id = layout_id & (2 ** 16 - 1)

    language_id_hex = hex(language_id)

    if language_id_hex in languages.keys():
        return languages[language_id_hex]
    else:
        return str(language_id_hex)