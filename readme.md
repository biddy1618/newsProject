# Project "News Analysis"

## Project plan (alpha)
Part 1 - getting the data:
* Crawl news data from __inform.kz__
* * Set up a crawler to fetch the data and store in DB - later
* * * For now, simply crawl the data in a single thread
* * * Write crawler in paraller (4 threads) - later
* * * Think about efficient I/O operation for storing the crawled data - later
* Set up PostgreSQL DB for storing the links and articles - done
* * Create table for links, create table for articles

Part 2 - working over models:
* Run EDA, some ETL and build models. Candidate models:
* * Text Generation based on LSTM
* * Label prediction
* * Will see based on EDA
* Deploy the model locally
* * Set up SQL database for storing database (later)
* * Set up the server for serving the service (or website)
* Write tests
* * First tests - done
* Write logs for crawler
* * Start working on logging

The project will be run based on flask server. The server will act as a daemon for crawler fetching the web-data while computer is on.


## Crawler structure
* Crawler for the links
* Crawler of the articles

___

# Notes:

* URL encoding using `requests` library: - [link](https://2.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls)
* Python OOP best practices 2020 - [link](https://towardsdatascience.com/5-best-practices-for-professional-object-oriented-programming-in-python-20613e08baee)
* The try and except blocks are used to handle exceptions. The assert is used to ensure the conditions are compatible with the requirements of a function. - [link](https://towardsdatascience.com/practical-python-try-except-and-assert-7117355ccaab)
* Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors. The goal of using assertions is to let developers find the likely root cause of a bug more quickly. An assertion error should never be raised unless there’s a bug in your program. - [link](https://medium.com/@jadhavmanoj/python-what-is-raise-and-assert-statement-c3908697bc62)
* Python style guide - [link](https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names)


# Logs

## 13-06-2021
* First test for retrieving links
* Custom test for retrieving articles
* Articles data structure will include links, date, title, and tags

```
Traceback (most recent call last):
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 382, in _make_request
    self._validate_conn(conn)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 1010, in _validate_conn
    conn.connect()
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connection.py", line 411, in connect
    self.sock = ssl_wrap_socket(
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/util/ssl_.py", line 449, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/util/ssl_.py", line 493, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "/usr/lib/python3.8/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/usr/lib/python3.8/ssl.py", line 1040, in _create
    self.do_handshake()
  File "/usr/lib/python3.8/ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
OSError: [Errno 0] Error

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/util/retry.py", line 532, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/packages/six.py", line 769, in reraise
    raise value.with_traceback(tb)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 382, in _make_request
    self._validate_conn(conn)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 1010, in _validate_conn
    conn.connect()
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/connection.py", line 411, in connect
    self.sock = ssl_wrap_socket(
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/util/ssl_.py", line 449, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/urllib3/util/ssl_.py", line 493, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "/usr/lib/python3.8/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/usr/lib/python3.8/ssl.py", line 1040, in _create
    self.do_handshake()
  File "/usr/lib/python3.8/ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
urllib3.exceptions.ProtocolError: ('Connection aborted.', OSError(0, 'Error'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "main.py", line 90, in <module>
    article_test()
  File "main.py", line 42, in article_test
    response = requests.get(url)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/requests/api.py", line 76, in get
    return request('get', url, params=params, **kwargs)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/requests/sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/requests/sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "/home/biddy/Personal/projectNews/venv/lib/python3.8/site-packages/requests/adapters.py", line 498, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', OSError(0, 'Error'))
```