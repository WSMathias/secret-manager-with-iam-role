# #!/bin/env python
import time
import json
import os.path
from os import path
import os
import pprint

def printEnvs():
    env_var = os.environ
    print("User's Environment variable:")
    pprint.pprint(dict(env_var), width = 1)


while True:
    print("main app logs")
    printEnvs()
    time.sleep(5)