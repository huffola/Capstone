#core/views.py
from flask import render_template,request,Blueprint
from dungeons_and_devs.models import Character
core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    characters = Character.query.order_by(Character.name.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',characters=characters)

@core.route('/info')
def info():
    return render_template('info.html')
