# what is this

* hacking on an interview problem

# how to run

* have Python 3+ install
* create project directory and `cd` into project
* create virtual environment: `python3 -m venv venv`
* activate virtual environment: `source venv/bin/activate`
* install dependencies: `make install`
* run app: `make run`

# log book

* scaffold project: grab Makefile that from [my boilerplate](https://github.com/zachvalenta/create-python-app) and strip it down to bare essentials, grab another Makefile rule from [another Flask project I have going](https://github.com/zachvalenta/book-db) 
* follow Flask [docs for file upload](http://flask.pocoo.org/docs/1.0/patterns/fileuploads/), work through error by adding last function from docs `uploaded_file`
* use python-dotenv to load `.env` to use Flask message flashing, extract template from view
