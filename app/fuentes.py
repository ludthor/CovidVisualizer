from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app.db import get_db

bp = Blueprint("fuentes", __name__, url_prefix="/fuentes")

@bp.route("/")
def index():
    db = get_db()
    fuentes = {}
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT f.Fecha, f.Caudal, f.Turbiedad, f.Color, (SELECT l.valor FROM Lugares l WHERE f.FK_LugarID == l.LugarID)"
            " FROM FuetnesAuga f"
        )
        fuentes = cursor.fetchall()
    return render_template("fuentes/index.html", data = fuentes)