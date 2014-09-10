from flask import render_template
from . import frontend

@frontend.route('/', methods=['GET'])
def index():
    return render_template('index.jinja')
