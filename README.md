# Disinfo-digest
The project is based on a script that downloads links to articles from RSS feeds of trusted sources and filters news primarily about disinformation.

A web application created with Flask then displays these articles and allows for easy searching within them.
## Setup
1. Install requirements
```commandline
pip install -r requirements.txt
```

2. Rename `.env.sample` to `.env` and fill in the necessary data

3. init db
```commandline
flask init_dby
```

4. run app
```commandline 
flask run
```

5. set up your CRON/scheduler to automatically call the `mediacheck.py` script
```commandline
python mediacheck.py
```


## Other Notes
Searching the database is case-insensitive and diacritic-insensitive. To enable this feature, you need to install the unaccent extension in your database:
```
CREATE EXTENSION unaccent;
```