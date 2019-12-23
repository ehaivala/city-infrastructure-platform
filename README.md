# City Infrastructure Platform

City Infrastructure Platform REST-API backend application.

## Development

### Install required system packages

#### PostgreSQL and PostGIS

Install PostgreSQL and PostGIS.

    # Ubuntu 16.04
    sudo apt-get install python3-dev libpq-dev postgresql postgis

#### GeoDjango extra packages

    # Ubuntu 16.04
    sudo apt-get install binutils libproj-dev gdal-bin

### Creating a Python virtualenv

Create a Python 3.x virtualenv either using the [`venv`](https://docs.python.org/3/library/venv.html) tool or using
the great [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) toolset. Assuming the latter,
once installed, simply do:

    mkvirtualenv -p /usr/bin/python3 city-infrastructure-platform

The virtualenv will automatically activate. To activate it in the future, just do:

    workon city-infrastructure-platform

### Creating and updating requirements

* Run `prequ update`

### Installing Python requirements

* Run `pip install -r requirements.txt`
* For development also run `pip install -r requirements-dev.txt`

### Prepare the database

Enable PostGIS extension for the default template

    sudo -u postgres psql -d template1 -c "CREATE EXTENSION IF NOT EXISTS postgis;"

Create user and database

    sudo -u postgres createuser -P -R -S city-infrastructure-platform  # use password `city-infrastructure-platform`
    sudo -u postgres createdb -O city-infrastructure-platform city-infrastructure-platform

Allow user to create test database

    sudo -u postgres psql -c "ALTER USER city-infrastructure-platform CREATEDB;"

### Django configuration

Environment variables are used to customize configuration in `city-infrastructure-platform/settings.py`. If you wish to override any
settings, you can place them in a local `.env` file which will automatically be sourced when Django imports
the settings file.

Copy .env.example file as .env: `cp .env.example .env`

### Running development environment

* Enable debug `echo 'DEBUG=True' >> .env`
* Run `python manage.py migrate`
* Run `python manage.py runserver 0.0.0.0:8000`
