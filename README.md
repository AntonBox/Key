# Project Django Shop

## Prerequisites

- Python 3.5
- pip
- virtualenv (or pew)(I`m using pew https://github.com/berdario/pew) 
- PostgreSQL

## Installation

### 1. Create virtualenv

#### If you are using pew:

```
    pew new -p python3.5 keyua
    pew workon keyua
```


### 2. Install dependencies

#### Install neccessary *-dev packages::

```
    sudo apt-get install python3-dev
```

```

#### Django dependencies:

```
    pip install -r requirements-dev.txt
```


### 3. Database:

#### Install PostgreSQL.

#### Create database:

```
    sudo -i -u postgres
    createuser keyua -P
    createdb keyua -O keyua
    exit
```

#### Migrate database:

```
    python manage.py migrate
```


### 4. Run project:
```
    python manage.py createsuperuser


    make run(dont forget to login in admin panel)
```
