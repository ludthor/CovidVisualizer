from app.db import get_db
import pandas as pd

class Stats():

    def calculate_syc(self):

        db = get_db()

        query = "SELECT * FROM IndicadoresCovivencia"
        indicadores_syc = pd.read_sql(query, db)
        indicadores_syc.sort_values(by=['Fecha'], ascending=True, inplace=True)
        return {'desa_pers' : indicadores_syc.iloc[-1]['DesacatosPersonas'],
                'desa_est': indicadores_syc.iloc[-1]['DesacatosEstablecimiento'],
                'desa_men' : indicadores_syc.iloc[-1]['DesacatosMenores'],
                'viol_fam' : indicadores_syc.iloc[-1]['ViolenciaFamiliar'], }
