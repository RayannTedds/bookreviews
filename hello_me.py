import os
import sqlite3
from flask import Flask, make_response, abort, redirect, g, render_template


app = Flask(__name__);

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recent.html')
def recent():
    return render_template('recent.html')
    
@app.route('/about-rayann.html')
def rayann():
    return render_template('about-rayann.html')
    
@app.route('/have-your-say.html')
def say():
    return render_template('have-your-say.html')

@app.route('/a-z.html')
def az():
    return render_template('a-z.html')

@app.before_request                     #to run a function before every request from the browser, getting the database
def before_request():
    g.db = sqlite3.connect("books.db")

@app.route('/gsaw.html')                                  #getting the query from the database for a specific page
def gsaw():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards  WHERE book.bookID=1000000 AND author.authorID=1 AND genre.genreID=1000 AND awards.awardGroupID='b'").fetchall()
    return render_template('book.html', cursor=cursor)
    
@app.route('/soh.html')                                  #getting the query from the database for a specific page
def soh():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000001 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/cft.html')                                  #getting the query from the database for a specific page
def cft():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000002 AND author.authorID=3 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)
    
def after_request(response):                    ##closing the database after each time
    g.db.close()
    return response

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)