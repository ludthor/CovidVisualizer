from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
import pandas as pd
from pandas import DataFrame, read_sql
import numpy as np

import plotly
import plotly.graph_objs as go
from flask import Flask, render_template
import json
import datetime

from app.db import get_db
from app.machine_learning import MachineLearning


bp = Blueprint("indicadores_convivencia", __name__, url_prefix='/iconv')

@bp.route("/")
def index():
    """Show all the posts, most recent first."""

    db = get_db()

    query = "SELECT * FROM IndicadoresCovivencia"
    indicadores = read_sql(query, db)
    indicadores.drop(indicadores.columns[0], axis=1, inplace=True)
    print(indicadores.info())


    ###MACHINE LEARNING MODEL
    #TRAINING
    ml = MachineLearning()

    indicadores['fecha_num'] = (indicadores['Fecha'] - indicadores['Fecha'].min()).dt.days
    indicadores['fecha_num'] += 1
    X = np.asarray(indicadores['fecha_num'].tolist(), dtype=np.int32).reshape(-1,1)
    y = np.asarray(indicadores['DesacatosPersonas'].tolist(), dtype=np.int32).reshape(-1,1)
    ml.train_model(X,y)

    #PREDICTIONS
    max_date = indicadores['fecha_num'].max()
    X_pred = list(range(indicadores['fecha_num'].max(),indicadores['fecha_num'].max() + 10))
    X_pred = np.asarray(X_pred, dtype=np.int32).reshape(-1,1)
    y_pred = ml.predict(X_pred)
    y_pred = y_pred.flatten()

    X_times = pd.date_range(indicadores['Fecha'].max(), periods=12).tolist()
    X_times =X_times[2:]

    X_fechas = []
    
    for ti in X_times:
        date_time = datetime.datetime.fromtimestamp(ti.timestamp())
        X_fechas.append(date_time.strftime("%Y-%m-%d"))

    print( indicadores['Fecha'])
    print(X_fechas)
    print("PREDICTIONS: ", y_pred)


    plot = create_plot(indicadores, pd.Series(X_fechas), pd.Series(y_pred))


    return render_template("iconv/index.html", tables=[indicadores.to_html(classes='table table-sm table-hover')],
                            titles=indicadores.columns.values, actual_plot = plot)


def create_plot(indicadores, X, y):
    trace1 = go.Scatter(
        x = indicadores['Fecha'],
        y = indicadores['DesacatosPersonas'],
        mode = 'lines+markers',
        name = 'Desacatos personas',
        marker_color = 'rgba(0, 0, 200, 1)'
    )

    trace2 = go.Scatter(
        x = indicadores['Fecha'],
        y = indicadores['DesacatosEstablecimiento'],
        mode = 'lines+markers',
        name = 'Desacatos establecimientos'
    )

    trace3 = go.Scatter(
        x = indicadores['Fecha'],
        y = indicadores['DesacatosMenores'],
        mode = 'lines+markers',
        name = 'Desacatos menores'
    )

    trace4 = go.Scatter(
        x = indicadores['Fecha'],
        y = indicadores['ViolenciaFamiliar'],
        mode = 'lines+markers',
        name = 'Violencia Familiar'
    )

    trace_preds = go.Scatter(
        x = X,
        y = y,
        mode = 'markers',
        name = 'Tendencia Desacatos personas',
        marker_color = 'rgba(0, 0, 200, .5)'
    )

    data = [trace1, trace2, trace3, trace4, trace_preds]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
