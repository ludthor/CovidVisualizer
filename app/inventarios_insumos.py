from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app.db import get_db

bp = Blueprint("iinsumos", __name__, url_prefix="/iinsumos")

@bp.route("/")
def index():
    db = get_db()
    insumos = {}
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT i.Fecha, i.CoagultanteDisponibleSulfato, i.CoagultanteDuracionSulfato, i.DesinfectanteDisponibleCloro, i.DesinfectanteDuracionCloro, (SELECT l.valor FROM Lugares l WHERE i.FK_LugarID == l.LugarID)"
            " FROM InventariosInsumos i"
        )
        insumos = cursor.fetchall()
    return render_template("iinsumos/index.html", data = insumos)