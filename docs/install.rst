Install
=======
This document describes steps required to make project run locally.

Project environment
-------------------
Before starting application itself you'll need to set up some dependencies in your environment.

PostgreSQL
~~~~~~~~~~
Installing PostgreSQL should be trivial for common operating systems. Below is a code snippet for MacOSX, assuming that
PostgreSQL was never installed on the machine and HomeBrew is available::

    brew install postgresql
    initdb /usr/local/var/postgres/
    createdb lifetech

Make sure that PostgreSQL can be accessed locally::

    $ psql -d lifetech
    psql (9.6.1)
    Type "help" for help.

    lifetech=#

Python environment
~~~~~~~~~~~~~~~~~~
This step may be optional if you already come up with Python environments management that works well for you. But it's
still here for the sake of completeness. **Whatever way to set up working environment you use make sure that there's a
proper isolation of packages in place. Pyenv, virtualenv, venv -- they all do good job.**

I find pyenv to be particularly useful for that task. Again, code snippet assuming MacOSX and HomeBrew::

    brew install pyenv-virtualenv
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
    source ~/.bash_profile
    pyenv install 3.5.2
    pyenv virtualenv 3.5.2 lifetech
    cd <ROOT OF THE PROJECT>
    pyenv local lifetech

That will create an environment with Python 3.5.2 and completely isolated set of packages.

GIT configuration
~~~~~~~~~~~~~~~~~
This project make use of git hooks to detect problems with code early, even before they reach CI server. In order to
configure these hooks as well as some other options regarding branch merging policies and so on it's **required** to
run script::

    utility/configure_repo

Application server
------------------

It's pretty simple for now::

    # from project's root directory
    pip install -r requirements/local.txt
    manage.py migrate

To run a basic check just run ``pytest``.

To start a server run ``./manage.py runserver_plus``. Usual ``./manage.py runserver`` will work too, but
``runserver_plus`` provides more convenient debugging.
