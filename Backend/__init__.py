from flask import Flask


Backend = Flask(__name__)

from Backend import routes, models
