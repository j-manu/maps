Database

* Use the maps.sql file to create a postgresql database named maps with table Data

From the project directory

* Install pipenv `pip install --user pipenv`
* Install all required packages `pipenv install`
* Change the value of `KEY` variable in `fetch.py` to a valid google maps API KEY
* Change the places.txt file to add more origins and destinations. First value is origin, second is destination
and they are separated by a `:`
* Run the program `pipenv run python fetch.py`

