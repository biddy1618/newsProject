# Project "News Analysis"

## Project plan (alpha)
Part 2 - working over models:
* Run EDA, some ETL and build models. Candidate models:
* * Text Generation based on LSTM
* * Label prediction
* * Will see based on EDA
* Deploy the model locally
* * Set up the server for serving the service (or website)
* Write tests
* * First tests - done
* Write logs for crawler - done
* * Start working on logging - done

More on Part 2:


* Try different NLP approaches:
* * Why traditional approach - perform good enough in many tasks, less costly, combined with DL can give good results
* * Rule-based methods (traditional NLP)
* * Probabilistic modeling and machine learning (traditional NLP)
* * Deep Learning (modern approach)
* Text classification task
* * Prediction of tag
* * Prediction of sentiment
* Word sequences
* * POS tagging - incorporate into transformation using embeddings
* * Named entities - need to think
* * Semantic slot filling - we can use this for question transformation - [link](https://medium.com/koderunners/semantic-slot-filling-part-1-7982d786928e)
* Embeddings and topic models
* * Word embeddings
* * Sentence embeddings
* * Topic modeling
* Seq2Seq tasks
* * Fake data generation - maybe I should try using semantic retrieval for loss function
* * Machine translation

* Text normalization methods
* * Tokenization and lemmatization
* * Text into units by - BOW, TFIDF
* * Text into units by - word2vec, CNN for n-grams


* I was thinking a lot about where to start but couldn't come to specific decision. So I think it is better start with deduplication task (or retrieval of similar articles) based on __TF-IDF__. So, let's go ahead and start working on this shit.


## Launching jupyter lab with hidden files on
`jupyter lab --ContentsManager.allow_hidden=True`
___

# Project setup
The project directory will contain:
* `flaskr/`, a Python package containing your application code and files.
* `tests/`, a directory containing test modules.
* `venv/`, a Python virtual environment where Flask and other dependencies are installed.
* Installation files telling Python how to install your project.
* Version control config, such as git. You should make a habit of using some type of version control for all your projects, no matter the size.
* Any other project files you might add in the future.

Project layout:
```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

## Setup
The most straightforward way to create a Flask application is to create a global Flask instance directly at the top of your code, like how the “Hello, World!” example did on the previous page. While this is simple and useful in some cases, it can cause some tricky issues as the project grows.

Instead of creating a Flask instance globally, you will create it inside a function. This function is known as the application factory. Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.

The `__init__.py` serves double duty: it will contain the application factory, and it tells Python that the flaskr directory should be treated as a package.

`instance_relative_config=True` tells the app that configuration files are relative to the instance folder. The instance folder is located outside the  `flaskr` package and can hold local data that shouldn’t be committed to version control, such as configuration secrets and the database file.

Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the Jinja template library to render templates.

Global variables that are available within Jinja2 templates by default - [Standard Context](https://flask.palletsprojects.com/en/2.0.x/templating/#standard-context)

`session` vs `g` - [link](https://stackoverflow.com/questions/32909851/flask-session-vs-g/32910056) - `g` is specific to request, i.e. exists along full request cycle, and once the request is torn down, g is torn down as well, while session is browser specific, i.e. it persists across different requests for the same user. Use cases for `g`: 
* Set it up for `before_request` hook to add information for the this specific request.
* Get connection to database which is in the scope of request.
* `app.teardown_appcontext(function_to_call_when_returning_response)` - clear the database session when returning the response.

More on making project installable - [link to tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/install/)

More on flask context [here](https://testdriven.io/blog/flask-contexts/). So, basically, flask makes it look like some variables (like `request` variable in views) are accessible globally, but in reality flask uses contexts to make a number of objects "act" like globals only for the particular context (a thread, process, or coroutine) being used. In flask, this is called a [context-local](https://werkzeug.palletsprojects.com/en/1.0.x/local/). When a request is received, Flask provides two contexts:
* Application - keeps track of the application-level data - `current_app`, `g`
* Request - keeps track of the request-level data (URL, HTTP method, headers, request data, session info) - `request`, `session`.

__One thing to note is that application context is provided in a view function, or CLI command.__ Otherwise, one should use `app_context()` in a `with` block to have access to `current_app`.
From official documentation:
>The application context is created and destroyed as necessary. When a Flask application begins handling a request, it pushes an application context and a request context. When the request ends it pops the request context then the application context. Typically, an application context will have the same lifetime as a request. We also can register function in `app.teardown_appcontext` to be called when the application context ends (context is available by default in this function, so no need to wrap the function being registered within decorater `@with_appcontext`.)


# Notes:

* Python OOP best practices 2020 - [link](https://towardsdatascience.com/5-best-practices-for-professional-object-oriented-programming-in-python-20613e08baee)
* The try and except blocks are used to handle exceptions. The assert is used to ensure the conditions are compatible with the requirements of a function. - [link](https://towardsdatascience.com/practical-python-try-except-and-assert-7117355ccaab)
* Python’s assert statement is a debugging aid, not a mechanism for handling run-time errors. The goal of using assertions is to let developers find the likely root cause of a bug more quickly. An assertion error should never be raised unless there’s a bug in your program. - [link](https://medium.com/@jadhavmanoj/python-what-is-raise-and-assert-statement-c3908697bc62)
* Python style guide - [link](https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names)
* How to structure `Flask App` - [link](https://itnext.io/flask-project-structure-the-right-choice-to-start-4553740fad98)
* Guide to python packaging tool (for file `setup.py`) - [link](https://realpython.com/pipenv-guide/)
* Python relative path importing using `setup.py` - [link](https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder)
* Using SQLAlchemy with Flask, not Flask-SQLAlchemy - [link](https://towardsdatascience.com/use-flask-and-sqlalchemy-not-flask-sqlalchemy-5a64fafe22a4)
* Thread-local session SQLAlchemy - [link](https://docs.sqlalchemy.org/en/13/orm/contextual.html#unitofwork-contextual)
* SQLAlchemy session how-to - [link](https://docs.sqlalchemy.org/en/13/orm/session_basics.html#session-faq-whentocreate)
* SQLAlchemy different quering approaches - through explicit session object and through models - [link](https://stackoverflow.com/questions/12350807/whats-the-difference-between-model-query-and-session-querymodel-in-sqlalchemy/14553324#14553324)
* Scoped session vs local session - `This pattern allows disparate sections of the application to call upon a global scoped_session, so that all those areas may share the same session without the need to pass it explicitly. The Session we’ve established in our registry will remain, until we explicitly tell our registry to dispose of it, by calling scoped_session.remove()` - [link](https://docs.sqlalchemy.org/en/13/orm/contextual.html)
* Very interesting - basically, ORM operations should separate session and orm operations (doing ORM operations and then act upon session), but this way it is hard to catch any exception due, one way to handle this is to create a function separate for session operations, maybe later.
* TypeHinting and return type in case of error - what should I return with type hinting in case of exception with no case of raising exception?
* `logging` modular - [link](https://stackoverflow.com/questions/15727420/using-logging-in-multiple-modules), general tutorial on logging - [link](https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial)
* How to set up a production using application factory pattern and celery - [medium](https://towardsdatascience.com/how-to-set-up-a-production-grade-flask-application-using-application-factory-pattern-and-celery-90281349fb7a)
* Setting up global variables 
* * [link](https://www.reddit.com/r/learnpython/comments/85tj08/flask_global_variable/)
* * [link](https://stackoverflow.com/questions/35309042/python-how-to-set-global-variables-in-flask)
* * [link](https://stackoverflow.com/questions/32815451/are-global-variables-thread-safe-in-flask-how-do-i-share-data-between-requests)

# History of pip packages
```
pip install Flask
Collecting Flask
  Using cached Flask-2.0.1-py3-none-any.whl (94 kB)
Collecting itsdangerous>=2.0
  Using cached itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting click>=7.1.2
  Using cached click-8.0.1-py3-none-any.whl (97 kB)
Collecting Jinja2>=3.0
  Using cached Jinja2-3.0.1-py3-none-any.whl (133 kB)
Collecting Werkzeug>=2.0
  Using cached Werkzeug-2.0.1-py3-none-any.whl (288 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-2.0.1-cp38-cp38-manylinux2010_x86_64.whl (30 kB)

pip install pymystem3
Collecting pymystem3
  Using cached pymystem3-0.2.0-py3-none-any.whl (10 kB)
Collecting requests
  Using cached requests-2.26.0-py2.py3-none-any.whl (62 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2021.5.30-py2.py3-none-any.whl (145 kB)
Collecting idna<4,>=2.5; python_version >= "3"
  Using cached idna-3.2-py3-none-any.whl (59 kB)
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.6-py2.py3-none-any.whl (138 kB)
Collecting charset-normalizer~=2.0.0; python_version >= "3"
  Using cached charset_normalizer-2.0.4-py3-none-any.whl (36 kB)

pip install autocorrect
Processing /home/biddy/.cache/pip/wheels/da/03/6e/62a48359ab630e39939dbb392cc079923bb77664e97a47645d/autocorrect-2.5.0-py3-none-any.whl

pip install SQLAlchemy
Collecting SQLAlchemy
  Downloading SQLAlchemy-1.4.23-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.5 MB)
Collecting greenlet!=0.4.17; python_version >= "3" and platform_machine in "x86_64 X86_64 aarch64 AARCH64 ppc64le PPC64LE amd64 AMD64 win32 WIN32"
  Downloading greenlet-1.1.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (150 kB)

pip install dateparser
Collecting dateparser
  Using cached dateparser-1.0.0-py2.py3-none-any.whl (279 kB)
Collecting regex!=2019.02.19
  Downloading regex-2021.8.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (738 kB)
Collecting pytz
  Using cached pytz-2021.1-py2.py3-none-any.whl (510 kB)
Collecting tzlocal
  Downloading tzlocal-3.0-py3-none-any.whl (16 kB)
Collecting python-dateutil
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting backports.zoneinfo; python_version < "3.9"
  Downloading backports.zoneinfo-0.2.1-cp38-cp38-manylinux1_x86_64.whl (74 kB)
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)

pip install numpy
Collecting numpy
  Downloading numpy-1.21.2-cp38-cp38-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (15.8 MB)

pip install scikit-learn
Collecting scikit-learn
  Using cached scikit_learn-0.24.2-cp38-cp38-manylinux2010_x86_64.whl (24.9 MB)
Collecting threadpoolctl>=2.0.0
  Using cached threadpoolctl-2.2.0-py3-none-any.whl (12 kB)
Collecting scipy>=0.19.1
  Downloading scipy-1.7.1-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (28.4 MB)
Requirement already satisfied: numpy>=1.13.3 in ./venv/lib/python3.8/site-packages (from scikit-learn) (1.21.2)
Collecting joblib>=0.11
  Using cached joblib-1.0.1-py3-none-any.whl (303 kB)

pip install psycopg2-binary
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.4 MB)

pip install transliterate
Collecting transliterate
  Using cached transliterate-1.10.2-py2.py3-none-any.whl (45 kB)
```

# Docker

In order to create network, use following script: `docker network create --driver bridge --publish 5000:5000 flaskapp-net`.

To inspect the network, run `docker inspect flaskapp-net`.

First, run the postgres container on this network:
```
docker run --network flaskapp-net --name postgres --restart unless-stopped -d postgres
docker exec  postgres sh -c "psql -U postgres < setup.sql"
docker exec postgres sh -c "psql -U biddy projectnews < dump.bak"
```

Then run the flask application with DB url host as postgres in the config file:
```
docker run --name flaskapp --network flaskapp-net --restart unless-stopped -v $PWD/:/app/ -p 5000:5000 flaskapp
```



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

## 24-06-2021
* Writing ORM operations
* Got some ideas from Raushan on models
* * Tags retrieval based on NER extraction model from DeepPavlov
* * Article embeddings for finding similar (or identical) articles using some google shit
* * Fake article generation based on BERT-embeddings with attention

## 25-06-2021
* Fixed SQL query regarding the primary key set up - [link](https://stackoverflow.com/questions/64016778/better-to-use-serial-primary-key-or-generated-always-as-identity-for-primary-key)
* Next [link](https://www.postgresqltutorial.com/postgresql-identity-column/)
* ~~__TODO__~~: Couldn't find any instruction on how to implement identity (`generate as always`) column - [link](https://github.com/sqlalchemy/alembic/issues/775), thus temporarily using autoincrement -> Solved it by using self designed ORM including Identity feature, need expertise opinion on this
* ~~__TODO__~~: New identity column attribute works differently than expected, we can insert similar articles, need to debug.

## 26-06-2021
* Finally finished testing, now need to implement function that will flawlessly crawl the data and save to DB.

## 27-06-2021
* Function that will flawlessly crawl the website and save to DB is implemented (seemingly)
* Now need to leave the crawler active over night or day to crawl data for several years. Maybe should first test it for one year, we will see.

## 01-07-2021
* Still crawling, at the same time thinking on what kind of models I can deploy.
* Also fixed the some bug in `get_url` function

## 18-07-2021
* Been working on separating crawler and flask app. Also passed `Flask` tutorial. Been brainstorming regarding the front-end. Understood that I have no clue how front-end works, but decided that for my project it wouldn't be wise to study separate framework just for the sake of building front-end, thus decided I will use flask's own rendering features using Jinja's templating library, and also `js`-free `css` framework for beautifying the front-end.
* Stopped on __bulma css framework__ that just works.
* Plan for today is desing and implement following pages - _about_, _articles_, and _search_. I should also set up the logic behind the retieval (search), code the views.

## 18-07-2021
* Going through some _Bulma_ templates for better understanding the `css` hierarchy and structuring the elements.

## 20-07-2021
* Finished _about_ page, set up some addtional `js` code, fixed some basic configuration bugs. Digged a lot into _Bulma_'s examples and templates. Set up the contact view.

## 24-07-2021
* Setting up the search page
* Next I need to load pickle file one time, and access them in a thread-safe way (process-safe)

## 07-08-2021
* Finished search with TFIDF
* Finished download CV button
* Need to dockerize the project
* Need to improve the search input
* * Automatic error correction
* * Encode latin into russian and vice versa
* Added transliteration to russian and spell checking, but it could be definitely improved