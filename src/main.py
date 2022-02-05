import threading;

from constants import ERR_MSG_MAP;
from utils import getSampleInput, fetchIdData;


def storeResult(id, response, result, errorIDs):
  if(response.status_code == 200):
    result.append(response.text);
  else:
    failedID = {
      'id' : id,
      'errorMsg' : ERR_MSG_MAP[response.status_code],
    };
    errorIDs.append(failedID);
  

def requestData(initialIndex, index, idArray, result, errorIDs):
  if(index[0] >= len(idArray)):
    return;
  currentIndex = 0;
  if(index[1]):
    currentIndex = initialIndex;
  else:
    currentIndex = index[0];
  try:
    ID = idArray[currentIndex];
    r = fetchIdData(ID);
    storeResult(ID, r, result, errorIDs);
  except:
    errorIDs.append({
      'id' : ID,
       'errorMsg': 'Something went wrong please check the network connection'
    });
  finally:
     index[0] = index[0] + 1;
     index[1] = False;
     requestData(initialIndex, index, idArray, result, errorIDs);

  

def main():
  inputSize = int(input("Enter the size of the input arrays IDs to be generated : "));
  ids = getSampleInput(inputSize);
  print('Input IDs', ids);
  pointerIndex = [0, True];
  result = [];
  errorIDs = [];
  threads = [];
  threadsCount = 0;
  
  if(len(ids) > 5):
    threadsCount = 5;
    pointerIndex[0] = 4;
  else:
    threadsCount = len(ids);
    pointerIndex[0] = len(ids);

  for i in range(0, threadsCount):
    t = threading.Thread(target=requestData, args=[i, pointerIndex, ids, result, errorIDs]);
    threads.append(t);
    t.start();

  print('Loading...')

  for thread in threads:
    thread.join()

  print('----------- RESULT -----------');
  print(result)

  if(len(errorIDs) > 0):
    print('------------ ERRORS -----------')
    print(errorIDs)

main();

  

  