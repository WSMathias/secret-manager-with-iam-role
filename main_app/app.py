# #!/bin/env python
import time
import json
import os.path
from os import path
import os
import pprint


###########################################################

# try:
#     filePath = os.environ['SECRET_FILE_PATH']
# except:
#     filePath = "/tmp/from_env.env"

# def loadSecret():
#     print("Saving serects to ", filePath)
#     try:
#         secretFile = open(filePath,"w")
#         secretFile.write("export USERNAME="+"'"+ os.environ['USERNAME'] +"'"+ "\n")
#         secretFile.write("export PASSWORD="+"'"+  os.environ['PASSWORD'] +"'"+ "\n")
#         secretFile.write("export HOST="+"'"+  os.environ['HOST'] +"'"+ "\n")
#         secretFile.write("export PORT="+"'"+  os.environ['PORT'] +"'"+ "\n")
#         secretFile.close()
#     except:
#         print("Failed to wite to file")
#################################################

def printEnvs():
    env_var = os.environ
    print("User's Environment variable:")
    pprint.pprint(dict(env_var), width = 1)


while True:
    print("main app logs")
    printEnvs()
    # loadSecret()
    time.sleep(5)