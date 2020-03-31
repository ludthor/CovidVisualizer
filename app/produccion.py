from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app.db import get_db

bp = Blueprint("prod", __name__, url_prefix="/prod")

@bp.route("/")
def index():
    db = get_db()
    produccion = {}
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT p.Fecha, p.CapacidadPlanta, p.CaudalTratado, p.CaudalSuministrado, p.ProduccionDiaria,  (SELECT l.valor FROM Lugares l WHERE p.FK_LugarID == l.LugarID)"
            " FROM ProduccionAgua p"
        )
        produccion = cursor.fetchall()
    return render_template("prod/index.html", data = produccion)