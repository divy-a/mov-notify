
from flask import Flask
import threading
import utils
import os
from dotenv import load_dotenv
load_dotenv()

movie_name = str(os.getenv('MOVIE_NAME', default=''))
route_id = str(os.getenv('RID', default=''))

app = Flask(__name__)

@app.route('/')
def index():
    return 'INDEX'

@app.route(f'/{route_id}')
def index():
    utils.ms(movie_name)
    return 'ROUTE', 200

if __name__ == '__main__':
    app.run()
