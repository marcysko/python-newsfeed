from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
<<<<<<< HEAD
  return render_template('single-post.html')
=======
  return render_template('single-post.html')
>>>>>>> e204f9e5b105b51655bad99d4741b546a9a93e1b
