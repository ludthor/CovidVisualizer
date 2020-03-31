from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app.db import get_db

bp = Blueprint("metrolinea", __name__, url_prefix='/metrolinea')

@bp.route("/")
def index():
    db = get_db()
    metrolinea = {}
    comparendos = {}
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT *"
            " FROM Metrolinea"
        )
        metrolinea = cursor.fetchall()
        cursor.execute(
            "SELECT *"
            " FROM ComparendosMetrolinea"
        )
        comparendos = cursor.fetchall()
    return render_template("metro/index.html", data = [metrolinea, comparendos])