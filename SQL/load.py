import pandas as pd
from sqlalchemy import create_engine

"""
IndicadoresCovivencia
"""
# data_convivencia = pd.read_excel('../data/datos separados.xlsx', 'Indicadores de convivencia decr')
# data_convivencia.columns = ['Fecha', 'DesacatosPersonas', 'DesacatosEstablecimiento', 'DesacatosMenores', 'ViolenciaFamiliar']
# print(data_convivencia.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_convivencia.to_sql('IndicadoresCovivencia', engine, if_exists='append', index=False)

# engine.dispose()

"""
IndicadoresSeguridad
"""
# data_seguridad = pd.read_excel('./data/datos separados.xlsx', 'Indicadores de seguridad')
# data_seguridad.columns = ['Fecha', 'HurtosPersona', 'HurtosComercio', 'LesionesPersonales', 'Homicidios']
# print(data_seguridad.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_seguridad.to_sql('IndicadoresSeguridad', engine, if_exists='append', index=False)

# engine.dispose()

"""
IndicadoresSeguridad
"""
# data_metrolinea = pd.read_excel('./data/datos separados.xlsx', 'Metrolínea')

# print(data_metrolinea.columns)
# data_metrolinea.drop(data_metrolinea.columns[3], axis=1, inplace=True)
# data_metrolinea.columns = ['Fecha', 'NumeroPasajeros', 'NumeroAnteriorPasajeros']
# print(data_metrolinea.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_metrolinea.to_sql('Metrolinea', engine, if_exists='append', index=False)

# engine.dispose()

"""
Metrolinea
"""
# data_metrolinea = pd.read_excel('./data/datos separados.xlsx', 'Metrolínea')

# print(data_metrolinea.columns)
# data_metrolinea.drop(data_metrolinea.columns[3], axis=1, inplace=True)
# data_metrolinea.columns = ['Fecha', 'NumeroPasajeros', 'NumeroAnteriorPasajeros']
# print(data_metrolinea.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_metrolinea.to_sql('Metrolinea', engine, if_exists='append', index=False)

# engine.dispose()
"""
ComparendosMetrolinea
"""
# data_comparendos_metrolinea = pd.read_excel('./data/datos separados.xlsx', 'Comparendos Metrolinea')
# data_comparendos_metrolinea.columns = ['Fecha', 'ComparendosTotal', 'ComparendosCovid']
# print(data_comparendos_metrolinea.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_comparendos_metrolinea.to_sql('ComparendosMetrolinea', engine, if_exists='append', index=False)

# engine.dispose()
"""
Transito#######################################
"""
# data_accidentes_transito = pd.read_excel('./data/datos separados.xlsx', 'Accidentes Transito')
# print(data_accidentes_transito.columns)
# data_accidentes_transito.columns = ['Fecha', 'NumeroAccidentesTransito', 'NumeroAccidentesMoto','NumeroAccidentesCarro',
#                                     'NumeroLesionesTransito','NumeroLesionesMoto','NumeroLesionesCarro','NumeroLesionesPeaton','NumeroLesionesCiclistas',
#                                     'NumeroMuertesTransito','NumeroMuertesMoto','NumeroMuertesCarro','NumeroMuertesPeatones', 'NumeroMuertesCiclista']
# print(data_accidentes_transito.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_accidentes_transito.to_sql('Transito', engine, if_exists='append', index=False)

# engine.dispose()
"""
ComparendosTransito
"""
# data_comparendos_metrolinea = pd.read_excel('./data/datos separados.xlsx', 'Comparendos Metrolinea')
# data_comparendos_metrolinea.columns = ['fecha', 'comparendos_totales', 'comparendos_covid']
# print(data_comparendos_metrolinea.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_comparendos_metrolinea.to_sql('ComparendosTransito', engine, if_exists='append', index=False)

# engine.dispose()
"""
ReconexionesAgua
"""
# data_reinstalacion_agua = pd.read_excel('./data/datos separados.xlsx', 'Reinstalación reconexión AGUA')
# data_reinstalacion_agua.columns = ['fecha', 'hogares_desconexion', 'hogares_reinstalacion']
# print(data_reinstalacion_agua.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_reinstalacion_agua.to_sql('ReconexionesAgua', engine, if_exists='append', index=False)

# engine.dispose()
"""
ReconexionesAgua
"""
# data_reinstalacion_agua = pd.read_excel('./data/datos separados.xlsx', 'Reinstalación reconexión AGUA')
# data_reinstalacion_agua.columns = ['fecha', 'hogares_desconexion', 'hogares_reinstalacion']
# print(data_reinstalacion_agua.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_reinstalacion_agua.to_sql('ReconexionesAgua', engine, if_exists='append', index=False)

# engine.dispose()
"""
LUGARES
"""
# data_lugares = pd.read_excel('./data/datos separados.xlsx', 'Lugares')
# data_lugares.columns = ['valor']
# print(data_lugares.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

#data_lugares.to_sql('Lugares', engine, if_exists='append', index=False)

# import pymysql

# # Connect to the database
# connection = pymysql.connect(host='database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com',
#                              user='switch',
#                              password='Covid2020',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:
#     # Read a single record
#     sql = "SELECT * FROM Lugares"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
"""
FuetnesAuga
"""
# data_fuentes = pd.read_excel('./data/datos separados.xlsx', 'Fuentes de agua')
# data_fuentes.columns = ['Fecha', 'Caudal', 'Turbiedad', 'Color', 'LugarID']
# print(data_fuentes.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_fuentes.to_sql('FuetnesAuga', engine, if_exists='append', index=False)

# engine.dispose()
"""
ProduccionAgua
"""
# data_produccion = pd.read_excel('./data/datos separados.xlsx', 'Producción de agua')
# data_produccion.columns = ['Fecha', 'CapacidadPlanta', 'CaudalTratado', 'CaudalSuministrado','ProduccionDiaria', 'LugarID']
# print(data_produccion.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_produccion.to_sql('ProduccionAgua', engine, if_exists='append', index=False)

# engine.dispose()
"""
InventariosInsumos
"""
# data_insumos = pd.read_excel('./data/datos separados.xlsx', 'Inventario Insumos')
# data_insumos.columns = ['Fecha', 'CoagultanteDisponibleSulfato', 'CoagultanteDuracionSulfato',
#                     'DesinfectanteDisponibleCloro','DesinfectanteDuracionCloro', 'LugarID']
# print(data_insumos.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_insumos.to_sql('InventariosInsumos', engine, if_exists='append', index=False)

# engine.dispose()
"""
TasaDanios
"""
# data_tasa_danios = pd.read_excel('./data/datos separados.xlsx', 'Tasa de daños')
# data_tasa_danios.columns = ['Fecha', 'NumeroAtentidosMatriz', 'NumeroAtendidosAcometidas']
# print(data_tasa_danios.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_tasa_danios.to_sql('TasaDanios', engine, if_exists='append', index=False)

# engine.dispose()
"""
AbastecimientoVol
"""
# abastecimiento_volumenes = pd.read_excel('./data/datos separados.xlsx', 'Abastecimiento Volumenes')
# abastecimiento_volumenes.columns = ['Fecha', 'VolEntradaSeisAM', 'VolSalidaSeisAM',
#                                     'VolSalidaUnaPM','VolAcopiado']
# print(abastecimiento_volumenes.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# abastecimiento_volumenes.to_sql('AbastecimientoVol', engine, if_exists='append', index=False)

# engine.dispose()

"""
LugaresSalida
"""
# import pymysql

# # Connect to the database
# connection = pymysql.connect(host='database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com',
#                              user='switch',
#                              password='Covid2020',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:
#     # Read a single record
#     sql = "CREATE TABLE LugaresSalida( LugarID INT NOT NULL AUTO_INCREMENT, valor CHAR(50) NOT NULL, PRIMARY KEY(LugarID));"
#     cursor.execute(sql)

# connection.commit()

# data_lugares_salida = pd.read_excel('./data/datos separados.xlsx', 'Lugares salida')
# data_lugares_salida.columns = ['valor']
# print(data_lugares_salida.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# data_lugares_salida.to_sql('LugaresSalida', engine, if_exists='append', index=False)


# with connection.cursor() as cursor:
#     # Read a single record
#     sql = "SELECT * FROM LugaresSalida"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
"""
AbastecimientoVolSalida
"""
# import pymysql

# # Connect to the database
# connection = pymysql.connect(host='database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com',
#                              user='switch',
#                              password='Covid2020',
#                              db='db',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:
#     # Read a single record
#     sql = "CREATE TABLE AbastecimientoSalida(AbastecimientoVolSalidaID INT NOT NULL AUTO_INCREMENT, Fecha DATETIME NOT NULL, VolAtlantico INT NOT NULL, VolGuajira INT NOT NULL, VolBolivar INT NOT NULL, VolCesar INT NOT NULL, VolMagdalena INT NOT NULL, VolSantander INT NOT NULL, VolMagdalenaMedio INT NOT NULL, VolNorAntioquia INT NOT NULL, VolGuanentina INT NOT NULL, PRIMARY KEY (AbastecimientoVolSalidaID));"
#     cursor.execute(sql)

# connection.commit()
# abastecimiento_volumenes_destino = pd.read_excel('./data/datos separados.xlsx', 'Abastecimiento Vol Destino')
# print(abastecimiento_volumenes_destino.columns)
# abastecimiento_volumenes_destino.columns = ['Fecha', 'VolAtlantico','VolGuajira' ,'VolBolivar',
#                                             'VolCesar', 'VolMagdalena', 'VolSantander', 'VolMagdalenaMedio',
#                                             'VolNorAntioquia', 'VolGuanentina']
# print(abastecimiento_volumenes_destino.columns)

# db_data = 'mysql+pymysql://' + 'switch' + ':' + 'Covid2020' + '@' + 'database-1.cwoz6iaqvzcl.us-east-2.rds.amazonaws.com' + ':3306/' \
#        + 'db' + '?charset=utf8mb4'
# engine = create_engine(db_data)

# abastecimiento_volumenes_destino.to_sql('AbastecimientoSalida', engine, if_exists='append', index=False)

# engine.dispose()