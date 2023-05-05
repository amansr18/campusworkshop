"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa4kqk728r8861mhh0-a.oregon-postgres.render.com",
        database="todo_wi5o",
        user="todo_wi5o_user",
        password="X8b66Pf0FOznTToF1K9WTjft1txnIZm3")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
#hello
from app import routes
