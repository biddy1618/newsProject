# Project "News Analysis"

## Project plan (alpha)
* Crawl news data from __inform.kz__
* * Set up a crawler to fetch the data and store in DB (later)
* Run EDA, some ETL and build models. Candidate models:
* * Text Generation based on LSTM
* * Label prediction
* * Will see based on EDA
* Deploy the model locally
* * Set up SQL database for storing database (later)
* * Set up the server for serving the service (or website)
* Write tests
* Write logs for crawler

The project will be run based on flask server. The server will act as a daemon for crawler fetching the web-data while computer is on.


## Crawler structure
* Crawler for the links
* Crawler of the articles

___

# Notes:

* URL encoding using `requests` librarys: - [link](https://2.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls)
* Python OOP best practices 2020 - [link](https://towardsdatascience.com/5-best-practices-for-professional-object-oriented-programming-in-python-20613e08baee)
* The try and except blocks are used to handle exceptions. The assert is used to ensure the conditions are compatible with the requirements of a function. - [link](https://towardsdatascience.com/practical-python-try-except-and-assert-7117355ccaab)
* Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors. The goal of using assertions is to let developers find the likely root cause of a bug more quickly. An assertion error should never be raised unless there’s a bug in your program. - [link](https://medium.com/@jadhavmanoj/python-what-is-raise-and-assert-statement-c3908697bc62)
