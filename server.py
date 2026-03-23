# ============================================================
# RemoteBioUnlock - server.py
# This is the brain of the app. It listens for unlock requests
# from your phone, validates them, and unlocks your Windows PC.
# ============================================================

import json
import time
import hmac
import hashlib
import subprocess
import ctypes
import os
from flask import Flask, request, jsonify

# ============================================================
# Load configuration from config.json
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #searches for the config file where ever it is located, not just in the current working directory. "__file__" is a python var that allows this search.
CONFIG_PATH = os.path.join(BASE_DIR, 'config.json')

with open(CONFIG_PATH, 'r') as f: #loads the Json file and stores it in the "config" variable as a dictionary. The "with" statement ensures that the file is properly closed after reading, even if an error occurs. The R is for read only mode, which is the default mode for open() but is explicitly stated here for clarity and safety.
    config = json.load(f) #Python dictionary that contains the configuration settings for the RemoteBioUnlock application. It is loaded from a JSON file named "config.json" which contains secret key etc.

# Extract configuration values / setters from Json file
SECRET_KEY = config['secret_key'].encode('utf-8')
UNLOCK_PIN = config['unlock_pin']
PORT = config['port']
TOKEN_EXPIRY = config['token_expiry_seconds']

print("[RemoteBioUnlock] Configuration loaded successfully.")