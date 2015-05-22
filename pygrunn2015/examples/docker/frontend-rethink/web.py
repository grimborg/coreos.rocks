import os

from flask import Flask
import rethinkdb as r
import json

app = Flask(__name__)

db_settings = {
    'host': os.environ['RETHINKDB_DRIVER_SERVICE_HOST'],
    'port': os.environ['RETHINKDB_DRIVER_SERVICE_PORT']
}

r.connect(db_settings['host'], db_settings['port']).repl()

@app.route("/")
def hello():
    values = [x for x in r.db('test').table('entries').run()]
    return "Connected to {db}. Found {values}".format(db=':'.join(db_settings.values()), values=json.dumps(values))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
