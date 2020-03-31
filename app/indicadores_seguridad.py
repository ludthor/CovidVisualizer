from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app.db import get_db

bp = Blueprint("indicadores_seguridad", __name__, url_prefix='/isegu')

@bp.route("/")
def index():
    db = get_db()
    indicadores = {}
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT *"
            " FROM IndicadoresSeguridad"
        )
        indicadores = cursor.fetchall()
    return render_template("isegu/index.html", indicadores=indicadores)