from flask import Flask
app = Flask(__name__)
from app import routes

# routes is a separate module
# the routes are the different URLs that the application implements
# handlers for the routes are written as functions in python
# these are view functions
