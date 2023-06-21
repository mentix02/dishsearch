# DishSearch

A simple Django webapp to search for dishes from different restaurants. There is not fancy REST API or anything, it uses
good old Django templating for the frontend and plain Sqlite3 for the database.

## Installation

Fairly straightforward process.

### Setup

```bash
$ git clone https://github.com/mentix02/dishsearch.git && cd dishsearch
$ virtualenv env && source env/bin/activate
$ pip install -r requirements.txt
```

### Populate Database (optional)

If you wish to use the provided, Sqlite3 database, you can skip the next step. Or if you wish to populate the database
fresh with the provided `restaurants_small.csv` file, you can run the custom management command [`loadres`](restaurant/management/commands/loadres.py).

**Note - this might take some time.**

```bash
$ rm db.sqlite3 # remove old database
$ python manage.py migrate # create new database
$ python manage.py loadres restaurants_small.csv # populate database
```

### Serve

```bash
$ python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) to view the app.
