import os
import sqlite3
from flask import Flask, make_response, abort, redirect, g, render_template, request, flash, url_for
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()
app = Flask(__name__)

app.secret_key='2801development1996key'

app.config.update(
    DEBUG=True,
    MAIL_SERVER='mail.tidbury.xyz',
    MAIL_PORT=26,
    MAIL_USE_SSL=False,
    MAIL_USERNAME = 'rayann@tidbury.xyz',
    MAIL_PASSWORD = 'rayanntedds123',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recent.html')
def recent():
    return render_template('recent.html')
    
@app.route('/about-rayann.html')
def rayann():
    return render_template('about-rayann.html')

@app.route('/a-z.html')
def az():
    return render_template('a-z.html')

@app.route('/comments.html', methods=['GET','POST'])
def contact():
    form = ContactForm()
    
    if request.method == 'POST':
        if form.validate() == False:
            flash('Please fill all the boxes!')
            return render_template('comments.html', form=form)
        else:
            msg = Message(form.bookname.data, sender='rayann@reviews.com', recipients=[form.email.data])
            msg.body = "Hello %s, \n\n Thank you for your recent view on my website. Keep an eye out to see if it appears on the site! \n Your review/comment is shown below: \n\n Reviewed book: %s\n %s\n\nRegards,\nRayann """%(form.name.data, form.bookname.data, form.message.data)
            mail.send(msg)
            msg = Message('New Review!', sender='rayann@reviews.com', recipients=['teddsy2801@hotmail.co.uk'])
            msg.body = "A new review has been submitted, the details are below: \n\n Name: %s \n Book associated: %s \n Comment: %s"""%(form.name.data, form.bookname.data, form.message.data)
            mail.send(msg)
            return render_template('comments.html', form=form)

    elif request.method == 'GET':
        return render_template('comments.html', form=form)

@app.route('/have-your-say.html')
def say():
    return render_template('have-your-say.html')

@app.route('/templates/modal.html')
def mod():
    return render_template('modal.html')

@app.before_request                     #to run a function before every request from the browser, getting the database
def before_request():
    g.db = sqlite3.connect("books.db")

@app.route('/gsaw.html')                                  #getting the query from the database for a specific page
def gsaw():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards  WHERE bookID=1000000 AND author.authorID=1 AND genre.genreID=1000 AND awards.awardGroupID='b'").fetchall()
    return render_template('book.html', cursor=cursor)
    
@app.route('/soh.html')                                  #getting the query from the database for a specific page
def soh():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000001 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/tkr.html')                                  #getting the query from the database for a specific page
def tkr():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000002 AND author.authorID=4 AND genre.genreID=1002 AND awards.awardGroupID='c'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/cft.html')                                  #getting the query from the database for a specific page
def cft():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000003 AND author.authorID=3 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/tgg.html')                                  #getting the query from the database for a specific page
def tgg():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000004 AND author.authorID=5 AND genre.genreID=1003 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/tswk.html')                                  #getting the query from the database for a specific page
def tswk():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000005 AND author.authorID=6 AND genre.genreID=1000 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/aad.html')                                  #getting the query from the database for a specific page
def aad():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000007 AND author.authorID=8 AND genre.genreID=1005 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/tdvc.html')                                  #getting the query from the database for a specific page
def tdvc():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000008 AND author.authorID=8 AND genre.genreID=1005 AND awards.awardGroupID='d'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/tls.html')                                  #getting the query from the database for a specific page
def tls():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000009 AND author.authorID=8 AND genre.genreID=1005 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/i.html')                                  #getting the query from the database for a specific page
def i():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000010 AND author.authorID=8 AND genre.genreID=1005 AND awards.awardGroupID='e'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/dp.html')                                  #getting the query from the database for a specific page
def dp():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000011 AND author.authorID=8 AND genre.genreID=1005 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/tsdoas.html')                                  #getting the query from the database for a specific page
def tsdoas():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000012 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)
    
@app.route('/sa.html')                                  #getting the query from the database for a specific page
def sa():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000013 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)
    
@app.route('/sttk.html')                                  #getting the query from the database for a specific page
def sttk():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000014 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)
    
@app.route('/sas.html')                                  #getting the query from the database for a specific page
def sas():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000015 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/sab.html')                                  #getting the query from the database for a specific page
def sab():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000016 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/ms.html')                                  #getting the query from the database for a specific page
def ms():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000017 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/stts.html')                                  #getting the query from the database for a specific page
def stts():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000018 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)
    
@app.route('/cykas.html')                                  #getting the query from the database for a specific page
def cykas():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000019 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='f'").fetchall()
    return render_template('book.html', cursor=cursor)
    
@app.route('/tug.html')                                  #getting the query from the database for a specific page
def tug():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000020 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)
    
@app.route('/rm.html')                                  #getting the query from the database for a specific page
def rm():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000021 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/tg.html')                                  #getting the query from the database for a specific page
def tg():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000022 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/wn.html')                                  #getting the query from the database for a specific page
def wn():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards WHERE bookID=1000023 AND author.authorID=2 AND genre.genreID=1001 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)

@app.route('/jf.html')                                  #getting the query from the database for a specific page
def jf():
    cursor = g.db.execute("SELECT * FROM book NATURAL  JOIN author, genre, awards  WHERE bookID=1000006 AND author.authorID=7 AND genre.genreID=1004 AND awards.awardGroupID='a'").fetchall()
    return render_template('book.html', cursor=cursor)
    
def after_request(response):                    ##closing the database after each time
    g.db.close()
    return response

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)