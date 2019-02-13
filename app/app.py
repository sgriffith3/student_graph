import os
from flask import Flask
from app.config import config

here = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_folder=os.path.join(here, 'static'),
            static_url_path='/static',
            template_folder=os.path.join(here, 'templates'))

#TODO Accept Posts On Flask Call!!!