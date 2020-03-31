import os

from flask import Flask, render_template
from app.stats import Stats

import http.client
import json

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI= 'mysql://admin:OkNSBTREwB0EZiEoDwfR@covid-switch.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com/db',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():

        conn = http.client.HTTPSConnection("covid-19-data.p.rapidapi.com")

        headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': "7182ae44d7msh52362a68ccfb119p108e0cjsnec2253c6956f"
            }

        conn.request("GET", "/totals?format=json", headers=headers)

        res = conn.getresponse()
        data = res.read()
        parsed_json = (json.loads(data))

        print(parsed_json[0])
        
        #Conectar a API
        global_data = {'total' : parsed_json[0]['confirmed'], 'muertos': parsed_json[0]['deaths'], 'recuperados' : parsed_json[0]['recovered']}
        syc_data = stats()


        return  render_template('home.html', global_data=global_data, syc_data = syc_data)

    def stats():
        datos_hoy = {}
        stats = Stats()

        syc = stats.calculate_syc()
        return syc

    
    from app import indicadores_convivencia

    app.register_blueprint(indicadores_convivencia.bp)

    return app