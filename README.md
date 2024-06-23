# Disinfo-digest
The project is based on a script that downloads links to articles from RSS feeds of trusted sources and filters news primarily about disinformation.

A web application created with Flask then displays these articles and allows for easy searching within them.
## Setup
1. Install requirements
```commandline
pip install -r requirements.txt
```
2. init db
```commandline
flask init_db.py
```

3. run app
```commandline 
flask run
```

4. set up your CRON/scheduler to automatically call the `mediacheck.py` script
```commandline
python mediacheck.py
```