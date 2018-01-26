from flask import Flask
from .config import DevConfig

app =   Flask(__name__)

# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views