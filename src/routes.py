from flask import render_template
from flask import request
from src import app
from src.loo.adventure import Adventure

adventure = Adventure()

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/game')
def game():
    adventure = Adventure()
    return render_template('game.html', adventure=adventure)

@app.route('/command')
def command():
    return adventure.tell(request.args.get('command',''));