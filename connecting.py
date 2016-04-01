from flask import g
import sqlite3

@app.before_request
def before_request():
    g.db = sqlite3.connect("books.db")