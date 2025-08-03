from flask import Flask, Blueprint, render_template, request, redirect, url_for
from blueprintapp.app import db
from blueprintapp.blueprints.todos.models import Todo

todos = Blueprint('todos', __name__, template_folder='templates')

@todos.route('/')
def index():
    todos = Todo.query.all()
    return render_template('todos/index.html', todos=todos)

@todos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('todos/create.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        done = True if request.form.get('done') else False
        
        new_todo = Todo(title=title, description=description, done=done)
        db.session.add(new_todo)
        db.session.commit()
        
        return redirect(url_for('todos.index'))