
from flask import Flask
import threading
import utils
import os
from dotenv import load_dotenv
load_dotenv()

movie_name = str(os.getenv('MOVIE_NAME', default=''))

threading.Thread(target=utils.keep_seaching,
                    args=(movie_name, 600,)).start()

app = Flask(__name__)

@app.route('/')
def index():
    return 'INDEX'

if __name__ == '__main__':
    app.run()
