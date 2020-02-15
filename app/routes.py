from app import app
from markdown import markdown
from flask import render_template, render_template_string, request, session, flash, url_for, redirect
from app.blog_helpers import render_markdown,render_my_html
import os
from os import walk
import flask

app.secret_key = "bhbfbdbiefbefrfyrtygb"


#home page
@app.route("/")
def home():
    return render_markdown('index.md')

@app.route("/all")
def all():
    view_data = {}
    view_data['pages']=[]
    

    for(dirpath, dirnames, filenames) in walk(r'C:\Users\David Uribe\Desktop\flask1.0\flaskwebapp\app\templates'):
        for file in filenames:
         view_data["pages"].append(file.rsplit(".",1)[0])
       

    return render_template("all.html",data=view_data)        

@app.route("/edit/<page_name>")
def edit(page_name):

    html = render_my_html(page_name+'.html')
  
    

    return render_template('edit.html',page_name = html)





    

@app.route("/favicon.ico")
def favicon():
    return ""

@app.route('/login', methods=['GET','POST'])
def login():
        
        error = ""
        if request.method == 'POST':
            if request.form['user_name'] != 'du13' or request.form['password'] != 'hello123' :
                error = 'Username or password is incorrect, try again please.'
            else:
                session['logged_in'] = True
                return redirect(url_for('home'))
            
        
        return render_template("login.html",error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route("/<view_name>")

#input parameter name must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.md')
    view_data = {} #create empty dictionary
    return render_template_string(html, view_data = session)