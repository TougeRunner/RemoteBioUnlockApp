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

