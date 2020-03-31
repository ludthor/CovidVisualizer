DROP DATABASE IF EXISTS db;

CREATE DATABASE db;

USE db;

CREATE TABLE IndicadoresCovivencia(
    IndicadorConvivenciaID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    DesacatosPersonas INT NOT NULL,
    DesacatosEstablecimiento INT NOT NULL,
    DesacatosMenores INT NOT NULL,
    ViolenciaFamiliar INT NOT NULL,
    PRIMARY KEY (IndicadorConvivenciaID)
);

CREATE TABLE IndicadoresSeguridad(
    IndicadorSeguridadID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    HurtosPersona INT NOT NULL,
    HurtosComercio INT NOT NULL,
    LesionesPersonales INT NOT NULL,
    Homicidios INT NOT NULL, 
    PRIMARY KEY (IndicadorSeguridadID)
);

CREATE TABLE Metrolinea(
    MetrolineaID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT  NULL,
    NumeroPasajeros INT NOT NULL,
    NumeroAnteriorPasajeros INT NOT NULL,
    PRIMARY KEY (MetrolineaID)
);

CREATE TABLE ComparendosMetrolinea(
    ComparendosMetroID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    ComparendosTotal INT NOT NULL,
    ComparendosCovid INT NOT NULL,
    PRIMARY KEY (ComparendosMetroID)
);

CREATE TABLE Transito(
    TransitoID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    NumeroAccidentesTransito INT NOT NULL,
    NumeroAccidentesMoto INT NOT NULL,
    NumeroAccidentesCarro INT NOT NULL,
    NumeroLesionesTransito INT NOT NULL,
    NumeroLesionesMoto INT NOT NULL,
    NumeroLesionesCarro INT NOT NULL,
    NumeroLesionesPeaton INT NOT NULL,
    NumeroLesionesCiclistas INT NOT NULL,
    NumeroMuertesTransito INT NOT NULL,
    NumeroMuertesCarro INT  NOT NULL,
    NumeroMuertesPeatones INT NOT NULL,
    NumeroMuertesCiclista INT NOT NULL,
    PRIMARY KEY (TransitoID)
);

CREATE TABLE ComparendosTransito(
    ComparendoTransitoID INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME NOT NULL,
    comparendos_totales INT NOT NULL,
    comparendos_covid INT NOT NULL,
    PRIMARY KEY (ComparendoTransitoID)
);

CREATE TABLE ReconexionesAgua(
    ReconexionesAguaID INT NOT NULL AUTO_INCREMENT,
    fecha DATETIME NOT NULL,
    hogares_desconexion INT NOT NULL,
    hogares_reinstalacion INT NOT NULL,
    PRIMARY KEY (ReconexionesAguaID)
);

CREATE TABLE Lugares(
    LugarID INT NOT NULL AUTO_INCREMENT,
    valor CHAR(50) NOT NULL, 
    PRIMARY KEY(LugarID)
);

CREATE TABLE FuetnesAuga(
    FuentesAguaID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    Caudal FLOAT NOT NULL,
    Turbiedad FLOAT NOT NULL,
    Color FLOAT NOT NULL,
    LugarID INT,
    PRIMARY KEY (FuentesAguaID),
    CONSTRAINT FK_LugarID FOREIGN KEY (LugarID)
    REFERENCES Lugares(LugarID)
);

CREATE TABLE ProduccionAgua(
    ProudccionAguaID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    CapacidadPlanta FLOAT NOT NULL,
    CaudalTratado FLOAT NOT NULL,
    CaudalSuministrado FLOAT NOT NULL,
    ProduccionDiaria FLOAT NOT NULL,
    LugarID INT,
    PRIMARY KEY (ProudccionAguaID),
    FOREIGN KEY (LugarID) REFERENCES Lugares(LugarID)
);

CREATE TABLE InventariosInsumos(
    InventariosInsumosID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    CoagultanteDisponibleSulfato FLOAT NOT NULL,
    CoagultanteDuracionSulfato INT NOT NULL,
    DesinfectanteDisponibleCloro FLOAT NOT NULL,
    DesinfectanteDuracionCloro INT NOT NULL,
    LugarID INT,
    PRIMARY KEY (InventariosInsumosID),
    FOREIGN KEY (LugarID) REFERENCES Lugares(LugarID)
);

CREATE TABLE TasaDanios(
    TasaDaniosID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    NumeroAtentidosMatriz FLOAT NOT NULL,
    NumeroAtendidosAcometidas FLOAT NOT NULL,
    PRIMARY KEY (TasaDaniosID)
);

CREATE TABLE AbastecimientoVol(
    AbastecimientoVolID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    VolEntradaSeisAM FLOAT NOT NULL,
    VolSalidaSeisAM FLOAT NOT NULL,
    VolSalidaUnaPM FLOAT NOT NULL,
    VolAcopiado FLOAT NOT NULL,
    PRIMARY KEY (AbastecimientoVolID)
);

CREATE TABLE AbastecimientoVolSalida(
    AbastecimientoVolSalidaID INT NOT NULL AUTO_INCREMENT,
    Fecha DATETIME NOT NULL,
    VolSalida FLOAT NOT NULL,
    LugarID INT,
    PRIMARY KEY (AbastecimientoVolSalidaID),
    FOREIGN KEY (LugarID) REFERENCES Lugares(LugarID)
);