#!/usr/bin/env python
# encoding: utf8
import os
from random import randint
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import json
from pprint import pprint

configData = []
# ------------------------------
# clientes

Clientes = []
numeroClientes = 0
numeroUltimoCliente = 0

# ------------------------------
# vars
clock = 0
tipoEvento = ""
cliente = 0
proxChegada = 999999
encontrouPrioritario = 0
idClientePrioritario = 0

# ------------------------------

# ------------------------------
# Zona de Vendedores
# -------------------
filaZV = []
filaZVP = []
filaZL = []
filaZLP = []

listaZVPostos = []
# -------------------
estadoZV1 = "livre"
partidaZV1 = 999999
clienteZV1 = 0
numClienteZV1 = 0
numClienteZV1P = 0
numClienteZV1_10_13 = 0
numClienteZV1_13_16 = 0
numClienteZV1_16_19 = 0
numClienteZV1_19_22 = 0
numClienteZV1P_10_13 = 0
numClienteZV1P_13_16 = 0
numClienteZV1P_16_19 = 0
numClienteZV1P_19_22 = 0
tempoEsperaZV1 = 0
tempoEsperaZV1P = 0
tempoEsperaZV1Min = 999999
tempoEsperaZV1Max = 0
tempoEsperaZV1PMin = 999999
tempoEsperaZV1PMax = 0
tempoEsperaZV1_10_13 = 0
tempoEsperaZV1_10_13_Min = 999999
tempoEsperaZV1_10_13_Max = 0
tempoEsperaZV1_13_16 = 0
tempoEsperaZV1_13_16_Min = 999999
tempoEsperaZV1_13_16_Max = 0
tempoEsperaZV1_16_19 = 0
tempoEsperaZV1_16_19_Min = 999999
tempoEsperaZV1_16_19_Max = 0
tempoEsperaZV1_19_22 = 0
tempoEsperaZV1_19_22_Min = 999999
tempoEsperaZV1_19_22_Max = 0
tempoEsperaZV1P_10_13 = 0
tempoEsperaZV1P_10_13_Min = 999999
tempoEsperaZV1P_10_13_Max = 0
tempoEsperaZV1P_13_16 = 0
tempoEsperaZV1P_13_16_Min = 999999
tempoEsperaZV1P_13_16_Max = 0
tempoEsperaZV1P_16_19 = 0
tempoEsperaZV1P_16_19_Min = 999999
tempoEsperaZV1P_16_19_Max = 0
tempoEsperaZV1P_19_22 = 0
tempoEsperaZV1P_19_22_Min = 999999
tempoEsperaZV1P_19_22_Max = 0
# -------------------
estadoZV2 = "livre"
partidaZV2 = 999999
clienteZV2 = 0
numClienteZV2 = 0
numClienteZV2P = 0
numClienteZV2_10_13 = 0
numClienteZV2_13_16 = 0
numClienteZV2_16_19 = 0
numClienteZV2_19_22 = 0
numClienteZV2P_10_13 = 0
numClienteZV2P_13_16 = 0
numClienteZV2P_16_19 = 0
numClienteZV2P_19_22 = 0
tempoEsperaZV2 = 0
tempoEsperaZV2P = 0
tempoEsperaZV2Min = 999999
tempoEsperaZV2Max = 0
tempoEsperaZV2PMin = 999999
tempoEsperaZV2PMax = 0
tempoEsperaZV2_10_13 = 0
tempoEsperaZV2_10_13_Min = 999999
tempoEsperaZV2_10_13_Max = 0
tempoEsperaZV2_13_16 = 0
tempoEsperaZV2_13_16_Min = 999999
tempoEsperaZV2_13_16_Max = 0
tempoEsperaZV2_16_19 = 0
tempoEsperaZV2_16_19_Min = 999999
tempoEsperaZV2_16_19_Max = 0
tempoEsperaZV2_19_22 = 0
tempoEsperaZV2_19_22_Min = 999999
tempoEsperaZV2_19_22_Max = 0
tempoEsperaZV2P_10_13 = 0
tempoEsperaZV2P_10_13_Min = 999999
tempoEsperaZV2P_10_13_Max = 0
tempoEsperaZV2P_13_16 = 0
tempoEsperaZV2P_13_16_Min = 999999
tempoEsperaZV2P_13_16_Max = 0
tempoEsperaZV2P_16_19 = 0
tempoEsperaZV2P_16_19_Min = 999999
tempoEsperaZV2P_16_19_Max = 0
tempoEsperaZV2P_19_22 = 0
tempoEsperaZV2P_19_22_Min = 999999
tempoEsperaZV2P_19_22_Max = 0
# -------------------
estadoZV3 = "livre"
partidaZV3 = 999999
clienteZV3 = 0
numClienteZV3 = 0
numClienteZV3P = 0
tempoEsperaZV3P = 0
numClienteZV3_10_13 = 0
numClienteZV3_13_16 = 0
numClienteZV3_16_19 = 0
numClienteZV3_19_22 = 0
numClienteZV3P_10_13 = 0
numClienteZV3P_13_16 = 0
numClienteZV3P_16_19 = 0
numClienteZV3P_19_22 = 0
tempoEsperaZV3 = 0
tempoEsperaZV3Min = 999999
tempoEsperaZV3Max = 0
tempoEsperaZV3PMin = 999999
tempoEsperaZV3PMax = 0
tempoEsperaZV3_10_13 = 0
tempoEsperaZV3_10_13_Min = 999999
tempoEsperaZV3_10_13_Max = 0
tempoEsperaZV3_13_16 = 0
tempoEsperaZV3_13_16_Min = 999999
tempoEsperaZV3_13_16_Max = 0
tempoEsperaZV3_16_19 = 0
tempoEsperaZV3_16_19_Min = 999999
tempoEsperaZV3_16_19_Max = 0
tempoEsperaZV3_19_22 = 0
tempoEsperaZV3_19_22_Min = 999999
tempoEsperaZV3_19_22_Max = 0
tempoEsperaZV3P_10_13 = 0
tempoEsperaZV3P_10_13_Min = 999999
tempoEsperaZV3P_10_13_Max = 0
tempoEsperaZV3P_13_16 = 0
tempoEsperaZV3P_13_16_Min = 999999
tempoEsperaZV3P_13_16_Max = 0
tempoEsperaZV3P_16_19 = 0
tempoEsperaZV3P_16_19_Min = 999999
tempoEsperaZV3P_16_19_Max = 0
tempoEsperaZV3P_19_22 = 0
tempoEsperaZV3P_19_22_Min = 999999
tempoEsperaZV3P_19_22_Max = 0
# -------------------
estadoZV4 = "livre"
partidaZV4 = 999999
clienteZV4 = 0
numClienteZV4 = 0
numClienteZV4P = 0
numClienteZV4_10_13 = 0
numClienteZV4_13_16 = 0
numClienteZV4_16_19 = 0
numClienteZV4_19_22 = 0
numClienteZV4P_10_13 = 0
numClienteZV4P_13_16 = 0
numClienteZV4P_16_19 = 0
numClienteZV4P_19_22 = 0
tempoEsperaZV4 = 0
tempoEsperaZV4P = 0
tempoEsperaZV4Min = 999999
tempoEsperaZV4Max = 0
tempoEsperaZV4PMin = 999999
tempoEsperaZV4PMax = 0
tempoEsperaZV4_10_13 = 0
tempoEsperaZV4_10_13_Min = 999999
tempoEsperaZV4_10_13_Max = 0
tempoEsperaZV4_13_16 = 0
tempoEsperaZV4_13_16_Min = 999999
tempoEsperaZV4_13_16_Max = 0
tempoEsperaZV4_16_19 = 0
tempoEsperaZV4_16_19_Min = 999999
tempoEsperaZV4_16_19_Max = 0
tempoEsperaZV4_19_22 = 0
tempoEsperaZV4_19_22_Min = 999999
tempoEsperaZV4_19_22_Max = 0
tempoEsperaZV4P_10_13 = 0
tempoEsperaZV4P_10_13_Min = 999999
tempoEsperaZV4P_10_13_Max = 0
tempoEsperaZV4P_13_16 = 0
tempoEsperaZV4P_13_16_Min = 999999
tempoEsperaZV4P_13_16_Max = 0
tempoEsperaZV4P_16_19 = 0
tempoEsperaZV4P_16_19_Min = 999999
tempoEsperaZV4P_16_19_Max = 0
tempoEsperaZV4P_19_22 = 0
tempoEsperaZV4P_19_22_Min = 999999
tempoEsperaZV4P_19_22_Max = 0
# -------------------
estadoZV5 = "livre"
partidaZV5 = 999999
clienteZV5 = 0
numClienteZV5 = 0
numClienteZV5P = 0
numClienteZV5_10_13 = 0
numClienteZV5_13_16 = 0
numClienteZV5_16_19 = 0
numClienteZV5_19_22 = 0
numClienteZV5P_10_13 = 0
numClienteZV5P_13_16 = 0
numClienteZV5P_16_19 = 0
numClienteZV5P_19_22 = 0
tempoEsperaZV5 = 0
tempoEsperaZV5P = 0
tempoEsperaZV5Min = 999999
tempoEsperaZV5Max = 0
tempoEsperaZV5PMin = 999999
tempoEsperaZV5PMax = 0
tempoEsperaZV5_10_13 = 0
tempoEsperaZV5_10_13_Min = 999999
tempoEsperaZV5_10_13_Max = 0
tempoEsperaZV5_13_16 = 0
tempoEsperaZV5_13_16_Min = 999999
tempoEsperaZV5_13_16_Max = 0
tempoEsperaZV5_16_19 = 0
tempoEsperaZV5_16_19_Min = 999999
tempoEsperaZV5_16_19_Max = 0
tempoEsperaZV5_19_22 = 0
tempoEsperaZV5_19_22_Min = 999999
tempoEsperaZV5_19_22_Max = 0
tempoEsperaZV5P_10_13 = 0
tempoEsperaZV5P_10_13_Min = 999999
tempoEsperaZV5P_10_13_Max = 0
tempoEsperaZV5P_13_16 = 0
tempoEsperaZV5P_13_16_Min = 999999
tempoEsperaZV5P_13_16_Max = 0
tempoEsperaZV5P_16_19 = 0
tempoEsperaZV5P_16_19_Min = 999999
tempoEsperaZV5P_16_19_Max = 0
tempoEsperaZV5P_19_22 = 0
tempoEsperaZV5P_19_22_Min = 999999
tempoEsperaZV5P_19_22_Max = 0
# -------------------
estadoZV6 = "livre"
partidaZV6 = 999999
clienteZV6 = 0
numClienteZV6 = 0
numClienteZV6P = 0
numClienteZV6_10_13 = 0
numClienteZV6_13_16 = 0
numClienteZV6_16_19 = 0
numClienteZV6_19_22 = 0
numClienteZV6P_10_13 = 0
numClienteZV6P_13_16 = 0
numClienteZV6P_16_19 = 0
numClienteZV6P_19_22 = 0
tempoEsperaZV6 = 0
tempoEsperaZV6P = 0
tempoEsperaZV6Min = 999999
tempoEsperaZV6Max = 0
tempoEsperaZV6PMin = 999999
tempoEsperaZV6PMax = 0
tempoEsperaZV6_10_13 = 0
tempoEsperaZV6_10_13_Min = 999999
tempoEsperaZV6_10_13_Max = 0
tempoEsperaZV6_13_16 = 0
tempoEsperaZV6_13_16_Min = 999999
tempoEsperaZV6_13_16_Max = 0
tempoEsperaZV6_16_19 = 0
tempoEsperaZV6_16_19_Min = 999999
tempoEsperaZV6_16_19_Max = 0
tempoEsperaZV6_19_22 = 0
tempoEsperaZV6_19_22_Min = 999999
tempoEsperaZV6_19_22_Max = 0
tempoEsperaZV6P_10_13 = 0
tempoEsperaZV6P_10_13_Min = 999999
tempoEsperaZV6P_10_13_Max = 0
tempoEsperaZV6P_13_16 = 0
tempoEsperaZV6P_13_16_Min = 999999
tempoEsperaZV6P_13_16_Max = 0
tempoEsperaZV6P_16_19 = 0
tempoEsperaZV6P_16_19_Min = 999999
tempoEsperaZV6P_16_19_Max = 0
tempoEsperaZV6P_19_22 = 0
tempoEsperaZV6P_19_22_Min = 999999
tempoEsperaZV6P_19_22_Max = 0
# -------------------
estadoZV7 = "livre"
partidaZV7 = 999999
clienteZV7 = 0
numClienteZV7 = 0
numClienteZV7P = 0
numClienteZV7_10_13 = 0
numClienteZV7_13_16 = 0
numClienteZV7_16_19 = 0
numClienteZV7_19_22 = 0
numClienteZV7P_10_13 = 0
numClienteZV7P_13_16 = 0
numClienteZV7P_16_19 = 0
numClienteZV7P_19_22 = 0
tempoEsperaZV7 = 0
tempoEsperaZV7P = 0
tempoEsperaZV7Min = 999999
tempoEsperaZV7Max = 0
tempoEsperaZV7PMin = 999999
tempoEsperaZV7PMax = 0
tempoEsperaZV7_10_13 = 0
tempoEsperaZV7_10_13_Min = 999999
tempoEsperaZV7_10_13_Max = 0
tempoEsperaZV7_13_16 = 0
tempoEsperaZV7_13_16_Min = 999999
tempoEsperaZV7_13_16_Max = 0
tempoEsperaZV7_16_19 = 0
tempoEsperaZV7_16_19_Min = 999999
tempoEsperaZV7_16_19_Max = 0
tempoEsperaZV7_19_22 = 0
tempoEsperaZV7_19_22_Min = 999999
tempoEsperaZV7_19_22_Max = 0
tempoEsperaZV7P_10_13 = 0
tempoEsperaZV7P_10_13_Min = 999999
tempoEsperaZV7P_10_13_Max = 0
tempoEsperaZV7P_13_16 = 0
tempoEsperaZV7P_13_16_Min = 999999
tempoEsperaZV7P_13_16_Max = 0
tempoEsperaZV7P_16_19 = 0
tempoEsperaZV7P_16_19_Min = 999999
tempoEsperaZV7P_16_19_Max = 0
tempoEsperaZV7P_19_22 = 0
tempoEsperaZV7P_19_22_Min = 999999
tempoEsperaZV7P_19_22_Max = 0
# -------------------
estadoZV8 = "livre"
partidaZV8 = 999999
clienteZV8 = 0
numClienteZV8 = 0
numClienteZV8P = 0
numClienteZV8_10_13 = 0
numClienteZV8_13_16 = 0
numClienteZV8_16_19 = 0
numClienteZV8_19_22 = 0
numClienteZV8P_10_13 = 0
numClienteZV8P_13_16 = 0
numClienteZV8P_16_19 = 0
numClienteZV8P_19_22 = 0
tempoEsperaZV8 = 0
tempoEsperaZV8P = 0
tempoEsperaZV8Min = 999999
tempoEsperaZV8Max = 0
tempoEsperaZV8PMin = 999999
tempoEsperaZV8PMax = 0
tempoEsperaZV8_10_13 = 0
tempoEsperaZV8_10_13_Min = 999999
tempoEsperaZV8_10_13_Max = 0
tempoEsperaZV8_13_16 = 0
tempoEsperaZV8_13_16_Min = 999999
tempoEsperaZV8_13_16_Max = 0
tempoEsperaZV8_16_19 = 0
tempoEsperaZV8_16_19_Min = 999999
tempoEsperaZV8_16_19_Max = 0
tempoEsperaZV8_19_22 = 0
tempoEsperaZV8_19_22_Min = 999999
tempoEsperaZV8_19_22_Max = 0
tempoEsperaZV8P_10_13 = 0
tempoEsperaZV8P_10_13_Min = 999999
tempoEsperaZV8P_10_13_Max = 0
tempoEsperaZV8P_13_16 = 0
tempoEsperaZV8P_13_16_Min = 999999
tempoEsperaZV8P_13_16_Max = 0
tempoEsperaZV8P_16_19 = 0
tempoEsperaZV8P_16_19_Min = 999999
tempoEsperaZV8P_16_19_Max = 0
tempoEsperaZV8P_19_22 = 0
tempoEsperaZV8P_19_22_Min = 999999
tempoEsperaZV8P_19_22_Max = 0
# -------------------
estadoZV9 = "livre"
partidaZV9 = 999999
clienteZV9 = 0
numClienteZV9 = 0
numClienteZV9P = 0
numClienteZV9_10_13 = 0
numClienteZV9_13_16 = 0
numClienteZV9_16_19 = 0
numClienteZV9_19_22 = 0
numClienteZV9P_10_13 = 0
numClienteZV9P_13_16 = 0
numClienteZV9P_16_19 = 0
numClienteZV9P_19_22 = 0
tempoEsperaZV9 = 0
tempoEsperaZV9P = 0
tempoEsperaZV9Min = 999999
tempoEsperaZV9Max = 0
tempoEsperaZV9PMin = 999999
tempoEsperaZV9PMax = 0
tempoEsperaZV9_10_13 = 0
tempoEsperaZV9_10_13_Min = 999999
tempoEsperaZV9_10_13_Max = 0
tempoEsperaZV9_13_16 = 0
tempoEsperaZV9_13_16_Min = 999999
tempoEsperaZV9_13_16_Max = 0
tempoEsperaZV9_16_19 = 0
tempoEsperaZV9_16_19_Min = 999999
tempoEsperaZV9_16_19_Max = 0
tempoEsperaZV9_19_22 = 0
tempoEsperaZV9_19_22_Min = 999999
tempoEsperaZV9_19_22_Max = 0
tempoEsperaZV9P_10_13 = 0
tempoEsperaZV9P_10_13_Min = 999999
tempoEsperaZV9P_10_13_Max = 0
tempoEsperaZV9P_13_16 = 0
tempoEsperaZV9P_13_16_Min = 999999
tempoEsperaZV9P_13_16_Max = 0
tempoEsperaZV9P_16_19 = 0
tempoEsperaZV9P_16_19_Min = 999999
tempoEsperaZV9P_16_19_Max = 0
tempoEsperaZV9P_19_22 = 0
tempoEsperaZV9P_19_22_Min = 999999
tempoEsperaZV9P_19_22_Max = 0
# -------------------
estadoZV10 = "livre"
partidaZV10 = 999999
clienteZV10 = 0
numClienteZV10 = 0
numClienteZV10P = 0
numClienteZV10_10_13 = 0
numClienteZV10_13_16 = 0
numClienteZV10_16_19 = 0
numClienteZV10_19_22 = 0
numClienteZV10P_10_13 = 0
numClienteZV10P_13_16 = 0
numClienteZV10P_16_19 = 0
numClienteZV10P_19_22 = 0
tempoEsperaZV10 = 0
tempoEsperaZV10P = 0
tempoEsperaZV10Min = 999999
tempoEsperaZV10Max = 0
tempoEsperaZV10PMin = 999999
tempoEsperaZV10PMax = 0
tempoEsperaZV10_10_13 = 0
tempoEsperaZV10_10_13_Min = 999999
tempoEsperaZV10_10_13_Max = 0
tempoEsperaZV10_13_16 = 0
tempoEsperaZV10_13_16_Min = 999999
tempoEsperaZV10_13_16_Max = 0
tempoEsperaZV10_16_19 = 0
tempoEsperaZV10_16_19_Min = 999999
tempoEsperaZV10_16_19_Max = 0
tempoEsperaZV10_19_22 = 0
tempoEsperaZV10_19_22_Min = 999999
tempoEsperaZV10_19_22_Max = 0
tempoEsperaZV10P_10_13 = 0
tempoEsperaZV10P_10_13_Min = 999999
tempoEsperaZV10P_10_13_Max = 0
tempoEsperaZV10P_13_16 = 0
tempoEsperaZV10P_13_16_Min = 999999
tempoEsperaZV10P_13_16_Max = 0
tempoEsperaZV10P_16_19 = 0
tempoEsperaZV10P_16_19_Min = 999999
tempoEsperaZV10P_16_19_Max = 0
tempoEsperaZV10P_19_22 = 0
tempoEsperaZV10P_19_22_Min = 999999
tempoEsperaZV10P_19_22_Max = 0
# ------------------------------

# ------------------------------
#  Zona de Pagamento
# -------------------
listaZPPostos = []
# -------------------
filaZP1 = []
filaZP1P = []
estadoZP1 = "livre"
partidaZP1 = 999999
clienteZP1 = 0
numClienteZP1 = 0
numClienteZP1P = 0
numClienteZP1_10_13 = 0
numClienteZP1_13_16 = 0
numClienteZP1_16_19 = 0
numClienteZP1_19_22 = 0
numClienteZP1P_10_13 = 0
numClienteZP1P_13_16 = 0
numClienteZP1P_16_19 = 0
numClienteZP1P_19_22 = 0
tempoEsperaZP1 = 0
tempoEsperaZP1P = 0
tempoEsperaZP1Min = 999999
tempoEsperaZP1Max = 0
tempoEsperaZP1PMin = 999999
tempoEsperaZP1PMax = 0
tempoEsperaZP1_10_13 = 0
tempoEsperaZP1_10_13_Min = 999999
tempoEsperaZP1_10_13_Max = 0
tempoEsperaZP1_13_16 = 0
tempoEsperaZP1_13_16_Min = 999999
tempoEsperaZP1_13_16_Max = 0
tempoEsperaZP1_16_19 = 0
tempoEsperaZP1_16_19_Min = 999999
tempoEsperaZP1_16_19_Max = 0
tempoEsperaZP1_19_22 = 0
tempoEsperaZP1_19_22_Min = 999999
tempoEsperaZP1_19_22_Max = 0
tempoEsperaZP1P_10_13 = 0
tempoEsperaZP1P_10_13_Min = 999999
tempoEsperaZP1P_10_13_Max = 0
tempoEsperaZP1P_13_16 = 0
tempoEsperaZP1P_13_16_Min = 999999
tempoEsperaZP1P_13_16_Max = 0
tempoEsperaZP1P_16_19 = 0
tempoEsperaZP1P_16_19_Min = 999999
tempoEsperaZP1P_16_19_Max = 0
tempoEsperaZP1P_19_22 = 0
tempoEsperaZP1P_19_22_Min = 999999
tempoEsperaZP1P_19_22_Max = 0
# -------------------
filaZP2 = []
filaZP2P = []
estadoZP2 = "livre"
partidaZP2 = 999999
clienteZP2 = 0
numClienteZP2 = 0
numClienteZP2P = 0
numClienteZP2_10_13 = 0
numClienteZP2_13_16 = 0
numClienteZP2_16_19 = 0
numClienteZP2_19_22 = 0
numClienteZP2P_10_13 = 0
numClienteZP2P_13_16 = 0
numClienteZP2P_16_19 = 0
numClienteZP2P_19_22 = 0
tempoEsperaZP2 = 0
tempoEsperaZP2P = 0
tempoEsperaZP2Min = 999999
tempoEsperaZP2Max = 0
tempoEsperaZP2PMin = 999999
tempoEsperaZP2PMax = 0
tempoEsperaZP2_10_13 = 0
tempoEsperaZP2_10_13_Min = 999999
tempoEsperaZP2_10_13_Max = 0
tempoEsperaZP2_13_16 = 0
tempoEsperaZP2_13_16_Min = 999999
tempoEsperaZP2_13_16_Max = 0
tempoEsperaZP2_16_19 = 0
tempoEsperaZP2_16_19_Min = 999999
tempoEsperaZP2_16_19_Max = 0
tempoEsperaZP2_19_22 = 0
tempoEsperaZP2_19_22_Min = 999999
tempoEsperaZP2_19_22_Max = 0
tempoEsperaZP2P_10_13 = 0
tempoEsperaZP2P_10_13_Min = 999999
tempoEsperaZP2P_10_13_Max = 0
tempoEsperaZP2P_13_16 = 0
tempoEsperaZP2P_13_16_Min = 999999
tempoEsperaZP2P_13_16_Max = 0
tempoEsperaZP2P_16_19 = 0
tempoEsperaZP2P_16_19_Min = 999999
tempoEsperaZP2P_16_19_Max = 0
tempoEsperaZP2P_19_22 = 0
tempoEsperaZP2P_19_22_Min = 999999
tempoEsperaZP2P_19_22_Max = 0
# -------------------
filaZP3 = []
filaZP3P = []
estadoZP3 = "livre"
partidaZP3 = 999999
clienteZP3 = 0
numClienteZP3 = 0
numClienteZP3P = 0
numClienteZP3_10_13 = 0
numClienteZP3_13_16 = 0
numClienteZP3_16_19 = 0
numClienteZP3_19_22 = 0
numClienteZP3P_10_13 = 0
numClienteZP3P_13_16 = 0
numClienteZP3P_16_19 = 0
numClienteZP3P_19_22 = 0
tempoEsperaZP3 = 0
tempoEsperaZP3P = 0
tempoEsperaZP3Min = 999999
tempoEsperaZP3Max = 0
tempoEsperaZP3PMin = 999999
tempoEsperaZP3PMax = 0
tempoEsperaZP3_10_13 = 0
tempoEsperaZP3_10_13_Min = 999999
tempoEsperaZP3_10_13_Max = 0
tempoEsperaZP3_13_16 = 0
tempoEsperaZP3_13_16_Min = 999999
tempoEsperaZP3_13_16_Max = 0
tempoEsperaZP3_16_19 = 0
tempoEsperaZP3_16_19_Min = 999999
tempoEsperaZP3_16_19_Max = 0
tempoEsperaZP3_19_22 = 0
tempoEsperaZP3_19_22_Min = 999999
tempoEsperaZP3_19_22_Max = 0
tempoEsperaZP3P_10_13 = 0
tempoEsperaZP3P_10_13_Min = 999999
tempoEsperaZP3P_10_13_Max = 0
tempoEsperaZP3P_13_16 = 0
tempoEsperaZP3P_13_16_Min = 999999
tempoEsperaZP3P_13_16_Max = 0
tempoEsperaZP3P_16_19 = 0
tempoEsperaZP3P_16_19_Min = 999999
tempoEsperaZP3P_16_19_Max = 0
tempoEsperaZP3P_19_22 = 0
tempoEsperaZP3P_19_22_Min = 999999
tempoEsperaZP3P_19_22_Max = 0
# -------------------
filaZP4 = []
filaZP4P = []
estadoZP4 = "livre"
partidaZP4 = 999999
clienteZP4 = 0
numClienteZP4 = 0
numClienteZP4P = 0
numClienteZP4_10_13 = 0
numClienteZP4_13_16 = 0
numClienteZP4_16_19 = 0
numClienteZP4_19_22 = 0
numClienteZP4P_10_13 = 0
numClienteZP4P_13_16 = 0
numClienteZP4P_16_19 = 0
numClienteZP4P_19_22 = 0
tempoEsperaZP4 = 0
tempoEsperaZP4P = 0
tempoEsperaZP4Min = 999999
tempoEsperaZP4Max = 0
tempoEsperaZP4PMin = 999999
tempoEsperaZP4PMax = 0
tempoEsperaZP4_10_13 = 0
tempoEsperaZP4_10_13_Min = 999999
tempoEsperaZP4_10_13_Max = 0
tempoEsperaZP4_13_16 = 0
tempoEsperaZP4_13_16_Min = 999999
tempoEsperaZP4_13_16_Max = 0
tempoEsperaZP4_16_19 = 0
tempoEsperaZP4_16_19_Min = 999999
tempoEsperaZP4_16_19_Max = 0
tempoEsperaZP4_19_22 = 0
tempoEsperaZP4_19_22_Min = 999999
tempoEsperaZP4_19_22_Max = 0
tempoEsperaZP4P_10_13 = 0
tempoEsperaZP4P_10_13_Min = 999999
tempoEsperaZP4P_10_13_Max = 0
tempoEsperaZP4P_13_16 = 0
tempoEsperaZP4P_13_16_Min = 999999
tempoEsperaZP4P_13_16_Max = 0
tempoEsperaZP4P_16_19 = 0
tempoEsperaZP4P_16_19_Min = 999999
tempoEsperaZP4P_16_19_Max = 0
tempoEsperaZP4P_19_22 = 0
tempoEsperaZP4P_19_22_Min = 999999
tempoEsperaZP4P_19_22_Max = 0
# ------------------------------

# ------------------------------
#  Zona de Levantamento
# -------------------
listaZLPostos = []
# -------------------
estadoZL1 = "livre"
partidaZL1 = 999999
clienteZL1 = 0
numClienteZL1 = 0
numClienteZL1P = 0
numClienteZL1_10_13 = 0
numClienteZL1_13_16 = 0
numClienteZL1_16_19 = 0
numClienteZL1_19_22 = 0
numClienteZL1P_10_13 = 0
numClienteZL1P_13_16 = 0
numClienteZL1P_16_19 = 0
numClienteZL1P_19_22 = 0
tempoEsperaZL1 = 0
tempoEsperaZL1P = 0
tempoEsperaZL1Min = 999999
tempoEsperaZL1Max = 0
tempoEsperaZL1PMin = 999999
tempoEsperaZL1PMax = 0
tempoEsperaZL1_10_13 = 0
tempoEsperaZL1_10_13_Min = 999999
tempoEsperaZL1_10_13_Max = 0
tempoEsperaZL1_13_16 = 0
tempoEsperaZL1_13_16_Min = 999999
tempoEsperaZL1_13_16_Max = 0
tempoEsperaZL1_16_19 = 0
tempoEsperaZL1_16_19_Min = 999999
tempoEsperaZL1_16_19_Max = 0
tempoEsperaZL1_19_22 = 0
tempoEsperaZL1_19_22_Min = 999999
tempoEsperaZL1_19_22_Max = 0
tempoEsperaZL1P_10_13 = 0
tempoEsperaZL1P_10_13_Min = 999999
tempoEsperaZL1P_10_13_Max = 0
tempoEsperaZL1P_13_16 = 0
tempoEsperaZL1P_13_16_Min = 999999
tempoEsperaZL1P_13_16_Max = 0
tempoEsperaZL1P_16_19 = 0
tempoEsperaZL1P_16_19_Min = 999999
tempoEsperaZL1P_16_19_Max = 0
tempoEsperaZL1P_19_22 = 0
tempoEsperaZL1P_19_22_Min = 999999
tempoEsperaZL1P_19_22_Max = 0
# -------------------
estadoZL2 = "livre"
partidaZL2 = 999999
clienteZL2 = 0
numClienteZL2 = 0
numClienteZL2P = 0
numClienteZL2_10_13 = 0
numClienteZL2_13_16 = 0
numClienteZL2_16_19 = 0
numClienteZL2_19_22 = 0
numClienteZL2P_10_13 = 0
numClienteZL2P_13_16 = 0
numClienteZL2P_16_19 = 0
numClienteZL2P_19_22 = 0
tempoEsperaZL2 = 0
tempoEsperaZL2P = 0
tempoEsperaZL2Min = 999999
tempoEsperaZL2Max = 0
tempoEsperaZL2PMin = 999999
tempoEsperaZL2PMax = 0
tempoEsperaZL2_10_13 = 0
tempoEsperaZL2_10_13_Min = 999999
tempoEsperaZL2_10_13_Max = 0
tempoEsperaZL2_13_16 = 0
tempoEsperaZL2_13_16_Min = 999999
tempoEsperaZL2_13_16_Max = 0
tempoEsperaZL2_16_19 = 0
tempoEsperaZL2_16_19_Min = 999999
tempoEsperaZL2_16_19_Max = 0
tempoEsperaZL2_19_22 = 0
tempoEsperaZL2_19_22_Min = 999999
tempoEsperaZL2_19_22_Max = 0
tempoEsperaZL2P_10_13 = 0
tempoEsperaZL2P_10_13_Min = 999999
tempoEsperaZL2P_10_13_Max = 0
tempoEsperaZL2P_13_16 = 0
tempoEsperaZL2P_13_16_Min = 999999
tempoEsperaZL2P_13_16_Max = 0
tempoEsperaZL2P_16_19 = 0
tempoEsperaZL2P_16_19_Min = 999999
tempoEsperaZL2P_16_19_Max = 0
tempoEsperaZL2P_19_22 = 0
tempoEsperaZL2P_19_22_Min = 999999
tempoEsperaZL2P_19_22_Max = 0
# ------------------------------


clockLST = []
eventoLST = []
clienteLST = []
proxChegadaLST = []
clientequepartiu = 0

filaZVLST = []
filaZVPLST = []
filaZLLST = []
filaZLPLST = []

estadoZV1LST = []
estadoZV2LST = []
estadoZV3LST = []
estadoZV4LST = []
estadoZV5LST = []
estadoZV6LST = []
estadoZV7LST = []
estadoZV8LST = []
estadoZV9LST = []
estadoZV10LST = []
partidaZV1LST = []
partidaZV2LST = []
partidaZV3LST = []
partidaZV4LST = []
partidaZV5LST = []
partidaZV6LST = []
partidaZV7LST = []
partidaZV8LST = []
partidaZV9LST = []
partidaZV10LST = []

estadoZP1LST = []
estadoZP2LST = []
estadoZP3LST = []
estadoZP4LST = []
filaZP1LST = []
filaZP2LST = []
filaZP3LST = []
filaZP4LST = []
filaZPP1LST = []
filaZPP2LST = []
filaZPP3LST = []
filaZPP4LST = []
partidaZP1LST = []
partidaZP2LST = []
partidaZP3LST = []
partidaZP4LST = []

estadoZL1LST = []
estadoZL2LST = []
partidaZL1LST = []
partidaZL2LST = []

def rand0to1():
    hello = (int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1))
    return hello


def criarClientes():
    min = configData["NumClientes"][0]["min"]
    max = configData["NumClientes"][0]["max"]
    numeroClientes = randint(int(min), int(max))
    Clientesaux = []
    per1 = configData["taxasEntrada"][0]["per"]
    per1 = int(per1) / 100
    per2 = configData["taxasEntrada"][1]["per"]
    per2 = int(per2) / 100
    per2 = per2 + per1
    per3 = configData["taxasEntrada"][2]["per"]
    per3 = int(per3) / 100
    per3 = per3 + per2
    for x in range(1, numeroClientes + 1):
        valorEntrada = rand0to1()
        chegada = 0
        if (valorEntrada <= per1):
            chegada = randint(0, 10800)
        elif (per1 < valorEntrada <= per2):
            chegada = randint(10801, 21600)
        elif (per2 < valorEntrada <= per3):
            chegada = randint(21601, 32400)
        elif (per3 < valorEntrada):
            chegada = randint(32400, 43200)


        valorPrioritario = rand0to1()
        perPrioridade = configData["perZonaVendPrioritarios"]
        perPrioridade = int(perPrioridade) / 100
        prioridade = 1 if valorPrioritario <= perPrioridade else 0

        atndZV = rand0to1()
        tempoAtendimentoZV = 0
        tempoAtendimentoZP = 0
        tempoAtendimentoZLP = 0
        passamZP = 0
        passamZLP = 0

        per1 = configData["temposAtendimentoZonaVend"][0]["per"]
        per1 = int(per1) / 100
        per2 = configData["temposAtendimentoZonaVend"][1]["per"]
        per2 = int(per2) / 100
        per2 = per2 + per1
        per3 = configData["temposAtendimentoZonaVend"][2]["per"]
        per3 = int(per3) / 100
        per3 = per3 + per2
        per4 = configData["temposAtendimentoZonaVend"][3]["per"]
        per4 = int(per4) / 100
        per4 = per4 + per3

        if (atndZV <= per1):
            tempoAtendimentoZV = randint(1, 300)
        elif (per1 < atndZV <= per2):
            tempoAtendimentoZV = randint(301, 600)
        elif (per2 < atndZV <= per3):
            tempoAtendimentoZV = randint(601, 900)
        elif (per3 < atndZV <= per4):
            tempoAtendimentoZV = randint(901, 1200)
        elif (per4 < atndZV <= 1):
            tempoAtendimentoZV = randint(1200, 99999)


        fazemCompras = rand0to1()
        perFazemCompras = configData["perZonaVendCompras"]
        perFazemCompras = int(perFazemCompras) / 100
        per1 = configData["temposAtendimentoZonaPag"][0]["per"]
        per1 = int(per1) / 100
        per2 = configData["temposAtendimentoZonaPag"][1]["per"]
        per2 = int(per2) / 100
        per2 = per2 + per1
        per3 = configData["temposAtendimentoZonaPag"][2]["per"]
        per3 = int(per3) / 100
        per3 = per3 + per2
        per4 = configData["temposAtendimentoZonaPag"][3]["per"]
        per4 = int(per4) / 100
        per4 = per4 + per3
        if (fazemCompras <= perFazemCompras):
            atndZP = rand0to1()
            passamZP = 1
            if (atndZP <= per1):
                tempoAtendimentoZP = randint(1, 60)
            elif (per1 < atndZP <= per2):
                tempoAtendimentoZP = randint(61, 120)
            elif (per2 < atndZP <= per3):
                tempoAtendimentoZP = randint(121, 180)
            elif (per3 < atndZP < per4):
                tempoAtendimentoZP = randint(181, 240)
            else:
                passamZP = 0


            vaoLevantar = rand0to1()
            per1 = configData["temposAtendimentoZonaLev"][0]["per"]
            per1 = int(per1) / 100
            per2 = configData["temposAtendimentoZonaLev"][1]["per"]
            per2 = int(per2) / 100
            per2 = per2 + per1
            per3 = configData["temposAtendimentoZonaLev"][2]["per"]
            per3 = int(per3) / 100
            per3 = per3 + per2
            perVaoLevantar = configData["perPassamZonaLev"]
            perVaoLevantar = int(perVaoLevantar) / 100
            if (vaoLevantar <= perVaoLevantar):
                passamZLP = 1
                atndZLP = rand0to1()
                if (atndZLP <= per1):
                    tempoAtendimentoZLP = randint(1, 300)
                elif (per1 < atndZLP <= per2):
                    tempoAtendimentoZLP = randint(301, 600)
                elif (per2 < atndZLP <= per3):
                    tempoAtendimentoZLP = randint(601, 900)
                elif (per3 < atndZLP):
                    tempoAtendimentoZLP = randint(901, 1200)


                levantamTudo = rand0to1()
                perlevantamTudo = configData["perPassamZonaLevSemLevarProdutos"]
                perlevantamTudo = int(perlevantamTudo) / 100
                per1 = configData["temposAtendimentoZonaPag"][0]["per"]
                per1 = int(per1) / 100
                per2 = configData["temposAtendimentoZonaPag"][1]["per"]
                per2 = int(per2) / 100
                per2 = per2 + per1
                per3 = configData["temposAtendimentoZonaPag"][2]["per"]
                per3 = int(per3) / 100
                per3 = per3 + per2
                per4 = configData["temposAtendimentoZonaPag"][3]["per"]
                per4 = int(per4) / 100
                per4 = per4 + per3
                if (levantamTudo <= perlevantamTudo):
                    atndZP = rand0to1()
                    if (atndZP <= per1):
                        tempoAtendimentoZP = tempoAtendimentoZP + randint(1, 60)
                    elif (per1 < atndZP <= per2):
                        tempoAtendimentoZP = tempoAtendimentoZP + randint(61, 120)
                    elif (per2 < atndZP <= per3):
                        tempoAtendimentoZP = tempoAtendimentoZP + randint(121, 180)
                    elif (per3 < atndZP < per4):
                        tempoAtendimentoZP = tempoAtendimentoZP + randint(181, 240)

        Clientesaux.append(
            (chegada, prioridade, passamZP, passamZLP, tempoAtendimentoZV, tempoAtendimentoZP, tempoAtendimentoZLP))

    Clientesaux = sorted(Clientesaux, key=lambda x: x[0])
    for x in range(0, numeroClientes):
        (a, b, c, d, e, f, g) = Clientesaux[x]
        Clientes.append(((x + 1), a, b, c, d, e, f, g))
        print((x + 1), a, b, c, d, e, f, g)


def primeiraIteração():
    clockLST.append(clock)
    eventoLST.append("-")
    clienteLST.append("-")
    proxChegadaLST.append(proxChegada)
    filaZVLST.append([])
    filaZLLST.append([])

    filaZP1LST.append([])
    filaZP2LST.append([])
    filaZP3LST.append([])
    filaZP4LST.append([])

    estadoZV1LST.append(estadoZV1)
    estadoZV2LST.append(estadoZV2)
    estadoZV3LST.append(estadoZV3)
    estadoZV4LST.append(estadoZV4)
    estadoZV5LST.append(estadoZV5)
    estadoZV6LST.append(estadoZV6)
    estadoZV7LST.append(estadoZV7)
    estadoZV8LST.append(estadoZV8)
    estadoZV9LST.append(estadoZV9)
    estadoZV10LST.append(estadoZV10)
    estadoZP1LST.append(estadoZP1)
    estadoZP2LST.append(estadoZP2)
    estadoZP3LST.append(estadoZP3)
    estadoZP4LST.append(estadoZP4)
    estadoZL1LST.append(estadoZL1)
    estadoZL2LST.append(estadoZL2)

    partidaZV1LST.append(partidaZV1)
    partidaZV2LST.append(partidaZV2)
    partidaZV3LST.append(partidaZV3)
    partidaZV4LST.append(partidaZV4)
    partidaZV5LST.append(partidaZV5)
    partidaZV6LST.append(partidaZV6)
    partidaZV7LST.append(partidaZV7)
    partidaZV8LST.append(partidaZV8)
    partidaZV9LST.append(partidaZV9)
    partidaZV10LST.append(partidaZV10)
    partidaZP1LST.append(partidaZP1)
    partidaZP2LST.append(partidaZP2)
    partidaZP3LST.append(partidaZP3)
    partidaZP4LST.append(partidaZP4)
    partidaZL1LST.append(partidaZL1)
    partidaZL2LST.append(partidaZL2)


def tempo():
    global clock
    global proxChegada, partidaZV1, partidaZV2, partidaZV3, partidaZV4, partidaZV5, partidaZV6, partidaZV7, partidaZV8, partidaZV9, partidaZV10
    global partidaZP1, partidaZP2, partidaZP3, partidaZP4, partidaZL1, partidaZL2

    if proxChegada <= partidaZV1 and proxChegada <= partidaZV2 and proxChegada <= partidaZV3 and proxChegada <= partidaZV4 and proxChegada <= partidaZV5 and proxChegada <= partidaZV6 and proxChegada <= partidaZV7 and proxChegada <= partidaZV8 and proxChegada <= partidaZV9 and proxChegada <= partidaZV10 and proxChegada <= partidaZP1 and proxChegada <= partidaZP2 and proxChegada <= partidaZP3 and proxChegada <= partidaZP4 and proxChegada <= partidaZL1 and proxChegada <= partidaZL2 and proxChegada != 999999:
        clock = proxChegada
    elif partidaZV1 <= proxChegada and partidaZV1 <= partidaZV2 and partidaZV1 <= partidaZV3 and partidaZV1 <= partidaZV4 and partidaZV1 <= partidaZV5 and partidaZV1 <= partidaZV6 and partidaZV1 <= partidaZV7 and partidaZV1 <= partidaZV8 and partidaZV1 <= partidaZV9 and partidaZV1 <= partidaZV10 and partidaZV1 <= partidaZP1 and partidaZV1 <= partidaZP2 and partidaZV1 <= partidaZP3 and partidaZV1 <= partidaZP4 and partidaZV1 <= partidaZL1 and partidaZV1 <= partidaZL2 and partidaZV1 != 999999:
        clock = proxChegada
    elif partidaZV2 <= proxChegada and partidaZV2 <= partidaZV1 and partidaZV2 <= partidaZV3 and partidaZV2 <= partidaZV4 and partidaZV2 <= partidaZV5 and partidaZV2 <= partidaZV6 and partidaZV2 <= partidaZV7 and partidaZV2 <= partidaZV8 and partidaZV2 <= partidaZV9 and partidaZV2 <= partidaZV10 and partidaZV2 <= partidaZP1 and partidaZV2 <= partidaZP2 and partidaZV2 <= partidaZP3 and partidaZV2 <= partidaZP4 and partidaZV2 <= partidaZL1 and partidaZV2 <= partidaZL2 and partidaZV2 != 999999:
        clock = proxChegada
    elif partidaZV3 <= proxChegada and partidaZV3 <= partidaZV1 and partidaZV3 <= partidaZV2 and partidaZV3 <= partidaZV4 and partidaZV3 <= partidaZV5 and partidaZV3 <= partidaZV6 and partidaZV3 <= partidaZV7 and partidaZV3 <= partidaZV8 and partidaZV3 <= partidaZV9 and partidaZV3 <= partidaZV10 and partidaZV3 <= partidaZP1 and partidaZV3 <= partidaZP2 and partidaZV3 <= partidaZP3 and partidaZV3 <= partidaZP4 and partidaZV3 <= partidaZL1 and partidaZV3 <= partidaZL2 and partidaZV3 != 999999:
        clock = proxChegada
    elif partidaZV4 <= proxChegada and partidaZV4 <= partidaZV1 and partidaZV4 <= partidaZV2 and partidaZV4 <= partidaZV3 and partidaZV4 <= partidaZV5 and partidaZV4 <= partidaZV6 and partidaZV4 <= partidaZV7 and partidaZV4 <= partidaZV8 and partidaZV4 <= partidaZV9 and partidaZV4 <= partidaZV10 and partidaZV4 <= partidaZP1 and partidaZV4 <= partidaZP2 and partidaZV4 <= partidaZP3 and partidaZV4 <= partidaZP4 and partidaZV4 <= partidaZL1 and partidaZV4 <= partidaZL2 and partidaZV4 != 999999:
        clock = proxChegada
    elif partidaZV5 <= proxChegada and partidaZV5 <= partidaZV1 and partidaZV5 <= partidaZV2 and partidaZV5 <= partidaZV3 and partidaZV5 <= partidaZV4 and partidaZV5 <= partidaZV6 and partidaZV5 <= partidaZV7 and partidaZV5 <= partidaZV8 and partidaZV5 <= partidaZV9 and partidaZV5 <= partidaZV10 and partidaZV5 <= partidaZP1 and partidaZV5 <= partidaZP2 and partidaZV5 <= partidaZP3 and partidaZV5 <= partidaZP4 and partidaZV5 <= partidaZL1 and partidaZV5 <= partidaZL2 and partidaZV5 != 999999:
        clock = proxChegada
    elif partidaZV6 <= proxChegada and partidaZV6 <= partidaZV1 and partidaZV6 <= partidaZV2 and partidaZV6 <= partidaZV3 and partidaZV6 <= partidaZV4 and partidaZV6 <= partidaZV5 and partidaZV6 <= partidaZV7 and partidaZV6 <= partidaZV8 and partidaZV6 <= partidaZV9 and partidaZV6 <= partidaZV10 and partidaZV6 <= partidaZP1 and partidaZV6 <= partidaZP2 and partidaZV6 <= partidaZP3 and partidaZV6 <= partidaZP4 and partidaZV6 <= partidaZL1 and partidaZV6 <= partidaZL2 and partidaZV6 != 999999:
        clock = proxChegada
    elif partidaZV7 <= proxChegada and partidaZV7 <= partidaZV1 and partidaZV7 <= partidaZV2 and partidaZV7 <= partidaZV3 and partidaZV7 <= partidaZV4 and partidaZV7 <= partidaZV5 and partidaZV7 <= partidaZV6 and partidaZV7 <= partidaZV8 and partidaZV7 <= partidaZV9 and partidaZV7 <= partidaZV10 and partidaZV7 <= partidaZP1 and partidaZV7 <= partidaZP2 and partidaZV7 <= partidaZP3 and partidaZV7 <= partidaZP4 and partidaZV7 <= partidaZL1 and partidaZV7 <= partidaZL2 and partidaZV7 != 999999:
        clock = proxChegada
    elif partidaZV8 <= proxChegada and partidaZV8 <= partidaZV1 and partidaZV8 <= partidaZV2 and partidaZV8 <= partidaZV3 and partidaZV8 <= partidaZV4 and partidaZV8 <= partidaZV5 and partidaZV8 <= partidaZV6 and partidaZV8 <= partidaZV7 and partidaZV8 <= partidaZV9 and partidaZV8 <= partidaZV10 and partidaZV8 <= partidaZP1 and partidaZV8 <= partidaZP2 and partidaZV8 <= partidaZP3 and partidaZV8 <= partidaZP4 and partidaZV8 <= partidaZL1 and partidaZV8 <= partidaZL2 and partidaZV8 != 999999:
        clock = proxChegada
    elif partidaZV9 <= proxChegada and partidaZV9 <= partidaZV1 and partidaZV9 <= partidaZV2 and partidaZV9 <= partidaZV3 and partidaZV9 <= partidaZV4 and partidaZV9 <= partidaZV5 and partidaZV9 <= partidaZV6 and partidaZV9 <= partidaZV7 and partidaZV9 <= partidaZV8 and partidaZV9 <= partidaZV10 and partidaZV9 <= partidaZP1 and partidaZV9 <= partidaZP2 and partidaZV9 <= partidaZP3 and partidaZV9 <= partidaZP4 and partidaZV9 <= partidaZL1 and partidaZV9 <= partidaZL2 and partidaZV9 != 999999:
        clock = proxChegada
    elif partidaZV10 <= proxChegada and partidaZV10 <= partidaZV1 and partidaZV10 <= partidaZV2 and partidaZV10 <= partidaZV3 and partidaZV10 <= partidaZV4 and partidaZV10 <= partidaZV5 and partidaZV10 <= partidaZV6 and partidaZV10 <= partidaZV7 and partidaZV10 <= partidaZV8 and partidaZV10 <= partidaZV9 and partidaZV10 <= partidaZP1 and partidaZV10 <= partidaZP2 and partidaZV10 <= partidaZP3 and partidaZV10 <= partidaZP4 and partidaZV10 <= partidaZL1 and partidaZV10 <= partidaZL2 and partidaZV10 != 999999:
        clock = proxChegada
    elif partidaZP1 <= proxChegada and partidaZP1 <= partidaZV1 and partidaZP1 <= partidaZV2 and partidaZP1 <= partidaZV3 and partidaZP1 <= partidaZV4 and partidaZP1 <= partidaZV5 and partidaZP1 <= partidaZV6 and partidaZP1 <= partidaZV7 and partidaZP1 <= partidaZV8 and partidaZP1 <= partidaZV9 and partidaZP1 <= partidaZV10 and partidaZP1 <= partidaZP2 and partidaZP1 <= partidaZP3 and partidaZP1 <= partidaZP4 and partidaZP1 <= partidaZL1 and partidaZP1 <= partidaZL2 and partidaZP1 != 999999:
        clock = proxChegada
    elif partidaZP2 <= proxChegada and partidaZP2 <= partidaZV1 and partidaZP2 <= partidaZV2 and partidaZP2 <= partidaZV3 and partidaZP2 <= partidaZV4 and partidaZP2 <= partidaZV5 and partidaZP2 <= partidaZV6 and partidaZP2 <= partidaZV7 and partidaZP2 <= partidaZV8 and partidaZP2 <= partidaZV9 and partidaZP2 <= partidaZV10 and partidaZP2 <= partidaZP1 and partidaZP2 <= partidaZP3 and partidaZP2 <= partidaZP4 and partidaZP2 <= partidaZL1 and partidaZP2 <= partidaZL2 and partidaZP2 != 999999:
        clock = proxChegada
    elif partidaZP3 <= proxChegada and partidaZP3 <= partidaZV1 and partidaZP3 <= partidaZV2 and partidaZP3 <= partidaZV3 and partidaZP3 <= partidaZV4 and partidaZP3 <= partidaZV5 and partidaZP3 <= partidaZV6 and partidaZP3 <= partidaZV7 and partidaZP3 <= partidaZV8 and partidaZP3 <= partidaZV9 and partidaZP3 <= partidaZV10 and partidaZP3 <= partidaZP1 and partidaZP3 <= partidaZP2 and partidaZP3 <= partidaZP4 and partidaZP3 <= partidaZL1 and partidaZP3 <= partidaZL2 and partidaZP3 != 999999:
        clock = proxChegada
    elif partidaZP4 <= proxChegada and partidaZP4 <= partidaZV1 and partidaZP4 <= partidaZV2 and partidaZP4 <= partidaZV3 and partidaZP4 <= partidaZV4 and partidaZP4 <= partidaZV5 and partidaZP4 <= partidaZV6 and partidaZP4 <= partidaZV7 and partidaZP4 <= partidaZV8 and partidaZP4 <= partidaZV9 and partidaZP4 <= partidaZV10 and partidaZP4 <= partidaZP1 and partidaZP4 <= partidaZP2 and partidaZP4 <= partidaZP3 and partidaZP4 <= partidaZL1 and partidaZP4 <= partidaZL2 and partidaZP4 != 999999:
        clock = proxChegada
    elif partidaZL1 <= proxChegada and partidaZL1 <= partidaZV1 and partidaZL1 <= partidaZV2 and partidaZL1 <= partidaZV3 and partidaZL1 <= partidaZV4 and partidaZL1 <= partidaZV5 and partidaZL1 <= partidaZV6 and partidaZL1 <= partidaZV7 and partidaZL1 <= partidaZV8 and partidaZL1 <= partidaZV9 and partidaZL1 <= partidaZV10 and partidaZL1 <= partidaZP1 and partidaZL1 <= partidaZP2 and partidaZL1 <= partidaZP3 and partidaZL1 <= partidaZP4 and partidaZL1 <= partidaZL2 and partidaZL1 != 999999:
        clock = proxChegada
    elif partidaZL2 <= proxChegada and partidaZL2 <= partidaZV1 and partidaZL2 <= partidaZV2 and partidaZL2 <= partidaZV3 and partidaZL2 <= partidaZV4 and partidaZL2 <= partidaZV5 and partidaZL2 <= partidaZV6 and partidaZL2 <= partidaZV7 and partidaZL2 <= partidaZV8 and partidaZL2 <= partidaZV9 and partidaZL2 <= partidaZV10 and partidaZL2 <= partidaZP1 and partidaZL2 <= partidaZP2 and partidaZL2 <= partidaZP3 and partidaZL2 <= partidaZP4 and partidaZL2 <= partidaZL1 and partidaZL2 != 999999:
        clock = proxChegada


def buscarProximoCliente():
    global numeroUltimoCliente
    numeroUltimoCliente = numeroUltimoCliente + 1
    if numeroUltimoCliente <= len(Clientes):
        return Clientes[numeroUltimoCliente - 1]
    else:
        return ((999999, 0, 0, 0, 0, 0, 0, 0))


def buscarProximoCliente2():
    global numeroUltimoCliente
    ult = numeroUltimoCliente + 1
    if ult <= len(Clientes):
        return Clientes[ult - 1]
    else:
        return ((999999, 0, 0, 0, 0, 0, 0, 0))


def atualizaEstatisticas(seg,fila,prioridade,inter):
    global tempoEsperaZV1, tempoEsperaZV2, tempoEsperaZV3, tempoEsperaZV4, tempoEsperaZV5, tempoEsperaZV6, tempoEsperaZV7, tempoEsperaZV8, tempoEsperaZV9, tempoEsperaZV10
    global tempoEsperaZV1P, tempoEsperaZV2P, tempoEsperaZV3P, tempoEsperaZV4P, tempoEsperaZV5P, tempoEsperaZV6P, tempoEsperaZV7P, tempoEsperaZV8P, tempoEsperaZV9P, tempoEsperaZV10P
    global tempoEsperaZV1PMin, tempoEsperaZV1PMax, tempoEsperaZV2PMin, tempoEsperaZV2PMax, tempoEsperaZV3PMin, tempoEsperaZV3PMax, tempoEsperaZV4PMin, tempoEsperaZV4PMax, tempoEsperaZV5PMin, tempoEsperaZV5PMax, tempoEsperaZV6PMin, tempoEsperaZV6PMax, tempoEsperaZV7PMin, tempoEsperaZV7PMax, tempoEsperaZV8PMin, tempoEsperaZV8PMax, tempoEsperaZV9PMin, tempoEsperaZV9PMax, tempoEsperaZV10PMin, tempoEsperaZV10PMax
    global tempoEsperaZP1PMin, tempoEsperaZP1PMax, tempoEsperaZP2PMin, tempoEsperaZP2PMax, tempoEsperaZP3PMin, tempoEsperaZP3PMax, tempoEsperaZP4PMin, tempoEsperaZP4PMax
    global tempoEsperaZL1PMin, tempoEsperaZL1PMax, tempoEsperaZL2PMin, tempoEsperaZL2PMax
    global tempoEsperaZV1Min, tempoEsperaZV1Max, tempoEsperaZV1_10_13, tempoEsperaZV1_10_13_Max, tempoEsperaZV1_10_13_Min, tempoEsperaZV1_13_16_Max, tempoEsperaZV1_13_16_Min, tempoEsperaZV1_16_19, tempoEsperaZV1_16_19_Max, tempoEsperaZV1_16_19_Min, tempoEsperaZV1_19_22, tempoEsperaZV1_19_22_Max, tempoEsperaZV1_19_22_Min
    global tempoEsperaZV2Min, tempoEsperaZV2Max, tempoEsperaZV2_10_13, tempoEsperaZV2_10_13_Max, tempoEsperaZV2_10_13_Min, tempoEsperaZV2_13_16_Max, tempoEsperaZV2_13_16_Min, tempoEsperaZV2_16_19, tempoEsperaZV2_16_19_Max, tempoEsperaZV2_16_19_Min, tempoEsperaZV2_19_22, tempoEsperaZV2_19_22_Max, tempoEsperaZV2_19_22_Min
    global tempoEsperaZV3Min, tempoEsperaZV3Max, tempoEsperaZV3_10_13, tempoEsperaZV3_10_13_Max, tempoEsperaZV3_10_13_Min, tempoEsperaZV3_13_16_Max, tempoEsperaZV3_13_16_Min, tempoEsperaZV3_16_19, tempoEsperaZV3_16_19_Max, tempoEsperaZV3_16_19_Min, tempoEsperaZV3_19_22, tempoEsperaZV3_19_22_Max, tempoEsperaZV3_19_22_Min
    global tempoEsperaZV4Min, tempoEsperaZV4Max, tempoEsperaZV4_10_13, tempoEsperaZV4_10_13_Max, tempoEsperaZV4_10_13_Min, tempoEsperaZV4_13_16_Max, tempoEsperaZV4_13_16_Min, tempoEsperaZV4_16_19, tempoEsperaZV4_16_19_Max, tempoEsperaZV4_16_19_Min, tempoEsperaZV4_19_22, tempoEsperaZV4_19_22_Max, tempoEsperaZV4_19_22_Min
    global tempoEsperaZV5Min, tempoEsperaZV5Max, tempoEsperaZV5_10_13, tempoEsperaZV5_10_13_Max, tempoEsperaZV5_10_13_Min, tempoEsperaZV5_13_16_Max, tempoEsperaZV5_13_16_Min, tempoEsperaZV5_16_19, tempoEsperaZV5_16_19_Max, tempoEsperaZV5_16_19_Min, tempoEsperaZV5_19_22, tempoEsperaZV5_19_22_Max, tempoEsperaZV5_19_22_Min
    global tempoEsperaZV6Min, tempoEsperaZV6Max, tempoEsperaZV6_10_13, tempoEsperaZV6_10_13_Max, tempoEsperaZV6_10_13_Min, tempoEsperaZV6_13_16_Max, tempoEsperaZV6_13_16_Min, tempoEsperaZV6_16_19, tempoEsperaZV6_16_19_Max, tempoEsperaZV6_16_19_Min, tempoEsperaZV6_19_22, tempoEsperaZV6_19_22_Max, tempoEsperaZV6_19_22_Min
    global tempoEsperaZV7Min, tempoEsperaZV7Max, tempoEsperaZV7_10_13, tempoEsperaZV7_10_13_Max, tempoEsperaZV7_10_13_Min, tempoEsperaZV7_13_16_Max, tempoEsperaZV7_13_16_Min, tempoEsperaZV7_16_19, tempoEsperaZV7_16_19_Max, tempoEsperaZV7_16_19_Min, tempoEsperaZV7_19_22, tempoEsperaZV7_19_22_Max, tempoEsperaZV7_19_22_Min
    global tempoEsperaZV8Min, tempoEsperaZV8Max, tempoEsperaZV8_10_13, tempoEsperaZV8_10_13_Max, tempoEsperaZV8_10_13_Min, tempoEsperaZV8_13_16_Max, tempoEsperaZV8_13_16_Min, tempoEsperaZV8_16_19, tempoEsperaZV8_16_19_Max, tempoEsperaZV8_16_19_Min, tempoEsperaZV8_19_22, tempoEsperaZV8_19_22_Max, tempoEsperaZV8_19_22_Min
    global tempoEsperaZV9Min, tempoEsperaZV9Max, tempoEsperaZV9_10_13, tempoEsperaZV9_10_13_Max, tempoEsperaZV9_10_13_Min, tempoEsperaZV9_13_16_Max, tempoEsperaZV9_13_16_Min, tempoEsperaZV9_16_19, tempoEsperaZV9_16_19_Max, tempoEsperaZV9_16_19_Min, tempoEsperaZV9_19_22, tempoEsperaZV9_19_22_Max, tempoEsperaZV9_19_22_Min
    global tempoEsperaZV10Min, tempoEsperaZV10Max, tempoEsperaZV10_10_13, tempoEsperaZV10_10_13_Max, tempoEsperaZV10_10_13_Min, tempoEsperaZV10_13_16_Max, tempoEsperaZV10_13_16_Min, tempoEsperaZV10_16_19, tempoEsperaZV10_16_19_Max, tempoEsperaZV10_16_19_Min, tempoEsperaZV10_19_22, tempoEsperaZV10_19_22_Max, tempoEsperaZV10_19_22_Min
    global tempoEsperaZP1, tempoEsperaZP1P, tempoEsperaZP2, tempoEsperaZP2P, tempoEsperaZP3, tempoEsperaZP3P, tempoEsperaZP4, tempoEsperaZP4P
    global tempoEsperaZP1Min, tempoEsperaZP1Max, tempoEsperaZP1_10_13, tempoEsperaZP1_10_13_Max, tempoEsperaZP1_10_13_Min, tempoEsperaZP1_13_16, tempoEsperaZP1_13_16_Max, tempoEsperaZP1_13_16_Min, tempoEsperaZP1_16_19, tempoEsperaZP1_16_19_Max, tempoEsperaZP1_16_19_Min, tempoEsperaZP1_19_22, tempoEsperaZP1_19_22_Max, tempoEsperaZP1_19_22_Min
    global tempoEsperaZP2Min, tempoEsperaZP2Max, tempoEsperaZP2_10_13, tempoEsperaZP2_10_13_Max, tempoEsperaZP2_10_13_Min, tempoEsperaZP2_13_16, tempoEsperaZP2_13_16_Max, tempoEsperaZP2_13_16_Min, tempoEsperaZP2_16_19, tempoEsperaZP2_16_19_Max, tempoEsperaZP2_16_19_Min, tempoEsperaZP2_19_22, tempoEsperaZP2_19_22_Max, tempoEsperaZP2_19_22_Min
    global tempoEsperaZP3Min, tempoEsperaZP3Max, tempoEsperaZP3_10_13, tempoEsperaZP3_10_13_Max, tempoEsperaZP3_10_13_Min, tempoEsperaZP3_13_16, tempoEsperaZP3_13_16_Max, tempoEsperaZP3_13_16_Min, tempoEsperaZP3_16_19, tempoEsperaZP3_16_19_Max, tempoEsperaZP3_16_19_Min, tempoEsperaZP3_19_22, tempoEsperaZP3_19_22_Max, tempoEsperaZP3_19_22_Min
    global tempoEsperaZP4Min, tempoEsperaZP4Max, tempoEsperaZP4_10_13, tempoEsperaZP4_10_13_Max, tempoEsperaZP4_10_13_Min, tempoEsperaZP4_13_16, tempoEsperaZP4_13_16_Max, tempoEsperaZP4_13_16_Min, tempoEsperaZP4_16_19, tempoEsperaZP4_16_19_Max, tempoEsperaZP4_16_19_Min, tempoEsperaZP4_19_22, tempoEsperaZP4_19_22_Max, tempoEsperaZP4_19_22_Min
    global tempoEsperaZL1Min, tempoEsperaZL1Max, tempoEsperaZL1_10_13, tempoEsperaZL1_10_13_Max, tempoEsperaZL1_10_13_Min, tempoEsperaZL1_13_16, tempoEsperaZL1_13_16_Max, tempoEsperaZL1_13_16_Min, tempoEsperaZL1_16_19, tempoEsperaZL1_16_19_Max, tempoEsperaZL1_16_19_Min, tempoEsperaZL1_19_22, tempoEsperaZL1_19_22_Max, tempoEsperaZL1_19_22_Min
    global tempoEsperaZL2Min, tempoEsperaZL2Max, tempoEsperaZL2_10_13, tempoEsperaZL2_10_13_Max, tempoEsperaZL2_10_13_Min, tempoEsperaZL2_13_16, tempoEsperaZL2_13_16_Max, tempoEsperaZL2_13_16_Min, tempoEsperaZL2_16_19, tempoEsperaZL2_16_19_Max, tempoEsperaZL2_16_19_Min, tempoEsperaZL2_19_22, tempoEsperaZL2_19_22_Max, tempoEsperaZL2_19_22_Min

    global tempoEsperaZV1PMin, tempoEsperaZV1PMax, tempoEsperaZV1P_10_13, tempoEsperaZV1P_10_13_Max, tempoEsperaZV1P_10_13_Min, tempoEsperaZV1P_13_16, tempoEsperaZV1P_13_16_Max, tempoEsperaZV1P_13_16_Min, tempoEsperaZV1P_16_19, tempoEsperaZV1P_16_19_Max, tempoEsperaZV1P_16_19_Min, tempoEsperaZV1P_19_22, tempoEsperaZV1P_19_22_Max, tempoEsperaZV1P_19_22_Min
    global tempoEsperaZV2PMin, tempoEsperaZV2PMax, tempoEsperaZV2P_10_13, tempoEsperaZV2P_10_13_Max, tempoEsperaZV2P_10_13_Min, tempoEsperaZV2P_13_16, tempoEsperaZV2P_13_16_Max, tempoEsperaZV2P_13_16_Min, tempoEsperaZV2P_16_19, tempoEsperaZV2P_16_19_Max, tempoEsperaZV2P_16_19_Min, tempoEsperaZV2P_19_22, tempoEsperaZV2P_19_22_Max, tempoEsperaZV2P_19_22_Min
    global tempoEsperaZV3PMin, tempoEsperaZV3PMax, tempoEsperaZV3P_10_13, tempoEsperaZV3P_10_13_Max, tempoEsperaZV3P_10_13_Min, tempoEsperaZV3P_13_16, tempoEsperaZV3P_13_16_Max, tempoEsperaZV3P_13_16_Min, tempoEsperaZV3P_16_19, tempoEsperaZV3P_16_19_Max, tempoEsperaZV3P_16_19_Min, tempoEsperaZV3P_19_22, tempoEsperaZV3P_19_22_Max, tempoEsperaZV3P_19_22_Min
    global tempoEsperaZV4PMin, tempoEsperaZV4PMax, tempoEsperaZV4P_10_13, tempoEsperaZV4P_10_13_Max, tempoEsperaZV4P_10_13_Min, tempoEsperaZV4P_13_16, tempoEsperaZV4P_13_16_Max, tempoEsperaZV4P_13_16_Min, tempoEsperaZV4P_16_19, tempoEsperaZV4P_16_19_Max, tempoEsperaZV4P_16_19_Min, tempoEsperaZV4P_19_22, tempoEsperaZV4P_19_22_Max, tempoEsperaZV4P_19_22_Min
    global tempoEsperaZV5PMin, tempoEsperaZV5PMax, tempoEsperaZV5P_10_13, tempoEsperaZV5P_10_13_Max, tempoEsperaZV5P_10_13_Min, tempoEsperaZV5P_13_16, tempoEsperaZV5P_13_16_Max, tempoEsperaZV5P_13_16_Min, tempoEsperaZV5P_16_19, tempoEsperaZV5P_16_19_Max, tempoEsperaZV5P_16_19_Min, tempoEsperaZV5P_19_22, tempoEsperaZV5P_19_22_Max, tempoEsperaZV5P_19_22_Min
    global tempoEsperaZV6PMin, tempoEsperaZV6PMax, tempoEsperaZV6P_10_13, tempoEsperaZV6P_10_13_Max, tempoEsperaZV6P_10_13_Min, tempoEsperaZV6P_13_16, tempoEsperaZV6P_13_16_Max, tempoEsperaZV6P_13_16_Min, tempoEsperaZV6P_16_19, tempoEsperaZV6P_16_19_Max, tempoEsperaZV6P_16_19_Min, tempoEsperaZV6P_19_22, tempoEsperaZV6P_19_22_Max, tempoEsperaZV6P_19_22_Min
    global tempoEsperaZV7PMin, tempoEsperaZV7PMax, tempoEsperaZV7P_10_13, tempoEsperaZV7P_10_13_Max, tempoEsperaZV7P_10_13_Min, tempoEsperaZV7P_13_16, tempoEsperaZV7P_13_16_Max, tempoEsperaZV7P_13_16_Min, tempoEsperaZV7P_16_19, tempoEsperaZV7P_16_19_Max, tempoEsperaZV7P_16_19_Min, tempoEsperaZV7P_19_22, tempoEsperaZV7P_19_22_Max, tempoEsperaZV7P_19_22_Min
    global tempoEsperaZV8PMin, tempoEsperaZV8PMax, tempoEsperaZV8P_10_13, tempoEsperaZV8P_10_13_Max, tempoEsperaZV8P_10_13_Min, tempoEsperaZV8P_13_16, tempoEsperaZV8P_13_16_Max, tempoEsperaZV8P_13_16_Min, tempoEsperaZV8P_16_19, tempoEsperaZV8P_16_19_Max, tempoEsperaZV8P_16_19_Min, tempoEsperaZV8P_19_22, tempoEsperaZV8P_19_22_Max, tempoEsperaZV8P_19_22_Min
    global tempoEsperaZV9PMin, tempoEsperaZV9PMax, tempoEsperaZV9P_10_13, tempoEsperaZV9P_10_13_Max, tempoEsperaZV9P_10_13_Min, tempoEsperaZV9P_13_16, tempoEsperaZV9P_13_16_Max, tempoEsperaZV9P_13_16_Min, tempoEsperaZV9P_16_19, tempoEsperaZV9P_16_19_Max, tempoEsperaZV9P_16_19_Min, tempoEsperaZV9P_19_22, tempoEsperaZV9P_19_22_Max, tempoEsperaZV9P_19_22_Min
    global tempoEsperaZV10PMin, tempoEsperaZV10PMax, tempoEsperaZV10P_10_13, tempoEsperaZV10P_10_13_Max, tempoEsperaZV10P_10_13_Min, tempoEsperaZV10P_13_16, tempoEsperaZV10P_13_16_Max, tempoEsperaZV10P_13_16_Min, tempoEsperaZV10P_16_19, tempoEsperaZV10P_16_19_Max, tempoEsperaZV10P_16_19_Min, tempoEsperaZV10P_19_22, tempoEsperaZV10P_19_22_Max, tempoEsperaZV10P_19_22_Min
    global tempoEsperaZP1PMin, tempoEsperaZP1PMax, tempoEsperaZP1P_10_13, tempoEsperaZP1P_10_13_Max, tempoEsperaZP1P_10_13_Min, tempoEsperaZP1P_13_16, tempoEsperaZP1P_13_16_Max, tempoEsperaZP1P_13_16_Min, tempoEsperaZP1P_16_19, tempoEsperaZP1P_16_19_Max, tempoEsperaZP1P_16_19_Min, tempoEsperaZP1P_19_22, tempoEsperaZP1P_19_22_Max, tempoEsperaZP1P_19_22_Min
    global tempoEsperaZP2PMin, tempoEsperaZP2PMax, tempoEsperaZP2P_10_13, tempoEsperaZP2P_10_13_Max, tempoEsperaZP2P_10_13_Min, tempoEsperaZP2P_13_16, tempoEsperaZP2P_13_16_Max, tempoEsperaZP2P_13_16_Min, tempoEsperaZP2P_16_19, tempoEsperaZP2P_16_19_Max, tempoEsperaZP2P_16_19_Min, tempoEsperaZP2P_19_22, tempoEsperaZP2P_19_22_Max, tempoEsperaZP2P_19_22_Min
    global tempoEsperaZP3PMin, tempoEsperaZP3PMax, tempoEsperaZP3P_10_13, tempoEsperaZP3P_10_13_Max, tempoEsperaZP3P_10_13_Min, tempoEsperaZP3P_13_16, tempoEsperaZP3P_13_16_Max, tempoEsperaZP3P_13_16_Min, tempoEsperaZP3P_16_19, tempoEsperaZP3P_16_19_Max, tempoEsperaZP3P_16_19_Min, tempoEsperaZP3P_19_22, tempoEsperaZP3P_19_22_Max, tempoEsperaZP3P_19_22_Min
    global tempoEsperaZP4PMin, tempoEsperaZP4PMax, tempoEsperaZP4P_10_13, tempoEsperaZP4P_10_13_Max, tempoEsperaZP4P_10_13_Min, tempoEsperaZP4P_13_16, tempoEsperaZP4P_13_16_Max, tempoEsperaZP4P_13_16_Min, tempoEsperaZP4P_16_19, tempoEsperaZP4P_16_19_Max, tempoEsperaZP4P_16_19_Min, tempoEsperaZP4P_19_22, tempoEsperaZP4P_19_22_Max, tempoEsperaZP4P_19_22_Min
    global tempoEsperaZL1PMin, tempoEsperaZL1PMax, tempoEsperaZL1P_10_13, tempoEsperaZL1P_10_13_Max, tempoEsperaZL1P_10_13_Min, tempoEsperaZL1P_13_16, tempoEsperaZL1P_13_16_Max, tempoEsperaZL1P_13_16_Min, tempoEsperaZL1P_16_19, tempoEsperaZL1P_16_19_Max, tempoEsperaZL1P_16_19_Min, tempoEsperaZL1P_19_22, tempoEsperaZL1P_19_22_Max, tempoEsperaZL1P_19_22_Min
    global tempoEsperaZL2PMin, tempoEsperaZL2PMax, tempoEsperaZL2P_10_13, tempoEsperaZL2P_10_13_Max, tempoEsperaZL2P_10_13_Min, tempoEsperaZL2P_13_16, tempoEsperaZL2P_13_16_Max, tempoEsperaZL2P_13_16_Min, tempoEsperaZL2P_16_19, tempoEsperaZL2P_16_19_Max, tempoEsperaZL2P_16_19_Min, tempoEsperaZL2P_19_22, tempoEsperaZL2P_19_22_Max, tempoEsperaZL2P_19_22_Min

    global numClienteZV1, numClienteZV1P, numClienteZV1_10_13, numClienteZV1_13_16, numClienteZV1_16_19, numClienteZV1_19_22, numClienteZV1P_10_13, numClienteZV1P_13_16, numClienteZV1P_16_19, numClienteZV1P_19_22
    global numClienteZV2, numClienteZV2P, numClienteZV2_10_13, numClienteZV2_13_16, numClienteZV2_16_19, numClienteZV2_19_22, numClienteZV2P_10_13, numClienteZV2P_13_16, numClienteZV2P_16_19, numClienteZV2P_19_22
    global numClienteZV3, numClienteZV3P, numClienteZV3_10_13, numClienteZV3_13_16, numClienteZV3_16_19, numClienteZV3_19_22, numClienteZV3P_10_13, numClienteZV3P_13_16, numClienteZV3P_16_19, numClienteZV3P_19_22
    global numClienteZV4, numClienteZV4P, numClienteZV4_10_13, numClienteZV4_13_16, numClienteZV4_16_19, numClienteZV4_19_22, numClienteZV4P_10_13, numClienteZV4P_13_16, numClienteZV4P_16_19, numClienteZV4P_19_22
    global numClienteZV5, numClienteZV5P, numClienteZV5_10_13, numClienteZV5_13_16, numClienteZV5_16_19, numClienteZV5_19_22, numClienteZV5P_10_13, numClienteZV5P_13_16, numClienteZV5P_16_19, numClienteZV5P_19_22
    global numClienteZV6, numClienteZV6P, numClienteZV6_10_13, numClienteZV6_13_16, numClienteZV6_16_19, numClienteZV6_19_22, numClienteZV6P_10_13, numClienteZV6P_13_16, numClienteZV6P_16_19, numClienteZV6P_19_22
    global numClienteZV7, numClienteZV7P, numClienteZV7_10_13, numClienteZV7_13_16, numClienteZV7_16_19, numClienteZV7_19_22, numClienteZV7P_10_13, numClienteZV7P_13_16, numClienteZV7P_16_19, numClienteZV7P_19_22
    global numClienteZV8, numClienteZV8P, numClienteZV8_10_13, numClienteZV8_13_16, numClienteZV8_16_19, numClienteZV8_19_22, numClienteZV8P_10_13, numClienteZV8P_13_16, numClienteZV8P_16_19, numClienteZV8P_19_22
    global numClienteZV9, numClienteZV9P, numClienteZV9_10_13, numClienteZV9_13_16, numClienteZV9_16_19, numClienteZV9_19_22, numClienteZV9P_10_13, numClienteZV9P_13_16, numClienteZV9P_16_19, numClienteZV9P_19_22
    global numClienteZV10, numClienteZV10P, numClienteZV10_10_13, numClienteZV10_13_16, numClienteZV10_16_19, numClienteZV10_19_22, numClienteZV10P_10_13, numClienteZV10P_13_16, numClienteZV10P_16_19, numClienteZV10P_19_22

    global numClienteZP1, numClienteZP1P, numClienteZP1_10_13, numClienteZP1_13_16, numClienteZP1_16_19, numClienteZP1_19_22, numClienteZP1P_10_13, numClienteZP1P_13_16, numClienteZP1P_16_19, numClienteZP1P_19_22
    global numClienteZP2, numClienteZP2P, numClienteZP2_10_13, numClienteZP2_13_16, numClienteZP2_16_19, numClienteZP2_19_22, numClienteZP2P_10_13, numClienteZP2P_13_16, numClienteZP2P_16_19, numClienteZP2P_19_22
    global numClienteZP3, numClienteZP3P, numClienteZP3_10_13, numClienteZP3_13_16, numClienteZP3_16_19, numClienteZP3_19_22, numClienteZP3P_10_13, numClienteZP3P_13_16, numClienteZP3P_16_19, numClienteZP3P_19_22
    global numClienteZP4, numClienteZP4P, numClienteZP4_10_13, numClienteZP4_13_16, numClienteZP4_16_19, numClienteZP4_19_22, numClienteZP4P_10_13, numClienteZP4P_13_16, numClienteZP4P_16_19, numClienteZP4P_19_22

    global numClienteZL1, numClienteZL1P, numClienteZL1_10_13, numClienteZL1_13_16, numClienteZL1_16_19, numClienteZL1_19_22, numClienteZL1P_10_13, numClienteZL1P_13_16, numClienteZL1P_16_19, numClienteZL1P_19_22
    global numClienteZL2, numClienteZL2P, numClienteZL2_10_13, numClienteZL2_13_16, numClienteZL2_16_19, numClienteZL2_19_22, numClienteZL2P_10_13, numClienteZL2P_13_16, numClienteZL2P_16_19, numClienteZL2P_19_22

    global tempoEsperaZV1_13_16, tempoEsperaZV2_13_16, tempoEsperaZV3_13_16, tempoEsperaZV4_13_16, tempoEsperaZV5_13_16, tempoEsperaZV6_13_16, tempoEsperaZV7_13_16, tempoEsperaZV8_13_16, tempoEsperaZV9_13_16, tempoEsperaZV10_13_16
    global tempoEsperaZP1_13_16, tempoEsperaZP2_13_16, tempoEsperaZP3_13_16, tempoEsperaZP4_13_16, tempoEsperaZL1_13_16, tempoEsperaZL2_13_16
    global tempoEsperaZL1P, tempoEsperaZL2P, tempoEsperaZL1, tempoEsperaZL2

    if fila=="ZV1":
        if prioridade==1:
            numClienteZV1P=numClienteZV1P+1
            tempoEsperaZV1P=tempoEsperaZV1P+seg
            if seg<tempoEsperaZV1PMin:
                tempoEsperaZV1PMin=seg
            if seg>tempoEsperaZV1PMax:
                tempoEsperaZV1PMax=seg
            if inter>=10 and inter<13:
                numClienteZV1P_10_13 = numClienteZV1P_10_13 +1
                tempoEsperaZV1P_10_13=tempoEsperaZV1P_10_13+seg
                if seg < tempoEsperaZV1P_10_13_Min:
                    tempoEsperaZV1P_10_13_Min = tempoEsperaZV1P_10_13_Min+seg
                if seg > tempoEsperaZV1P_10_13_Max:
                    tempoEsperaZV1P_10_13_Max = tempoEsperaZV1P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV1P_13_16 = numClienteZV1P_13_16 + 1
                tempoEsperaZV1P_13_16 = tempoEsperaZV1P_13_16 + seg
                if seg < tempoEsperaZV1P_13_16_Min:
                    tempoEsperaZV1P_13_16_Min = tempoEsperaZV1P_13_16_Min + seg
                if seg > tempoEsperaZV1P_13_16_Max:
                    tempoEsperaZV1P_13_16_Max = tempoEsperaZV1P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV1P_16_19 = numClienteZV1P_16_19 + 1
                tempoEsperaZV1P_16_19 = tempoEsperaZV1P_16_19 + seg
                if seg < tempoEsperaZV1P_16_19_Min:
                    tempoEsperaZV1P_16_19_Min = tempoEsperaZV1P_16_19_Min + seg
                if seg > tempoEsperaZV1P_16_19_Max:
                    tempoEsperaZV1P_16_19_Max = tempoEsperaZV1P_16_19_Max + seg
            if inter >= 19:
                numClienteZV1P_19_22 = numClienteZV1P_19_22 + 1
                tempoEsperaZV1P_19_22 = tempoEsperaZV1P_19_22 + seg
                if seg < tempoEsperaZV1P_19_22_Min:
                    tempoEsperaZV1P_19_22_Min = tempoEsperaZV1P_19_22_Min + seg
                if seg > tempoEsperaZV1P_19_22_Max:
                    tempoEsperaZV1P_19_22_Max = tempoEsperaZV1P_19_22_Max + seg
        else:
            numClienteZV1 = numClienteZV1 + 1
            tempoEsperaZV1 = tempoEsperaZV1 + seg
            if seg < tempoEsperaZV1Min:
                tempoEsperaZV1Min = seg
            if seg > tempoEsperaZV1Max:
                tempoEsperaZV1Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV1_10_13 = numClienteZV1_10_13 + 1
                tempoEsperaZV1_10_13 = tempoEsperaZV1_10_13 + seg
                if seg < tempoEsperaZV1_10_13_Min:
                    tempoEsperaZV1_10_13_Min = tempoEsperaZV1_10_13_Min + seg
                if seg > tempoEsperaZV1_10_13_Max:
                    tempoEsperaZV1_10_13_Max = tempoEsperaZV1_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV1_13_16 = numClienteZV1_13_16 + 1
                tempoEsperaZV1_13_16 = tempoEsperaZV1_13_16 + seg
                if seg < tempoEsperaZV1_13_16_Min:
                    tempoEsperaZV1_13_16_Min = tempoEsperaZV1_13_16_Min + seg
                if seg > tempoEsperaZV1_13_16_Max:
                    tempoEsperaZV1_13_16_Max = tempoEsperaZV1_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV1_16_19 = numClienteZV1_16_19 + 1
                tempoEsperaZV1_16_19 = tempoEsperaZV1_16_19 + seg
                if seg < tempoEsperaZV1_16_19_Min:
                    tempoEsperaZV1_16_19_Min = tempoEsperaZV1_16_19_Min + seg
                if seg > tempoEsperaZV1_16_19_Max:
                    tempoEsperaZV1_16_19_Max = tempoEsperaZV1_16_19_Max + seg
            if inter >= 19:
                numClienteZV1_19_22 = numClienteZV1_19_22 + 1
                tempoEsperaZV1_19_22 = tempoEsperaZV1_19_22 + seg
                if seg < tempoEsperaZV1_19_22_Min:
                    tempoEsperaZV1_19_22_Min = tempoEsperaZV1_19_22_Min + seg
                if seg > tempoEsperaZV1_19_22_Max:
                    tempoEsperaZV1_19_22_Max = tempoEsperaZV1_19_22_Max + seg

    elif fila=="ZV2":
        if prioridade==1:
            numClienteZV2P=numClienteZV2P+1
            tempoEsperaZV2P=tempoEsperaZV2P+seg
            if seg<tempoEsperaZV2PMin:
                tempoEsperaZV2PMin=seg
            if seg>tempoEsperaZV2PMax:
                tempoEsperaZV2PMax=seg
            if inter>=10 and inter<13:
                numClienteZV2P_10_13 = numClienteZV2P_10_13 +1
                tempoEsperaZV2P_10_13=tempoEsperaZV2P_10_13+seg
                if seg < tempoEsperaZV2P_10_13_Min:
                    tempoEsperaZV2P_10_13_Min = tempoEsperaZV2P_10_13_Min+seg
                if seg > tempoEsperaZV2P_10_13_Max:
                    tempoEsperaZV2P_10_13_Max = tempoEsperaZV2P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV2P_13_16 = numClienteZV2P_13_16 + 1
                tempoEsperaZV2P_13_16 = tempoEsperaZV2P_13_16 + seg
                if seg < tempoEsperaZV2P_13_16_Min:
                    tempoEsperaZV2P_13_16_Min = tempoEsperaZV2P_13_16_Min + seg
                if seg > tempoEsperaZV2P_13_16_Max:
                    tempoEsperaZV2P_13_16_Max = tempoEsperaZV2P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV2P_16_19 = numClienteZV2P_16_19 + 1
                tempoEsperaZV2P_16_19 = tempoEsperaZV2P_16_19 + seg
                if seg < tempoEsperaZV2P_16_19_Min:
                    tempoEsperaZV2P_16_19_Min = tempoEsperaZV2P_16_19_Min + seg
                if seg > tempoEsperaZV2P_16_19_Max:
                    tempoEsperaZV2P_16_19_Max = tempoEsperaZV2P_16_19_Max + seg
            if inter >= 19:
                numClienteZV2P_19_22 = numClienteZV2P_19_22 + 1
                tempoEsperaZV2P_19_22 = tempoEsperaZV2P_19_22 + seg
                if seg < tempoEsperaZV2P_19_22_Min:
                    tempoEsperaZV2P_19_22_Min = tempoEsperaZV2P_19_22_Min + seg
                if seg > tempoEsperaZV2P_19_22_Max:
                    tempoEsperaZV2P_19_22_Max = tempoEsperaZV2P_19_22_Max + seg
        else:
            numClienteZV2 = numClienteZV2 + 1
            tempoEsperaZV2 = tempoEsperaZV2 + seg
            if seg < tempoEsperaZV2Min:
                tempoEsperaZV2Min = seg
            if seg > tempoEsperaZV2Max:
                tempoEsperaZV2Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV2_10_13 = numClienteZV2_10_13 + 1
                tempoEsperaZV2_10_13 = tempoEsperaZV2_10_13 + seg
                if seg < tempoEsperaZV2_10_13_Min:
                    tempoEsperaZV2_10_13_Min = tempoEsperaZV2_10_13_Min + seg
                if seg > tempoEsperaZV2_10_13_Max:
                    tempoEsperaZV2_10_13_Max = tempoEsperaZV2_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV2_13_16 = numClienteZV2_13_16 + 1
                tempoEsperaZV2_13_16 = tempoEsperaZV2_13_16 + seg
                if seg < tempoEsperaZV2_13_16_Min:
                    tempoEsperaZV2_13_16_Min = tempoEsperaZV2_13_16_Min + seg
                if seg > tempoEsperaZV2_13_16_Max:
                    tempoEsperaZV2_13_16_Max = tempoEsperaZV2_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV2_16_19 = numClienteZV2_16_19 + 1
                tempoEsperaZV2_16_19 = tempoEsperaZV2_16_19 + seg
                if seg < tempoEsperaZV2_16_19_Min:
                    tempoEsperaZV2_16_19_Min = tempoEsperaZV2_16_19_Min + seg
                if seg > tempoEsperaZV2_16_19_Max:
                    tempoEsperaZV2_16_19_Max = tempoEsperaZV2_16_19_Max + seg
            if inter >= 19:
                numClienteZV2_19_22 = numClienteZV2_19_22 + 1
                tempoEsperaZV2_19_22 = tempoEsperaZV2_19_22 + seg
                if seg < tempoEsperaZV2_19_22_Min:
                    tempoEsperaZV2_19_22_Min = tempoEsperaZV2_19_22_Min + seg
                if seg > tempoEsperaZV2_19_22_Max:
                    tempoEsperaZV2_19_22_Max = tempoEsperaZV2_19_22_Max + seg

    elif fila=="ZV3":
        if prioridade==1:
            numClienteZV3P=numClienteZV3P+1
            tempoEsperaZV3P=tempoEsperaZV3P+seg
            if seg<tempoEsperaZV3PMin:
                tempoEsperaZV3PMin=seg
            if seg>tempoEsperaZV3PMax:
                tempoEsperaZV3PMax=seg
            if inter>=10 and inter<13:
                numClienteZV3P_10_13 = numClienteZV3P_10_13 +1
                tempoEsperaZV3P_10_13=tempoEsperaZV3P_10_13+seg
                if seg < tempoEsperaZV3P_10_13_Min:
                    tempoEsperaZV3P_10_13_Min = tempoEsperaZV3P_10_13_Min+seg
                if seg > tempoEsperaZV3P_10_13_Max:
                    tempoEsperaZV3P_10_13_Max = tempoEsperaZV3P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV3P_13_16 = numClienteZV3P_13_16 + 1
                tempoEsperaZV3P_13_16 = tempoEsperaZV3P_13_16 + seg
                if seg < tempoEsperaZV3P_13_16_Min:
                    tempoEsperaZV3P_13_16_Min = tempoEsperaZV3P_13_16_Min + seg
                if seg > tempoEsperaZV3P_13_16_Max:
                    tempoEsperaZV3P_13_16_Max = tempoEsperaZV3P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV3P_16_19 = numClienteZV3P_16_19 + 1
                tempoEsperaZV3P_16_19 = tempoEsperaZV3P_16_19 + seg
                if seg < tempoEsperaZV3P_16_19_Min:
                    tempoEsperaZV3P_16_19_Min = tempoEsperaZV3P_16_19_Min + seg
                if seg > tempoEsperaZV3P_16_19_Max:
                    tempoEsperaZV3P_16_19_Max = tempoEsperaZV3P_16_19_Max + seg
            if inter >= 19:
                numClienteZV3P_19_22 = numClienteZV3P_19_22 + 1
                tempoEsperaZV3P_19_22 = tempoEsperaZV3P_19_22 + seg
                if seg < tempoEsperaZV3P_19_22_Min:
                    tempoEsperaZV3P_19_22_Min = tempoEsperaZV3P_19_22_Min + seg
                if seg > tempoEsperaZV3P_19_22_Max:
                    tempoEsperaZV3P_19_22_Max = tempoEsperaZV3P_19_22_Max + seg
        else:
            numClienteZV3 = numClienteZV3 + 1
            tempoEsperaZV3 = tempoEsperaZV3 + seg
            if seg < tempoEsperaZV3Min:
                tempoEsperaZV3Min = seg
            if seg > tempoEsperaZV3Max:
                tempoEsperaZV3Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV3_10_13 = numClienteZV3_10_13 + 1
                tempoEsperaZV3_10_13 = tempoEsperaZV3_10_13 + seg
                if seg < tempoEsperaZV3_10_13_Min:
                    tempoEsperaZV3_10_13_Min = tempoEsperaZV3_10_13_Min + seg
                if seg > tempoEsperaZV3_10_13_Max:
                    tempoEsperaZV3_10_13_Max = tempoEsperaZV3_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV3_13_16 = numClienteZV3_13_16 + 1
                tempoEsperaZV3_13_16 = tempoEsperaZV3_13_16 + seg
                if seg < tempoEsperaZV3_13_16_Min:
                    tempoEsperaZV3_13_16_Min = tempoEsperaZV3_13_16_Min + seg
                if seg > tempoEsperaZV3_13_16_Max:
                    tempoEsperaZV3_13_16_Max = tempoEsperaZV3_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV3_16_19 = numClienteZV3_16_19 + 1
                tempoEsperaZV3_16_19 = tempoEsperaZV3_16_19 + seg
                if seg < tempoEsperaZV3_16_19_Min:
                    tempoEsperaZV3_16_19_Min = tempoEsperaZV3_16_19_Min + seg
                if seg > tempoEsperaZV3_16_19_Max:
                    tempoEsperaZV3_16_19_Max = tempoEsperaZV3_16_19_Max + seg
            if inter >= 19:
                numClienteZV3_19_22 = numClienteZV3_19_22 + 1
                tempoEsperaZV3_19_22 = tempoEsperaZV3_19_22 + seg
                if seg < tempoEsperaZV3_19_22_Min:
                    tempoEsperaZV3_19_22_Min = tempoEsperaZV3_19_22_Min + seg
                if seg > tempoEsperaZV3_19_22_Max:
                    tempoEsperaZV3_19_22_Max = tempoEsperaZV3_19_22_Max + seg

    elif fila=="ZV4":
        if prioridade==1:
            numClienteZV4P=numClienteZV4P+1
            tempoEsperaZV4P=tempoEsperaZV4P+seg
            if seg<tempoEsperaZV4PMin:
                tempoEsperaZV4PMin=seg
            if seg>tempoEsperaZV4PMax:
                tempoEsperaZV4PMax=seg
            if inter>=10 and inter<13:
                numClienteZV4P_10_13 = numClienteZV4P_10_13 +1
                tempoEsperaZV4P_10_13=tempoEsperaZV4P_10_13+seg
                if seg < tempoEsperaZV4P_10_13_Min:
                    tempoEsperaZV4P_10_13_Min = tempoEsperaZV4P_10_13_Min+seg
                if seg > tempoEsperaZV4P_10_13_Max:
                    tempoEsperaZV4P_10_13_Max = tempoEsperaZV4P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV4P_13_16 = numClienteZV4P_13_16 + 1
                tempoEsperaZV4P_13_16 = tempoEsperaZV4P_13_16 + seg
                if seg < tempoEsperaZV4P_13_16_Min:
                    tempoEsperaZV4P_13_16_Min = tempoEsperaZV4P_13_16_Min + seg
                if seg > tempoEsperaZV4P_13_16_Max:
                    tempoEsperaZV4P_13_16_Max = tempoEsperaZV4P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV4P_16_19 = numClienteZV4P_16_19 + 1
                tempoEsperaZV4P_16_19 = tempoEsperaZV4P_16_19 + seg
                if seg < tempoEsperaZV4P_16_19_Min:
                    tempoEsperaZV4P_16_19_Min = tempoEsperaZV4P_16_19_Min + seg
                if seg > tempoEsperaZV4P_16_19_Max:
                    tempoEsperaZV4P_16_19_Max = tempoEsperaZV4P_16_19_Max + seg
            if inter >= 19:
                numClienteZV4P_19_22 = numClienteZV4P_19_22 + 1
                tempoEsperaZV4P_19_22 = tempoEsperaZV4P_19_22 + seg
                if seg < tempoEsperaZV4P_19_22_Min:
                    tempoEsperaZV4P_19_22_Min = tempoEsperaZV4P_19_22_Min + seg
                if seg > tempoEsperaZV4P_19_22_Max:
                    tempoEsperaZV4P_19_22_Max = tempoEsperaZV4P_19_22_Max + seg
        else:
            numClienteZV4 = numClienteZV4 + 1
            tempoEsperaZV4 = tempoEsperaZV4 + seg
            if seg < tempoEsperaZV4Min:
                tempoEsperaZV4Min = seg
            if seg > tempoEsperaZV4Max:
                tempoEsperaZV4Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV4_10_13 = numClienteZV4_10_13 + 1
                tempoEsperaZV4_10_13 = tempoEsperaZV4_10_13 + seg
                if seg < tempoEsperaZV4_10_13_Min:
                    tempoEsperaZV4_10_13_Min = tempoEsperaZV4_10_13_Min + seg
                if seg > tempoEsperaZV4_10_13_Max:
                    tempoEsperaZV4_10_13_Max = tempoEsperaZV4_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV4_13_16 = numClienteZV4_13_16 + 1
                tempoEsperaZV4_13_16 = tempoEsperaZV4_13_16 + seg
                if seg < tempoEsperaZV4_13_16_Min:
                    tempoEsperaZV4_13_16_Min = tempoEsperaZV4_13_16_Min + seg
                if seg > tempoEsperaZV4_13_16_Max:
                    tempoEsperaZV4_13_16_Max = tempoEsperaZV4_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV4_16_19 = numClienteZV4_16_19 + 1
                tempoEsperaZV4_16_19 = tempoEsperaZV4_16_19 + seg
                if seg < tempoEsperaZV4_16_19_Min:
                    tempoEsperaZV4_16_19_Min = tempoEsperaZV4_16_19_Min + seg
                if seg > tempoEsperaZV4_16_19_Max:
                    tempoEsperaZV4_16_19_Max = tempoEsperaZV4_16_19_Max + seg
            if inter >= 19:
                numClienteZV4_19_22 = numClienteZV4_19_22 + 1
                tempoEsperaZV4_19_22 = tempoEsperaZV4_19_22 + seg
                if seg < tempoEsperaZV4_19_22_Min:
                    tempoEsperaZV4_19_22_Min = tempoEsperaZV4_19_22_Min + seg
                if seg > tempoEsperaZV4_19_22_Max:
                    tempoEsperaZV4_19_22_Max = tempoEsperaZV4_19_22_Max + seg


    elif fila=="ZV5":
        if prioridade==1:
            numClienteZV5P=numClienteZV5P+1
            tempoEsperaZV5P=tempoEsperaZV5P+seg
            if seg<tempoEsperaZV5PMin:
                tempoEsperaZV5PMin=seg
            if seg>tempoEsperaZV5PMax:
                tempoEsperaZV5PMax=seg
            if inter>=10 and inter<13:
                numClienteZV5P_10_13 = numClienteZV5P_10_13 +1
                tempoEsperaZV5P_10_13=tempoEsperaZV5P_10_13+seg
                if seg < tempoEsperaZV5P_10_13_Min:
                    tempoEsperaZV5P_10_13_Min = tempoEsperaZV5P_10_13_Min+seg
                if seg > tempoEsperaZV5P_10_13_Max:
                    tempoEsperaZV5P_10_13_Max = tempoEsperaZV5P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV5P_13_16 = numClienteZV5P_13_16 + 1
                tempoEsperaZV5P_13_16 = tempoEsperaZV5P_13_16 + seg
                if seg < tempoEsperaZV5P_13_16_Min:
                    tempoEsperaZV5P_13_16_Min = tempoEsperaZV5P_13_16_Min + seg
                if seg > tempoEsperaZV5P_13_16_Max:
                    tempoEsperaZV5P_13_16_Max = tempoEsperaZV5P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV5P_16_19 = numClienteZV5P_16_19 + 1
                tempoEsperaZV5P_16_19 = tempoEsperaZV5P_16_19 + seg
                if seg < tempoEsperaZV5P_16_19_Min:
                    tempoEsperaZV5P_16_19_Min = tempoEsperaZV5P_16_19_Min + seg
                if seg > tempoEsperaZV5P_16_19_Max:
                    tempoEsperaZV5P_16_19_Max = tempoEsperaZV5P_16_19_Max + seg
            if inter >= 19:
                numClienteZV5P_19_22 = numClienteZV5P_19_22 + 1
                tempoEsperaZV5P_19_22 = tempoEsperaZV5P_19_22 + seg
                if seg < tempoEsperaZV5P_19_22_Min:
                    tempoEsperaZV5P_19_22_Min = tempoEsperaZV5P_19_22_Min + seg
                if seg > tempoEsperaZV5P_19_22_Max:
                    tempoEsperaZV5P_19_22_Max = tempoEsperaZV5P_19_22_Max + seg
        else:
            numClienteZV5 = numClienteZV5 + 1
            tempoEsperaZV5 = tempoEsperaZV5 + seg
            if seg < tempoEsperaZV5Min:
                tempoEsperaZV5Min = seg
            if seg > tempoEsperaZV5Max:
                tempoEsperaZV5Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV5_10_13 = numClienteZV5_10_13 + 1
                tempoEsperaZV5_10_13 = tempoEsperaZV5_10_13 + seg
                if seg < tempoEsperaZV5_10_13_Min:
                    tempoEsperaZV5_10_13_Min = tempoEsperaZV5_10_13_Min + seg
                if seg > tempoEsperaZV5_10_13_Max:
                    tempoEsperaZV5_10_13_Max = tempoEsperaZV5_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV5_13_16 = numClienteZV5_13_16 + 1
                tempoEsperaZV5_13_16 = tempoEsperaZV5_13_16 + seg
                if seg < tempoEsperaZV5_13_16_Min:
                    tempoEsperaZV5_13_16_Min = tempoEsperaZV5_13_16_Min + seg
                if seg > tempoEsperaZV5_13_16_Max:
                    tempoEsperaZV5_13_16_Max = tempoEsperaZV5_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV5_16_19 = numClienteZV5_16_19 + 1
                tempoEsperaZV5_16_19 = tempoEsperaZV5_16_19 + seg
                if seg < tempoEsperaZV5_16_19_Min:
                    tempoEsperaZV5_16_19_Min = tempoEsperaZV5_16_19_Min + seg
                if seg > tempoEsperaZV5_16_19_Max:
                    tempoEsperaZV5_16_19_Max = tempoEsperaZV5_16_19_Max + seg
            if inter >= 19:
                numClienteZV5_19_22 = numClienteZV5_19_22 + 1
                tempoEsperaZV5_19_22 = tempoEsperaZV5_19_22 + seg
                if seg < tempoEsperaZV5_19_22_Min:
                    tempoEsperaZV5_19_22_Min = tempoEsperaZV5_19_22_Min + seg
                if seg > tempoEsperaZV5_19_22_Max:
                    tempoEsperaZV5_19_22_Max = tempoEsperaZV5_19_22_Max + seg

    elif fila=="ZV6":
        if prioridade==1:
            numClienteZV6P=numClienteZV6P+1
            tempoEsperaZV6P=tempoEsperaZV6P+seg
            if seg<tempoEsperaZV6PMin:
                tempoEsperaZV6PMin=seg
            if seg>tempoEsperaZV6PMax:
                tempoEsperaZV6PMax=seg
            if inter>=10 and inter<13:
                numClienteZV6P_10_13 = numClienteZV6P_10_13 +1
                tempoEsperaZV6P_10_13=tempoEsperaZV6P_10_13+seg
                if seg < tempoEsperaZV6P_10_13_Min:
                    tempoEsperaZV6P_10_13_Min = tempoEsperaZV6P_10_13_Min+seg
                if seg > tempoEsperaZV6P_10_13_Max:
                    tempoEsperaZV6P_10_13_Max = tempoEsperaZV6P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV6P_13_16 = numClienteZV6P_13_16 + 1
                tempoEsperaZV6P_13_16 = tempoEsperaZV6P_13_16 + seg
                if seg < tempoEsperaZV6P_13_16_Min:
                    tempoEsperaZV6P_13_16_Min = tempoEsperaZV6P_13_16_Min + seg
                if seg > tempoEsperaZV6P_13_16_Max:
                    tempoEsperaZV6P_13_16_Max = tempoEsperaZV6P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV6P_16_19 = numClienteZV6P_16_19 + 1
                tempoEsperaZV6P_16_19 = tempoEsperaZV6P_16_19 + seg
                if seg < tempoEsperaZV6P_16_19_Min:
                    tempoEsperaZV6P_16_19_Min = tempoEsperaZV6P_16_19_Min + seg
                if seg > tempoEsperaZV6P_16_19_Max:
                    tempoEsperaZV6P_16_19_Max = tempoEsperaZV6P_16_19_Max + seg
            if inter >= 19:
                numClienteZV6P_19_22 = numClienteZV6P_19_22 + 1
                tempoEsperaZV6P_19_22 = tempoEsperaZV6P_19_22 + seg
                if seg < tempoEsperaZV6P_19_22_Min:
                    tempoEsperaZV6P_19_22_Min = tempoEsperaZV6P_19_22_Min + seg
                if seg > tempoEsperaZV6P_19_22_Max:
                    tempoEsperaZV6P_19_22_Max = tempoEsperaZV6P_19_22_Max + seg
        else:
            numClienteZV6 = numClienteZV6 + 1
            tempoEsperaZV6 = tempoEsperaZV6 + seg
            if seg < tempoEsperaZV6Min:
                tempoEsperaZV6Min = seg
            if seg > tempoEsperaZV6Max:
                tempoEsperaZV6Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV6_10_13 = numClienteZV6_10_13 + 1
                tempoEsperaZV6_10_13 = tempoEsperaZV6_10_13 + seg
                if seg < tempoEsperaZV6_10_13_Min:
                    tempoEsperaZV6_10_13_Min = tempoEsperaZV6_10_13_Min + seg
                if seg > tempoEsperaZV6_10_13_Max:
                    tempoEsperaZV6_10_13_Max = tempoEsperaZV6_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV6_13_16 = numClienteZV6_13_16 + 1
                tempoEsperaZV6_13_16 = tempoEsperaZV6_13_16 + seg
                if seg < tempoEsperaZV6_13_16_Min:
                    tempoEsperaZV6_13_16_Min = tempoEsperaZV6_13_16_Min + seg
                if seg > tempoEsperaZV6_13_16_Max:
                    tempoEsperaZV6_13_16_Max = tempoEsperaZV6_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV6_16_19 = numClienteZV6_16_19 + 1
                tempoEsperaZV6_16_19 = tempoEsperaZV6_16_19 + seg
                if seg < tempoEsperaZV6_16_19_Min:
                    tempoEsperaZV6_16_19_Min = tempoEsperaZV6_16_19_Min + seg
                if seg > tempoEsperaZV6_16_19_Max:
                    tempoEsperaZV6_16_19_Max = tempoEsperaZV6_16_19_Max + seg
            if inter >= 19:
                numClienteZV6_19_22 = numClienteZV6_19_22 + 1
                tempoEsperaZV6_19_22 = tempoEsperaZV6_19_22 + seg
                if seg < tempoEsperaZV6_19_22_Min:
                    tempoEsperaZV6_19_22_Min = tempoEsperaZV6_19_22_Min + seg
                if seg > tempoEsperaZV6_19_22_Max:
                    tempoEsperaZV6_19_22_Max = tempoEsperaZV6_19_22_Max + seg


    elif fila=="ZV7":
        if prioridade==1:
            numClienteZV7P=numClienteZV7P+1
            tempoEsperaZV7P=tempoEsperaZV7P+seg
            if seg<tempoEsperaZV7PMin:
                tempoEsperaZV7PMin=seg
            if seg>tempoEsperaZV7PMax:
                tempoEsperaZV7PMax=seg
            if inter>=10 and inter<13:
                numClienteZV7P_10_13 = numClienteZV7P_10_13 +1
                tempoEsperaZV7P_10_13=tempoEsperaZV7P_10_13+seg
                if seg < tempoEsperaZV7P_10_13_Min:
                    tempoEsperaZV7P_10_13_Min = tempoEsperaZV7P_10_13_Min+seg
                if seg > tempoEsperaZV7P_10_13_Max:
                    tempoEsperaZV7P_10_13_Max = tempoEsperaZV7P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV7P_13_16 = numClienteZV7P_13_16 + 1
                tempoEsperaZV7P_13_16 = tempoEsperaZV7P_13_16 + seg
                if seg < tempoEsperaZV7P_13_16_Min:
                    tempoEsperaZV7P_13_16_Min = tempoEsperaZV7P_13_16_Min + seg
                if seg > tempoEsperaZV7P_13_16_Max:
                    tempoEsperaZV7P_13_16_Max = tempoEsperaZV7P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV7P_16_19 = numClienteZV7P_16_19 + 1
                tempoEsperaZV7P_16_19 = tempoEsperaZV7P_16_19 + seg
                if seg < tempoEsperaZV7P_16_19_Min:
                    tempoEsperaZV7P_16_19_Min = tempoEsperaZV7P_16_19_Min + seg
                if seg > tempoEsperaZV7P_16_19_Max:
                    tempoEsperaZV7P_16_19_Max = tempoEsperaZV7P_16_19_Max + seg
            if inter >= 19:
                numClienteZV7P_19_22 = numClienteZV7P_19_22 + 1
                tempoEsperaZV7P_19_22 = tempoEsperaZV7P_19_22 + seg
                if seg < tempoEsperaZV7P_19_22_Min:
                    tempoEsperaZV7P_19_22_Min = tempoEsperaZV7P_19_22_Min + seg
                if seg > tempoEsperaZV7P_19_22_Max:
                    tempoEsperaZV7P_19_22_Max = tempoEsperaZV7P_19_22_Max + seg
        else:
            numClienteZV7 = numClienteZV7 + 1
            tempoEsperaZV7 = tempoEsperaZV7 + seg
            if seg < tempoEsperaZV7Min:
                tempoEsperaZV7Min = seg
            if seg > tempoEsperaZV7Max:
                tempoEsperaZV7Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV7_10_13 = numClienteZV7_10_13 + 1
                tempoEsperaZV7_10_13 = tempoEsperaZV7_10_13 + seg
                if seg < tempoEsperaZV7_10_13_Min:
                    tempoEsperaZV7_10_13_Min = tempoEsperaZV7_10_13_Min + seg
                if seg > tempoEsperaZV7_10_13_Max:
                    tempoEsperaZV7_10_13_Max = tempoEsperaZV7_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV7_13_16 = numClienteZV7_13_16 + 1
                tempoEsperaZV7_13_16 = tempoEsperaZV7_13_16 + seg
                if seg < tempoEsperaZV7_13_16_Min:
                    tempoEsperaZV7_13_16_Min = tempoEsperaZV7_13_16_Min + seg
                if seg > tempoEsperaZV7_13_16_Max:
                    tempoEsperaZV7_13_16_Max = tempoEsperaZV7_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV7_16_19 = numClienteZV7_16_19 + 1
                tempoEsperaZV7_16_19 = tempoEsperaZV7_16_19 + seg
                if seg < tempoEsperaZV7_16_19_Min:
                    tempoEsperaZV7_16_19_Min = tempoEsperaZV7_16_19_Min + seg
                if seg > tempoEsperaZV7_16_19_Max:
                    tempoEsperaZV7_16_19_Max = tempoEsperaZV7_16_19_Max + seg
            if inter >= 19:
                numClienteZV7_19_22 = numClienteZV7_19_22 + 1
                tempoEsperaZV7_19_22 = tempoEsperaZV7_19_22 + seg
                if seg < tempoEsperaZV7_19_22_Min:
                    tempoEsperaZV7_19_22_Min = tempoEsperaZV7_19_22_Min + seg
                if seg > tempoEsperaZV7_19_22_Max:
                    tempoEsperaZV7_19_22_Max = tempoEsperaZV7_19_22_Max + seg

    elif fila=="ZV8":
        if prioridade==1:
            numClienteZV8P=numClienteZV8P+1
            tempoEsperaZV8P=tempoEsperaZV8P+seg
            if seg<tempoEsperaZV8PMin:
                tempoEsperaZV8PMin=seg
            if seg>tempoEsperaZV8PMax:
                tempoEsperaZV8PMax=seg
            if inter>=10 and inter<13:
                numClienteZV8P_10_13 = numClienteZV8P_10_13 +1
                tempoEsperaZV8P_10_13=tempoEsperaZV8P_10_13+seg
                if seg < tempoEsperaZV8P_10_13_Min:
                    tempoEsperaZV8P_10_13_Min = tempoEsperaZV8P_10_13_Min+seg
                if seg > tempoEsperaZV8P_10_13_Max:
                    tempoEsperaZV8P_10_13_Max = tempoEsperaZV8P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV8P_13_16 = numClienteZV8P_13_16 + 1
                tempoEsperaZV8P_13_16 = tempoEsperaZV8P_13_16 + seg
                if seg < tempoEsperaZV8P_13_16_Min:
                    tempoEsperaZV8P_13_16_Min = tempoEsperaZV8P_13_16_Min + seg
                if seg > tempoEsperaZV8P_13_16_Max:
                    tempoEsperaZV8P_13_16_Max = tempoEsperaZV8P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV8P_16_19 = numClienteZV8P_16_19 + 1
                tempoEsperaZV8P_16_19 = tempoEsperaZV8P_16_19 + seg
                if seg < tempoEsperaZV8P_16_19_Min:
                    tempoEsperaZV8P_16_19_Min = tempoEsperaZV8P_16_19_Min + seg
                if seg > tempoEsperaZV8P_16_19_Max:
                    tempoEsperaZV8P_16_19_Max = tempoEsperaZV8P_16_19_Max + seg
            if inter >= 19:
                numClienteZV8P_19_22 = numClienteZV8P_19_22 + 1
                tempoEsperaZV8P_19_22 = tempoEsperaZV8P_19_22 + seg
                if seg < tempoEsperaZV8P_19_22_Min:
                    tempoEsperaZV8P_19_22_Min = tempoEsperaZV8P_19_22_Min + seg
                if seg > tempoEsperaZV8P_19_22_Max:
                    tempoEsperaZV8P_19_22_Max = tempoEsperaZV8P_19_22_Max + seg
        else:
            numClienteZV8 = numClienteZV8 + 1
            tempoEsperaZV8 = tempoEsperaZV8 + seg
            if seg < tempoEsperaZV8Min:
                tempoEsperaZV8Min = seg
            if seg > tempoEsperaZV8Max:
                tempoEsperaZV8Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV8_10_13 = numClienteZV8_10_13 + 1
                tempoEsperaZV8_10_13 = tempoEsperaZV8_10_13 + seg
                if seg < tempoEsperaZV8_10_13_Min:
                    tempoEsperaZV8_10_13_Min = tempoEsperaZV8_10_13_Min + seg
                if seg > tempoEsperaZV8_10_13_Max:
                    tempoEsperaZV8_10_13_Max = tempoEsperaZV8_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV8_13_16 = numClienteZV8_13_16 + 1
                tempoEsperaZV8_13_16 = tempoEsperaZV8_13_16 + seg
                if seg < tempoEsperaZV8_13_16_Min:
                    tempoEsperaZV8_13_16_Min = tempoEsperaZV8_13_16_Min + seg
                if seg > tempoEsperaZV8_13_16_Max:
                    tempoEsperaZV8_13_16_Max = tempoEsperaZV8_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV8_16_19 = numClienteZV8_16_19 + 1
                tempoEsperaZV8_16_19 = tempoEsperaZV8_16_19 + seg
                if seg < tempoEsperaZV8_16_19_Min:
                    tempoEsperaZV8_16_19_Min = tempoEsperaZV8_16_19_Min + seg
                if seg > tempoEsperaZV8_16_19_Max:
                    tempoEsperaZV8_16_19_Max = tempoEsperaZV8_16_19_Max + seg
            if inter >= 19:
                numClienteZV8_19_22 = numClienteZV8_19_22 + 1
                tempoEsperaZV8_19_22 = tempoEsperaZV8_19_22 + seg
                if seg < tempoEsperaZV8_19_22_Min:
                    tempoEsperaZV8_19_22_Min = tempoEsperaZV8_19_22_Min + seg
                if seg > tempoEsperaZV8_19_22_Max:
                    tempoEsperaZV8_19_22_Max = tempoEsperaZV8_19_22_Max + seg

    elif fila=="ZV9":
        if prioridade==1:
            numClienteZV9P=numClienteZV9P+1
            tempoEsperaZV9P=tempoEsperaZV9P+seg
            if seg<tempoEsperaZV9PMin:
                tempoEsperaZV9PMin=seg
            if seg>tempoEsperaZV9PMax:
                tempoEsperaZV9PMax=seg
            if inter>=10 and inter<13:
                numClienteZV9P_10_13 = numClienteZV9P_10_13 +1
                tempoEsperaZV9P_10_13=tempoEsperaZV9P_10_13+seg
                if seg < tempoEsperaZV9P_10_13_Min:
                    tempoEsperaZV9P_10_13_Min = tempoEsperaZV9P_10_13_Min+seg
                if seg > tempoEsperaZV9P_10_13_Max:
                    tempoEsperaZV9P_10_13_Max = tempoEsperaZV9P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV9P_13_16 = numClienteZV9P_13_16 + 1
                tempoEsperaZV9P_13_16 = tempoEsperaZV9P_13_16 + seg
                if seg < tempoEsperaZV9P_13_16_Min:
                    tempoEsperaZV9P_13_16_Min = tempoEsperaZV9P_13_16_Min + seg
                if seg > tempoEsperaZV9P_13_16_Max:
                    tempoEsperaZV9P_13_16_Max = tempoEsperaZV9P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV9P_16_19 = numClienteZV9P_16_19 + 1
                tempoEsperaZV9P_16_19 = tempoEsperaZV9P_16_19 + seg
                if seg < tempoEsperaZV9P_16_19_Min:
                    tempoEsperaZV9P_16_19_Min = tempoEsperaZV9P_16_19_Min + seg
                if seg > tempoEsperaZV9P_16_19_Max:
                    tempoEsperaZV9P_16_19_Max = tempoEsperaZV9P_16_19_Max + seg
            if inter >= 19:
                numClienteZV9P_19_22 = numClienteZV9P_19_22 + 1
                tempoEsperaZV9P_19_22 = tempoEsperaZV9P_19_22 + seg
                if seg < tempoEsperaZV9P_19_22_Min:
                    tempoEsperaZV9P_19_22_Min = tempoEsperaZV9P_19_22_Min + seg
                if seg > tempoEsperaZV9P_19_22_Max:
                    tempoEsperaZV9P_19_22_Max = tempoEsperaZV9P_19_22_Max + seg
        else:
            numClienteZV9 = numClienteZV9 + 1
            tempoEsperaZV9 = tempoEsperaZV9 + seg
            if seg < tempoEsperaZV9Min:
                tempoEsperaZV9Min = seg
            if seg > tempoEsperaZV9Max:
                tempoEsperaZV9Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV9_10_13 = numClienteZV9_10_13 + 1
                tempoEsperaZV9_10_13 = tempoEsperaZV9_10_13 + seg
                if seg < tempoEsperaZV9_10_13_Min:
                    tempoEsperaZV9_10_13_Min = tempoEsperaZV9_10_13_Min + seg
                if seg > tempoEsperaZV9_10_13_Max:
                    tempoEsperaZV9_10_13_Max = tempoEsperaZV9_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV9_13_16 = numClienteZV9_13_16 + 1
                tempoEsperaZV9_13_16 = tempoEsperaZV9_13_16 + seg
                if seg < tempoEsperaZV9_13_16_Min:
                    tempoEsperaZV9_13_16_Min = tempoEsperaZV9_13_16_Min + seg
                if seg > tempoEsperaZV9_13_16_Max:
                    tempoEsperaZV9_13_16_Max = tempoEsperaZV9_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV9_16_19 = numClienteZV9_16_19 + 1
                tempoEsperaZV9_16_19 = tempoEsperaZV9_16_19 + seg
                if seg < tempoEsperaZV9_16_19_Min:
                    tempoEsperaZV9_16_19_Min = tempoEsperaZV9_16_19_Min + seg
                if seg > tempoEsperaZV9_16_19_Max:
                    tempoEsperaZV9_16_19_Max = tempoEsperaZV9_16_19_Max + seg
            if inter >= 19:
                numClienteZV9_19_22 = numClienteZV9_19_22 + 1
                tempoEsperaZV9_19_22 = tempoEsperaZV9_19_22 + seg
                if seg < tempoEsperaZV9_19_22_Min:
                    tempoEsperaZV9_19_22_Min = tempoEsperaZV9_19_22_Min + seg
                if seg > tempoEsperaZV9_19_22_Max:
                    tempoEsperaZV9_19_22_Max = tempoEsperaZV9_19_22_Max + seg

    elif fila=="ZV10":
        if prioridade==1:
            numClienteZV10P=numClienteZV10P+1
            tempoEsperaZV10P=tempoEsperaZV10P+seg
            if seg<tempoEsperaZV10PMin:
                tempoEsperaZV10PMin=seg
            if seg>tempoEsperaZV10PMax:
                tempoEsperaZV10PMax=seg
            if inter>=10 and inter<13:
                numClienteZV10P_10_13 = numClienteZV10P_10_13 +1
                tempoEsperaZV10P_10_13=tempoEsperaZV10P_10_13+seg
                if seg < tempoEsperaZV10P_10_13_Min:
                    tempoEsperaZV10P_10_13_Min = tempoEsperaZV10P_10_13_Min+seg
                if seg > tempoEsperaZV10P_10_13_Max:
                    tempoEsperaZV10P_10_13_Max = tempoEsperaZV10P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZV10P_13_16 = numClienteZV10P_13_16 + 1
                tempoEsperaZV10P_13_16 = tempoEsperaZV10P_13_16 + seg
                if seg < tempoEsperaZV10P_13_16_Min:
                    tempoEsperaZV10P_13_16_Min = tempoEsperaZV10P_13_16_Min + seg
                if seg > tempoEsperaZV10P_13_16_Max:
                    tempoEsperaZV10P_13_16_Max = tempoEsperaZV10P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV10P_16_19 = numClienteZV10P_16_19 + 1
                tempoEsperaZV10P_16_19 = tempoEsperaZV10P_16_19 + seg
                if seg < tempoEsperaZV10P_16_19_Min:
                    tempoEsperaZV10P_16_19_Min = tempoEsperaZV10P_16_19_Min + seg
                if seg > tempoEsperaZV10P_16_19_Max:
                    tempoEsperaZV10P_16_19_Max = tempoEsperaZV10P_16_19_Max + seg
            if inter >= 19:
                numClienteZV10P_19_22 = numClienteZV10P_19_22 + 1
                tempoEsperaZV10P_19_22 = tempoEsperaZV10P_19_22 + seg
                if seg < tempoEsperaZV10P_19_22_Min:
                    tempoEsperaZV10P_19_22_Min = tempoEsperaZV10P_19_22_Min + seg
                if seg > tempoEsperaZV10P_19_22_Max:
                    tempoEsperaZV10P_19_22_Max = tempoEsperaZV10P_19_22_Max + seg
        else:
            numClienteZV10 = numClienteZV10 + 1
            tempoEsperaZV10 = tempoEsperaZV10 + seg
            if seg < tempoEsperaZV10Min:
                tempoEsperaZV10Min = seg
            if seg > tempoEsperaZV10Max:
                tempoEsperaZV10Max = seg
            if inter >= 10 and inter < 13:
                numClienteZV10_10_13 = numClienteZV10_10_13 + 1
                tempoEsperaZV10_10_13 = tempoEsperaZV10_10_13 + seg
                if seg < tempoEsperaZV10_10_13_Min:
                    tempoEsperaZV10_10_13_Min = tempoEsperaZV10_10_13_Min + seg
                if seg > tempoEsperaZV10_10_13_Max:
                    tempoEsperaZV10_10_13_Max = tempoEsperaZV10_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZV10_13_16 = numClienteZV10_13_16 + 1
                tempoEsperaZV10_13_16 = tempoEsperaZV10_13_16 + seg
                if seg < tempoEsperaZV10_13_16_Min:
                    tempoEsperaZV10_13_16_Min = tempoEsperaZV10_13_16_Min + seg
                if seg > tempoEsperaZV10_13_16_Max:
                    tempoEsperaZV10_13_16_Max = tempoEsperaZV10_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZV10_16_19 = numClienteZV10_16_19 + 1
                tempoEsperaZV10_16_19 = tempoEsperaZV10_16_19 + seg
                if seg < tempoEsperaZV10_16_19_Min:
                    tempoEsperaZV10_16_19_Min = tempoEsperaZV10_16_19_Min + seg
                if seg > tempoEsperaZV10_16_19_Max:
                    tempoEsperaZV10_16_19_Max = tempoEsperaZV10_16_19_Max + seg
            if inter >= 19:
                numClienteZV10_19_22 = numClienteZV10_19_22 + 1
                tempoEsperaZV10_19_22 = tempoEsperaZV10_19_22 + seg
                if seg < tempoEsperaZV10_19_22_Min:
                    tempoEsperaZV10_19_22_Min = tempoEsperaZV10_19_22_Min + seg
                if seg > tempoEsperaZV10_19_22_Max:
                    tempoEsperaZV10_19_22_Max = tempoEsperaZV10_19_22_Max + seg


    elif fila=="ZP1":
        if prioridade==1:
            numClienteZP1P=numClienteZP1P+1
            tempoEsperaZP1P=tempoEsperaZP1P+seg
            if seg<tempoEsperaZP1PMin:
                tempoEsperaZP1PMin=seg
            if seg>tempoEsperaZP1PMax:
                tempoEsperaZP1PMax=seg
            if inter>=10 and inter<13:
                numClienteZP1P_10_13 = numClienteZP1P_10_13 +1
                tempoEsperaZP1P_10_13=tempoEsperaZP1P_10_13+seg
                if seg < tempoEsperaZP1P_10_13_Min:
                    tempoEsperaZP1P_10_13_Min = tempoEsperaZP1P_10_13_Min+seg
                if seg > tempoEsperaZP1P_10_13_Max:
                    tempoEsperaZP1P_10_13_Max = tempoEsperaZP1P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZP1P_13_16 = numClienteZP1P_13_16 + 1
                tempoEsperaZP1P_13_16 = tempoEsperaZP1P_13_16 + seg
                if seg < tempoEsperaZP1P_13_16_Min:
                    tempoEsperaZP1P_13_16_Min = tempoEsperaZP1P_13_16_Min + seg
                if seg > tempoEsperaZP1P_13_16_Max:
                    tempoEsperaZP1P_13_16_Max = tempoEsperaZP1P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZP1P_16_19 = numClienteZP1P_16_19 + 1
                tempoEsperaZP1P_16_19 = tempoEsperaZP1P_16_19 + seg
                if seg < tempoEsperaZP1P_16_19_Min:
                    tempoEsperaZP1P_16_19_Min = tempoEsperaZP1P_16_19_Min + seg
                if seg > tempoEsperaZP1P_16_19_Max:
                    tempoEsperaZP1P_16_19_Max = tempoEsperaZP1P_16_19_Max + seg
            if inter >= 19:
                numClienteZP1P_19_22 = numClienteZP1P_19_22 + 1
                tempoEsperaZP1P_19_22 = tempoEsperaZP1P_19_22 + seg
                if seg < tempoEsperaZP1P_19_22_Min:
                    tempoEsperaZP1P_19_22_Min = tempoEsperaZP1P_19_22_Min + seg
                if seg > tempoEsperaZP1P_19_22_Max:
                    tempoEsperaZP1P_19_22_Max = tempoEsperaZP1P_19_22_Max + seg
        else:
            numClienteZP1 = numClienteZP1 + 1
            tempoEsperaZP1 = tempoEsperaZP1 + seg
            if seg < tempoEsperaZP1Min:
                tempoEsperaZP1Min = seg
            if seg > tempoEsperaZP1Max:
                tempoEsperaZP1Max = seg
            if inter >= 10 and inter < 13:
                numClienteZP1_10_13 = numClienteZP1_10_13 + 1
                tempoEsperaZP1_10_13 = tempoEsperaZP1_10_13 + seg
                if seg < tempoEsperaZP1_10_13_Min:
                    tempoEsperaZP1_10_13_Min = tempoEsperaZP1_10_13_Min + seg
                if seg > tempoEsperaZP1_10_13_Max:
                    tempoEsperaZP1_10_13_Max = tempoEsperaZP1_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZP1_13_16 = numClienteZP1_13_16 + 1
                tempoEsperaZP1_13_16 = tempoEsperaZP1_13_16 + seg
                if seg < tempoEsperaZP1_13_16_Min:
                    tempoEsperaZP1_13_16_Min = tempoEsperaZP1_13_16_Min + seg
                if seg > tempoEsperaZP1_13_16_Max:
                    tempoEsperaZP1_13_16_Max = tempoEsperaZP1_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZP1_16_19 = numClienteZP1_16_19 + 1
                tempoEsperaZP1_16_19 = tempoEsperaZP1_16_19 + seg
                if seg < tempoEsperaZP1_16_19_Min:
                    tempoEsperaZP1_16_19_Min = tempoEsperaZP1_16_19_Min + seg
                if seg > tempoEsperaZP1_16_19_Max:
                    tempoEsperaZP1_16_19_Max = tempoEsperaZP1_16_19_Max + seg
            if inter >= 19:
                numClienteZP1_19_22 = numClienteZP1_19_22 + 1
                tempoEsperaZP1_19_22 = tempoEsperaZP1_19_22 + seg
                if seg < tempoEsperaZP1_19_22_Min:
                    tempoEsperaZP1_19_22_Min = tempoEsperaZP1_19_22_Min + seg
                if seg > tempoEsperaZP1_19_22_Max:
                    tempoEsperaZP1_19_22_Max = tempoEsperaZP1_19_22_Max + seg

    elif fila=="ZP2":
        if prioridade==1:
            numClienteZP2P=numClienteZP2P+1
            tempoEsperaZP2P=tempoEsperaZP2P+seg
            if seg<tempoEsperaZP2PMin:
                tempoEsperaZP2PMin=seg
            if seg>tempoEsperaZP2PMax:
                tempoEsperaZP2PMax=seg
            if inter>=10 and inter<13:
                numClienteZP2P_10_13 = numClienteZP2P_10_13 +1
                tempoEsperaZP2P_10_13=tempoEsperaZP2P_10_13+seg
                if seg < tempoEsperaZP2P_10_13_Min:
                    tempoEsperaZP2P_10_13_Min = tempoEsperaZP2P_10_13_Min+seg
                if seg > tempoEsperaZP2P_10_13_Max:
                    tempoEsperaZP2P_10_13_Max = tempoEsperaZP2P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZP2P_13_16 = numClienteZP2P_13_16 + 1
                tempoEsperaZP2P_13_16 = tempoEsperaZP2P_13_16 + seg
                if seg < tempoEsperaZP2P_13_16_Min:
                    tempoEsperaZP2P_13_16_Min = tempoEsperaZP2P_13_16_Min + seg
                if seg > tempoEsperaZP2P_13_16_Max:
                    tempoEsperaZP2P_13_16_Max = tempoEsperaZP2P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZP2P_16_19 = numClienteZP2P_16_19 + 1
                tempoEsperaZP2P_16_19 = tempoEsperaZP2P_16_19 + seg
                if seg < tempoEsperaZP2P_16_19_Min:
                    tempoEsperaZP2P_16_19_Min = tempoEsperaZP2P_16_19_Min + seg
                if seg > tempoEsperaZP2P_16_19_Max:
                    tempoEsperaZP2P_16_19_Max = tempoEsperaZP2P_16_19_Max + seg
            if inter >= 19:
                numClienteZP2P_19_22 = numClienteZP2P_19_22 + 1
                tempoEsperaZP2P_19_22 = tempoEsperaZP2P_19_22 + seg
                if seg < tempoEsperaZP2P_19_22_Min:
                    tempoEsperaZP2P_19_22_Min = tempoEsperaZP2P_19_22_Min + seg
                if seg > tempoEsperaZP2P_19_22_Max:
                    tempoEsperaZP2P_19_22_Max = tempoEsperaZP2P_19_22_Max + seg
        else:
            numClienteZP2 = numClienteZP2 + 1
            tempoEsperaZP2 = tempoEsperaZP2 + seg
            if seg < tempoEsperaZP2Min:
                tempoEsperaZP2Min = seg
            if seg > tempoEsperaZP2Max:
                tempoEsperaZP2Max = seg
            if inter >= 10 and inter < 13:
                numClienteZP2_10_13 = numClienteZP2_10_13 + 1
                tempoEsperaZP2_10_13 = tempoEsperaZP2_10_13 + seg
                if seg < tempoEsperaZP2_10_13_Min:
                    tempoEsperaZP2_10_13_Min = tempoEsperaZP2_10_13_Min + seg
                if seg > tempoEsperaZP2_10_13_Max:
                    tempoEsperaZP2_10_13_Max = tempoEsperaZP2_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZP2_13_16 = numClienteZP2_13_16 + 1
                tempoEsperaZP2_13_16 = tempoEsperaZP2_13_16 + seg
                if seg < tempoEsperaZP2_13_16_Min:
                    tempoEsperaZP2_13_16_Min = tempoEsperaZP2_13_16_Min + seg
                if seg > tempoEsperaZP2_13_16_Max:
                    tempoEsperaZP2_13_16_Max = tempoEsperaZP2_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZP2_16_19 = numClienteZP2_16_19 + 1
                tempoEsperaZP2_16_19 = tempoEsperaZP2_16_19 + seg
                if seg < tempoEsperaZP2_16_19_Min:
                    tempoEsperaZP2_16_19_Min = tempoEsperaZP2_16_19_Min + seg
                if seg > tempoEsperaZP2_16_19_Max:
                    tempoEsperaZP2_16_19_Max = tempoEsperaZP2_16_19_Max + seg
            if inter >= 19:
                numClienteZP2_19_22 = numClienteZP2_19_22 + 1
                tempoEsperaZP2_19_22 = tempoEsperaZP2_19_22 + seg
                if seg < tempoEsperaZP2_19_22_Min:
                    tempoEsperaZP2_19_22_Min = tempoEsperaZP2_19_22_Min + seg
                if seg > tempoEsperaZP2_19_22_Max:
                    tempoEsperaZP2_19_22_Max = tempoEsperaZP2_19_22_Max + seg

    elif fila=="ZP3":
        if prioridade==1:
            numClienteZP3P=numClienteZP3P+1
            tempoEsperaZP3P=tempoEsperaZP3P+seg
            if seg<tempoEsperaZP3PMin:
                tempoEsperaZP3PMin=seg
            if seg>tempoEsperaZP3PMax:
                tempoEsperaZP3PMax=seg
            if inter>=10 and inter<13:
                numClienteZP3P_10_13 = numClienteZP3P_10_13 +1
                tempoEsperaZP3P_10_13=tempoEsperaZP3P_10_13+seg
                if seg < tempoEsperaZP3P_10_13_Min:
                    tempoEsperaZP3P_10_13_Min = tempoEsperaZP3P_10_13_Min+seg
                if seg > tempoEsperaZP3P_10_13_Max:
                    tempoEsperaZP3P_10_13_Max = tempoEsperaZP3P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZP3P_13_16 = numClienteZP3P_13_16 + 1
                tempoEsperaZP3P_13_16 = tempoEsperaZP3P_13_16 + seg
                if seg < tempoEsperaZP3P_13_16_Min:
                    tempoEsperaZP3P_13_16_Min = tempoEsperaZP3P_13_16_Min + seg
                if seg > tempoEsperaZP3P_13_16_Max:
                    tempoEsperaZP3P_13_16_Max = tempoEsperaZP3P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZP3P_16_19 = numClienteZP3P_16_19 + 1
                tempoEsperaZP3P_16_19 = tempoEsperaZP3P_16_19 + seg
                if seg < tempoEsperaZP3P_16_19_Min:
                    tempoEsperaZP3P_16_19_Min = tempoEsperaZP3P_16_19_Min + seg
                if seg > tempoEsperaZP3P_16_19_Max:
                    tempoEsperaZP3P_16_19_Max = tempoEsperaZP3P_16_19_Max + seg
            if inter >= 19:
                numClienteZP3P_19_22 = numClienteZP3P_19_22 + 1
                tempoEsperaZP3P_19_22 = tempoEsperaZP3P_19_22 + seg
                if seg < tempoEsperaZP3P_19_22_Min:
                    tempoEsperaZP3P_19_22_Min = tempoEsperaZP3P_19_22_Min + seg
                if seg > tempoEsperaZP3P_19_22_Max:
                    tempoEsperaZP3P_19_22_Max = tempoEsperaZP3P_19_22_Max + seg
        else:
            numClienteZP3 = numClienteZP3 + 1
            tempoEsperaZP3 = tempoEsperaZP3 + seg
            if seg < tempoEsperaZP3Min:
                tempoEsperaZP3Min = seg
            if seg > tempoEsperaZP3Max:
                tempoEsperaZP3Max = seg
            if inter >= 10 and inter < 13:
                numClienteZP3_10_13 = numClienteZP3_10_13 + 1
                tempoEsperaZP3_10_13 = tempoEsperaZP3_10_13 + seg
                if seg < tempoEsperaZP3_10_13_Min:
                    tempoEsperaZP3_10_13_Min = tempoEsperaZP3_10_13_Min + seg
                if seg > tempoEsperaZP3_10_13_Max:
                    tempoEsperaZP3_10_13_Max = tempoEsperaZP3_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZP3_13_16 = numClienteZP3_13_16 + 1
                tempoEsperaZP3_13_16 = tempoEsperaZP3_13_16 + seg
                if seg < tempoEsperaZP3_13_16_Min:
                    tempoEsperaZP3_13_16_Min = tempoEsperaZP3_13_16_Min + seg
                if seg > tempoEsperaZP3_13_16_Max:
                    tempoEsperaZP3_13_16_Max = tempoEsperaZP3_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZP3_16_19 = numClienteZP3_16_19 + 1
                tempoEsperaZP3_16_19 = tempoEsperaZP3_16_19 + seg
                if seg < tempoEsperaZP3_16_19_Min:
                    tempoEsperaZP3_16_19_Min = tempoEsperaZP3_16_19_Min + seg
                if seg > tempoEsperaZP3_16_19_Max:
                    tempoEsperaZP3_16_19_Max = tempoEsperaZP3_16_19_Max + seg
            if inter >= 19:
                numClienteZP3_19_22 = numClienteZP3_19_22 + 1
                tempoEsperaZP3_19_22 = tempoEsperaZP3_19_22 + seg
                if seg < tempoEsperaZP3_19_22_Min:
                    tempoEsperaZP3_19_22_Min = tempoEsperaZP3_19_22_Min + seg
                if seg > tempoEsperaZP3_19_22_Max:
                    tempoEsperaZP3_19_22_Max = tempoEsperaZP3_19_22_Max + seg

    elif fila=="ZP4":
        if prioridade==1:
            numClienteZP4P=numClienteZP4P+1
            tempoEsperaZP4P=tempoEsperaZP4P+seg
            if seg<tempoEsperaZP4PMin:
                tempoEsperaZP4PMin=seg
            if seg>tempoEsperaZP4PMax:
                tempoEsperaZP4PMax=seg
            if inter>=10 and inter<13:
                numClienteZP4P_10_13 = numClienteZP4P_10_13 +1
                tempoEsperaZP4P_10_13=tempoEsperaZP4P_10_13+seg
                if seg < tempoEsperaZP4P_10_13_Min:
                    tempoEsperaZP4P_10_13_Min = tempoEsperaZP4P_10_13_Min+seg
                if seg > tempoEsperaZP4P_10_13_Max:
                    tempoEsperaZP4P_10_13_Max = tempoEsperaZP4P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZP4P_13_16 = numClienteZP4P_13_16 + 1
                tempoEsperaZP4P_13_16 = tempoEsperaZP4P_13_16 + seg
                if seg < tempoEsperaZP4P_13_16_Min:
                    tempoEsperaZP4P_13_16_Min = tempoEsperaZP4P_13_16_Min + seg
                if seg > tempoEsperaZP4P_13_16_Max:
                    tempoEsperaZP4P_13_16_Max = tempoEsperaZP4P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZP4P_16_19 = numClienteZP4P_16_19 + 1
                tempoEsperaZP4P_16_19 = tempoEsperaZP4P_16_19 + seg
                if seg < tempoEsperaZP4P_16_19_Min:
                    tempoEsperaZP4P_16_19_Min = tempoEsperaZP4P_16_19_Min + seg
                if seg > tempoEsperaZP4P_16_19_Max:
                    tempoEsperaZP4P_16_19_Max = tempoEsperaZP4P_16_19_Max + seg
            if inter >= 19:
                numClienteZP4P_19_22 = numClienteZP4P_19_22 + 1
                tempoEsperaZP4P_19_22 = tempoEsperaZP4P_19_22 + seg
                if seg < tempoEsperaZP4P_19_22_Min:
                    tempoEsperaZP4P_19_22_Min = tempoEsperaZP4P_19_22_Min + seg
                if seg > tempoEsperaZP4P_19_22_Max:
                    tempoEsperaZP4P_19_22_Max = tempoEsperaZP4P_19_22_Max + seg
        else:
            numClienteZP4 = numClienteZP4 + 1
            tempoEsperaZP4 = tempoEsperaZP4 + seg
            if seg < tempoEsperaZP4Min:
                tempoEsperaZP4Min = seg
            if seg > tempoEsperaZP4Max:
                tempoEsperaZP4Max = seg
            if inter >= 10 and inter < 13:
                numClienteZP4_10_13 = numClienteZP4_10_13 + 1
                tempoEsperaZP4_10_13 = tempoEsperaZP4_10_13 + seg
                if seg < tempoEsperaZP4_10_13_Min:
                    tempoEsperaZP4_10_13_Min = tempoEsperaZP4_10_13_Min + seg
                if seg > tempoEsperaZP4_10_13_Max:
                    tempoEsperaZP4_10_13_Max = tempoEsperaZP4_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZP4_13_16 = numClienteZP4_13_16 + 1
                tempoEsperaZP4_13_16 = tempoEsperaZP4_13_16 + seg
                if seg < tempoEsperaZP4_13_16_Min:
                    tempoEsperaZP4_13_16_Min = tempoEsperaZP4_13_16_Min + seg
                if seg > tempoEsperaZP4_13_16_Max:
                    tempoEsperaZP4_13_16_Max = tempoEsperaZP4_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZP4_16_19 = numClienteZP4_16_19 + 1
                tempoEsperaZP4_16_19 = tempoEsperaZP4_16_19 + seg
                if seg < tempoEsperaZP4_16_19_Min:
                    tempoEsperaZP4_16_19_Min = tempoEsperaZP4_16_19_Min + seg
                if seg > tempoEsperaZP4_16_19_Max:
                    tempoEsperaZP4_16_19_Max = tempoEsperaZP4_16_19_Max + seg
            if inter >= 19:
                numClienteZP4_19_22 = numClienteZP4_19_22 + 1
                tempoEsperaZP4_19_22 = tempoEsperaZP4_19_22 + seg
                if seg < tempoEsperaZP4_19_22_Min:
                    tempoEsperaZP4_19_22_Min = tempoEsperaZP4_19_22_Min + seg
                if seg > tempoEsperaZP4_19_22_Max:
                    tempoEsperaZP4_19_22_Max = tempoEsperaZP4_19_22_Max + seg


    elif fila=="ZL1":
        if prioridade==1:
            numClienteZL1P=numClienteZL1P+1
            tempoEsperaZL1P=tempoEsperaZL1P+seg
            if seg<tempoEsperaZL1PMin:
                tempoEsperaZL1PMin=seg
            if seg>tempoEsperaZL1PMax:
                tempoEsperaZL1PMax=seg
            if inter>=10 and inter<13:
                numClienteZL1P_10_13 = numClienteZL1P_10_13 +1
                tempoEsperaZL1P_10_13=tempoEsperaZL1P_10_13+seg
                if seg < tempoEsperaZL1P_10_13_Min:
                    tempoEsperaZL1P_10_13_Min = tempoEsperaZL1P_10_13_Min+seg
                if seg > tempoEsperaZL1P_10_13_Max:
                    tempoEsperaZL1P_10_13_Max = tempoEsperaZL1P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZL1P_13_16 = numClienteZL1P_13_16 + 1
                tempoEsperaZL1P_13_16 = tempoEsperaZL1P_13_16 + seg
                if seg < tempoEsperaZL1P_13_16_Min:
                    tempoEsperaZL1P_13_16_Min = tempoEsperaZL1P_13_16_Min + seg
                if seg > tempoEsperaZL1P_13_16_Max:
                    tempoEsperaZL1P_13_16_Max = tempoEsperaZL1P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZL1P_16_19 = numClienteZL1P_16_19 + 1
                tempoEsperaZL1P_16_19 = tempoEsperaZL1P_16_19 + seg
                if seg < tempoEsperaZL1P_16_19_Min:
                    tempoEsperaZL1P_16_19_Min = tempoEsperaZL1P_16_19_Min + seg
                if seg > tempoEsperaZL1P_16_19_Max:
                    tempoEsperaZL1P_16_19_Max = tempoEsperaZL1P_16_19_Max + seg
            if inter >= 19:
                numClienteZL1P_19_22 = numClienteZL1P_19_22 + 1
                tempoEsperaZL1P_19_22 = tempoEsperaZL1P_19_22 + seg
                if seg < tempoEsperaZL1P_19_22_Min:
                    tempoEsperaZL1P_19_22_Min = tempoEsperaZL1P_19_22_Min + seg
                if seg > tempoEsperaZL1P_19_22_Max:
                    tempoEsperaZL1P_19_22_Max = tempoEsperaZL1P_19_22_Max + seg
        else:
            numClienteZL1 = numClienteZL1 + 1
            tempoEsperaZL1 = tempoEsperaZL1 + seg
            if seg < tempoEsperaZL1Min:
                tempoEsperaZL1Min = seg
            if seg > tempoEsperaZL1Max:
                tempoEsperaZL1Max = seg
            if inter >= 10 and inter < 13:
                numClienteZL1_10_13 = numClienteZL1_10_13 + 1
                tempoEsperaZL1_10_13 = tempoEsperaZL1_10_13 + seg
                if seg < tempoEsperaZL1_10_13_Min:
                    tempoEsperaZL1_10_13_Min = tempoEsperaZL1_10_13_Min + seg
                if seg > tempoEsperaZL1_10_13_Max:
                    tempoEsperaZL1_10_13_Max = tempoEsperaZL1_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZL1_13_16 = numClienteZL1_13_16 + 1
                tempoEsperaZL1_13_16 = tempoEsperaZL1_13_16 + seg
                if seg < tempoEsperaZL1_13_16_Min:
                    tempoEsperaZL1_13_16_Min = tempoEsperaZL1_13_16_Min + seg
                if seg > tempoEsperaZL1_13_16_Max:
                    tempoEsperaZL1_13_16_Max = tempoEsperaZL1_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZL1_16_19 = numClienteZL1_16_19 + 1
                tempoEsperaZL1_16_19 = tempoEsperaZL1_16_19 + seg
                if seg < tempoEsperaZL1_16_19_Min:
                    tempoEsperaZL1_16_19_Min = tempoEsperaZL1_16_19_Min + seg
                if seg > tempoEsperaZL1_16_19_Max:
                    tempoEsperaZL1_16_19_Max = tempoEsperaZL1_16_19_Max + seg
            if inter >= 19:
                numClienteZL1_19_22 = numClienteZL1_19_22 + 1
                tempoEsperaZL1_19_22 = tempoEsperaZL1_19_22 + seg
                if seg < tempoEsperaZL1_19_22_Min:
                    tempoEsperaZL1_19_22_Min = tempoEsperaZL1_19_22_Min + seg
                if seg > tempoEsperaZL1_19_22_Max:
                    tempoEsperaZL1_19_22_Max = tempoEsperaZL1_19_22_Max + seg

    elif fila=="ZL2":
        if prioridade==1:
            numClienteZL2P=numClienteZL2P+1
            tempoEsperaZL2P=tempoEsperaZL2P+seg
            if seg<tempoEsperaZL2PMin:
                tempoEsperaZL2PMin=seg
            if seg>tempoEsperaZL2PMax:
                tempoEsperaZL2PMax=seg
            if inter>=10 and inter<13:
                numClienteZL2P_10_13 = numClienteZL2P_10_13 +1
                tempoEsperaZL2P_10_13=tempoEsperaZL2P_10_13+seg
                if seg < tempoEsperaZL2P_10_13_Min:
                    tempoEsperaZL2P_10_13_Min = tempoEsperaZL2P_10_13_Min+seg
                if seg > tempoEsperaZL2P_10_13_Max:
                    tempoEsperaZL2P_10_13_Max = tempoEsperaZL2P_10_13_Max+seg
            if inter >= 13 and inter < 16:
                numClienteZL2P_13_16 = numClienteZL2P_13_16 + 1
                tempoEsperaZL2P_13_16 = tempoEsperaZL2P_13_16 + seg
                if seg < tempoEsperaZL2P_13_16_Min:
                    tempoEsperaZL2P_13_16_Min = tempoEsperaZL2P_13_16_Min + seg
                if seg > tempoEsperaZL2P_13_16_Max:
                    tempoEsperaZL2P_13_16_Max = tempoEsperaZL2P_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZL2P_16_19 = numClienteZL2P_16_19 + 1
                tempoEsperaZL2P_16_19 = tempoEsperaZL2P_16_19 + seg
                if seg < tempoEsperaZL2P_16_19_Min:
                    tempoEsperaZL2P_16_19_Min = tempoEsperaZL2P_16_19_Min + seg
                if seg > tempoEsperaZL2P_16_19_Max:
                    tempoEsperaZL2P_16_19_Max = tempoEsperaZL2P_16_19_Max + seg
            if inter >= 19:
                numClienteZL2P_19_22 = numClienteZL2P_19_22 + 1
                tempoEsperaZL2P_19_22 = tempoEsperaZL2P_19_22 + seg
                if seg < tempoEsperaZL2P_19_22_Min:
                    tempoEsperaZL2P_19_22_Min = tempoEsperaZL2P_19_22_Min + seg
                if seg > tempoEsperaZL2P_19_22_Max:
                    tempoEsperaZL2P_19_22_Max = tempoEsperaZL2P_19_22_Max + seg
        else:
            numClienteZL2 = numClienteZL2 + 1
            tempoEsperaZL2 = tempoEsperaZL2 + seg
            if seg < tempoEsperaZL2Min:
                tempoEsperaZL2Min = seg
            if seg > tempoEsperaZL2Max:
                tempoEsperaZL2Max = seg
            if inter >= 10 and inter < 13:
                numClienteZL2_10_13 = numClienteZL2_10_13 + 1
                tempoEsperaZL2_10_13 = tempoEsperaZL2_10_13 + seg
                if seg < tempoEsperaZL2_10_13_Min:
                    tempoEsperaZL2_10_13_Min = tempoEsperaZL2_10_13_Min + seg
                if seg > tempoEsperaZL2_10_13_Max:
                    tempoEsperaZL2_10_13_Max = tempoEsperaZL2_10_13_Max + seg
            if inter >= 13 and inter < 16:
                numClienteZL2_13_16 = numClienteZL2_13_16 + 1
                tempoEsperaZL2_13_16 = tempoEsperaZL2_13_16 + seg
                if seg < tempoEsperaZL2_13_16_Min:
                    tempoEsperaZL2_13_16_Min = tempoEsperaZL2_13_16_Min + seg
                if seg > tempoEsperaZL2_13_16_Max:
                    tempoEsperaZL2_13_16_Max = tempoEsperaZL2_13_16_Max + seg
            if inter >= 16 and inter < 19:
                numClienteZL2_16_19 = numClienteZL2_16_19 + 1
                tempoEsperaZL2_16_19 = tempoEsperaZL2_16_19 + seg
                if seg < tempoEsperaZL2_16_19_Min:
                    tempoEsperaZL2_16_19_Min = tempoEsperaZL2_16_19_Min + seg
                if seg > tempoEsperaZL2_16_19_Max:
                    tempoEsperaZL2_16_19_Max = tempoEsperaZL2_16_19_Max + seg
            if inter >= 19:
                numClienteZL2_19_22 = numClienteZL2_19_22 + 1
                tempoEsperaZL2_19_22 = tempoEsperaZL2_19_22 + seg
                if seg < tempoEsperaZL2_19_22_Min:
                    tempoEsperaZL2_19_22_Min = tempoEsperaZL2_19_22_Min + seg
                if seg > tempoEsperaZL2_19_22_Max:
                    tempoEsperaZL2_19_22_Max = tempoEsperaZL2_19_22_Max + seg



def eventoChegada():
    global filaZV
    global filaZVP
    global proxChegada
    global clienteZV1, clienteZV2, clienteZV3, clienteZV4, clienteZV5, clienteZV6, clienteZV7, clienteZV8, clienteZV9, clienteZV10
    global estadoZV1, estadoZV2, estadoZV3, estadoZV4, estadoZV5, estadoZV6, estadoZV7, estadoZV8, estadoZV9, estadoZV10
    global partidaZV1, partidaZV2, partidaZV3, partidaZV4, partidaZV5, partidaZV6, partidaZV7, partidaZV8, partidaZV9, partidaZV10
    global numClienteZV1, numClienteZV2, numClienteZV3, numClienteZV4, numClienteZV5, numClienteZV6, numClienteZV7, numClienteZV8, numClienteZV9, numClienteZV10

    proxCliente = buscarProximoCliente()
    if proxCliente[0] == 999999:
        proxChegada = 999999
    else:
        proxChegada = buscarProximoCliente2()[1]
        if estadoZV1 == "livre":
            estadoZV1 = "ocupado"
            partidaZV1 = clock + proxCliente[5]
            clienteZV1 = proxCliente
            atualizaEstatisticas(0, "ZV1", proxCliente[2], (clock / 60 / 60) + 9)
        elif estadoZV1 == "ocupado":
            if estadoZV2 == "livre":
                estadoZV2 = "ocupado"
                partidaZV2 = clock + proxCliente[5]
                clienteZV2 = proxCliente
                atualizaEstatisticas(0, "ZV2", proxCliente[2], (clock / 60 / 60) + 9)
            elif estadoZV2 == "ocupado":
                if estadoZV3 == "livre":
                    estadoZV3 = "ocupado"
                    partidaZV3 = clock + proxCliente[5]
                    clienteZV3 = proxCliente
                    atualizaEstatisticas(0, "ZV3", proxCliente[2], (clock / 60 / 60) + 9)
                elif estadoZV3 == "ocupado":
                    if estadoZV4 == "livre":
                        estadoZV4 = "ocupado"
                        partidaZV4 = clock + proxCliente[5]
                        clienteZV4 = proxCliente
                        atualizaEstatisticas(0, "ZV4", proxCliente[2], (clock / 60 / 60) + 9)
                    elif estadoZV4 == "ocupado":
                        if estadoZV5 == "livre":
                            estadoZV5 = "ocupado"
                            partidaZV5 = clock + proxCliente[5]
                            clienteZV5 = proxCliente
                            atualizaEstatisticas(0, "ZV5", proxCliente[2], (clock / 60 / 60) + 9)
                        elif estadoZV5 == "ocupado":
                            if estadoZV6 == "livre":
                                estadoZV6 = "ocupado"
                                partidaZV6 = clock + proxCliente[5]
                                clienteZV6 = proxCliente
                                atualizaEstatisticas(0, "ZV6", proxCliente[2], (clock / 60 / 60) + 9)
                            elif estadoZV6 == "ocupado":
                                if estadoZV7 == "livre":
                                    estadoZV7 = "ocupado"
                                    partidaZV7 = clock + proxCliente[5]
                                    clienteZV7 = proxCliente
                                    atualizaEstatisticas(0, "ZV7", proxCliente[2], (clock / 60 / 60) + 9)
                                elif estadoZV7 == "ocupado":
                                    if estadoZV8 == "livre":
                                        estadoZV8 = "ocupado"
                                        partidaZV8 = clock + proxCliente[5]
                                        clienteZV8 = proxCliente
                                        atualizaEstatisticas(0, "ZV8", proxCliente[2], (clock / 60 / 60) + 9)
                                    elif estadoZV8 == "ocupado":
                                        if estadoZV9 == "livre":
                                            estadoZV9 = "ocupado"
                                            partidaZV9 = clock + proxCliente[5]
                                            clienteZV9 = proxCliente
                                            atualizaEstatisticas(0, "ZV9", proxCliente[2], (clock / 60 / 60) + 9)
                                        elif estadoZV9 == "ocupado":
                                            if estadoZV10 == "livre":
                                                estadoZV10 = "ocupado"
                                                partidaZV10 = clock + proxCliente[5]
                                                clienteZV10 = proxCliente
                                                atualizaEstatisticas(0, "ZV10", proxCliente[2], (clock / 60 / 60) + 9)
                                            elif estadoZV10 == "ocupado":
                                                aux = ((proxCliente), clock)
                                                if (proxCliente[2] == 1):
                                                    filaZVP.append(aux)
                                                else:
                                                    filaZV.append(aux)


def eventoPartidaZV1():
    global estadoZV1, partidaZV1, filaZV, filaZVP, proxChegada, clienteZV1
    global estadoZV2, partidaZV2, filaZV, filaZVP, proxChegada, clienteZV2
    global estadoZV3, partidaZV3, filaZV, filaZVP, proxChegada, clienteZV3
    global estadoZV4, partidaZV4, filaZV, filaZVP, proxChegada, clienteZV4
    global estadoZV5, partidaZV5, filaZV, filaZVP, proxChegada, clienteZV5
    global estadoZV6, partidaZV6, filaZV, filaZVP, proxChegada, clienteZV6
    global estadoZV7, partidaZV7, filaZV, filaZVP, proxChegada, clienteZV7
    global estadoZV8, partidaZV8, filaZV, filaZVP, proxChegada, clienteZV8
    global estadoZV9, partidaZV9, filaZV, filaZVP, proxChegada, clienteZV9
    global estadoZV10, partidaZV10, filaZV, filaZVP, proxChegada, clienteZV10
    global tempoEsperaZV1, tempoEsperaZV1_10_13, tempoEsperaZV1_10_13_Max, tempoEsperaZV1_10_13_Min, tempoEsperaZV1_13_16, tempoEsperaZV1_13_16_Max, tempoEsperaZV1_13_16_Min, tempoEsperaZV1_16_19, tempoEsperaZV1_16_19_Min, tempoEsperaZV1_16_19_Max, tempoEsperaZV1_19_22, tempoEsperaZV1_19_22_Max, tempoEsperaZV1_19_22_Min
    global numClienteZL1, numClienteZL1_10_13, numClienteZL1_13_16, numClienteZL1_16_19, numClienteZL1_19_22
    global numClienteZV10
    global clientequepartiu

    clientequepartiu = clienteZV1[0]
    if(clienteZV1[3]==1):
        if(estadoZV10 == "livre"):
             estadoZV10 = "ocupado"
             partidaZV10 = clock + clienteZV1[10]
             clienteZV10 = clienteZV1
             actualizaListasFolhaExcel(0,"ZV10",clienteZV10[2],((clock/60/60)+9))
        elif estadoZV10 == "ocupado":
            aux = ((clienteZV1),clock)
            if((clienteZV1),clock):
                filaZVP.append(aux)
            else:
                filaZV.append(aux)




def eventoPartidaZV2():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV2, estadoZV2, partidaZV2, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV2[0]
    if(clienteZV2[7] == 0):
        if(clienteZV2[5]==1):
            if(estadoZL2 == "livre"):
                estadoZL2 = "ocupado"
                partidaZL2 = clock + clienteZV2[10]
                clienteZL2 = clienteZV2
                actualizaListasFolhaExcel(0, "T", clienteZV2[2], (clienteZV2[1]/60/60)+9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV2),clock)
                if (clienteZV2[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV2[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV2[2] == 0):
                    filaZL.append(aux)


    if len(filaZVP) > 0:
        estadoZV2 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV2 = proxcliente[0]
        actualizaListasFolhaExcel((clock - proxcliente[1]), "A", clienteZV2[2], (clienteZV2[1] / 60 / 60) + 9)
        if (clienteZV2[7] == 1):
            partidaZV2 = clock + round((clienteZV2[9] * 0.2))
        elif (clienteZV2[6] == 1):
            partidaZV2 = clock + round((clienteZV2[9] * 0.8))
        elif (clienteZV2[6] == 0):
            partidaZV2 = clock + clienteZV2[9]
    elif len(filaZV) > 0:
        estadoZV2 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV2 = proxcliente[0]
        actualizaListasFolhaExcel((clock - proxcliente[1]), "A", clienteZV2[2], (clienteZV2[1] / 60 / 60) + 9)
        if (clienteZV2[7] == 1):
            partidaZV2 = clock + round((clienteZV2[9] * 0.2))
        elif (clienteZV2[6] == 1):
            partidaZV2 = clock + round((clienteZV2[9] * 0.8))
        elif (clienteZV2[6] == 0):
            partidaZV2 = clock + clienteZV2[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV2 = "livre"
        partidaZV2 = 999999


def eventoPartidaZV3():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV3, estadoZV3, partidaZV3, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV3[0]
    if (clienteZV3[7] == 0):
        if (clienteZV3[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV3 = "ocupado"
                partidaZL2 = clock + clienteZV3[10]
                clienteZL2 = clienteZV3
                actualizaListasFolhaExcel(0, "T", clienteZV3[2], (clienteZV3[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV3), clock)
                if (clienteZV3[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV3[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV3[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV3 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV3 = proxcliente[0]
        actualizaListasFolhaExcel((clock - proxcliente[1]), "A", clienteZV3[2], (clienteZV3[1] / 60 / 60) + 9)
        if (clienteZV3[7] == 1):
            partidaZV3 = clock + round((clienteZV3[9] * 0.2))
        elif (clienteZV3[6] == 1):
            partidaZV3 = clock + round((clienteZV3[9] * 0.8))
        elif (clienteZV3[6] == 0):
            partidaZV3 = clock + clienteZV3[9]
    elif len(filaZV) > 0:
        estadoZV3 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV3 = proxcliente[0]
        actualizaListasFolhaExcel((clock - proxcliente[1]), "A", clienteZV3[2], (clienteZV3[1] / 60 / 60) + 9)
        if (clienteZV3[7] == 1):
            partidaZV3 = clock + round((clienteZV3[9] * 0.2))
        elif (clienteZV3[6] == 1):
            partidaZV3 = clock + round((clienteZV3[9] * 0.8))
        elif (clienteZV3[6] == 0):
            partidaZV3 = clock + clienteZV3[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV3 = "livre"
        partidaZV3 = 999999

def returnClockEntradaTuplo(x):
    return x[1]


def actualizaListasFolhaExcel(evento):
    global clock, clockLST, proxChegadaLST
    global partidaZV1LST, partidaZV2LST, partidaZV3LST, partidaZV4LST, partidaZV5LST, partidaZV6LST, partidaZV7LST, partidaZV8LST, partidaZV9LST, partidaZV10LST, partidaZP1LST, partidaZP2LST, partidaZP3LST, partidaZP4LST, partidaZL1LST, partidaZL2LST
    global filaZLLST, filaZP1LST, filaZP2LST, filaZP3LST, filaZP4LST, filaZVLST
    global clienteZV1, clienteZV2, clienteZV3, clienteZV4, clienteZV5, clienteZV6, clienteZV7, clienteZV8, clienteZV9, clienteZV10, clienteZP1, clienteZP2, clienteZP3, clienteZP4, clienteZL1, clienteZL2
    global filaZL, filaZV, filaZP1, filaZP2, filaZP3, filaZP4

    clockLST.append(clock)
    if evento == "Cheg":
        eventoLST.append("Chegada")
        clienteLST.append(numeroUltimoCliente)
    if evento == "PZV1":
        eventoLST.append("Partida ZV1")
        clockLST.append(clientequepartiu)
    if evento == "PZV2":
        eventoLST.append("Partida ZV2")
        clockLST.append(clientequepartiu)
    if evento == "PZV3":
        eventoLST.append("Partida ZV3")
        clockLST.append(clientequepartiu)
    if evento == "PZV4":
        eventoLST.append("Partida ZV4")
        clockLST.append(clientequepartiu)
    if evento == "PZV5":
        eventoLST.append("Partida ZV5")
        clockLST.append(clientequepartiu)
    if evento == "PZV6":
        eventoLST.append("Partida ZV6")
        clockLST.append(clientequepartiu)
    if evento == "PZV7":
        eventoLST.append("Partida ZV7")
        clockLST.append(clientequepartiu)
    if evento == "PZV8":
        eventoLST.append("Partida ZV8")
        clockLST.append(clientequepartiu)
    if evento == "PZV9":
        eventoLST.append("Partida ZV9")
        clockLST.append(clientequepartiu)
    if evento == "PZV10":
        eventoLST.append("Partida ZV10")
        clockLST.append(clientequepartiu)

    if evento == "PZP1":
        eventoLST.append("Partida ZP1")
        clockLST.append(clientequepartiu)
    if evento == "PZP2":
        eventoLST.append("Partida ZP2")
        clockLST.append(clientequepartiu)
    if evento == "PZP3":
        eventoLST.append("Partida ZP3")
        clockLST.append(clientequepartiu)
    if evento == "PZP4":
        eventoLST.append("Partida ZP4")
        clockLST.append(clientequepartiu)

    if evento == "PZL1":
        eventoLST.append("Partida ZL1")
        clockLST.append(clientequepartiu)
    if evento == "PZL2":
        eventoLST.append("Partida ZL1")
        clockLST.append(clientequepartiu)

    proxChegadaLST.append(proxChegada)
    aux123 = list(map(returnClockEntradaTuplo, filaZV))
    filaZVLST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaZVP))
    filaZVPLST.append(aux123)
    estadoZV1LST.append(estadoZV1)
    partidaZV1LST.append(partidaZV1)
    estadoZV2LST.append(estadoZV2)
    partidaZV2LST.append(partidaZV2)
    estadoZV3LST.append(estadoZV3)
    partidaZV3LST.append(partidaZV3)
    estadoZV4LST.append(estadoZV4)
    partidaZV4LST.append(partidaZV4)
    estadoZV5LST.append(estadoZV5)
    partidaZV5LST.append(partidaZV5)
    estadoZV6LST.append(estadoZV6)
    partidaZV6LST.append(partidaZV6)
    estadoZV7LST.append(estadoZV7)
    partidaZV7LST.append(partidaZV7)
    estadoZV8LST.append(estadoZV8)
    partidaZV8LST.append(partidaZV8)
    estadoZV9LST.append(estadoZV9)
    partidaZV9LST.append(partidaZV9)
    estadoZV10LST.append(estadoZV10)
    partidaZV10LST.append(partidaZV10)

    aux123 = list(map(returnClockEntradaTuplo, filaZP1))
    filaZP1LST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaZP1P))
    filaZPP1LST.append(aux123)
    estadoZP1LST.append(estadoZP1)
    partidaZP1LST.append(partidaZP1)

    aux123 = list(map(returnClockEntradaTuplo, filaZP2))
    filaZP2LST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaZP2P))
    filaZPP2LST.append(aux123)
    estadoZP2LST.append(estadoZP2)
    partidaZP2LST.append(partidaZP2)

    aux123 = list(map(returnClockEntradaTuplo, filaZP3))
    filaZP3LST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaZP3P))
    filaZPP3LST.append(aux123)
    estadoZP3LST.append(estadoZP3)
    partidaZP3LST.append(partidaZP3)

    aux123 = list(map(returnClockEntradaTuplo, filaZP4))
    filaZP4LST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaZP4P))
    filaZPP4LST.append(aux123)
    estadoZP4LST.append(estadoZP4)
    partidaZP4LST.append(partidaZP4)

    aux123 = list(map(returnClockEntradaTuplo, filaZL))
    filaZLLST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaZLP))
    filaZLPLST.append(aux123)
    estadoZL1LST.append(estadoZL1)
    partidaZL1LST.append(partidaZL1)
    estadoZL2LST.append(estadoZL2)
    partidaZL2LST.append(partidaZL2)


def printClientes(clientess):
    nclientes = list(x[0] for x in clientess)
    tempochegada = list(x[1] for x in clientess)
    prioritario = list(x[2] for x in clientess)
    passamZP = list(x[3] for x in clientess)
    passamZLP = list(x[4] for x in clientess)
    tempoAtendimentoZV = list(x[5] for x in clientess)
    tempoAtendimentoZP = list(x[6] for x in clientess)
    tempoAtendimentoZLP = list(x[7] for x in clientess)

    df = DataFrame({'N. Cliente': nclientes, 'Tempo Chegada': tempochegada, 'Prioritario': prioritario,
                    'Passam Zona Pagamento': passamZP, 'Passam Zona Levantamento de Produtos': passamZLP,
                    'Tempo de Atendimento Zona Vendedores': tempoAtendimentoZV,
                    'Tempo de Atendimento Zona Pagamento': tempoAtendimentoZP,
                    'Tempo de Atendimento Zona Levantamento de Produtos': tempoAtendimentoZLP})
    df.to_excel('trabalho_clientes.xlsx', sheet_name='clientes', index=False,
                columns=['N. Cliente', 'Tempo Chegada', 'Prioritario', 'Passam Zona Pagamento',
                         'Passam Zona Levantamento de Produtos', 'Tempo de Atendimento Zona Vendedores',
                         'Tempo de Atendimento Zona Pagamento', 'Tempo de Atendimento Zona Levantamento de Produtos'])


def desenharGraficos():
    fig = plt.figure()
    ar = list(map(lambda x: x[1], Clientes))
    plt.xlabel('Clock (s)')
    plt.title('Eventos de Chegada\nao Sistema.')
    plt.plot(ar, len(ar) * [0], "x")
    fig.savefig("plot_Chegadas.png")

    plt.clf()

    objects = ('Zona de Vendedores 1', 'Zona de Vendedores 2', 'Zona de Vendedores 3', 'Zona de Vendedores 4'
               , 'Zona de Vendedores 5', 'Zona de Vendedores 6', 'Zona de Vendedores 7', 'Zona de Vendedores 8'
               , 'Zona de Vendedores 9', 'Zona de Vendedores 10', 'Zona de Pagamento 1', 'Zona de Pagamento 2'
               , 'Zona de Pagamento 3', 'Zona de Pagamento 4', 'Zona de Levantamento 1', 'Zona de Levantamento 2')
    y_pos = np.arange(len(objects))
    auxZV1 = ((tempoEsperaZV1 + tempoEsperaZV1P) / (numClienteZV1 + numClienteZV1P)) if (
                                                                                                    numClienteZV1 + numClienteZV1P) != 0 else 0
    auxZV2 = ((tempoEsperaZV2 + tempoEsperaZV2P) / (numClienteZV2 + numClienteZV2P)) if (
                                                                                                    numClienteZV2 + numClienteZV2P) != 0 else 0
    auxZV3 = ((tempoEsperaZV3 + tempoEsperaZV3P) / (numClienteZV3 + numClienteZV3P)) if (
                                                                                                    numClienteZV3 + numClienteZV3P) != 0 else 0
    auxZV4 = ((tempoEsperaZV4 + tempoEsperaZV4P) / (numClienteZV4 + numClienteZV4P)) if (
                                                                                                    numClienteZV4 + numClienteZV4P) != 0 else 0
    auxZV5 = ((tempoEsperaZV5 + tempoEsperaZV5P) / (numClienteZV5 + numClienteZV5P)) if (
                                                                                                    numClienteZV5 + numClienteZV5P) != 0 else 0
    auxZV6 = ((tempoEsperaZV6 + tempoEsperaZV6P) / (numClienteZV6 + numClienteZV6P)) if (
                                                                                                    numClienteZV6 + numClienteZV6P) != 0 else 0
    auxZV7 = ((tempoEsperaZV7 + tempoEsperaZV7P) / (numClienteZV7 + numClienteZV7P)) if (
                                                                                                    numClienteZV7 + numClienteZV7P) != 0 else 0
    auxZV8 = ((tempoEsperaZV8 + tempoEsperaZV8P) / (numClienteZV8 + numClienteZV8P)) if (
                                                                                                    numClienteZV8 + numClienteZV8P) != 0 else 0
    auxZV9 = ((tempoEsperaZV9 + tempoEsperaZV9P) / (numClienteZV9 + numClienteZV9P)) if (
                                                                                                    numClienteZV9 + numClienteZV9P) != 0 else 0
    auxZV10 = ((tempoEsperaZV10 + tempoEsperaZV10P) / (numClienteZV10 + numClienteZV10P)) if (
                                                                                                         numClienteZV10 + numClienteZV10P) != 0 else 0
    auxZP1 = ((tempoEsperaZP1 + tempoEsperaZP1P) / (numClienteZP1 + numClienteZP1P)) if (
                                                                                                    numClienteZP1 + numClienteZP1P) != 0 else 0
    auxZP2 = ((tempoEsperaZP2 + tempoEsperaZP2P) / (numClienteZP2 + numClienteZP2P)) if (
                                                                                                    numClienteZP2 + numClienteZP2P) != 0 else 0
    auxZP3 = ((tempoEsperaZP3 + tempoEsperaZP3P) / (numClienteZP3 + numClienteZP3P)) if (
                                                                                                    numClienteZP3 + numClienteZP3P) != 0 else 0
    auxZP4 = ((tempoEsperaZP4 + tempoEsperaZP4P) / (numClienteZP4 + numClienteZP4P)) if (
                                                                                                    numClienteZP4 + numClienteZP4P) != 0 else 0
    auxZL1 = ((tempoEsperaZL1 + tempoEsperaZL1P) / (numClienteZL1 + numClienteZL1P)) if (
                                                                                                    numClienteZL1 + numClienteZL1P) != 0 else 0
    auxZL2 = ((tempoEsperaZL2 + tempoEsperaZL2P) / (numClienteZL2 + numClienteZL2P)) if (
                                                                                                    numClienteZL2 + numClienteZL2P) != 0 else 0
    performance = [auxZV1, auxZV2, auxZV3, auxZV4, auxZV5, auxZV6, auxZV7, auxZV8, auxZV9, auxZV10
        , auxZP1, auxZP2, auxZP3, auxZP4, auxZL1, auxZL2]
    plt.figure(figsize=(6, 16))
    plt.bar(y_pos, performance, align='center', alpha=1)
    plt.xticks(y_pos, objects)
    plt.ylabel('Segundos')
    plt.xlabel('Posto Atendimento')
    plt.title('Tempo Médio Total de Espera')
    plt.savefig("bar_TempoEsperaMedio.png")


def printEstatisticas():
    global tempoEsperaZV1, tempoEsperaZV2, tempoEsperaZV3, tempoEsperaZV4, tempoEsperaZV5, tempoEsperaZV6, tempoEsperaZV7, tempoEsperaZV8, tempoEsperaZV9, tempoEsperaZV10
    global tempoEsperaZV1P, tempoEsperaZV2P, tempoEsperaZV3P, tempoEsperaZV4P, tempoEsperaZV5P, tempoEsperaZV6P, tempoEsperaZV7P, tempoEsperaZV8P, tempoEsperaZV9P, tempoEsperaZV10P
    global tempoEsperaZV1PMin, tempoEsperaZV1PMax, tempoEsperaZV2PMin, tempoEsperaZV2PMax, tempoEsperaZV3PMin, tempoEsperaZV3PMax, tempoEsperaZV4PMin, tempoEsperaZV4PMax, tempoEsperaZV5PMin, tempoEsperaZV5PMax, tempoEsperaZV6PMin, tempoEsperaZV6PMax, tempoEsperaZV7PMin, tempoEsperaZV7PMax, tempoEsperaZV8PMin, tempoEsperaZV8PMax, tempoEsperaZV9PMin, tempoEsperaZV9PMax, tempoEsperaZV10PMin, tempoEsperaZV10PMax
    global tempoEsperaZP1PMin, tempoEsperaZP1PMax, tempoEsperaZP2PMin, tempoEsperaZP2PMax, tempoEsperaZP3PMin, tempoEsperaZP3PMax, tempoEsperaZP4PMin, tempoEsperaZP4PMax
    global tempoEsperaZL1PMin, tempoEsperaZL1PMax, tempoEsperaZL2PMin, tempoEsperaZL2PMax
    global tempoEsperaZV1Min, tempoEsperaZV1Max, tempoEsperaZV1_10_13, tempoEsperaZV1_10_13_Max, tempoEsperaZV1_10_13_Min, tempoEsperaZV1_13_16_Max, tempoEsperaZV1_13_16_Min, tempoEsperaZV1_16_19, tempoEsperaZV1_16_19_Max, tempoEsperaZV1_16_19_Min, tempoEsperaZV1_19_22, tempoEsperaZV1_19_22_Max, tempoEsperaZV1_19_22_Min
    global tempoEsperaZV2Min, tempoEsperaZV2Max, tempoEsperaZV2_10_13, tempoEsperaZV2_10_13_Max, tempoEsperaZV2_10_13_Min, tempoEsperaZV2_13_16_Max, tempoEsperaZV2_13_16_Min, tempoEsperaZV2_16_19, tempoEsperaZV2_16_19_Max, tempoEsperaZV2_16_19_Min, tempoEsperaZV2_19_22, tempoEsperaZV2_19_22_Max, tempoEsperaZV2_19_22_Min
    global tempoEsperaZV3Min, tempoEsperaZV3Max, tempoEsperaZV3_10_13, tempoEsperaZV3_10_13_Max, tempoEsperaZV3_10_13_Min, tempoEsperaZV3_13_16_Max, tempoEsperaZV3_13_16_Min, tempoEsperaZV3_16_19, tempoEsperaZV3_16_19_Max, tempoEsperaZV3_16_19_Min, tempoEsperaZV3_19_22, tempoEsperaZV3_19_22_Max, tempoEsperaZV3_19_22_Min
    global tempoEsperaZV4Min, tempoEsperaZV4Max, tempoEsperaZV4_10_13, tempoEsperaZV4_10_13_Max, tempoEsperaZV4_10_13_Min, tempoEsperaZV4_13_16_Max, tempoEsperaZV4_13_16_Min, tempoEsperaZV4_16_19, tempoEsperaZV4_16_19_Max, tempoEsperaZV4_16_19_Min, tempoEsperaZV4_19_22, tempoEsperaZV4_19_22_Max, tempoEsperaZV4_19_22_Min
    global tempoEsperaZV5Min, tempoEsperaZV5Max, tempoEsperaZV5_10_13, tempoEsperaZV5_10_13_Max, tempoEsperaZV5_10_13_Min, tempoEsperaZV5_13_16_Max, tempoEsperaZV5_13_16_Min, tempoEsperaZV5_16_19, tempoEsperaZV5_16_19_Max, tempoEsperaZV5_16_19_Min, tempoEsperaZV5_19_22, tempoEsperaZV5_19_22_Max, tempoEsperaZV5_19_22_Min
    global tempoEsperaZV6Min, tempoEsperaZV6Max, tempoEsperaZV6_10_13, tempoEsperaZV6_10_13_Max, tempoEsperaZV6_10_13_Min, tempoEsperaZV6_13_16_Max, tempoEsperaZV6_13_16_Min, tempoEsperaZV6_16_19, tempoEsperaZV6_16_19_Max, tempoEsperaZV6_16_19_Min, tempoEsperaZV6_19_22, tempoEsperaZV6_19_22_Max, tempoEsperaZV6_19_22_Min
    global tempoEsperaZV7Min, tempoEsperaZV7Max, tempoEsperaZV7_10_13, tempoEsperaZV7_10_13_Max, tempoEsperaZV7_10_13_Min, tempoEsperaZV7_13_16_Max, tempoEsperaZV7_13_16_Min, tempoEsperaZV7_16_19, tempoEsperaZV7_16_19_Max, tempoEsperaZV7_16_19_Min, tempoEsperaZV7_19_22, tempoEsperaZV7_19_22_Max, tempoEsperaZV7_19_22_Min
    global tempoEsperaZV8Min, tempoEsperaZV8Max, tempoEsperaZV8_10_13, tempoEsperaZV8_10_13_Max, tempoEsperaZV8_10_13_Min, tempoEsperaZV8_13_16_Max, tempoEsperaZV8_13_16_Min, tempoEsperaZV8_16_19, tempoEsperaZV8_16_19_Max, tempoEsperaZV8_16_19_Min, tempoEsperaZV8_19_22, tempoEsperaZV8_19_22_Max, tempoEsperaZV8_19_22_Min
    global tempoEsperaZV9Min, tempoEsperaZV9Max, tempoEsperaZV9_10_13, tempoEsperaZV9_10_13_Max, tempoEsperaZV9_10_13_Min, tempoEsperaZV9_13_16_Max, tempoEsperaZV9_13_16_Min, tempoEsperaZV9_16_19, tempoEsperaZV9_16_19_Max, tempoEsperaZV9_16_19_Min, tempoEsperaZV9_19_22, tempoEsperaZV9_19_22_Max, tempoEsperaZV9_19_22_Min
    global tempoEsperaZV10Min, tempoEsperaZV10Max, tempoEsperaZV10_10_13, tempoEsperaZV10_10_13_Max, tempoEsperaZV10_10_13_Min, tempoEsperaZV10_13_16_Max, tempoEsperaZV10_13_16_Min, tempoEsperaZV10_16_19, tempoEsperaZV10_16_19_Max, tempoEsperaZV10_16_19_Min, tempoEsperaZV10_19_22, tempoEsperaZV10_19_22_Max, tempoEsperaZV10_19_22_Min
    global tempoEsperaZP1, tempoEsperaZP1P, tempoEsperaZP2, tempoEsperaZP2P, tempoEsperaZP3, tempoEsperaZP3P, tempoEsperaZP4, tempoEsperaZP4P
    global tempoEsperaZP1Min, tempoEsperaZP1Max, tempoEsperaZP1_10_13, tempoEsperaZP1_10_13_Max, tempoEsperaZP1_10_13_Min, tempoEsperaZP1_13_16, tempoEsperaZP1_13_16_Max, tempoEsperaZP1_13_16_Min, tempoEsperaZP1_16_19, tempoEsperaZP1_16_19_Max, tempoEsperaZP1_16_19_Min, tempoEsperaZP1_19_22, tempoEsperaZP1_19_22_Max, tempoEsperaZP1_19_22_Min
    global tempoEsperaZP2Min, tempoEsperaZP2Max, tempoEsperaZP2_10_13, tempoEsperaZP2_10_13_Max, tempoEsperaZP2_10_13_Min, tempoEsperaZP2_13_16, tempoEsperaZP2_13_16_Max, tempoEsperaZP2_13_16_Min, tempoEsperaZP2_16_19, tempoEsperaZP2_16_19_Max, tempoEsperaZP2_16_19_Min, tempoEsperaZP2_19_22, tempoEsperaZP2_19_22_Max, tempoEsperaZP2_19_22_Min
    global tempoEsperaZP3Min, tempoEsperaZP3Max, tempoEsperaZP3_10_13, tempoEsperaZP3_10_13_Max, tempoEsperaZP3_10_13_Min, tempoEsperaZP3_13_16, tempoEsperaZP3_13_16_Max, tempoEsperaZP3_13_16_Min, tempoEsperaZP3_16_19, tempoEsperaZP3_16_19_Max, tempoEsperaZP3_16_19_Min, tempoEsperaZP3_19_22, tempoEsperaZP3_19_22_Max, tempoEsperaZP3_19_22_Min
    global tempoEsperaZP4Min, tempoEsperaZP4Max, tempoEsperaZP4_10_13, tempoEsperaZP4_10_13_Max, tempoEsperaZP4_10_13_Min, tempoEsperaZP4_13_16, tempoEsperaZP4_13_16_Max, tempoEsperaZP4_13_16_Min, tempoEsperaZP4_16_19, tempoEsperaZP4_16_19_Max, tempoEsperaZP4_16_19_Min, tempoEsperaZP4_19_22, tempoEsperaZP4_19_22_Max, tempoEsperaZP4_19_22_Min
    global tempoEsperaZL1Min, tempoEsperaZL1Max, tempoEsperaZL1_10_13, tempoEsperaZL1_10_13_Max, tempoEsperaZL1_10_13_Min, tempoEsperaZL1_13_16, tempoEsperaZL1_13_16_Max, tempoEsperaZL1_13_16_Min, tempoEsperaZL1_16_19, tempoEsperaZL1_16_19_Max, tempoEsperaZL1_16_19_Min, tempoEsperaZL1_19_22, tempoEsperaZL1_19_22_Max, tempoEsperaZL1_19_22_Min
    global tempoEsperaZL2Min, tempoEsperaZL2Max, tempoEsperaZL2_10_13, tempoEsperaZL2_10_13_Max, tempoEsperaZL2_10_13_Min, tempoEsperaZL2_13_16, tempoEsperaZL2_13_16_Max, tempoEsperaZL2_13_16_Min, tempoEsperaZL2_16_19, tempoEsperaZL2_16_19_Max, tempoEsperaZL2_16_19_Min, tempoEsperaZL2_19_22, tempoEsperaZL2_19_22_Max, tempoEsperaZL2_19_22_Min

    global tempoEsperaZV1PMin, tempoEsperaZV1PMax, tempoEsperaZV1P_10_13, tempoEsperaZV1P_10_13_Max, tempoEsperaZV1P_10_13_Min, tempoEsperaZV1P_13_16_Max, tempoEsperaZV1P_13_16_Min, tempoEsperaZV1P_16_19, tempoEsperaZV1P_16_19_Max, tempoEsperaZV1P_16_19_Min, tempoEsperaZV1P_19_22, tempoEsperaZV1P_19_22_Max, tempoEsperaZV1P_19_22_Min
    global tempoEsperaZV2PMin, tempoEsperaZV2PMax, tempoEsperaZV2P_10_13, tempoEsperaZV2P_10_13_Max, tempoEsperaZV2P_10_13_Min, tempoEsperaZV2P_13_16_Max, tempoEsperaZV2P_13_16_Min, tempoEsperaZV2P_16_19, tempoEsperaZV2P_16_19_Max, tempoEsperaZV2P_16_19_Min, tempoEsperaZV2P_19_22, tempoEsperaZV2P_19_22_Max, tempoEsperaZV2P_19_22_Min
    global tempoEsperaZV3PMin, tempoEsperaZV3PMax, tempoEsperaZV3P_10_13, tempoEsperaZV3P_10_13_Max, tempoEsperaZV3P_10_13_Min, tempoEsperaZV3P_13_16_Max, tempoEsperaZV3P_13_16_Min, tempoEsperaZV3P_16_19, tempoEsperaZV3P_16_19_Max, tempoEsperaZV3P_16_19_Min, tempoEsperaZV3P_19_22, tempoEsperaZV3P_19_22_Max, tempoEsperaZV3P_19_22_Min
    global tempoEsperaZV4PMin, tempoEsperaZV4PMax, tempoEsperaZV4P_10_13, tempoEsperaZV4P_10_13_Max, tempoEsperaZV4P_10_13_Min, tempoEsperaZV4P_13_16_Max, tempoEsperaZV4P_13_16_Min, tempoEsperaZV4P_16_19, tempoEsperaZV4P_16_19_Max, tempoEsperaZV4P_16_19_Min, tempoEsperaZV4P_19_22, tempoEsperaZV4P_19_22_Max, tempoEsperaZV4P_19_22_Min
    global tempoEsperaZV5PMin, tempoEsperaZV5PMax, tempoEsperaZV5P_10_13, tempoEsperaZV5P_10_13_Max, tempoEsperaZV5P_10_13_Min, tempoEsperaZV5P_13_16_Max, tempoEsperaZV5P_13_16_Min, tempoEsperaZV5P_16_19, tempoEsperaZV5P_16_19_Max, tempoEsperaZV5P_16_19_Min, tempoEsperaZV5P_19_22, tempoEsperaZV5P_19_22_Max, tempoEsperaZV5P_19_22_Min
    global tempoEsperaZV6PMin, tempoEsperaZV6PMax, tempoEsperaZV6P_10_13, tempoEsperaZV6P_10_13_Max, tempoEsperaZV6P_10_13_Min, tempoEsperaZV6P_13_16_Max, tempoEsperaZV6P_13_16_Min, tempoEsperaZV6P_16_19, tempoEsperaZV6P_16_19_Max, tempoEsperaZV6P_16_19_Min, tempoEsperaZV6P_19_22, tempoEsperaZV6P_19_22_Max, tempoEsperaZV6P_19_22_Min
    global tempoEsperaZV7PMin, tempoEsperaZV7PMax, tempoEsperaZV7P_10_13, tempoEsperaZV7P_10_13_Max, tempoEsperaZV7P_10_13_Min, tempoEsperaZV7P_13_16_Max, tempoEsperaZV7P_13_16_Min, tempoEsperaZV7P_16_19, tempoEsperaZV7P_16_19_Max, tempoEsperaZV7P_16_19_Min, tempoEsperaZV7P_19_22, tempoEsperaZV7P_19_22_Max, tempoEsperaZV7P_19_22_Min
    global tempoEsperaZV8PMin, tempoEsperaZV8PMax, tempoEsperaZV8P_10_13, tempoEsperaZV8P_10_13_Max, tempoEsperaZV8P_10_13_Min, tempoEsperaZV8P_13_16_Max, tempoEsperaZV8P_13_16_Min, tempoEsperaZV8P_16_19, tempoEsperaZV8P_16_19_Max, tempoEsperaZV8P_16_19_Min, tempoEsperaZV8P_19_22, tempoEsperaZV8P_19_22_Max, tempoEsperaZV8P_19_22_Min
    global tempoEsperaZV9PMin, tempoEsperaZV9PMax, tempoEsperaZV9P_10_13, tempoEsperaZV9P_10_13_Max, tempoEsperaZV9P_10_13_Min, tempoEsperaZV9P_13_16_Max, tempoEsperaZV9P_13_16_Min, tempoEsperaZV9P_16_19, tempoEsperaZV9P_16_19_Max, tempoEsperaZV9P_16_19_Min, tempoEsperaZV9P_19_22, tempoEsperaZV9P_19_22_Max, tempoEsperaZV9P_19_22_Min
    global tempoEsperaZV10PMin, tempoEsperaZV10PMax, tempoEsperaZV10P_10_13, tempoEsperaZV10P_10_13_Max, tempoEsperaZV10P_10_13_Min, tempoEsperaZV10P_13_16_Max, tempoEsperaZV10P_13_16_Min, tempoEsperaZV10P_16_19, tempoEsperaZV10P_16_19_Max, tempoEsperaZV10P_16_19_Min, tempoEsperaZV10P_19_22, tempoEsperaZV10P_19_22_Max, tempoEsperaZV10P_19_22_Min
    global tempoEsperaZP1PMin, tempoEsperaZP1PMax, tempoEsperaZP1P_10_13, tempoEsperaZP1P_10_13_Max, tempoEsperaZP1P_10_13_Min, tempoEsperaZP1P_13_16, tempoEsperaZP1P_13_16_Max, tempoEsperaZP1P_13_16_Min, tempoEsperaZP1P_16_19, tempoEsperaZP1P_16_19_Max, tempoEsperaZP1P_16_19_Min, tempoEsperaZP1P_19_22, tempoEsperaZP1P_19_22_Max, tempoEsperaZP1P_19_22_Min
    global tempoEsperaZP2PMin, tempoEsperaZP2PMax, tempoEsperaZP2P_10_13, tempoEsperaZP2P_10_13_Max, tempoEsperaZP2P_10_13_Min, tempoEsperaZP2P_13_16, tempoEsperaZP2P_13_16_Max, tempoEsperaZP2P_13_16_Min, tempoEsperaZP2P_16_19, tempoEsperaZP2P_16_19_Max, tempoEsperaZP2P_16_19_Min, tempoEsperaZP2P_19_22, tempoEsperaZP2P_19_22_Max, tempoEsperaZP2P_19_22_Min
    global tempoEsperaZP3PMin, tempoEsperaZP3PMax, tempoEsperaZP3P_10_13, tempoEsperaZP3P_10_13_Max, tempoEsperaZP3P_10_13_Min, tempoEsperaZP3P_13_16, tempoEsperaZP3P_13_16_Max, tempoEsperaZP3P_13_16_Min, tempoEsperaZP3P_16_19, tempoEsperaZP3P_16_19_Max, tempoEsperaZP3P_16_19_Min, tempoEsperaZP3P_19_22, tempoEsperaZP3P_19_22_Max, tempoEsperaZP3P_19_22_Min
    global tempoEsperaZP4PMin, tempoEsperaZP4PMax, tempoEsperaZP4P_10_13, tempoEsperaZP4P_10_13_Max, tempoEsperaZP4P_10_13_Min, tempoEsperaZP4P_13_16, tempoEsperaZP4P_13_16_Max, tempoEsperaZP4P_13_16_Min, tempoEsperaZP4P_16_19, tempoEsperaZP4P_16_19_Max, tempoEsperaZP4P_16_19_Min, tempoEsperaZP4P_19_22, tempoEsperaZP4P_19_22_Max, tempoEsperaZP4P_19_22_Min
    global tempoEsperaZL1PMin, tempoEsperaZL1PMax, tempoEsperaZL1P_10_13, tempoEsperaZL1P_10_13_Max, tempoEsperaZL1P_10_13_Min, tempoEsperaZL1P_13_16, tempoEsperaZL1P_13_16_Max, tempoEsperaZL1P_13_16_Min, tempoEsperaZL1P_16_19, tempoEsperaZL1P_16_19_Max, tempoEsperaZL1P_16_19_Min, tempoEsperaZL1P_19_22, tempoEsperaZL1P_19_22_Max, tempoEsperaZL1P_19_22_Min
    global tempoEsperaZL2PMin, tempoEsperaZL2PMax, tempoEsperaZL2P_10_13, tempoEsperaZL2P_10_13_Max, tempoEsperaZL2P_10_13_Min, tempoEsperaZL2P_13_16, tempoEsperaZL2P_13_16_Max, tempoEsperaZL2P_13_16_Min, tempoEsperaZL2P_16_19, tempoEsperaZL2P_16_19_Max, tempoEsperaZL2P_16_19_Min, tempoEsperaZL2P_19_22, tempoEsperaZL2P_19_22_Max, tempoEsperaZL2P_19_22_Min

    global numClienteZV1, numClienteZV1P, numClienteZV1_10_13, numClienteZV1_13_16, numClienteZV1_16_19, numClienteZV1_19_22
    global numClienteZV2, numClienteZV2P, numClienteZV2_10_13, numClienteZV2_13_16, numClienteZV2_16_19, numClienteZV2_19_22
    global numClienteZV3, numClienteZV3P, numClienteZV3_10_13, numClienteZV3_13_16, numClienteZV3_16_19, numClienteZV3_19_22
    global numClienteZV4, numClienteZV4P, numClienteZV4_10_13, numClienteZV4_13_16, numClienteZV4_16_19, numClienteZV4_19_22
    global numClienteZV5, numClienteZV5P, numClienteZV5_10_13, numClienteZV5_13_16, numClienteZV5_16_19, numClienteZV5_19_22
    global numClienteZV6, numClienteZV6P, numClienteZV6_10_13, numClienteZV6_13_16, numClienteZV6_16_19, numClienteZV6_19_22
    global numClienteZV7, numClienteZV7P, numClienteZV7_10_13, numClienteZV7_13_16, numClienteZV7_16_19, numClienteZV7_19_22
    global numClienteZV8, numClienteZV8P, numClienteZV8_10_13, numClienteZV8_13_16, numClienteZV8_16_19, numClienteZV8_19_22
    global numClienteZV9, numClienteZV9P, numClienteZV9_10_13, numClienteZV9_13_16, numClienteZV9_16_19, numClienteZV9_19_22
    global numClienteZV10, numClienteZV10P, numClienteZV10_10_13, numClienteZV10_13_16, numClienteZV10_16_19, numClienteZV10_19_22

    global numClienteZP1, numClienteZP1P, numClienteZP1_10_13, numClienteZP1_13_16, numClienteZP1_16_19, numClienteZP1_19_22
    global numClienteZP2, numClienteZP2P, numClienteZP2_10_13, numClienteZP2_13_16, numClienteZP2_16_19, numClienteZP2_19_22
    global numClienteZP3, numClienteZP3P, numClienteZP3_10_13, numClienteZP3_13_16, numClienteZP3_16_19, numClienteZP3_19_22
    global numClienteZP4, numClienteZP4P, numClienteZP4_10_13, numClienteZP4_13_16, numClienteZP4_16_19, numClienteZP4_19_22

    global numClienteZL1, numClienteZL1P, numClienteZL1_10_13, numClienteZL1_13_16, numClienteZL1_16_19, numClienteZL1_19_22
    global numClienteZL2, numClienteZL2P, numClienteZL2_10_13, numClienteZL2_13_16, numClienteZL2_16_19, numClienteZL2_19_22

    tempoEsperaZV1Min = 0 if tempoEsperaZV1Min == 999999 else tempoEsperaZV1Min
    tempoEsperaZV2Min = 0 if tempoEsperaZV2Min == 999999 else tempoEsperaZV2Min
    tempoEsperaZV3Min = 0 if tempoEsperaZV3Min == 999999 else tempoEsperaZV3Min
    tempoEsperaZV4Min = 0 if tempoEsperaZV4Min == 999999 else tempoEsperaZV4Min
    tempoEsperaZV5Min = 0 if tempoEsperaZV5Min == 999999 else tempoEsperaZV5Min
    tempoEsperaZV6Min = 0 if tempoEsperaZV6Min == 999999 else tempoEsperaZV6Min
    tempoEsperaZV7Min = 0 if tempoEsperaZV7Min == 999999 else tempoEsperaZV7Min
    tempoEsperaZV8Min = 0 if tempoEsperaZV8Min == 999999 else tempoEsperaZV8Min
    tempoEsperaZV9Min = 0 if tempoEsperaZV9Min == 999999 else tempoEsperaZV9Min
    tempoEsperaZV10Min = 0 if tempoEsperaZV10Min == 999999 else tempoEsperaZV10Min
    tempoEsperaZP1Min = 0 if tempoEsperaZP1Min == 999999 else tempoEsperaZP1Min
    tempoEsperaZP2Min = 0 if tempoEsperaZP2Min == 999999 else tempoEsperaZP2Min
    tempoEsperaZP3Min = 0 if tempoEsperaZP3Min == 999999 else tempoEsperaZP3Min
    tempoEsperaZP4Min = 0 if tempoEsperaZP4Min == 999999 else tempoEsperaZP4Min
    tempoEsperaZL1Min = 0 if tempoEsperaZL1Min == 999999 else tempoEsperaZL1Min
    tempoEsperaZL2Min = 0 if tempoEsperaZL2Min == 999999 else tempoEsperaZL2Min

    tempoEsperaZV1PMin = 0 if tempoEsperaZV1PMin == 999999 else tempoEsperaZV1PMin
    tempoEsperaZV2PMin = 0 if tempoEsperaZV2PMin == 999999 else tempoEsperaZV2PMin
    tempoEsperaZV3PMin = 0 if tempoEsperaZV3PMin == 999999 else tempoEsperaZV3PMin
    tempoEsperaZV4PMin = 0 if tempoEsperaZV4PMin == 999999 else tempoEsperaZV4PMin
    tempoEsperaZV5PMin = 0 if tempoEsperaZV5PMin == 999999 else tempoEsperaZV5PMin
    tempoEsperaZV6PMin = 0 if tempoEsperaZV6PMin == 999999 else tempoEsperaZV6PMin
    tempoEsperaZV7PMin = 0 if tempoEsperaZV7PMin == 999999 else tempoEsperaZV7PMin
    tempoEsperaZV8PMin = 0 if tempoEsperaZV8PMin == 999999 else tempoEsperaZV8PMin
    tempoEsperaZV9PMin = 0 if tempoEsperaZV9PMin == 999999 else tempoEsperaZV9PMin
    tempoEsperaZV10PMin = 0 if tempoEsperaZV10PMin == 999999 else tempoEsperaZV10PMin
    tempoEsperaZP1PMin = 0 if tempoEsperaZP1PMin == 999999 else tempoEsperaZP1PMin
    tempoEsperaZP2PMin = 0 if tempoEsperaZP2PMin == 999999 else tempoEsperaZP2PMin
    tempoEsperaZP3PMin = 0 if tempoEsperaZP3PMin == 999999 else tempoEsperaZP3PMin
    tempoEsperaZP4PMin = 0 if tempoEsperaZP4PMin == 999999 else tempoEsperaZP4PMin
    tempoEsperaZL1PMin = 0 if tempoEsperaZL1PMin == 999999 else tempoEsperaZL1PMin
    tempoEsperaZL2PMin = 0 if tempoEsperaZL2PMin == 999999 else tempoEsperaZL2PMin

    tempoEsperaZV1_10_13_Min = 0 if tempoEsperaZV1_10_13_Min == 999999 else tempoEsperaZV1_10_13_Min
    tempoEsperaZV1_13_16_Min = 0 if tempoEsperaZV1_13_16_Min == 999999 else tempoEsperaZV1_13_16_Min
    tempoEsperaZV1_16_19_Min = 0 if tempoEsperaZV1_16_19_Min == 999999 else tempoEsperaZV1_16_19_Min
    tempoEsperaZV1_19_22_Min = 0 if tempoEsperaZV1_19_22_Min == 999999 else tempoEsperaZV1_19_22_Min
    tempoEsperaZV1P_10_13_Min = 0 if tempoEsperaZV1P_10_13_Min == 999999 else tempoEsperaZV1P_10_13_Min
    tempoEsperaZV1P_13_16_Min = 0 if tempoEsperaZV1P_13_16_Min == 999999 else tempoEsperaZV1P_13_16_Min
    tempoEsperaZV1P_16_19_Min = 0 if tempoEsperaZV1P_16_19_Min == 999999 else tempoEsperaZV1P_16_19_Min
    tempoEsperaZV1P_19_22_Min = 0 if tempoEsperaZV1P_19_22_Min == 999999 else tempoEsperaZV1P_19_22_Min
    tempoEsperaZV2_10_13_Min = 0 if tempoEsperaZV2_10_13_Min == 999999 else tempoEsperaZV2_10_13_Min
    tempoEsperaZV2_13_16_Min = 0 if tempoEsperaZV2_13_16_Min == 999999 else tempoEsperaZV2_13_16_Min
    tempoEsperaZV2_16_19_Min = 0 if tempoEsperaZV2_16_19_Min == 999999 else tempoEsperaZV2_16_19_Min
    tempoEsperaZV2_19_22_Min = 0 if tempoEsperaZV2_19_22_Min == 999999 else tempoEsperaZV2_19_22_Min
    tempoEsperaZV2P_10_13_Min = 0 if tempoEsperaZV2P_10_13_Min == 999999 else tempoEsperaZV2P_10_13_Min
    tempoEsperaZV2P_13_16_Min = 0 if tempoEsperaZV2P_13_16_Min == 999999 else tempoEsperaZV2P_13_16_Min
    tempoEsperaZV2P_16_19_Min = 0 if tempoEsperaZV2P_16_19_Min == 999999 else tempoEsperaZV2P_16_19_Min
    tempoEsperaZV2P_19_22_Min = 0 if tempoEsperaZV2P_19_22_Min == 999999 else tempoEsperaZV2P_19_22_Min
    tempoEsperaZV3_10_13_Min = 0 if tempoEsperaZV3_10_13_Min == 999999 else tempoEsperaZV3_10_13_Min
    tempoEsperaZV3_13_16_Min = 0 if tempoEsperaZV3_13_16_Min == 999999 else tempoEsperaZV3_13_16_Min
    tempoEsperaZV3_16_19_Min = 0 if tempoEsperaZV3_16_19_Min == 999999 else tempoEsperaZV3_16_19_Min
    tempoEsperaZV3_19_22_Min = 0 if tempoEsperaZV3_19_22_Min == 999999 else tempoEsperaZV3_19_22_Min
    tempoEsperaZV3P_10_13_Min = 0 if tempoEsperaZV3P_10_13_Min == 999999 else tempoEsperaZV3P_10_13_Min
    tempoEsperaZV3P_13_16_Min = 0 if tempoEsperaZV3P_13_16_Min == 999999 else tempoEsperaZV3P_13_16_Min
    tempoEsperaZV3P_16_19_Min = 0 if tempoEsperaZV3P_16_19_Min == 999999 else tempoEsperaZV3P_16_19_Min
    tempoEsperaZV3P_19_22_Min = 0 if tempoEsperaZV3P_19_22_Min == 999999 else tempoEsperaZV3P_19_22_Min
    tempoEsperaZV4_10_13_Min = 0 if tempoEsperaZV4_10_13_Min == 999999 else tempoEsperaZV4_10_13_Min
    tempoEsperaZV4_13_16_Min = 0 if tempoEsperaZV4_13_16_Min == 999999 else tempoEsperaZV4_13_16_Min
    tempoEsperaZV4_16_19_Min = 0 if tempoEsperaZV4_16_19_Min == 999999 else tempoEsperaZV4_16_19_Min
    tempoEsperaZV4_19_22_Min = 0 if tempoEsperaZV4_19_22_Min == 999999 else tempoEsperaZV4_19_22_Min
    tempoEsperaZV4P_10_13_Min = 0 if tempoEsperaZV4P_10_13_Min == 999999 else tempoEsperaZV4P_10_13_Min
    tempoEsperaZV4P_13_16_Min = 0 if tempoEsperaZV4P_13_16_Min == 999999 else tempoEsperaZV4P_13_16_Min
    tempoEsperaZV4P_16_19_Min = 0 if tempoEsperaZV4P_16_19_Min == 999999 else tempoEsperaZV4P_16_19_Min
    tempoEsperaZV4P_19_22_Min = 0 if tempoEsperaZV4P_19_22_Min == 999999 else tempoEsperaZV4P_19_22_Min
    tempoEsperaZV5_10_13_Min = 0 if tempoEsperaZV5_10_13_Min == 999999 else tempoEsperaZV5_10_13_Min
    tempoEsperaZV5_13_16_Min = 0 if tempoEsperaZV5_13_16_Min == 999999 else tempoEsperaZV5_13_16_Min
    tempoEsperaZV5_16_19_Min = 0 if tempoEsperaZV5_16_19_Min == 999999 else tempoEsperaZV5_16_19_Min
    tempoEsperaZV5_19_22_Min = 0 if tempoEsperaZV5_19_22_Min == 999999 else tempoEsperaZV5_19_22_Min
    tempoEsperaZV5P_10_13_Min = 0 if tempoEsperaZV5P_10_13_Min == 999999 else tempoEsperaZV5P_10_13_Min
    tempoEsperaZV5P_13_16_Min = 0 if tempoEsperaZV5P_13_16_Min == 999999 else tempoEsperaZV5P_13_16_Min
    tempoEsperaZV5P_16_19_Min = 0 if tempoEsperaZV5P_16_19_Min == 999999 else tempoEsperaZV5P_16_19_Min
    tempoEsperaZV5P_19_22_Min = 0 if tempoEsperaZV5P_19_22_Min == 999999 else tempoEsperaZV5P_19_22_Min
    tempoEsperaZV6_10_13_Min = 0 if tempoEsperaZV6_10_13_Min == 999999 else tempoEsperaZV6_10_13_Min
    tempoEsperaZV6_13_16_Min = 0 if tempoEsperaZV6_13_16_Min == 999999 else tempoEsperaZV6_13_16_Min
    tempoEsperaZV6_16_19_Min = 0 if tempoEsperaZV6_16_19_Min == 999999 else tempoEsperaZV6_16_19_Min
    tempoEsperaZV6_19_22_Min = 0 if tempoEsperaZV6_19_22_Min == 999999 else tempoEsperaZV6_19_22_Min
    tempoEsperaZV6P_10_13_Min = 0 if tempoEsperaZV6P_10_13_Min == 999999 else tempoEsperaZV6P_10_13_Min
    tempoEsperaZV6P_13_16_Min = 0 if tempoEsperaZV6P_13_16_Min == 999999 else tempoEsperaZV6P_13_16_Min
    tempoEsperaZV6P_16_19_Min = 0 if tempoEsperaZV6P_16_19_Min == 999999 else tempoEsperaZV6P_16_19_Min
    tempoEsperaZV6P_19_22_Min = 0 if tempoEsperaZV6P_19_22_Min == 999999 else tempoEsperaZV6P_19_22_Min
    tempoEsperaZV7_10_13_Min = 0 if tempoEsperaZV7_10_13_Min == 999999 else tempoEsperaZV7_10_13_Min
    tempoEsperaZV7_13_16_Min = 0 if tempoEsperaZV7_13_16_Min == 999999 else tempoEsperaZV7_13_16_Min
    tempoEsperaZV7_16_19_Min = 0 if tempoEsperaZV7_16_19_Min == 999999 else tempoEsperaZV7_16_19_Min
    tempoEsperaZV7_19_22_Min = 0 if tempoEsperaZV7_19_22_Min == 999999 else tempoEsperaZV7_19_22_Min
    tempoEsperaZV7P_10_13_Min = 0 if tempoEsperaZV7P_10_13_Min == 999999 else tempoEsperaZV7P_10_13_Min
    tempoEsperaZV7P_13_16_Min = 0 if tempoEsperaZV7P_13_16_Min == 999999 else tempoEsperaZV7P_13_16_Min
    tempoEsperaZV7P_16_19_Min = 0 if tempoEsperaZV7P_16_19_Min == 999999 else tempoEsperaZV7P_16_19_Min
    tempoEsperaZV7P_19_22_Min = 0 if tempoEsperaZV7P_19_22_Min == 999999 else tempoEsperaZV7P_19_22_Min
    tempoEsperaZV8_10_13_Min = 0 if tempoEsperaZV8_10_13_Min == 999999 else tempoEsperaZV8_10_13_Min
    tempoEsperaZV8_13_16_Min = 0 if tempoEsperaZV8_13_16_Min == 999999 else tempoEsperaZV8_13_16_Min
    tempoEsperaZV8_16_19_Min = 0 if tempoEsperaZV8_16_19_Min == 999999 else tempoEsperaZV8_16_19_Min
    tempoEsperaZV8_19_22_Min = 0 if tempoEsperaZV8_19_22_Min == 999999 else tempoEsperaZV8_19_22_Min
    tempoEsperaZV8P_10_13_Min = 0 if tempoEsperaZV8P_10_13_Min == 999999 else tempoEsperaZV8P_10_13_Min
    tempoEsperaZV8P_13_16_Min = 0 if tempoEsperaZV8P_13_16_Min == 999999 else tempoEsperaZV8P_13_16_Min
    tempoEsperaZV8P_16_19_Min = 0 if tempoEsperaZV8P_16_19_Min == 999999 else tempoEsperaZV8P_16_19_Min
    tempoEsperaZV8P_19_22_Min = 0 if tempoEsperaZV8P_19_22_Min == 999999 else tempoEsperaZV8P_19_22_Min
    tempoEsperaZV9_10_13_Min = 0 if tempoEsperaZV9_10_13_Min == 999999 else tempoEsperaZV9_10_13_Min
    tempoEsperaZV9_13_16_Min = 0 if tempoEsperaZV9_13_16_Min == 999999 else tempoEsperaZV9_13_16_Min
    tempoEsperaZV9_16_19_Min = 0 if tempoEsperaZV9_16_19_Min == 999999 else tempoEsperaZV9_16_19_Min
    tempoEsperaZV9_19_22_Min = 0 if tempoEsperaZV9_19_22_Min == 999999 else tempoEsperaZV9_19_22_Min
    tempoEsperaZV9P_10_13_Min = 0 if tempoEsperaZV9P_10_13_Min == 999999 else tempoEsperaZV9P_10_13_Min
    tempoEsperaZV9P_13_16_Min = 0 if tempoEsperaZV9P_13_16_Min == 999999 else tempoEsperaZV9P_13_16_Min
    tempoEsperaZV9P_16_19_Min = 0 if tempoEsperaZV9P_16_19_Min == 999999 else tempoEsperaZV9P_16_19_Min
    tempoEsperaZV9P_19_22_Min = 0 if tempoEsperaZV9P_19_22_Min == 999999 else tempoEsperaZV9P_19_22_Min
    tempoEsperaZV10_10_13_Min = 0 if tempoEsperaZV10_10_13_Min == 999999 else tempoEsperaZV10_10_13_Min
    tempoEsperaZV10_13_16_Min = 0 if tempoEsperaZV10_13_16_Min == 999999 else tempoEsperaZV10_13_16_Min
    tempoEsperaZV10_16_19_Min = 0 if tempoEsperaZV10_16_19_Min == 999999 else tempoEsperaZV10_16_19_Min
    tempoEsperaZV10_19_22_Min = 0 if tempoEsperaZV10_19_22_Min == 999999 else tempoEsperaZV10_19_22_Min
    tempoEsperaZV10P_10_13_Min = 0 if tempoEsperaZV10P_10_13_Min == 999999 else tempoEsperaZV10P_10_13_Min
    tempoEsperaZV10P_13_16_Min = 0 if tempoEsperaZV10P_13_16_Min == 999999 else tempoEsperaZV10P_13_16_Min
    tempoEsperaZV10P_16_19_Min = 0 if tempoEsperaZV10P_16_19_Min == 999999 else tempoEsperaZV10P_16_19_Min
    tempoEsperaZV10P_19_22_Min = 0 if tempoEsperaZV10P_19_22_Min == 999999 else tempoEsperaZV10P_19_22_Min

    tempoEsperaZP1_10_13_Min = 0 if tempoEsperaZP1_10_13_Min == 999999 else tempoEsperaZP1_10_13_Min
    tempoEsperaZP1_13_16_Min = 0 if tempoEsperaZP1_13_16_Min == 999999 else tempoEsperaZP1_13_16_Min
    tempoEsperaZP1_16_19_Min = 0 if tempoEsperaZP1_16_19_Min == 999999 else tempoEsperaZP1_16_19_Min
    tempoEsperaZP1_19_22_Min = 0 if tempoEsperaZP1_19_22_Min == 999999 else tempoEsperaZP1_19_22_Min
    tempoEsperaZP1P_10_13_Min = 0 if tempoEsperaZP1P_10_13_Min == 999999 else tempoEsperaZP1P_10_13_Min
    tempoEsperaZP1P_13_16_Min = 0 if tempoEsperaZP1P_13_16_Min == 999999 else tempoEsperaZP1P_13_16_Min
    tempoEsperaZP1P_16_19_Min = 0 if tempoEsperaZP1P_16_19_Min == 999999 else tempoEsperaZP1P_16_19_Min
    tempoEsperaZP1P_19_22_Min = 0 if tempoEsperaZP1P_19_22_Min == 999999 else tempoEsperaZP1P_19_22_Min
    tempoEsperaZP2_10_13_Min = 0 if tempoEsperaZP2_10_13_Min == 999999 else tempoEsperaZP2_10_13_Min
    tempoEsperaZP2_13_16_Min = 0 if tempoEsperaZP2_13_16_Min == 999999 else tempoEsperaZP2_13_16_Min
    tempoEsperaZP2_16_19_Min = 0 if tempoEsperaZP2_16_19_Min == 999999 else tempoEsperaZP2_16_19_Min
    tempoEsperaZP2_19_22_Min = 0 if tempoEsperaZP2_19_22_Min == 999999 else tempoEsperaZP2_19_22_Min
    tempoEsperaZP2P_10_13_Min = 0 if tempoEsperaZP2P_10_13_Min == 999999 else tempoEsperaZP2P_10_13_Min
    tempoEsperaZP2P_13_16_Min = 0 if tempoEsperaZP2P_13_16_Min == 999999 else tempoEsperaZP2P_13_16_Min
    tempoEsperaZP2P_16_19_Min = 0 if tempoEsperaZP2P_16_19_Min == 999999 else tempoEsperaZP2P_16_19_Min
    tempoEsperaZP2P_19_22_Min = 0 if tempoEsperaZP2P_19_22_Min == 999999 else tempoEsperaZP2P_19_22_Min
    tempoEsperaZP3_10_13_Min = 0 if tempoEsperaZP3_10_13_Min == 999999 else tempoEsperaZP3_10_13_Min
    tempoEsperaZP3_13_16_Min = 0 if tempoEsperaZP3_13_16_Min == 999999 else tempoEsperaZP3_13_16_Min
    tempoEsperaZP3_16_19_Min = 0 if tempoEsperaZP3_16_19_Min == 999999 else tempoEsperaZP3_16_19_Min
    tempoEsperaZP3_19_22_Min = 0 if tempoEsperaZP3_19_22_Min == 999999 else tempoEsperaZP3_19_22_Min
    tempoEsperaZP3P_10_13_Min = 0 if tempoEsperaZP3P_10_13_Min == 999999 else tempoEsperaZP3P_10_13_Min
    tempoEsperaZP3P_13_16_Min = 0 if tempoEsperaZP3P_13_16_Min == 999999 else tempoEsperaZP3P_13_16_Min
    tempoEsperaZP3P_16_19_Min = 0 if tempoEsperaZP3P_16_19_Min == 999999 else tempoEsperaZP3P_16_19_Min
    tempoEsperaZP3P_19_22_Min = 0 if tempoEsperaZP3P_19_22_Min == 999999 else tempoEsperaZP3P_19_22_Min
    tempoEsperaZP4_10_13_Min = 0 if tempoEsperaZP4_10_13_Min == 999999 else tempoEsperaZP4_10_13_Min
    tempoEsperaZP4_13_16_Min = 0 if tempoEsperaZP4_13_16_Min == 999999 else tempoEsperaZP4_13_16_Min
    tempoEsperaZP4_16_19_Min = 0 if tempoEsperaZP4_16_19_Min == 999999 else tempoEsperaZP4_16_19_Min
    tempoEsperaZP4_19_22_Min = 0 if tempoEsperaZP4_19_22_Min == 999999 else tempoEsperaZP4_19_22_Min
    tempoEsperaZP4P_10_13_Min = 0 if tempoEsperaZP4P_10_13_Min == 999999 else tempoEsperaZP4P_10_13_Min
    tempoEsperaZP4P_13_16_Min = 0 if tempoEsperaZP4P_13_16_Min == 999999 else tempoEsperaZP4P_13_16_Min
    tempoEsperaZP4P_16_19_Min = 0 if tempoEsperaZP4P_16_19_Min == 999999 else tempoEsperaZP4P_16_19_Min
    tempoEsperaZP4P_19_22_Min = 0 if tempoEsperaZP4P_19_22_Min == 999999 else tempoEsperaZP4P_19_22_Min

    tempoEsperaZL1_10_13_Min = 0 if tempoEsperaZL1_10_13_Min == 999999 else tempoEsperaZL1_10_13_Min
    tempoEsperaZL1_13_16_Min = 0 if tempoEsperaZL1_13_16_Min == 999999 else tempoEsperaZL1_13_16_Min
    tempoEsperaZL1_16_19_Min = 0 if tempoEsperaZL1_16_19_Min == 999999 else tempoEsperaZL1_16_19_Min
    tempoEsperaZL1_19_22_Min = 0 if tempoEsperaZL1_19_22_Min == 999999 else tempoEsperaZL1_19_22_Min
    tempoEsperaZL1P_10_13_Min = 0 if tempoEsperaZL1P_10_13_Min == 999999 else tempoEsperaZL1P_10_13_Min
    tempoEsperaZL1P_13_16_Min = 0 if tempoEsperaZL1P_13_16_Min == 999999 else tempoEsperaZL1P_13_16_Min
    tempoEsperaZL1P_16_19_Min = 0 if tempoEsperaZL1P_16_19_Min == 999999 else tempoEsperaZL1P_16_19_Min
    tempoEsperaZL1P_19_22_Min = 0 if tempoEsperaZL1P_19_22_Min == 999999 else tempoEsperaZL1P_19_22_Min
    tempoEsperaZL2_10_13_Min = 0 if tempoEsperaZL2_10_13_Min == 999999 else tempoEsperaZL2_10_13_Min
    tempoEsperaZL2_13_16_Min = 0 if tempoEsperaZL2_13_16_Min == 999999 else tempoEsperaZL2_13_16_Min
    tempoEsperaZL2_16_19_Min = 0 if tempoEsperaZL2_16_19_Min == 999999 else tempoEsperaZL2_16_19_Min
    tempoEsperaZL2_19_22_Min = 0 if tempoEsperaZL2_19_22_Min == 999999 else tempoEsperaZL2_19_22_Min
    tempoEsperaZL2P_10_13_Min = 0 if tempoEsperaZL2P_10_13_Min == 999999 else tempoEsperaZL2P_10_13_Min
    tempoEsperaZL2P_13_16_Min = 0 if tempoEsperaZL2P_13_16_Min == 999999 else tempoEsperaZL2P_13_16_Min
    tempoEsperaZL2P_16_19_Min = 0 if tempoEsperaZL2P_16_19_Min == 999999 else tempoEsperaZL2P_16_19_Min
    tempoEsperaZL2P_19_22_Min = 0 if tempoEsperaZL2P_19_22_Min == 999999 else tempoEsperaZL2P_19_22_Min


def eventoPartidaZV1():
    global estadoZV1, partidaZV1, filaZV, filaZVP, proxChegada, clienteZV1
    global estadoZV2, partidaZV2, filaZV, filaZVP, proxChegada, clienteZV2
    global estadoZV3, partidaZV3, filaZV, filaZVP, proxChegada, clienteZV3
    global estadoZV4, partidaZV4, filaZV, filaZVP, proxChegada, clienteZV4
    global estadoZV5, partidaZV5, filaZV, filaZVP, proxChegada, clienteZV5
    global estadoZV6, partidaZV6, filaZV, filaZVP, proxChegada, clienteZV6
    global estadoZV7, partidaZV7, filaZV, filaZVP, proxChegada, clienteZV7
    global estadoZV8, partidaZV8, filaZV, filaZVP, proxChegada, clienteZV8
    global estadoZV9, partidaZV9, filaZV, filaZVP, proxChegada, clienteZV9
    global estadoZV10, partidaZV10, filaZV, filaZVP, proxChegada, clienteZV10
    global tempoEsperaZV1, tempoEsperaZV1_10_13, tempoEsperaZV1_10_13_Max, tempoEsperaZV1_10_13_Min, tempoEsperaZV1_13_16, tempoEsperaZV1_13_16_Max, tempoEsperaZV1_13_16_Min, tempoEsperaZV1_16_19, tempoEsperaZV1_16_19_Min, tempoEsperaZV1_16_19_Max, tempoEsperaZV1_19_22, tempoEsperaZV1_19_22_Max, tempoEsperaZV1_19_22_Min
    global numClienteZL1, numClienteZL1_10_13, numClienteZL1_13_16, numClienteZL1_16_19, numClienteZL1_19_22
    global numClienteZV10
    global clientequepartiu

    clientequepartiu = clienteZV1[0]
    if(clienteZV1[3]==1):
        if(estadoZL2 == "livre"):
             estadoZV10 = "ocupado"
             partidaZV10 = clock + clienteZV1[10]
             clienteZV10 = clienteZV1
             atualizaEstatisticas(0,"ZV1",clienteZV1[2],((clock/60/60)+9))
        elif estadoZV10 == "ocupado":
            aux = ((clienteZV1),clock)
            if((clienteZV1),clock):
                filaZVP.append(aux)
            else:
                filaZV.append(aux)




def eventoPartidaZV2():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV2, estadoZV2, partidaZV2, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV2[0]
    if(clienteZV2[7] == 0):
        if(clienteZV2[5]==1):
            if(estadoZL2 == "livre"):
                estadoZL2 = "ocupado"
                partidaZL2 = clock + clienteZV2[10]
                clienteZL2 = clienteZV2
                atualizaEstatisticas(0, "ZV2", clienteZV2[2], (clienteZV2[1]/60/60)+9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV2),clock)
                if (clienteZV2[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV2[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV2[2] == 0):
                    filaZL.append(aux)


    if len(filaZVP) > 0:
        estadoZV2 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV2 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV2", clienteZV2[2], (clienteZV2[1] / 60 / 60) + 9)
        if (clienteZV2[7] == 1):
            partidaZV2 = clock + round((clienteZV2[9] * 0.2))
        elif (clienteZV2[6] == 1):
            partidaZV2 = clock + round((clienteZV2[9] * 0.8))
        elif (clienteZV2[6] == 0):
            partidaZV2 = clock + clienteZV2[9]
    elif len(filaZV) > 0:
        estadoZV2 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV2 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV2", clienteZV2[2], (clienteZV2[1] / 60 / 60) + 9)
        if (clienteZV2[7] == 1):
            partidaZV2 = clock + round((clienteZV2[9] * 0.2))
        elif (clienteZV2[6] == 1):
            partidaZV2 = clock + round((clienteZV2[9] * 0.8))
        elif (clienteZV2[6] == 0):
            partidaZV2 = clock + clienteZV2[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV2 = "livre"
        partidaZV2 = 999999


def eventoPartidaZV3():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV3, estadoZV3, partidaZV3, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV3[0]
    if (clienteZV3[7] == 0):
        if (clienteZV3[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV3 = "ocupado"
                partidaZL2 = clock + clienteZV3[10]
                clienteZL2 = clienteZV3
                atualizaEstatisticas(0, "ZV3", clienteZV3[2], (clienteZV3[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV3), clock)
                if (clienteZV3[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV3[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV3[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV3 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV3 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV3", clienteZV3[2], (clienteZV3[1] / 60 / 60) + 9)
        if (clienteZV3[7] == 1):
            partidaZV3 = clock + round((clienteZV3[9] * 0.2))
        elif (clienteZV3[6] == 1):
            partidaZV3 = clock + round((clienteZV3[9] * 0.8))
        elif (clienteZV3[6] == 0):
            partidaZV3 = clock + clienteZV3[9]
    elif len(filaZV) > 0:
        estadoZV3 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV3 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV3", clienteZV3[2], (clienteZV3[1] / 60 / 60) + 9)
        if (clienteZV3[7] == 1):
            partidaZV3 = clock + round((clienteZV3[9] * 0.2))
        elif (clienteZV3[6] == 1):
            partidaZV3 = clock + round((clienteZV3[9] * 0.8))
        elif (clienteZV3[6] == 0):
            partidaZV3 = clock + clienteZV3[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV3 = "livre"
        partidaZV3 = 999999


def eventoPartidaZV4():

    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV4, estadoZV4, partidaZV4, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV4[0]
    if (clienteZV4[7] == 0):
        if (clienteZV4[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV4 = "ocupado"
                partidaZL2 = clock + clienteZV4[10]
                clienteZL2 = clienteZV4
                atualizaEstatisticas(0, "ZV4", clienteZV4[2], (clienteZV4[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV4), clock)
                if (clienteZV4[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV4[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV4[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV4 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV4 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV4", clienteZV4[2], (clienteZV4[1] / 60 / 60) + 9)
        if (clienteZV4[7] == 1):
            partidaZV4 = clock + round((clienteZV4[9] * 0.2))
        elif (clienteZV4[6] == 1):
            partidaZV4 = clock + round((clienteZV4[9] * 0.8))
        elif (clienteZV4[6] == 0):
            partidaZV4 = clock + clienteZV4[9]
    elif len(filaZV) > 0:
        estadoZV4 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV4 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV4", clienteZV4[2], (clienteZV4[1] / 60 / 60) + 9)
        if (clienteZV4[7] == 1):
            partidaZV4 = clock + round((clienteZV4[9] * 0.2))
        elif (clienteZV4[6] == 1):
            partidaZV4 = clock + round((clienteZV4[9] * 0.8))
        elif (clienteZV4[6] == 0):
            partidaZV4 = clock + clienteZV4[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV4 = "livre"
        partidaZV4 = 999999


def eventoPartidaZV5():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV5, estadoZV5, partidaZV5, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV5[0]
    if (clienteZV5[7] == 0):
        if (clienteZV5[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV5 = "ocupado"
                partidaZL2 = clock + clienteZV5[10]
                clienteZL2 = clienteZV5
                atualizaEstatisticas(0, "ZV5", clienteZV5[2], (clienteZV5[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV5), clock)
                if (clienteZV5[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV5[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV5[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV5 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV5 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV5", clienteZV5[2], (clienteZV5[1] / 60 / 60) + 9)
        if (clienteZV5[7] == 1):
            partidaZV5 = clock + round((clienteZV5[9] * 0.2))
        elif (clienteZV5[6] == 1):
            partidaZV5 = clock + round((clienteZV5[9] * 0.8))
        elif (clienteZV5[6] == 0):
            partidaZV5 = clock + clienteZV5[9]
    elif len(filaZV) > 0:
        estadoZV5 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV5 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV5", clienteZV5[2], (clienteZV5[1] / 60 / 60) + 9)
        if (clienteZV5[7] == 1):
            partidaZV5 = clock + round((clienteZV5[9] * 0.2))
        elif (clienteZV5[6] == 1):
            partidaZV5 = clock + round((clienteZV5[9] * 0.8))
        elif (clienteZV5[6] == 0):
            partidaZV5 = clock + clienteZV5[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV5 = "livre"
        partidaZV5 = 999999


def eventoPartidaZV6():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV6, estadoZV6, partidaZV6, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV6[0]
    if (clienteZV6[7] == 0):
        if (clienteZV6[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV6 = "ocupado"
                partidaZL2 = clock + clienteZV6[10]
                clienteZL2 = clienteZV6
                atualizaEstatisticas(0, "ZV6", clienteZV6[2], (clienteZV6[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV6), clock)
                if (clienteZV6[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV6[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV6[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV6 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV6 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV6", clienteZV6[2], (clienteZV6[1] / 60 / 60) + 9)
        if (clienteZV6[7] == 1):
            partidaZV6 = clock + round((clienteZV6[9] * 0.2))
        elif (clienteZV6[6] == 1):
            partidaZV6 = clock + round((clienteZV6[9] * 0.8))
        elif (clienteZV6[6] == 0):
            partidaZV6 = clock + clienteZV6[9]
    elif len(filaZV) > 0:
        estadoZV6 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV6 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV6", clienteZV6[2], (clienteZV6[1] / 60 / 60) + 9)
        if (clienteZV6[7] == 1):
            partidaZV6 = clock + round((clienteZV6[9] * 0.2))
        elif (clienteZV6[6] == 1):
            partidaZV6 = clock + round((clienteZV6[9] * 0.8))
        elif (clienteZV6[6] == 0):
            partidaZV6 = clock + clienteZV6[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV6 = "livre"
        partidaZV6 = 999999

def eventoPartidaZV7():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV7, estadoZV7, partidaZV7, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV7[0]
    if (clienteZV7[7] == 0):
        if (clienteZV7[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV7 = "ocupado"
                partidaZL2 = clock + clienteZV7[10]
                clienteZL2 = clienteZV7
                atualizaEstatisticas(0, "ZV7", clienteZV7[2], (clienteZV7[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV7), clock)
                if (clienteZV7[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV7[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV7[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV7 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV7 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV7", clienteZV7[2], (clienteZV7[1] / 60 / 60) + 9)
        if (clienteZV7[7] == 1):
            partidaZV7 = clock + round((clienteZV7[9] * 0.2))
        elif (clienteZV7[6] == 1):
            partidaZV7 = clock + round((clienteZV7[9] * 0.8))
        elif (clienteZV7[6] == 0):
            partidaZV7 = clock + clienteZV7[9]
    elif len(filaZV) > 0:
        estadoZV7 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV7 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV7", clienteZV7[2], (clienteZV7[1] / 60 / 60) + 9)
        if (clienteZV7[7] == 1):
            partidaZV7 = clock + round((clienteZV7[9] * 0.2))
        elif (clienteZV7[6] == 1):
            partidaZV7 = clock + round((clienteZV7[9] * 0.8))
        elif (clienteZV7[6] == 0):
            partidaZV7 = clock + clienteZV7[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV7 = "livre"
        partidaZV7 = 999999

def eventoPartidaZV8():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV8, estadoZV8, partidaZV8, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV8[0]
    if (clienteZV8[7] == 0):
        if (clienteZV8[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV8 = "ocupado"
                partidaZL2 = clock + clienteZV8[10]
                clienteZL2 = clienteZV8
                atualizaEstatisticas(0, "ZV8", clienteZV8[2], (clienteZV8[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV8), clock)
                if (clienteZV8[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV8[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV8[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV8 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV8 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV8", clienteZV8[2], (clienteZV8[1] / 60 / 60) + 9)
        if (clienteZV8[7] == 1):
            partidaZV8 = clock + round((clienteZV8[9] * 0.2))
        elif (clienteZV8[6] == 1):
            partidaZV8 = clock + round((clienteZV8[9] * 0.8))
        elif (clienteZV8[6] == 0):
            partidaZV8 = clock + clienteZV8[9]
    elif len(filaZV) > 0:
        estadoZV8 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV8 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV8", clienteZV8[2], (clienteZV8[1] / 60 / 60) + 9)
        if (clienteZV8[7] == 1):
            partidaZV8 = clock + round((clienteZV8[9] * 0.2))
        elif (clienteZV8[6] == 1):
            partidaZV8 = clock + round((clienteZV8[9] * 0.8))
        elif (clienteZV8[6] == 0):
            partidaZV8 = clock + clienteZV8[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV8 = "livre"
        partidaZV8 = 999999

def eventoPartidaZV9():

    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV9, estadoZV9, partidaZV9, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV9[0]
    if (clienteZV9[7] == 0):
        if (clienteZV9[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV9 = "ocupado"
                partidaZL2 = clock + clienteZV9[10]
                clienteZL2 = clienteZV9
                atualizaEstatisticas(0, "ZV9", clienteZV9[2], (clienteZV9[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV9), clock)
                if (clienteZV9[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV9[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV9[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV9 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV9 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV9", clienteZV9[2], (clienteZV9[1] / 60 / 60) + 9)
        if (clienteZV9[7] == 1):
            partidaZV9 = clock + round((clienteZV9[9] * 0.2))
        elif (clienteZV9[6] == 1):
            partidaZV9 = clock + round((clienteZV9[9] * 0.8))
        elif (clienteZV9[6] == 0):
            partidaZV9 = clock + clienteZV9[9]
    elif len(filaZV) > 0:
        estadoZV9 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV9 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV9", clienteZV9[2], (clienteZV9[1] / 60 / 60) + 9)
        if (clienteZV9[7] == 1):
            partidaZV9 = clock + round((clienteZV9[9] * 0.2))
        elif (clienteZV9[6] == 1):
            partidaZV9 = clock + round((clienteZV9[9] * 0.8))
        elif (clienteZV9[6] == 0):
            partidaZV9 = clock + clienteZV9[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV9 = "livre"
        partidaZV9 = 999999


def eventoPartidaZV10():

    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZV10, estadoZV10, partidaZV10, filaZV, filaZVP
    global clientequepartiu

    clientequepartiu = clienteZV10[0]
    if (clienteZV10[7] == 0):
        if (clienteZV10[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZV10 = "ocupado"
                partidaZL2 = clock + clienteZV10[10]
                clienteZL2 = clienteZV10
                atualizaEstatisticas(0, "ZV10", clienteZV10[2], (clienteZV10[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZV10), clock)
                if (clienteZV10[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZV10[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZV10[2] == 0):
                    filaZL.append(aux)

    if len(filaZVP) > 0:
        estadoZV10 = "ocupado"
        proxcliente = filaZVP.pop(0)
        clienteZV10 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV10", clienteZV10[2], (clienteZV10[1] / 60 / 60) + 9)
        if (clienteZV10[7] == 1):
            partidaZV10 = clock + round((clienteZV10[9] * 0.2))
        elif (clienteZV10[6] == 1):
            partidaZV10 = clock + round((clienteZV10[9] * 0.8))
        elif (clienteZV10[6] == 0):
            partidaZV10 = clock + clienteZV10[9]
    elif len(filaZV) > 0:
        estadoZV10 = "ocupado"
        proxcliente = filaZV.pop(0)
        clienteZV10 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZV10", clienteZV10[2], (clienteZV10[1] / 60 / 60) + 9)
        if (clienteZV10[7] == 1):
            partidaZV10 = clock + round((clienteZV10[9] * 0.2))
        elif (clienteZV10[6] == 1):
            partidaZV10 = clock + round((clienteZV10[9] * 0.8))
        elif (clienteZV10[6] == 0):
            partidaZV10 = clock + clienteZV10[9]
    elif len(filaZVP) == 0 and len(filaZV) == 0:
        estadoZV10 = "livre"
        partidaZV10 = 999999


def eventoPartidaZP1():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZP1, estadoZP1, partidaZP1, filaZP, filaZP1
    global clientequepartiu

    clientequepartiu = clienteZP1[0]
    if (clienteZP1[7] == 0):
        if (clienteZP1[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZP1 = "ocupado"
                partidaZL2 = clock + clienteZP1[10]
                clienteZL2 = clienteZP1
                atualizaEstatisticas(0, "ZP1", clienteZP1[2], (clienteZP1[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZP1), clock)
                if (clienteZP1[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZP1[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZP1[2] == 0):
                    filaZL.append(aux)

    if len(filaZP1) > 0:
        estadoZP1 = "ocupado"
        proxcliente = filaZP1.pop(0)
        clienteZP1 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZP1", clienteZP1[2], (clienteZP1[1] / 60 / 60) + 9)
        if (clienteZP1[7] == 1):
            partidaZP1 = clock + round((clienteZP1[9] * 0.2))
        elif (clienteZP1[6] == 1):
            partidaZP1 = clock + round((clienteZP1[9] * 0.8))
        elif (clienteZP1[6] == 0):
            partidaZP1 = clock + clienteZP1[9]
    elif len(filaZP) > 0:
        estadoZP1 = "ocupado"
        proxcliente = filaZP.pop(0)
        clienteZP1 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZP1", clienteZP1[2], (clienteZP1[1] / 60 / 60) + 9)
        if (clienteZP1[7] == 1):
            partidaZP1 = clock + round((clienteZP1[9] * 0.2))
        elif (clienteZP1[6] == 1):
            partidaZP1 = clock + round((clienteZP1[9] * 0.8))
        elif (clienteZP1[6] == 0):
            partidaZP1 = clock + clienteZP1[9]
    elif len(filaZP1) == 0 and len(filaZP) == 0:
        estadoZP1 = "livre"
        partidaZP1 = 999999

def eventoPartidaZP2():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZP2, estadoZP2, partidaZP2, filaZP, filaZP2
    global clientequepartiu

    clientequepartiu = clienteZP2[0]
    if (clienteZP2[7] == 0):
        if (clienteZP2[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZP2 = "ocupado"
                partidaZL2 = clock + clienteZP2[10]
                clienteZL2 = clienteZP2
                atualizaEstatisticas(0, "ZP2", clienteZP2[2], (clienteZP2[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZP2), clock)
                if (clienteZP2[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZP2[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZP2[2] == 0):
                    filaZL.append(aux)

    if len(filaZP2) > 0:
        estadoZP2 = "ocupado"
        proxcliente = filaZP2.pop(0)
        clienteZP2 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZP2", clienteZP2[2], (clienteZP2[1] / 60 / 60) + 9)
        if (clienteZP2[7] == 1):
            partidaZP2 = clock + round((clienteZP2[9] * 0.2))
        elif (clienteZP2[6] == 1):
            partidaZP2 = clock + round((clienteZP2[9] * 0.8))
        elif (clienteZP2[6] == 0):
            partidaZP2 = clock + clienteZP2[9]
    elif len(filaZP) > 0:
        estadoZP2 = "ocupado"
        proxcliente = filaZP.pop(0)
        clienteZP2 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZP2", clienteZP2[2], (clienteZP2[1] / 60 / 60) + 9)
        if (clienteZP2[7] == 1):
            partidaZP2 = clock + round((clienteZP2[9] * 0.2))
        elif (clienteZP2[6] == 1):
            partidaZP2 = clock + round((clienteZP2[9] * 0.8))
        elif (clienteZP2[6] == 0):
            partidaZP2 = clock + clienteZP2[9]
    elif len(filaZP2) == 0 and len(filaZP) == 0:
        estadoZP2 = "livre"
        partidaZP2 = 999999


def eventoPartidaZP3():

    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZP3, estadoZP3, partidaZP3, filaZP, filaZP3
    global clientequepartiu

    clientequepartiu = clienteZP3[0]
    if (clienteZP3[7] == 0):
        if (clienteZP3[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZP3 = "ocupado"
                partidaZL2 = clock + clienteZP3[10]
                clienteZL2 = clienteZP3
                atualizaEstatisticas(0, "ZP3", clienteZP3[2], (clienteZP3[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZP3), clock)
                if (clienteZP3[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZP3[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZP3[2] == 0):
                    filaZL.append(aux)

    if len(filaZP3) > 0:
        estadoZP3 = "ocupado"
        proxcliente = filaZP3.pop(0)
        clienteZP3 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZP3", clienteZP3[2], (clienteZP3[1] / 60 / 60) + 9)
        if (clienteZP3[7] == 1):
            partidaZP3 = clock + round((clienteZP3[9] * 0.2))
        elif (clienteZP3[6] == 1):
            partidaZP3 = clock + round((clienteZP3[9] * 0.8))
        elif (clienteZP3[6] == 0):
            partidaZP3 = clock + clienteZP3[9]
    elif len(filaZP) > 0:
        estadoZP3 = "ocupado"
        proxcliente = filaZP.pop(0)
        clienteZP3 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZP3", clienteZP3[2], (clienteZP3[1] / 60 / 60) + 9)
        if (clienteZP3[7] == 1):
            partidaZP3 = clock + round((clienteZP3[9] * 0.2))
        elif (clienteZP3[6] == 1):
            partidaZP3 = clock + round((clienteZP3[9] * 0.8))
        elif (clienteZP3[6] == 0):
            partidaZP3 = clock + clienteZP3[9]
    elif len(filaZP3) == 0 and len(filaZP) == 0:
        estadoZP3 = "livre"
        partidaZP3 = 999999

def eventoPartidaZP4():

    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZP4, estadoZP4, partidaZP4, filaZP, filaZP4
    global clientequepartiu

    clientequepartiu = clienteZP4[0]
    if (clienteZP4[7] == 0):
        if (clienteZP4[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZP4 = "ocupado"
                partidaZL2 = clock + clienteZP4[10]
                clienteZL2 = clienteZP4
                atualizaEstatisticas(0, "ZP4", clienteZP4[2], (clienteZP4[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZP4), clock)
                if (clienteZP4[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZP4[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZP4[2] == 0):
                    filaZL.append(aux)

    if len(filaZP4) > 0:
        estadoZP4 = "ocupado"
        proxcliente = filaZP4.pop(0)
        clienteZP4 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZP4", clienteZP4[2], (clienteZP4[1] / 60 / 60) + 9)
        if (clienteZP4[7] == 1):
            partidaZP4 = clock + round((clienteZP4[9] * 0.2))
        elif (clienteZP4[6] == 1):
            partidaZP4 = clock + round((clienteZP4[9] * 0.8))
        elif (clienteZP4[6] == 0):
            partidaZP4 = clock + clienteZP4[9]
    elif len(filaZP) > 0:
        estadoZP4 = "ocupado"
        proxcliente = filaZP.pop(0)
        clienteZP4 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZP4", clienteZP4[2], (clienteZP4[1] / 60 / 60) + 9)
        if (clienteZP4[7] == 1):
            partidaZP4 = clock + round((clienteZP4[9] * 0.2))
        elif (clienteZP4[6] == 1):
            partidaZP4 = clock + round((clienteZP4[9] * 0.8))
        elif (clienteZP4[6] == 0):
            partidaZP4 = clock + clienteZP4[9]
    elif len(filaZP4) == 0 and len(filaZP) == 0:
        estadoZP4 = "livre"
        partidaZP4 = 999999


def eventoPartidaZL1():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZL1, estadoZL1, partidaZL1, filaZL, filaZLP
    global clientequepartiu

    clientequepartiu = clienteZL1[0]
    if (clienteZL1[7] == 0):
        if (clienteZL1[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZL1 = "ocupado"
                partidaZL2 = clock + clienteZL1[10]
                clienteZL2 = clienteZL1
                atualizaEstatisticas(0, "ZL1", clienteZL1[2], (clienteZL1[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZL1), clock)
                if (clienteZL1[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZL1[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZL1[2] == 0):
                    filaZL.append(aux)

    if len(filaZLP) > 0:
        estadoZL1 = "ocupado"
        proxcliente = filaZLP.pop(0)
        clienteZL1 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZL1", clienteZL1[2], (clienteZL1[1] / 60 / 60) + 9)
        if (clienteZL1[7] == 1):
            partidaZL1 = clock + round((clienteZL1[9] * 0.2))
        elif (clienteZL1[6] == 1):
            partidaZL1 = clock + round((clienteZL1[9] * 0.8))
        elif (clienteZL1[6] == 0):
            partidaZL1 = clock + clienteZL1[9]
    elif len(filaZL) > 0:
        estadoZL1 = "ocupado"
        proxcliente = filaZL.pop(0)
        clienteZL1 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZL1", clienteZL1[2], (clienteZL1[1] / 60 / 60) + 9)
        if (clienteZL1[7] == 1):
            partidaZL1 = clock + round((clienteZL1[9] * 0.2))
        elif (clienteZL1[6] == 1):
            partidaZL1 = clock + round((clienteZL1[9] * 0.8))
        elif (clienteZL1[6] == 0):
            partidaZL1 = clock + clienteZL1[9]
    elif len(filaZLP) == 0 and len(filaZL) == 0:
        estadoZL1 = "livre"
        partidaZL1 = 999999


def eventoPartidaZL2():
    global estadoZL2, partidaZL2, clienteZL2, filaZLP, filaZL
    global clienteZL2, estadoZL2, partidaZL2, filaZL, filaZLP
    global clientequepartiu

    clientequepartiu = clienteZL2[0]
    if (clienteZL2[7] == 0):
        if (clienteZL2[5] == 1):
            if (estadoZL2 == "livre"):
                estadoZL2 = "ocupado"
                partidaZL2 = clock + clienteZL2[10]
                clienteZL2 = clienteZL2
                atualizaEstatisticas(0, "ZL2", clienteZL2[2], (clienteZL2[1] / 60 / 60) + 9)
            elif estadoZL2 == "ocupado":
                aux = ((clienteZL2), clock)
                if (clienteZL2[6] == 1):
                    filaZLP.append(aux)
                elif (clienteZL2[2] == 1):
                    filaZLP.append(aux)
                elif (clienteZL2[2] == 0):
                    filaZL.append(aux)

    if len(filaZLP) > 0:
        estadoZL2 = "ocupado"
        proxcliente = filaZLP.pop(0)
        clienteZL2 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZL2", clienteZL2[1], (clienteZL2[1] / 60 / 60) + 9)
        if (clienteZL2[7] == 1):
            partidaZL2 = clock + round((clienteZL2[9] * 0.2))
        elif (clienteZL2[6] == 1):
            partidaZL2 = clock + round((clienteZL2[9] * 0.8))
        elif (clienteZL2[6] == 0):
            partidaZL2 = clock + clienteZL2[9]
    elif len(filaZL) > 0:
        estadoZL2 = "ocupado"
        proxcliente = filaZL.pop(0)
        clienteZL2 = proxcliente[0]
        atualizaEstatisticas((clock - proxcliente[1]), "ZL2", clienteZL2[1], (clienteZL2[1] / 60 / 60) + 9)
        if (clienteZL2[7] == 1):
            partidaZL2 = clock + round((clienteZL2[9] * 0.2))
        elif (clienteZL2[6] == 1):
            partidaZL2 = clock + round((clienteZL2[9] * 0.8))
        elif (clienteZL2[6] == 0):
            partidaZL2 = clock + clienteZL2[9]
    elif len(filaZLP) == 0 and len(filaZL) == 0:
        estadoZL2 = "livre"
        partidaZL2 = 999999


def main():
    global proxChegada, partidaZL1, partidaZL2, partidaZP1, partidaZP2, partidaZP3, partidaZP4, partidaZV1, partidaZV2, partidaZV3, partidaZV4, partidaZV5, partidaZV6, partidaZV7, partidaZV8, partidaZV9, partidaZV10
    global filaZLLST, filaZP1LST, filaZP2LST, filaZP3LST, filaZP4LST, filaZVLST
    global numeroUltimoCliente
    openJsonConfig()
    criarClientes()
    proxChegada = Clientes[0][1]
    primeiraIteração()
    while 1:
        tempo()
        if proxChegada == 999999 and partidaZV1 == 999999 and partidaZV2 == 999999 and partidaZV3 == 999999 and partidaZV4 == 999999 and partidaZV5 == 999999 and partidaZV6 == 999999 and partidaZV7 == 999999 and partidaZV8 == 999999 and partidaZV9 == 999999 and partidaZV10 == 999999 and partidaZP1 == 999999 and partidaZP2 == 999999 and partidaZP3 == 999999 and partidaZP4 == 999999 and partidaZL1 == 999999 and partidaZL2 == 999999:
            break
        if clock == proxChegada:
            eventoChegada()
            if (numeroUltimoCliente <= len(Clientes)):
                actualizaListasFolhaExcel("Cheg")
        elif clock == partidaZV1:
            eventoPartidaZV1()
            actualizaListasFolhaExcel("PZV1")
        elif clock == partidaZV2:
            eventoPartidaZV2()
            actualizaListasFolhaExcel("PZV2")
        elif clock == partidaZV3:
            eventoPartidaZV3()
            actualizaListasFolhaExcel("PZV3")
        elif clock == partidaZV4:
            eventoPartidaZV4()
            actualizaListasFolhaExcel("PZV4")
        elif clock == partidaZV5:
            eventoPartidaZV5()
            actualizaListasFolhaExcel("PZV5")
        elif clock == partidaZV6:
            eventoPartidaZV6()
            actualizaListasFolhaExcel("PZV6")
        elif clock == partidaZV7:
            eventoPartidaZV7()
            actualizaListasFolhaExcel("PZV7")
        elif clock == partidaZV8:
            eventoPartidaZV8()
            actualizaListasFolhaExcel("PZV8")
        elif clock == partidaZV9:
            eventoPartidaZV9()
            actualizaListasFolhaExcel("PZV9")
        elif clock == partidaZV10:
            eventoPartidaZV10()
            actualizaListasFolhaExcel("PZV10")
        elif clock == partidaZP1:
            eventoPartidaZP1()
            actualizaListasFolhaExcel("PZP1")
        elif clock == partidaZP2:
            eventoPartidaZP2()
            actualizaListasFolhaExcel("PZP2")
        elif clock == partidaZP3:
            eventoPartidaZP3()
            actualizaListasFolhaExcel("PZP3")
        elif clock == partidaZP4:
            eventoPartidaZP4()
            actualizaListasFolhaExcel("PZP4")
        elif clock == partidaZL1:
            eventoPartidaZL1()
            actualizaListasFolhaExcel("PZL1")
        elif clock == partidaZL2:
            eventoPartidaZL2()
            actualizaListasFolhaExcel("PZL2")

    printEstatisticas()
    df = DataFrame({'Clock': clockLST, 'TipoEvento': eventoLST, 'Cliente': clienteLST, 'ProxChegada': proxChegadaLST,
                    'FilaZV': filaZVLST, 'FilaZVP': filaZVLST, 'EstadoZV1': estadoZV1LST, 'PartidaZV1': partidaZV1LST,
                    'EstadoZV2': estadoZV2LST, 'PartidaZV2': partidaZV2LST, 'EstadoZV3': estadoZV3LST,
                    'PartidaZV3': partidaZV3LST,
                    'EstadoZV4': estadoZV4LST, 'PartidaZV4': partidaZV4LST, 'EstadoZV5': estadoZV5LST,
                    'PartidaZV5': partidaZV5LST,
                    'EstadoZV6': estadoZV6LST, 'PartidaZV6': partidaZV6LST, 'EstadoZV7': estadoZV7LST,
                    'PartidaZV7': partidaZV7LST,
                    'EstadoZV8': estadoZV8LST, 'PartidaZV8': partidaZV8LST, 'EstadoZV9': estadoZV9LST,
                    'PartidaZV9': partidaZV9LST,
                    'EstadoZV10': estadoZV10LST, 'PartidaZV10': partidaZV10LST,

                    'FilaZP1': filaZP1LST, 'FilaZP2': filaZP2LST, 'FilaZP3': filaZP3LST, 'FilaZP4': filaZP4LST,
                    'FilaZP1P': filaZPP1LST, 'FilaZP2P': filaZPP2LST, 'FilaZP3P': filaZPP3LST, 'FilaZP4P': filaZPP4LST,
                    'EstadoZP1': estadoZP1LST, 'EstadoZP2': estadoZP2LST, 'EstadoZP3': estadoZP3LST,
                    'EstadoZP4': estadoZP4LST,
                    'PartidaZP1': partidaZP1LST, 'PartidaZP2': partidaZP2LST, 'PartidaZP3': partidaZP3LST,
                    'PartidaZP4': partidaZP4LST,

                    'FilaZL': filaZLLST, 'FilaZLP': filaZLPLST, 'EstadoZL1': estadoZL1LST, 'EstadoZL2': estadoZL2LST,
                    'PartidaZL1': partidaZL1LST, 'PartidaZL2': partidaZL2LST

                    })
    df.to_excel('trabalho.xlsx', sheet_name='tabela', index=False,
                columns=['Clock', 'TipoEvento', 'Cliente', 'ProxChegada', 'FilaZV', 'FilaZVP', 'EstadoZV1',
                         'PartidaZV1',
                         'EstadoZV2', 'PartidaZV2', 'EstadoZV3', 'PartidaZV3', 'EstadoZV4', 'PartidaZV4', 'EstadoZV5',
                         'PartidaZV5',
                         'EstadoZV6', 'PartidaZV6', 'EstadoZV7', 'PartidaZV7', 'EstadoZV8', 'PartidaZV8', 'EstadoZV9',
                         'PartidaZV9',
                         'EstadoZV10', 'PartidaZV10', 'FilaZP1', 'FilaZP2', 'FilaZP3', 'FilaZP4', 'FilaZP1P',
                         'FilaZP2P', 'FilaZP3P',
                         'FilaZP4P', 'EstadoZP1', 'EstadoZP2', 'EstadoZP3', 'EstadoZP4', 'PartidaZP1', 'PartidaZP2',
                         'PartidaZP3', 'PartidaZP4',
                         'FilaZL', 'FilaZLP', 'EstadoZL1', 'EstadoZL2', 'PartidaZL1', 'PartidaZL2'])

    printClientes(Clientes)
    desenharGraficos()
    print("\n\nFicheiros e gráficos criados e escritos com sucesso.")



def openJsonConfig():
    global configData
    with open('config.json') as f:
        configData = json.load(f)
    pprint(configData)


main()
