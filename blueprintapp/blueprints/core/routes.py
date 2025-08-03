from flask import Flask, Blueprint, render_template, request, redirect, url_for

core = Blueprint('core', __name__, template_folder='templates')

@core.route('/')
def index():
    return render_template('core/index.html')
