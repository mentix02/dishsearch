# DishSearch

A simple Django webapp to search for dishes from different restaurants. There is not fancy REST API or anything, it uses
good old Django templating for the frontend and plain Sqlite3 for the database.

## Demo

View a video [here](https://vimeo.com/838458453).

## Tech Stack

+ Backend
  - Django
  - Sqlite3
+ Frontend
  - Bootstrap 5

## Design

The project is quite basic in its implementation. The [`restaurant`](restaurant/) app contains a sole model `Restaurant` 
which is populated from the provided `restaurants_small.csv` file via the custom management command [`loadres`](restaurant/management/commands/loadres.py).

The [`dish`](dish/) app contains the `Dish` model with a custom (mostly convienience) manager `DishManager`.

This manager implements the `search` method to perform a native Sqlite3 full-text search on the `name` field of the
dishes. It also ranks the results based on the aggregated rating of the restaurant the dish belongs to.

The frontend is in plain old HTML5 with Bootstrap 5 for styling. You can search for dishes from any page via the navbar
and specifically from the home page. Pagination is implemented farily simply via the generic `ListView` class' built-in
`paginate_by` attribute and with some [custom clever template logic](dish/templatetags/paginator_tags.py) for eliding.

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
