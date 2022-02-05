import base64;
import requests;
from constants import BASE_URL;

def getSampleInput(size):
  IDs = [];
  for i in range(1, size + 1):
    IDs.append(str(i));
  return IDs;

def getBase64String(str):
  stringBytes = str.encode("ascii");
  base64Bytes = base64.b64encode(stringBytes);
  return base64Bytes.decode("ascii");

def getAuthHeader(ID):
  authToken = getBase64String(ID);
  return {'Authorization' : authToken}

def fetchIdData(ID):
  authHeader = getAuthHeader(ID);
  r = requests.get(f'{BASE_URL}{ID}', 
                      headers = authHeader);
  return r;
