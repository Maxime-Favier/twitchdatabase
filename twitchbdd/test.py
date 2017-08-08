import os

try:
    config = open("config/first-run.conf", "r")
except FileNotFoundError:
    print("s")