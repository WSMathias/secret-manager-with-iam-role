# !/bin/env python
import json
import boto3
import base64
import os.path
from os import path
from botocore.exceptions import ClientError

def getSecretKeys():
    secretKeys = dict()
    for (key, value) in os.environ.items():
        if( key.startswith("SM_")):
            secretKeys[key] = value
    if(bool(secretKeys)):
        return secretKeys
    else:
        raise ValueError("Secret manager Key not found")

def getSecretFileName():
    secretFile = os.environ["SECRET_FILE_PATH"]
    return secretFile

def get_secret(secret_name):
    region_name = "ap-southeast-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return decoded_binary_secret

def loadSecret(prefix, secret_name, secretFile):
    print("Saving", secret_name, "serects to", secretFile)
    data=get_secret(secret_name)
    secret = json.loads(data)
    secretFile.write("export " + prefix + "USERNAME="+"'"+ secret["username"]+"'"+ "\n")
    secretFile.write("export " + prefix + "PASSWORD="+"'"+  secret["password"]+"'"+ "\n")
    secretFile.write("export " + prefix + "HOST="+"'"+  secret["host"]+"'"+ "\n")
    secretFile.write("export " + prefix + "PORT="+"'"+  str(secret["port"])+"'"+ "\n")
    print("Done fetching ", secret_name)


print("Running init container script")
allSecrets = getSecretKeys()
secretFileName = getSecretFileName()
secretFile = open(secretFileName,"w")
try:
    for (key, secret_name) in allSecrets.items():
        prefix = key.split("_")[1]
        loadSecret(prefix, secret_name, secretFile)
finally:
    secretFile.close()
    print("exiting init container script")