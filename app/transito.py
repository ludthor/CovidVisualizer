from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app.db import get_db

bp = Blueprint("transito", __name__, url_prefix='/transito')

@bp.route("/")
def index():
    db = get_db()
    transito = {}
    comparendos = {}
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT *"
            " FROM Transito"
        )
        transito = cursor.fetchall()
        cursor.execute(
            "SELECT *"
            " FROM ComparendosTransito"
        )
        comparendos = cursor.fetchall()
    return render_template("transito/index.html", data=[transito, comparendos])

