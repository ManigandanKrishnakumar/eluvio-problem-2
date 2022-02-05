# eluvio-problem-2

Solution of the problem is based on multi threading, 

1. if the input ids are greater than 4 then we are creating 5 threads, start them parellely.
2. As soon as 1 request is complete the thread will move to the next unfetched ID.
3. In this way we keep all 5 threads working parellely and will work till all the IDs in the input array is fetched without getting 429 error from server, as the server is configured to handle 5 requests simultaneously.
4. In case of network error or any other error, the failed requests are stored in separate output array as errorIDs which then can be used for retrying.


To run the application:
1. In the root folder run the following commang
`python3 -m pip install -r requirements.txt`
2. Then traverse to src folder using `cd src`
3. Then run the main.py by  `python3 main.py`
4. The program will prompt you for entering the size of the input array enter any number, the getSampleInputs function will generate an array of inputs for the given size.
