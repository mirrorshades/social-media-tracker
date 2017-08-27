"""Views: Routes to your templates."""
from flask import Blueprint
from flask import render_template

main = Blueprint('blueprint', __name__)


@main.route("/")
def index_view():
    """Home screen."""
    return render_template('index.html')
