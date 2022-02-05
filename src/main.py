import threading;

from constants import ERR_MSG_MAP, MAX_THREAD_COUNT;
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
  
# initialIndex - index initially used for threads, like each thread starts with 0, 1, 2, 3, 5
# index - pointerIndex Array as defined in main function
# idArray - input id array
# result - result array
# errorIDs - Failed requestd IDs
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

  # IDs to fetch
  ids = getSampleInput(inputSize);
  print('Input IDs', ids);

  # As python shares object reference, pointer index is shared between threads
  # pointerIndex[0] => will hold index of the id that needs to be fetched after first five index
  # pointerIndex[1] => holds a boolean value indicating the first five index are fetched or not
  pointerIndex = [len(ids), True];
  
  # Fetch results for IDs
  result = [];

  # Failed requests along with error messages
  errorIDs = [];

  # threads that are used to fetch requests
  threads = [];
  threadsCount = len(ids);
  
  # Only if the input IDs are more than MAX_THREAD_COUNT allowed by server we need more thread else we only need len of input array 
  if(len(ids) > MAX_THREAD_COUNT):
    threadsCount = MAX_THREAD_COUNT;
    pointerIndex[0] = MAX_THREAD_COUNT - 1;


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

  

  