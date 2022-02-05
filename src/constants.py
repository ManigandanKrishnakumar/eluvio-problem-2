BASE_URL = 'https://challenges.qluv.io/items/';

ERR_MSG_MAP = {
  401 : 'Invalid Authorization Header',
  404 : 'Invalid URL',
  500 : 'Something went wrong, Internal Server Error',
};

# We are keeping the max thread count in constant because it can be easy to modify if server is configured to handle different number of requests simultaneously
MAX_THREAD_COUNT = 5;