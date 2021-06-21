# Project "News Analysis"

## Project plan (alpha)
Part 1 - getting the data:
* Crawl news data from __inform.kz__
* * Set up a crawler to fetch the data and store in DB - later
* * * For now, simply crawl the data in a single thread
* * * Write crawler in paraller (4 threads) - later
* * * Think about efficient I/O operation for storing the crawled data - later
* Set up PostgreSQL DB for storing the links and articles - done
* * Set up tables and build ORM using sqlalchemy - done (need to test it)

Part 2 - working over models:
* Run EDA, some ETL and build models. Candidate models:
* * Text Generation based on LSTM
* * Label prediction
* * Will see based on EDA
* Deploy the model locally
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
* How to structure `Flask App` - [link](https://itnext.io/flask-project-structure-the-right-choice-to-start-4553740fad98)
* Guide to python packaging tool (for file `setup.py`) - [link](https://realpython.com/pipenv-guide/)
* Python relative path importing usint `setup.py` - [link](https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder)
* Using SQLAlchemy with Flask, not Flask-SQLAlchemy - [link](https://towardsdatascience.com/use-flask-and-sqlalchemy-not-flask-sqlalchemy-5a64fafe22a4)


# Logs

## 13-06-2021
* First test for retrieving links
* Custom test for retrieving articles
* Articles data structure will include links, date, title, and tags

## 15-06-2021
* Created ORM using sqlacodegen
* When parsing sometimes OSError is raised along with ConnectionError and ProtocolError
* * Should wrap the calls with try-except closure
* Implement corrrect way of making request using the same [session](https://docs.python-requests.org/en/master/user/advanced/) and maybe set up the [header values](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/)

## 16-06-2021
* Did modification to test crawling script
* Need to implement logging in try-except closure

## 19-06-2021
* Modified crawler
* Formatted code

## 21-06-2021
* Testing ORM
* TO-DO: write ORM operations for testing
* NOTE: I don't if additional class for `Base` is implemented correctly. Some expert opinion would be helpful.