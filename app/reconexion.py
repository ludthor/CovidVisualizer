from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from app.db import get_db

bp = Blueprint("reconexion", __name__, url_prefix='/recon')

@bp.route("/")
def index():
    db = get_db()
    reconexion = {}
    with db.cursor() as cursor:
        cursor.execute(
            "SELECT *"
            " FROM ReconexionesAgua"
        )
        reconexion = cursor.fetchall()
    return render_template("recon/index.html", data=reconexion)