import pandas as pd
from functools import reduce


def load():
    print("Cargando datos")

    datos ={}

    """
    Seguridad y convivencia
    """
    datos['Convivencia'] = data_convivencia = pd.read_excel('./data/datos separados.xlsx', 'Indicadores de convivencia decr')
    datos['Seguridad'] = data_seguridad = pd.read_excel('./data/datos separados.xlsx', 'Indicadores de seguridad')
    """
    Tránsito
    """
    datos['Metrolinea'] = data_metrolinea = pd.read_excel('./data/datos separados.xlsx', 'Metrolínea')
    datos['ComparendosMetrolinea'] = data_comparendos_metrolinea = pd.read_excel('./data/datos separados.xlsx', 'Comparendos Metrolinea')
    
    datos['AccidentesTransito'] = data_accidentes_transito = pd.read_excel('./data/datos separados.xlsx', 'Accidentes Transito')
    """
    Agua
    """
    datos['ReinstalacionAgua'] = data_reinstalacion_agua = pd.read_excel('./data/datos separados.xlsx', 'Reinstalación reconexión AGUA')
    
    datos['Fuentes'] = data_fuentes = pd.read_excel('./data/datos separados.xlsx', 'Fuentes de agua')
    datos['Produccion'] = data_produccion = pd.read_excel('./data/datos separados.xlsx', 'Producción de agua')
    datos['ProduccionTotal'] = data_produccion_total = pd.read_excel('./data/datos separados.xlsx', 'Producción de agua TOTAL')
    datos['Insumos'] = data_insumos = pd.read_excel('./data/datos separados.xlsx', 'Inventario Insumos')
    datos['TasaDanios'] = data_tasa_danios = pd.read_excel('./data/datos separados.xlsx', 'Tasa de daños')

    """
    Abastecimiento
    """
    datos['AbastecimientoVolumenes'] = abastecimiento_volumenes = pd.read_excel('./data/datos separados.xlsx', 'Abastecimiento Volumenes')
    datos['AbastecimientoDestino'] = abastecimiento_volumenes_destino = pd.read_excel('./data/datos separados.xlsx', 'Abastecimiento Vol Destino')


    merged = reduce(lambda  left,right: pd.merge(left,right,on=['Fecha'],
                                            how='outer'), datos.values()).fillna(-1)
    print(merged)
    merged.to_csv('./data/merged.csv', sep=';', encoding='utf-8', decimal='.')
    
if(__name__ == "__main__"):
    load()