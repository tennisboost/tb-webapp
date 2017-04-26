# tb-webapp
Both frontend and backend combined into the web app portion of Tennisboost

Running on `python3`

Use `pip3 install -r requirements.txt` to install all packages into (preferably) a [virtualenv](https://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

## Setting up the database

You need to set up a postgres database. Use postgres.app as a GUI interface and click `start server`.

You then need to create the database:
`$ psql`
`# CREATE DATABASE tboost OWNER <your_username>`
(`$` and `#` denote terminal tags)

Ensure that your_username is also defined in models.py as the user you are connecting to.
