from flask import Flask, render_template, abort, request, jsonify, g, flash
import sqlite3
import config
from contextlib import closing

app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('DC25_CONFIG',silent=True)

@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shortlist/', methods=['POST'])
def shortlist():
    email_address=request.form['email']
    g.db.execute('insert into waitlist (email) values (?)',
                 [email_address])
    g.db.commit()
    flash('New entry was successfully posted')
    return render_template('registered.html',email_address=email_address)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT,debug=config.DEBUG)


