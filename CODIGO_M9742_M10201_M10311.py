#!/usr/bin/env python
# encoding: utf8
import os
from random import randint #randint(a,b) -> [a,b]
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

from operator import itemgetter

#lista com todos os Utentes
Utentes = []
numeroUtentes = randint(120, 150) #inclusive, [120,150]
nrUltimoUtente = 0 #saber qual o foi o ultimo Utente a entrar no sistema

#variaveis estatisticas
clock=0
tipoEvento=""
Utente=0
proxChegada=999999
filaRF=[]
filaRFP=[]
estadoRF="livre"
partidaRF=999999
filaA=[]
filaAP=[]
estadoA1="livre"
estadoA2="livre"
partidaA1=999999
partidaA2=999999
filaB=[]
filaBP=[]
estadoB1="livre"
estadoB2="livre"
partidaB1=999999
partidaB2=999999
filaC=[]
filaCP=[]
estadoC="livre"
partidaC=999999
filaT=[]
filaTP=[]
estadoT="livre"
partidaT=999999

UtenteRF = 0 
UtenteA1 = 0
UtenteA2 = 0
UtenteB1 = 0
UtenteB2 = 0
UtenteC = 0
UtenteT = 0

tempEspRF=0
tempEspA=0
tempEspB=0
tempEspC=0
tempEspT=0
tempEspRFP=0
tempEspAP=0
tempEspBP=0
tempEspCP=0
tempEspTP=0
tempEspRFMin=99999
tempEspAMin=99999
tempEspBMin=99999
tempEspCMin=99999
tempEspTMin=99999
tempEspRFPMin=99999
tempEspAPMin=99999
tempEspBPMin=99999
tempEspCPMin=99999
tempEspTPMin=99999
tempEspRFMax=0
tempEspAMax=0
tempEspBMax=0
tempEspCMax=0
tempEspTMax=0
tempEspRFPMax=0
tempEspAPMax=0
tempEspBPMax=0
tempEspCPMax=0
tempEspTPMax=0
tempEspRF9_11=0
tempEspA9_11=0
tempEspB9_11=0
tempEspC9_11=0
tempEspT9_11=0
tempEspRFP9_11=0
tempEspAP9_11=0
tempEspBP9_11=0
tempEspCP9_11=0
tempEspTP9_11=0
tempEspRF11_13=0
tempEspA11_13=0
tempEspB11_13=0
tempEspC11_13=0
tempEspT11_13=0
tempEspRFP11_13=0
tempEspAP11_13=0
tempEspBP11_13=0
tempEspCP11_13=0
tempEspTP11_13=0
tempEspRF13_15=0
tempEspA13_15=0
tempEspB13_15=0
tempEspC13_15=0
tempEspT13_15=0
tempEspRFP13_15=0
tempEspAP13_15=0
tempEspBP13_15=0
tempEspCP13_15=0
tempEspTP13_15=0
tempEspRF15_17=0
tempEspA15_17=0
tempEspB15_17=0
tempEspC15_17=0
tempEspT15_17=0
tempEspRFP15_17=0
tempEspAP15_17=0
tempEspBP15_17=0
tempEspCP15_17=0
tempEspTP15_17=0


tempEspRF9_11Max=0
tempEspRFP9_11Max=0
tempEspRF9_11Min=99999
tempEspRFP9_11Min=99999
tempEspRF11_13Max=0
tempEspRFP11_13Max=0
tempEspRF11_13Min=99999
tempEspRFP11_13Min=99999
tempEspRF13_15Max=0
tempEspRFP13_15Max=0
tempEspRF13_15Min=99999
tempEspRFP13_15Min=99999
tempEspRF15_17Max=0
tempEspRFP15_17Max=0
tempEspRF15_17Min=99999
tempEspRFP15_17Min=99999

tempEspA9_11Max=0
tempEspAP9_11Max=0
tempEspA9_11Min=99999
tempEspAP9_11Min=99999
tempEspA11_13Max=0
tempEspAP11_13Max=0
tempEspA11_13Min=99999
tempEspAP11_13Min=99999
tempEspA13_15Max=0
tempEspAP13_15Max=0
tempEspA13_15Min=99999
tempEspAP13_15Min=99999
tempEspA15_17Max=0
tempEspAP15_17Max=0
tempEspA15_17Min=99999
tempEspAP15_17Min=99999

tempEspB9_11Max=0
tempEspBP9_11Max=0
tempEspB9_11Min=99999
tempEspBP9_11Min=99999
tempEspB11_13Max=0
tempEspBP11_13Max=0
tempEspB11_13Min=99999
tempEspBP11_13Min=99999
tempEspB13_15Max=0
tempEspBP13_15Max=0
tempEspB13_15Min=99999
tempEspBP13_15Min=99999
tempEspB15_17Max=0
tempEspBP15_17Max=0
tempEspB15_17Min=99999
tempEspBP15_17Min=99999

tempEspC9_11Max=0
tempEspCP9_11Max=0
tempEspC9_11Min=99999
tempEspCP9_11Min=99999
tempEspC11_13Max=0
tempEspCP11_13Max=0
tempEspC11_13Min=99999
tempEspCP11_13Min=99999
tempEspC13_15Max=0
tempEspCP13_15Max=0
tempEspC13_15Min=99999
tempEspCP13_15Min=99999
tempEspC15_17Max=0
tempEspCP15_17Max=0
tempEspC15_17Min=99999
tempEspCP15_17Min=99999

tempEspT9_11Max=0
tempEspTP9_11Max=0
tempEspT9_11Min=99999
tempEspTP9_11Min=99999
tempEspT11_13Max=0
tempEspTP11_13Max=0
tempEspT11_13Min=99999
tempEspTP11_13Min=99999
tempEspT13_15Max=0
tempEspTP13_15Max=0
tempEspT13_15Min=99999
tempEspTP13_15Min=99999
tempEspT15_17Max=0
tempEspTP15_17Max=0
tempEspT15_17Min=99999
tempEspTP15_17Min=99999

numWearerRF=0
numWearerRFP=0
numWearerA=0
numWearerAP=0
numWearerB=0
numWearerBP=0
numWearerC=0
numWearerCP=0
numWearerT=0
numWearerTP=0

numWearerRF9_11=0
numWearerRFP9_11=0
numWearerA9_11=0
numWearerAP9_11=0
numWearerB9_11=0
numWearerBP9_11=0
numWearerC9_11=0
numWearerCP9_11=0
numWearerT9_11=0
numWearerTP9_11=0

numWearerRF11_13=0
numWearerRFP11_13=0
numWearerA11_13=0
numWearerAP11_13=0
numWearerB11_13=0
numWearerBP11_13=0
numWearerC11_13=0
numWearerCP11_13=0
numWearerT11_13=0
numWearerTP11_13=0

numWearerRF13_15=0
numWearerRFP13_15=0
numWearerA13_15=0
numWearerAP13_15=0
numWearerB13_15=0
numWearerBP13_15=0
numWearerC13_15=0
numWearerCP13_15=0
numWearerT13_15=0
numWearerTP13_15=0

numWearerRF15_17=0
numWearerRFP15_17=0
numWearerA15_17=0
numWearerAP15_17=0
numWearerB15_17=0
numWearerBP15_17=0
numWearerC15_17=0
numWearerCP15_17=0
numWearerT15_17=0
numWearerTP15_17=0

clockLST       = []
eventoLST      = []
UtenteLST     = []
proxChegadaLST = []
filaRFLST      = []
filaRFPLST     = []
estadoRFLST    = []
partidaRFLST   = []
filaALST       = []
filaAPLST      = []
estadoA1LST    = []
estadoA2LST    = []
partidaA1LST   = []
partidaA2LST   = []
filaBLST       = []
filaBPLST      = []
estadoB1LST    = []
estadoB2LST    = []
partidaB1LST   = []
partidaB2LST   = []
filaCLST       = []
filaCPLST      = []
estadoCLST     = []
partidaCLST    = []
filaTLST       = []
filaTPLST      = []
estadoTLST     = []
partidaTLST    = []

Utentequepartiu = 0

#random entre 0 e 1
def rand0to1():
    hello = (int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1))
    return hello

def printUtentes(Utentess):

    nUtentes= list(x[0] for x in Utentess)
    tempochegada = list(x[1] for x in Utentess)
    prioritario = list(x[2] for x in Utentess)
    passadiretamente = list(x[3] for x in Utentess)
    posto2afase = list(x[4] for x in Utentess)
    vai3afase = list(x[5] for x in Utentess)
    cicloapos3a = list(x[6] for x in Utentess)
    afazerciclo = list(x[7] for x in Utentess)
    tat = list(x[8] for x in Utentess)
    ta2 = list(x[9] for x in Utentess)
    tap3 = list(x[10] for x in Utentess)

    df = DataFrame({'N. Utente': nUtentes, 'Tempo Chegada':tempochegada, 'Prioritario':prioritario, 'PassaDiretamente3aFase':passadiretamente, 'Posto2aFase':posto2afase, 'Vai3aFase':vai3afase, 'CicloApos3aFase':cicloapos3a, 'AfazerCiclo':afazerciclo, 'TempoAtendimentoTriagem':tat, 'TempoAtendimento2oPosto': ta2, 'TempoAtendimento3oPosto':tap3})
    df.to_excel('trabalho_Utentes.xlsx', sheet_name='Utentes', index=False, columns=['N. Utente','Tempo Chegada','Prioritario','PassaDiretamente3aFase','Posto2aFase','Vai3aFase','CicloApos3aFase','AfazerCiclo','TempoAtendimentoTriagem','TempoAtendimento2oPosto','TempoAtendimento3oPosto'])

def criaUtentes():
    Utentesaux=[]
    for x in range(1,numeroUtentes+1): #para o número de Utentes ir de 1 a 150
        valorEntrada = rand0to1()
        chegada = 0
        vai3aFase = 0
        if(valorEntrada <= 0.1): #entra em [0,7200]
            chegada = randint(0, 7200)
        elif(valorEntrada > 0.1 and valorEntrada <= 0.35): #entra em ]7200,14400]
            chegada = randint(7201,14400)
        elif(valorEntrada > 0.35 and valorEntrada <= 0.8): #entra em ]14400,21600]
            chegada = randint(14401,21600)
        elif(valorEntrada > 0.8): #entra em ]21600,28800]
            chegada = randint(21601,28800);

        #calcula se é prioritario52
        valorPrioritario = rand0to1()
        prioridade = 1 if valorPrioritario <= 0.05 else 0 #se for prioritario fica com o valor 1

        # calcula tempo de atendimento na triagem
        atndTriagem = rand0to1()
        tempoAtendimentoTriagem = randint(1, 60) if atndTriagem <= 0.55 else (
            randint(61, 120) if atndTriagem > 0.55 and atndTriagem <= 0.9 else (
            randint(121, 180) if atndTriagem > 0.9 else 1))

        # se passa diretamente da 1a para a 3a fase
        passa3aFase = rand0to1()
        passaDiretamente3Fase = 1 if passa3aFase <= 0.15 else 0 #15% hipotese de ir diretamente da 1a fase para a 3a

        if(passaDiretamente3Fase == 0): #se passar pela 2a fase pode ser : A B C, se não passar fica : NA
            escolhaDoPosto2aFase = rand0to1()
            posto2aFase = "A" if escolhaDoPosto2aFase <= 0.35 else( "B" if escolhaDoPosto2aFase <= 0.85 and escolhaDoPosto2aFase > 0.3 else ("C" if escolhaDoPosto2aFase > 0.85 else "C"))
        else:
            posto2aFase = "NA"
            tempoAtendimento2aFase = -1
            cicloApos3AFase = 0 #se passar diretamente para 3a fase, não vai a 2a fase após a 3a

        if posto2aFase == "A":
            passa3aFase = rand0to1()
            vai3aFase   = 1 if passa3aFase <= 0.3 else 0
            if(vai3aFase == 1):
                ciclo       = rand0to1()
                cicloApos3AFase = 1 if ciclo <= 0.25 else 0
            else: cicloApos3AFase = 0

            #tempo atendimento no posto
            atnd2aFase = rand0to1()
            tempoAtendimento2aFase = randint(1,300) if atnd2aFase <= 0.25 else (randint(301,900) if atnd2aFase > 0.25 and atnd2aFase <= 0.6 else ( randint(901,1500) if atnd2aFase > 0.6 and atnd2aFase <= 0.9 else (randint(1501,1800) if atnd2aFase > 0.9 else 1)))
        elif posto2aFase == "B":
            passa3aFase = rand0to1()
            vai3aFase = 1 if passa3aFase <= 0.2 else 0

            if (vai3aFase == 1):
                ciclo = rand0to1()
                cicloApos3AFase = 1 if ciclo <= 0.15 else 0
            else: cicloApos3AFase = 0

            # tempo atendimento no posto
            atnd2aFase = rand0to1()
            tempoAtendimento2aFase = randint(1, 300) if atnd2aFase <= 0.25 else (
            randint(301, 600) if atnd2aFase > 0.25 and atnd2aFase <= 0.7 else (
            randint(601, 900) if atnd2aFase > 0.7 and atnd2aFase <= 0.95 else (
            randint(900, 1200) if atnd2aFase > 0.95 else 1)))

        elif posto2aFase == "C":
            passa3aFase = rand0to1()
            vai3aFase = 1 if passa3aFase <= 0.7 else 0

            if (vai3aFase == 1):
                ciclo = rand0to1()
                cicloApos3AFase = 1 if ciclo <= 0.25 else 0
            else: cicloApos3AFase = 0

            
            atnd2aFase = rand0to1()
            tempoAtendimento2aFase = randint(1, 300) if atnd2aFase <= 0.1 else (
            randint(301, 600) if atnd2aFase > 0.1 and atnd2aFase <= 0.45 else (
            randint(601, 900) if atnd2aFase > 0.45 and atnd2aFase <= 0.9 else (
            randint(900, 1200) if atnd2aFase > 0.90 else 1)))

        if vai3aFase == 1 or passaDiretamente3Fase == 1:
            atnd3aFase = rand0to1()
            tempoAtendimento3aFase = randint(1, 60) if atnd3aFase <= 0.4 else (
                randint(61, 120) if atnd3aFase > 0.4 and atnd3aFase <= 0.95 else (
                randint(121, 180) if atnd3aFase > 0.95 else 1))
        else:
            tempoAtendimento3aFase = -1

        #adicionar a informação a lista de Utentes
        Utentesaux.append((chegada,prioridade,passaDiretamente3Fase,posto2aFase,vai3aFase,cicloApos3AFase,0,tempoAtendimentoTriagem,tempoAtendimento2aFase,tempoAtendimento3aFase))

   

def tempo():
    global clock
    #print("clock antes: "+str(clock))
    global proxChega, partidaRF, partidaA1, partidaA2, partidaB1, partidaB2, partidaC, partidaT
    if proxChegada <= partidaRF and proxChegada <= partidaA1 and proxChegada <= partidaA2 and proxChegada <= partidaB1 and proxChegada <= partidaB2 and proxChegada <= partidaC and proxChegada <= partidaT and proxChegada!=999999:
        clock=proxChegada
    elif partidaRF <= proxChegada and partidaRF <= partidaA1 and partidaRF <= partidaA2 and partidaRF <= partidaB1 and partidaRF <= partidaB2 and partidaRF <= partidaC and partidaRF <= partidaT and partidaRF!=999999:
        clock=partidaRF
    elif partidaA1 <= proxChegada and partidaA1 <= partidaRF and partidaA1 <= partidaA2 and partidaA1 <= partidaB1 and partidaA1 <= partidaB2 and partidaA1 <= partidaC and partidaA1 <= partidaT and partidaA1 !=999999:
        clock=partidaA1
    elif partidaA2 <= proxChegada and partidaA2 <= partidaRF and partidaA2 <= partidaA1 and partidaA2 <= partidaB1 and partidaA2 <= partidaB2 and partidaA2 <= partidaC and partidaA2 <= partidaT and partidaA2 != 999999:
        clock=partidaA2
    elif partidaB1 <= proxChegada and partidaB1 <= partidaRF and partidaB1 <= partidaA1 and partidaB1 <= partidaA2 and partidaB1 <= partidaB2 and partidaB1 <= partidaC and partidaB1 <= partidaT and partidaB1 != 999999:
        clock=partidaB1
    elif partidaB2 <= proxChegada and partidaB2 <= partidaRF and partidaB2 <= partidaA1 and partidaB2 <= partidaA2 and partidaB2 <= partidaB1 and partidaB2 <= partidaC and partidaB2 <= partidaT and partidaB2 != 999999:
        clock=partidaB2
    elif partidaC <= proxChegada and partidaC <= partidaRF and partidaC <= partidaA1 and partidaC <= partidaA2 and partidaC <= partidaB1 and partidaC <= partidaB2 and partidaC <= partidaT and partidaC != 999999:
        clock=partidaC
    elif partidaT <= proxChegada and partidaT <= partidaRF and partidaT <= partidaA1 and partidaT <= partidaA2 and partidaT <= partidaB1 and partidaT <= partidaB2 and partidaT <= partidaC and partidaT != 999999:
        clock=partidaT
    #print("clock depois: "+str(clock))


def buscarProximoUtente():
    global nrUltimoUtente
    nrUltimoUtente = nrUltimoUtente + 1 #incrementa o número do ultimo Utente
    if nrUltimoUtente <= len(Utentes):
        return Utentes[nrUltimoUtente-1] #vai buscar a posição desse Utente
    else:
        return ((999999,0,0,0,0,0,0,0,0,0,0)) # se já não houver Utentes, retorna máximo para avisar


def buscarProximoUtente2():
    global nrUltimoUtente
    ult = nrUltimoUtente+1
    if ult <= len(Utentes):
        return Utentes[ult-1] #vai buscar a posição desse Utente
    else:
        return ((999999,0,0,0,0,0,0,0,0,0,0)) # se já não houver Utentes, retorna máximo para avisar

def eventoChegada():
    global estadoRF
    global partidaRF
    global filaRF
    global filaRFP
    global proxChegada
    global UtenteRF
    global numWearerRF, numWearerRF9_11, numWearerRF11_13, numWearerRF13_15, numWearerRF15_17 
    #ir buscar proximo Utente
    proxUtente = buscarProximoUtente()
    #print(proxUtente[0])
    if proxUtente[0] == 999999:
        proxChegada = 999999
    else:
        #proxChegada = proxUtente[1]
        proxChegada = buscarProximoUtente2()[1] #proxchegada é igual ao valor da chegada do proximo Utente a entrar
        if estadoRF == "livre":
            estadoRF = "ocupado"
            partidaRF = clock+proxUtente[8]
            UtenteRF = proxUtente
            #actualizar variavel estatistica, seg = 0 porque entra diretamente
            atualizaEstatisticas(0,"RF",proxUtente[2],(clock/60/60)+9)
        elif estadoRF == "ocupado":
            aux = ((proxUtente),clock)
            if(proxUtente[2]==1):
                filaRFP.append(aux)
            else:
                filaRF.append(aux)

def eventoPartidaRF():
    global estadoRF
    global partidaRF
    global filaRF
    global filaRFP
    global proxChegada
    global UtenteRF
    global estadoT, partidaT, UtenteT
    global estadoA1, partidaA1, UtenteA1, estadoA2, partidaA2, UtenteA2, filaA, filaAP
    global estadoB1, partidaB1, UtenteB1, estadoB2, partidaB2, UtenteB2, filaB, filaBP
    global estadoC, partidaC, UtenteC, filaC, filaCP
    global tempEspRF, tempEspRF9_11, tempEspRF9_11Max, tempEspRF9_11Min, tempEspRF11_13, tempEsprf11_13Max, tempEspRF11_13Min, tempEspRF13_15, tempEsprf13_15Max, tempEspRF13_15Min, tempEspRF15_17, tempEsprf15_17Max, tempEspRF15_17Min
    global numUtenteRF, numWearerRF9_11, numWearerRF11_13, numWearerRF13_15, numWearerRF15_17 #quantos utilizadores passaram na fila RF
    global numWearerT
    global Utentequepartiu

    Utentequepartiu = UtenteRF[0]
    #se passar diretamente para a 3a fase!
    if(UtenteRF[3]==1):
        #print(UtenteRF)
        if(estadoT == "livre"):
            estadoT = "ocupado"
            partidaT = clock+UtenteRF[10]
            UtenteT = UtenteRF
            #actualiza, seg = 0 porque entra diretamente
            atualizaEstatisticas(0,"T",UtenteT[2],((clock/60/60)+9))
        elif estadoT == "ocupado":
            aux = ((UtenteRF),clock)
            if(UtenteRF[2]==1):
                filaTP.append(aux)
            else:
                filaT.append(aux)
    #se não for diretamente para a 3a fase!
    else:
        if(UtenteRF[4]=="A"):
            if(estadoA1 == "livre"):
                estadoA1 = "ocupado"
                if(UtenteRF[6]==1):
                    partidaA1=clock+ round((UtenteRF[9]*0.8))
                else:
                    partidaA1 = clock+UtenteRF[9]
                UtenteA1 = UtenteRF
                #atualizar variavel estatica, seg = 0 porque entra diretamente
                atualizaEstatisticas(0, "A", UtenteA1[2], ((clock/60/60)+9))
            elif estadoA2 == "livre":
                estadoA2 = "ocupado"
                if (UtenteRF[6] == 1):
                    partidaA2 = clock+ round((UtenteRF[9]*0.8)) #fazer 80% do tempo agora, 20% depois de voltar da 3a fase
                else:
                    partidaA2 = clock + UtenteRF[9]
                UtenteA2 = UtenteRF
                #atualizar variavel estatica, seg = 0 porque entra diretamente
                atualizaEstatisticas(0, "A", UtenteA2[2], ((clock/60/60)+9))
            elif estadoA1 == "ocupado" and estadoA2 == "ocupado":
                aux = ((UtenteRF), clock)
                if (UtenteRF[2] == 1):
                    filaAP.append(aux)
                else:
                    filaA.append(aux)
        elif UtenteRF[4] == "B":
            if (estadoB1 == "livre"):
                estadoB1 = "ocupado"
                if (UtenteRF[6] == 1):
                    partidaB1 = clock + round((UtenteRF[9]*0.8))
                else:
                    partidaB1 = clock + UtenteRF[9]
                UtenteB1 = UtenteRF
                #atualiza variavel estatistica
                atualizaEstatisticas(0, "B", UtenteB1[2], ((clock/60/60)+9))
            elif estadoB2 == "livre":
                estadoB2 = "ocupado"
                if (UtenteRF[6] == 1):
                    partidaB2 = clock + round((UtenteRF[9]*0.8))
                else:
                    partidaB2 = clock + UtenteRF[9]
                UtenteB2 = UtenteRF
                #seg = 0 porque entra diretamente
                atualizaEstatisticas(0, "B", UtenteB2[2], ((clock/60/60)+9))
            elif estadoB1 == "ocupado" and estadoB2 == "ocupado":
                aux = ((UtenteRF), clock)
                if (UtenteRF[2] == 1):
                    filaBP.append(aux)
                else:
                    filaB.append(aux)
        elif UtenteRF[4] == "C":
            if (estadoC == "livre"):
                estadoC = "ocupado"
                if (UtenteRF[6] == 1):
                    partidaC = clock + round((UtenteRF[9]*0.8))
                else:
                    partidaC = clock + UtenteRF[9]
                UtenteC = UtenteRF
                #Atualizar variavel estatica, seg = 0 porque entra diretamente
                atualizaEstatisticas(0, "C", UtenteC[2], ((clock/60/60)+9))
            elif estadoC == "ocupado":
                aux = ((UtenteRF), clock)
                if (UtenteRF[2] == 1):
                    filaCP.append(aux)
                else:
                    filaC.append(aux)

    #agora fazer a entrada do prox Utente
    if len(filaRFP) > 0:
        estadoRF = "ocupado"
        proxUtente = filaRFP.pop(0)
        UtenteRF = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "RF", UtenteRF[2], (UtenteRF[1]/60/60)+9)
        partidaRF = clock+UtenteRF[8]
        #actualizar variavel do Utente
    elif len(filaRF) > 0:
        estadoRF = "ocupado"
        proxUtente = filaRF.pop(0)
        UtenteRF = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "RF", UtenteRF[2], (UtenteRF[1]/60/60)+9)
        partidaRF = clock + UtenteRF[8]
        # actualizar variavel do Utente
    elif len(filaRFP) == 0 and len(filaRF) == 0:
        estadoRF = "livre"
        partidaRF = 999999

def eventoPartidaA1():
    global estadoT, partidaT, UtenteT, filaTP, filaT
    global UtenteA1, estadoA1, partidaA1, filaA, filaAP
    global Utentequepartiu

    Utentequepartiu = UtenteA1[0]

    if(UtenteA1[7] == 0): #não está a fazer ciclo
        if(UtenteA1[5]==1): #vai a 3a fase
            if(estadoT == "livre"):
                estadoT = "ocupado"
                partidaT = clock + UtenteA1[10]
                UtenteT = UtenteA1
                #seg= 0 porque passa na fila 0 segundos
                atualizaEstatisticas(0, "T", UtenteT[2], (UtenteT[1]/60/60)+9)
            elif estadoT == "ocupado":
                aux = ((UtenteA1),clock)
                if (UtenteA1[6] == 1): #se for fazer ciclo, "interrompeu", tem prioridade na 3a fase
                    filaTP.append(aux)
                elif (UtenteA1[2] == 1):
                    filaTP.append(aux)
                elif (UtenteA1[2] == 0):
                    filaT.append(aux)

    #meter novo Utente a ser atendido
    if len(filaAP) > 0:
        estadoA1 = "ocupado"
        proxUtente = filaAP.pop(0)
        UtenteA1 = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "A", UtenteA1[2], (UtenteA1[1]/60/60)+9)
        if(UtenteA1[7] == 1): #já está a fazer ciclo, so faz 20% do tempo
            partidaA1 = clock + round((UtenteA1[9]*0.2))
        elif (UtenteA1[6] == 1):
            partidaA1 = clock + round((UtenteA1[9]*0.8))
        elif (UtenteA1[6] == 0):
            partidaA1 = clock + UtenteA1[9]
    elif len(filaA) > 0:
        estadoA1 = "ocupado"
        proxUtente = filaA.pop(0)
        UtenteA1 = proxUtente[0]
        atualizaEstatisticas(clock-proxUtente[1], "A", UtenteA1[2], (UtenteA1[1]/60/60)+9)
        if (UtenteA1[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaA1 = clock + round((UtenteA1[9] * 0.2))
        elif (UtenteA1[6] == 1):
            partidaA1 = clock + round((UtenteA1[9] * 0.8))
        elif (UtenteA1[6] == 0):
            partidaA1 = clock + UtenteA1[9]
    elif len(filaAP) == 0 and len(filaA) == 0:
        estadoA1 = "livre"
        partidaA1 = 999999


def eventoPartidaA2():
    global estadoT, partidaT, UtenteT, filaTP, filaT
    global UtenteA2, estadoA2, partidaA2, filaA, filaAP
    global Utentequepartiu

    Utentequepartiu = UtenteA2[0]

    if (UtenteA2[7] == 0):  # não está a fazer ciclo
        if (UtenteA2[5] == 1):  # vai a 3a fase
            if (estadoT == "livre"):
                estadoT = "ocupado"
                partidaT = clock + UtenteA2[10]
                UtenteT = UtenteA2
                atualizaEstatisticas(0, "T", UtenteT[2], (UtenteT[1]/60/60)+9)
            elif estadoT == "ocupado":
                aux = ((UtenteA2), clock)
                if (UtenteA2[6] == 1): #se for fazer ciclo, "interrompeu", tem prioridade na 3a fase
                    filaTP.append(aux)
                elif (UtenteA2[2] == 1):
                    filaTP.append(aux)
                elif (UtenteA2[2] == 0):
                    filaT.append(aux)

    # meter novo Utente a ser atendido
    if len(filaAP) > 0:
        estadoA2 = "ocupado"
        proxUtente = filaAP.pop(0)
        UtenteA2 = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "A", UtenteA2[2], (UtenteA2[1]/60/60)+9)
        if (UtenteA2[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaA2 = clock + round((UtenteA2[9] * 0.2))
        elif (UtenteA2[6] == 1):
            partidaA2 = clock + round((UtenteA2[9] * 0.8))
        elif (UtenteA2[6] == 0):
            partidaA2 = clock + UtenteA2[9]
    elif len(filaA) > 0:
        estadoA2 = "ocupado"
        proxUtente = filaA.pop(0)
        UtenteA2 = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "A", UtenteA2[2], (UtenteA2[1]/60/60)+9)
        if (UtenteA2[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaA2 = clock + round((UtenteA2[9] * 0.2))
        elif (UtenteA2[6] == 1):
            partidaA2 = clock + round((UtenteA2[9] * 0.8))
        elif (UtenteA2[6] == 0):
            partidaA2 = clock + UtenteA2[9]
    elif len(filaAP) == 0 and len(filaA) == 0:
        estadoA2 = "livre"
        partidaA2 = 999999

def eventoPartidaB1():
    global estadoT, partidaT, UtenteT, filaTP, filaT
    global UtenteB1, estadoB1, partidaB1, filaB, filaBP
    global Utentequepartiu

    Utentequepartiu = UtenteB1[0]

    if (UtenteB1[7] == 0):  # não está a fazer ciclo
        if (UtenteB1[5] == 1):  # vai a 3a fase
            if (estadoT == "livre"):
                estadoT = "ocupado"
                partidaT = clock + UtenteB1[10]
                UtenteT = UtenteB1
                atualizaEstatisticas(0, "T", UtenteT[2], (UtenteT[1]/60/60)+9)
            elif estadoT == "ocupado":
                aux = ((UtenteB1), clock)
                if (UtenteB1[6] == 1): #se for fazer ciclo, "interrompeu", tem prioridade na 3a fase
                    filaTP.append(aux)
                elif (UtenteB1[2] == 1):
                    filaTP.append(aux)
                elif (UtenteB1[2] == 0):
                    filaT.append(aux)

    # meter novo Utente a ser atendido
    if len(filaBP) > 0:
        estadoB1 = "ocupado"
        proxUtente = filaBP.pop(0)
        UtenteB1 = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "B", UtenteB1[2], (UtenteB1[1]/60/60)+9)
        if (UtenteB1[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaB1 = clock + round((UtenteB1[9] * 0.2))
        elif (UtenteB1[6] == 1):
            partidaB1 = clock + round((UtenteB1[9] * 0.8))
        elif (UtenteB1[6] == 0):
            partidaB1 = clock + UtenteB1[9]
    elif len(filaB) > 0:
        estadoB1 = "ocupado"
        proxUtente = filaB.pop(0)
        UtenteB1 = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "B", UtenteB1[2], (UtenteB1[1]/60/60)+9)
        if (UtenteB1[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaB1 = clock + round((UtenteB1[9] * 0.2))
        elif (UtenteB1[6] == 1):
            partidaB1 = clock + round((UtenteB1[9] * 0.8))
        elif (UtenteB1[6] == 0):
            partidaB1 = clock + UtenteB1[9]
    elif len(filaBP) == 0 and len(filaB) == 0:
        estadoB1 = "livre"
        partidaB1 = 999999

def eventoPartidaB2():
    global estadoT, partidaT, UtenteT, filaTP, filaT
    global UtenteB2, estadoB2, partidaB2, filaB, filaBP
    global Utentequepartiu

    Utentequepartiu = UtenteB2[0]

    if (UtenteB2[7] == 0):  # não está a fazer ciclo
        if (UtenteB2[5] == 1):  # vai a 3a fase
            if (estadoT == "livre"):
                estadoT = "ocupado"
                partidaT = clock + UtenteB2[10]
                UtenteT = UtenteB2
                atualizaEstatisticas(0, "T", UtenteT[2], (UtenteT[1]/60/60)+9)
            elif estadoT == "ocupado":
                aux = ((UtenteB2), clock)
                if (UtenteB2[6] == 1): #se for fazer ciclo, "interrompeu", tem prioridade na 3a fase
                    filaTP.append(aux)
                elif (UtenteB2[2] == 1):
                    filaTP.append(aux)
                elif (UtenteB2[2] == 0):
                    filaT.append(aux)

    # meter novo Utente a ser atendido
    if len(filaBP) > 0:
        estadoB2 = "ocupado"
        proxUtente = filaBP.pop(0)
        UtenteB2 = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "B", UtenteB2[2], (UtenteB2[1]/60/60)+9)
        if (UtenteB2[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaB2 = clock + round((UtenteB2[9] * 0.2))
        elif (UtenteB2[6] == 1):
            partidaB2 = clock + round((UtenteB2[9] * 0.8))
        elif (UtenteB2[6] == 0):
            partidaB2 = clock + UtenteB2[9]
    elif len(filaB) > 0:
        estadoB2 = "ocupado"
        proxUtente = filaB.pop(0)
        UtenteB2 = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "B", UtenteB2[2], (UtenteB2[1]/60/60)+9)
        if (UtenteB2[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaB2 = clock + round((UtenteB2[9] * 0.2))
        elif (UtenteB2[6] == 1):
            partidaB2 = clock + round((UtenteB2[9] * 0.8))
        elif (UtenteB2[6] == 0):
            partidaB2 = clock + UtenteB2[9]
    elif len(filaBP) == 0 and len(filaB) == 0:
        estadoB2 = "livre"
        partidaB2 = 999999

def eventoPartidaC():
    global estadoT, partidaT, UtenteT, filaTP, filaT
    global UtenteC, estadoC, partidaC, filaC, filaCP
    global Utentequepartiu

    Utentequepartiu = UtenteC[0]

    if (UtenteC[7] == 0):  # não está a fazer ciclo
        if (UtenteC[5] == 1):  # vai a 3a fase
            if (estadoT == "livre"):
                estadoT = "ocupado"
                partidaT = clock + UtenteC[10]
                UtenteT = UtenteC
                atualizaEstatisticas(0, "T", UtenteT[2], (UtenteT[1]/60/60)+9)
            elif estadoT == "ocupado":
                aux = ((UtenteC), clock)
                if (UtenteC[6] == 1): #se for fazer ciclo, "interrompeu", tem prioridade na 3a fase
                    filaTP.append(aux)
                elif (UtenteC[2] == 1):
                    filaTP.append(aux)
                elif (UtenteC[2] == 0):
                    filaT.append(aux)

    # meter novo Utente a ser atendido
    if len(filaCP) > 0:
        estadoC = "ocupado"
        proxUtente = filaCP.pop(0)
        UtenteC = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "C", UtenteC[2], (UtenteC[1]/60/60)+9)
        if (UtenteC[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaC = clock + round((UtenteC[9] * 0.2))
        elif (UtenteC[6] == 1):
            partidaC = clock + round((UtenteC[9] * 0.8))
        elif (UtenteC[6] == 0):
            partidaC = clock + UtenteC[9]
    elif len(filaC) > 0:
        estadoC = "ocupado"
        proxUtente = filaC.pop(0)
        UtenteC = proxUtente[0]
        atualizaEstatisticas((clock-proxUtente[1]), "C", UtenteC[2], (UtenteC[1]/60/60)+9)
        if (UtenteC[7] == 1):  # já está a fazer ciclo, so faz 20% do tempo
            partidaC = clock + round((UtenteC[9] * 0.2))
        elif (UtenteC[6] == 1):
            partidaC = clock + round((UtenteC[9] * 0.8))
        elif (UtenteC[6] == 0):
            partidaC = clock + UtenteC[9]
    elif len(filaCP) == 0 and len(filaC) == 0:
        estadoC = "livre"
        partidaC = 999999

def eventoPartidaT():
    global estadoA1, estadoA2, UtenteA1, filaA, filaAP, partidaA1, partidaA2, UtenteA2
    global estadoB1, estadoB2, UtenteB1, filaB, filaBP, partidaB1, partidaB2, UtenteB2
    global estadoC, UtenteC, filaC, filaCP, partidaC
    global UtenteT, estadoT, partidaT, filaTP, filaT
    global Utentequepartiu

    Utentequepartiu = UtenteT[0]

    #se for fazer ciclo, ver para qual vai entrar
    if(UtenteT[7]==0 and UtenteT[6]==1):
        UtenteT = UtenteT[:7] + (1,) + UtenteT[8:]  # mudar o valor da variavel "EstaAFazerCiclo"
        if(UtenteT[4]=="A"):
            if (estadoA1 == "livre"):
                estadoA1 = "ocupado"
                partidaA1 = clock + round((UtenteT[9] * 0.2))
                UtenteA1 = UtenteT
                atualizaEstatisticas(0, "A", UtenteA1[2], (UtenteA1[1]/60/60)+9)
            elif estadoA2 == "livre":
                estadoA2 = "ocupado"
                partidaA2 = clock + round((UtenteT[9] * 0.2))  # fazer 20% do tempo, ja fez 80% anteriormente.
                UtenteA2 = UtenteT
                atualizaEstatisticas(0, "A", UtenteA2[2], (UtenteA2[1]/60/60)+9)
            elif estadoA1 == "ocupado" and estadoA2 == "ocupado":
                aux = ((UtenteT), clock)
                filaAP.append(aux)
        if (UtenteT[4] == "B"):
            if (estadoB1 == "livre"):
               # print("UtenteT antes"+str(UtenteT))
                #print("UtenteT antes" + str(UtenteT))
                estadoB1 = "ocupado"
                partidaB1 = clock + round((UtenteT[9] * 0.2))
                UtenteB1 = UtenteT
                atualizaEstatisticas(0, "B", UtenteB1[2], (UtenteB1[1]/60/60)+9)
            elif estadoB2 == "livre":
                estadoB2 = "ocupado"
                partidaB2 = clock + round((UtenteT[9] * 0.2))  # fazer 20% do tempo, ja fez 80% anteriormente.
                UtenteB2 = UtenteT
                atualizaEstatisticas(0, "B", UtenteB2[2], (UtenteB2[1]/60/60)+9)
            elif estadoB1 == "ocupado" and estadoB2 == "ocupado":
                # actualizar variavel estatica
                aux = ((UtenteT), clock)
                filaBP.append(aux) # tem prioridade por estar a fazer ciclo
        if (UtenteT[4] == "C"):
            if (estadoC == "livre"):
                estadoC = "ocupado"
                partidaC = clock + round((UtenteT[9] * 0.2))
                UtenteC = UtenteT
                atualizaEstatisticas(0, "C", UtenteC[2], (UtenteC[1]/60/60)+9)
            elif estadoC == "ocupado":
                # actualizar variavel estatica
                aux = ((UtenteT), clock)
                filaCP.append(aux) # tem prioridade por estar a fazer ciclo
    if len(filaTP) > 0:
        estadoT = "ocupado"
        proxUtente = filaTP.pop(0)
        UtenteT = proxUtente[0]
        partidaT = clock + UtenteT[10]
        atualizaEstatisticas((clock-proxUtente[1]), "T", UtenteT[2], (UtenteT[1]/60/60)+9)
    elif len(filaT) > 0:
        estadoT = "ocupado"
        proxUtente = filaT.pop(0)
        UtenteT = proxUtente[0]
        partidaT = clock + UtenteT[10]
        atualizaEstatisticas((clock-proxUtente[1]), "T", UtenteT[2], (UtenteT[1]/60/60)+9)
    elif len(filaT) == 0 and len(filaTP) == 0:
        estadoT = "livre"
        partidaT = 999999

def atualizaEstatisticas(seg,fila,prioridade,inter): #tempo,fila,prioridade,intervalotempo 9-11 //// seg=tempo espera; inter � o intervalo em que o utilizador entrou
    global tempEspRF
    global tempEspA
    global tempEspB
    global tempEspC
    global tempEspT
    global tempEspRFP
    global tempEspAP
    global tempEspBP
    global tempEspCP
    global tempEspTP
    global tempEspRFMin
    global tempEspAMin
    global tempEspBMin
    global tempEspCMin
    global tempEspTMin
    global tempEspRFPMin
    global tempEspAPMin
    global tempEspBPMin
    global tempEspCPMin
    global tempEspTPMin
    global tempEspRFMax
    global tempEspAMax
    global tempEspBMax
    global tempEspCMax
    global tempEspTMax
    global tempEspRFPMax
    global tempEspAPMax
    global tempEspBPMax
    global tempEspCPMax
    global tempEspTPMax
    global tempEspRF9_11
    global tempEspA9_11
    global tempEspB9_11
    global tempEspC9_11
    global tempEspT9_11
    global tempEspRFP9_11
    global tempEspAP9_11
    global tempEspBP9_11
    global tempEspCP9_11
    global tempEspTP9_11
    global tempEspRF11_13
    global tempEspA11_13
    global tempEspB11_13
    global tempEspC11_13
    global tempEspT11_13
    global tempEspRFP11_13
    global tempEspAP11_13
    global tempEspBP11_13
    global tempEspCP11_13
    global tempEspTP11_13
    global tempEspRF13_15
    global tempEspA13_15
    global tempEspB13_15
    global tempEspC13_15
    global tempEspT13_15
    global tempEspRFP13_15
    global tempEspAP13_15
    global tempEspBP13_15
    global tempEspCP13_15
    global tempEspTP13_15
    global tempEspRF15_17
    global tempEspA15_17
    global tempEspB15_17
    global tempEspC15_17
    global tempEspT15_17
    global tempEspRFP15_17
    global tempEspAP15_17
    global tempEspBP15_17
    global tempEspCP15_17
    global tempEspTP15_17
    global tempEspRF9_11Max
    global tempEspRFP9_11Max
    global tempEspRF9_11Min
    global tempEspRFP9_11Min
    global tempEspRF11_13Max
    global tempEspRFP11_13Max
    global tempEspRF11_13Min
    global tempEspRFP11_13Min
    global tempEspRF13_15Max
    global tempEspRFP13_15Max
    global tempEspRF13_15Min
    global tempEspRFP13_15Min
    global tempEspRF15_17Max
    global tempEspRFP15_17Max
    global tempEspRF15_17Min
    global tempEspRFP15_17Min
    global tempEspA9_11Max
    global tempEspAP9_11Max
    global tempEspA9_11Min
    global tempEspAP9_11Min
    global tempEspA11_13Max
    global tempEspAP11_13Max
    global tempEspA11_13Min
    global tempEspAP11_13Min
    global tempEspA13_15Max
    global tempEspAP13_15Max
    global tempEspA13_15Min
    global tempEspAP13_15Min
    global tempEspA15_17Max
    global tempEspAP15_17Max
    global tempEspA15_17Min
    global tempEspAP15_17Min
    global tempEspB9_11Max
    global tempEspBP9_11Max
    global tempEspB9_11Min
    global tempEspBP9_11Min
    global tempEspB11_13Max
    global tempEspBP11_13Max
    global tempEspB11_13Min
    global tempEspBP11_13Min
    global tempEspB13_15Max
    global tempEspBP13_15Max
    global tempEspB13_15Min
    global tempEspBP13_15Min
    global tempEspB15_17Max
    global tempEspBP15_17Max
    global tempEspB15_17Min
    global tempEspBP15_17Min
    global tempEspC9_11Max
    global tempEspCP9_11Max
    global tempEspC9_11Min
    global tempEspCP9_11Min
    global tempEspC11_13Max
    global tempEspCP11_13Max
    global tempEspC11_13Min
    global tempEspCP11_13Min
    global tempEspC13_15Max
    global tempEspCP13_15Max
    global tempEspC13_15Min
    global tempEspCP13_15Min
    global tempEspC15_17Max
    global tempEspCP15_17Max
    global tempEspC15_17Min
    global tempEspCP15_17Min
    global tempEspT9_11Max
    global tempEspTP9_11Max
    global tempEspT9_11Min
    global tempEspTP9_11Min
    global tempEspT11_13Max
    global tempEspTP11_13Max
    global tempEspT11_13Min
    global tempEspTP11_13Min
    global tempEspT13_15Max
    global tempEspTP13_15Max
    global tempEspT13_15Min
    global tempEspTP13_15Min
    global tempEspT15_17Max
    global tempEspTP15_17Max
    global tempEspT15_17Min
    global tempEspTP15_17Min

    global numWearerRF
    global numWearerRFP
    global numWearerA
    global numWearerAP
    global numWearerB
    global numWearerBP
    global numWearerC
    global numWearerCP
    global numWearerT
    global numWearerTP

    global numWearerRF9_11
    global numWearerRFP9_11
    global numWearerA9_11
    global numWearerAP9_11
    global numWearerB9_11
    global numWearerBP9_11
    global numWearerC9_11
    global numWearerCP9_11
    global numWearerT9_11
    global numWearerTP9_11

    global numWearerRF11_13
    global numWearerRFP11_13
    global numWearerA11_13
    global numWearerAP11_13
    global numWearerB11_13
    global numWearerBP11_13
    global numWearerC11_13
    global numWearerCP11_13
    global numWearerT11_13
    global numWearerTP11_13

    global numWearerRF13_15
    global numWearerRFP13_15
    global numWearerA13_15
    global numWearerAP13_15
    global numWearerB13_15
    global numWearerBP13_15
    global numWearerC13_15
    global numWearerCP13_15
    global numWearerT13_15
    global numWearerTP13_15
    global numWearerRF15_17
    global numWearerRFP15_17
    global numWearerA15_17
    global numWearerAP15_17
    global numWearerB15_17
    global numWearerBP15_17
    global numWearerC15_17
    global numWearerCP15_17
    global numWearerT15_17
    global numWearerTP15_17
#seg,fila,prioridade,inter
    #print("seg:"+str(seg)+" | fila:"+fila+" | prioridade: "+str(prioridade) + " | "+" | inter:" + str(inter))
    if fila=="RF":
        if prioridade==1:
            numWearerRFP=numWearerRFP+1
            tempEspRFP=tempEspRFP+seg
            if seg<tempEspRFPMin:
                tempEspRFPMin=seg
            if seg>tempEspRFPMax:
                tempEspRFPMax=seg
            if inter>=9 and inter<11:
                numWearerRFP9_11=numWearerRFP9_11+1
                tempEspRFP9_11=tempEspRFP9_11+seg
                if seg < tempEspRFP9_11Min:
                    tempEspRFP9_11Min = seg
                if seg > tempEspRFP9_11Max:
                    tempEspRFP9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerRFP11_13 = numWearerRFP11_13 + 1
                tempEspRFP11_13 = tempEspRFP11_13 + seg
                if seg < tempEspRFP11_13Min:
                    tempEspRFP11_13Min = seg
                if seg > tempEspRFP11_13Max:
                    tempEspRFP11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerRFP13_15 = numWearerRFP13_15 + 1
                tempEspRFP13_15 = tempEspRFP13_15 + seg
                if seg < tempEspRFP13_15Min:
                    tempEspRFP13_15Min = seg
                if seg > tempEspRFP13_15Max:
                    tempEspRFP13_15Max = seg
            if inter >= 15:
                numWearerRFP15_17 = numWearerRFP15_17 + 1
                tempEspRFP15_17 = tempEspRFP15_17 + seg
                if seg < tempEspRFP15_17Min:
                    tempEspRFP15_17Min = seg
                if seg > tempEspRFP15_17Max:
                    tempEspRFP15_17Max = seg
        else:
            numWearerRF = numWearerRF + 1
            tempEspRF = tempEspRF + seg
            if seg < tempEspRFMin:
                tempEspRFMin = seg
            if seg > tempEspRFMax:
                tempEspRFMax = seg
            if inter >= 9 and inter < 11:
                numWearerRF9_11=numWearerRF9_11+1
                tempEspRF9_11 = tempEspRF9_11 + seg
                if seg < tempEspRF9_11Min:
                    tempEspRF9_11Min = seg
                if seg > tempEspRF9_11Max:
                    tempEspRF9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerRF11_13 = numWearerRF11_13 + 1
                tempEspRF11_13 = tempEspRF11_13 + seg
                if seg < tempEspRF11_13Min:
                    tempEspRF11_13Min = seg
                if seg > tempEspRF11_13Max:
                    tempEspRF11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerRF13_15 = numWearerRF13_15 + 1
                tempEspRF13_15 = tempEspRF13_15 + seg
                if seg < tempEspRF13_15Min:
                    tempEspRF13_15Min = seg
                if seg > tempEspRF13_15Max:
                    tempEspRF13_15Max = seg
            if inter >= 15:
                numWearerRF15_17 = numWearerRF15_17 + 1
                tempEspRF15_17 = tempEspRF15_17 + seg
                if seg < tempEspRF15_17Min:
                    tempEspRF15_17Min = seg
                if seg > tempEspRF15_17Max:
                    tempEspRF15_17Max = seg
    elif fila=="A":
        if prioridade==1:
            numWearerAP=numWearerAP+1
            tempEspAP=tempEspAP+seg
            if seg<tempEspAPMin:
                tempEspAPMin=seg
            if seg>tempEspAPMax:
                tempEspAPMax=seg
            if inter>=9 and inter<11:
                numWearerAP9_11=numWearerAP9_11+1
                tempEspAP9_11=tempEspAP9_11+seg
                if seg < tempEspAP9_11Min:
                    tempEspAP9_11Min = seg
                if seg > tempEspAP9_11Max:
                    tempEspAP9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerAP11_13 = numWearerAP11_13 + 1
                tempEspAP11_13 = tempEspAP11_13 + seg
                if seg < tempEspAP11_13Min:
                    tempEspAP11_13Min = seg
                if seg > tempEspAP11_13Max:
                    tempEspAP11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerAP13_15 = numWearerAP13_15 + 1
                tempEspAP13_15 = tempEspAP13_15 + seg
                if seg < tempEspAP13_15Min:
                    tempEspAP13_15Min = seg
                if seg > tempEspAP13_15Max:
                    tempEspAP13_15Max = seg
            if inter >= 15:
                numWearerAP15_17 = numWearerAP15_17 + 1
                tempEspAP15_17 = tempEspAP15_17 + seg
                if seg < tempEspAP15_17Min:
                    tempEspAP15_17Min = seg
                if seg > tempEspAP15_17Max:
                    tempEspAP15_17Max = seg
        else:
            numWearerA=numWearerA+1
            tempEspA = tempEspA + seg
            if seg < tempEspAMin:
                tempEspAMin = seg
            if seg > tempEspAMax:
                tempEspAMax = seg
            if inter >= 9 and inter < 11:
                numWearerA9_11 = numWearerA9_11 + 1
                tempEspA9_11 = tempEspA9_11 + seg
                if seg < tempEspA9_11Min:
                    tempEspA9_11Min = seg
                if seg > tempEspA9_11Max:
                    tempEspA9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerA11_13 = numWearerA11_13 + 1
                tempEspA11_13 = tempEspA11_13 + seg
                if seg < tempEspA11_13Min:
                    tempEspA11_13Min = seg
                if seg > tempEspA11_13Max:
                    tempEspA11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerA13_15 = numWearerA13_15 + 1
                tempEspA13_15 = tempEspA13_15 + seg
                if seg < tempEspA13_15Min:
                    tempEspA13_15Min = seg
                if seg > tempEspA13_15Max:
                    tempEspA13_15Max = seg
            if inter >= 15:
                numWearerA15_17 = numWearerA15_17 + 1
                tempEspA15_17 = tempEspA15_17 + seg
                if seg < tempEspA15_17Min:
                    tempEspA15_17Min = seg
                if seg > tempEspA15_17Max:
                    tempEspA15_17Max = seg
    elif fila == "B":
        if prioridade==1:
            numWearerBP=numWearerBP+1
            tempEspBP=tempEspBP+seg
            if seg<tempEspBPMin:
                tempEspBPMin=seg
            if seg>tempEspBPMax:
                tempEspBPMax=seg
            if inter>=9 and inter<11:
                numWearerBP9_11 = numWearerBP9_11 + 1
                tempEspBP9_11=tempEspBP9_11+seg
                if seg < tempEspBP9_11Min:
                    tempEspBP9_11Min = seg
                if seg > tempEspBP9_11Max:
                    tempEspBP9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerBP11_13 = numWearerBP11_13 + 1
                tempEspBP11_13 = tempEspBP11_13 + seg
                if seg < tempEspBP11_13Min:
                    tempEspBP11_13Min = seg
                if seg > tempEspBP11_13Max:
                    tempEspBP11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerBP13_15 = numWearerBP13_15 + 1
                tempEspBP13_15 = tempEspBP13_15 + seg
                if seg < tempEspBP13_15Min:
                    tempEspBP13_15Min = seg
                if seg > tempEspBP13_15Max:
                    tempEspBP13_15Max = seg
            if inter >= 15:
                numWearerBP15_17 = numWearerBP15_17 + 1
                tempEspBP15_17 = tempEspBP15_17 + seg
                if seg < tempEspBP15_17Min:
                    tempEspBP15_17Min = seg
                if seg > tempEspBP15_17Max:
                    tempEspBP15_17Max = seg
        else:
            numWearerB = numWearerB + 1
            tempEspB = tempEspB + seg
            if seg < tempEspBMin:
                tempEspBMin = seg
            if seg > tempEspBMax:
                tempEspBMax = seg
            if inter >= 9 and inter < 11:
                numWearerB9_11 = numWearerB9_11 + 1
                tempEspB9_11 = tempEspB9_11 + seg
                if seg < tempEspB9_11Min:
                    tempEspB9_11Min = seg
                if seg > tempEspB9_11Max:
                    tempEspB9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerB11_13 = numWearerB11_13 + 1
                tempEspB11_13 = tempEspB11_13 + seg
                if seg < tempEspB11_13Min:
                    tempEspB11_13Min = seg
                if seg > tempEspB11_13Max:
                    tempEspB11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerB13_15 = numWearerB13_15 + 1
                tempEspB13_15 = tempEspB13_15 + seg
                if seg < tempEspB13_15Min:
                    tempEspB13_15Min = seg
                if seg > tempEspB13_15Max:
                    tempEspB13_15Max = seg
            if inter >= 15:
                numWearerB15_17 = numWearerB15_17 + 1
                tempEspB15_17 = tempEspB15_17 + seg
                if seg < tempEspB15_17Min:
                    tempEspB15_17Min = seg
                if seg > tempEspB15_17Max:
                    tempEspB15_17Max = seg
    elif fila == "C":
        if prioridade==1:
            numWearerCP=numWearerCP+1
            tempEspCP=tempEspCP+seg
            if seg<tempEspCPMin:
                tempEspCPMin=seg
            if seg>tempEspCPMax:
                tempEspCPMax=seg
            if inter>=9 and inter<11:
                numWearerCP9_11 = numWearerCP9_11 + 1
                tempEspCP9_11=tempEspCP9_11+seg
                if seg < tempEspCP9_11Min:
                    tempEspCP9_11Min = seg
                if seg > tempEspCP9_11Max:
                    tempEspCP9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerCP11_13 = numWearerCP11_13 + 1
                tempEspCP11_13 = tempEspCP11_13 + seg
                if seg < tempEspCP11_13Min:
                    tempEspCP11_13Min = seg
                if seg > tempEspCP11_13Max:
                    tempEspCP11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerCP13_15 = numWearerCP13_15 + 1
                tempEspCP13_15 = tempEspCP13_15 + seg
                if seg < tempEspCP13_15Min:
                    tempEspCP13_15Min = seg
                if seg > tempEspCP13_15Max:
                    tempEspCP13_15Max = seg
            if inter >= 15:
                numWearerCP15_17 = numWearerCP15_17 + 1
                tempEspCP15_17 = tempEspCP15_17 + seg
                if seg < tempEspCP15_17Min:
                    tempEspCP15_17Min = seg
                if seg > tempEspCP15_17Max:
                    tempEspCP15_17Max = seg
        else:
            numWearerC = numWearerC + 1
            tempEspC = tempEspC + seg
            if seg < tempEspCMin:
                tempEspCMin = seg
            if seg > tempEspCMax:
                tempEspCMax = seg
            if inter >= 9 and inter < 11:
                numWearerC9_11 = numWearerC9_11 + 1
                tempEspC9_11 = tempEspC9_11 + seg
                if seg < tempEspC9_11Min:
                    tempEspC9_11Min = seg
                if seg > tempEspC9_11Max:
                    tempEspC9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerC11_13 = numWearerC11_13 + 1
                tempEspC11_13 = tempEspC11_13 + seg
                if seg < tempEspC11_13Min:
                    tempEspC11_13Min = seg
                if seg > tempEspC11_13Max:
                    tempEspC11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerC13_15 = numWearerC13_15 + 1
                tempEspC13_15 = tempEspC13_15 + seg
                if seg < tempEspC13_15Min:
                    tempEspC13_15Min = seg
                if seg > tempEspC13_15Max:
                    tempEspC13_15Max = seg
            if inter >= 15:
                numWearerC15_17 = numWearerC15_17 + 1
                tempEspC15_17 = tempEspC15_17 + seg
                if seg < tempEspC15_17Min:
                    tempEspC15_17Min = seg
                if seg > tempEspC15_17Max:
                    tempEspC15_17Max = seg
    elif fila == "T":
        if prioridade==1:
            numWearerTP = numWearerTP + 1
            tempEspTP=tempEspTP+seg
            if seg<tempEspTPMin:
                tempEspTPMin=seg
            if seg>tempEspTPMax:
                tempEspTPMax=seg
            if inter>=9 and inter<11:
                numWearerTP9_11 = numWearerTP9_11 + 1
                tempEspTP9_11=tempEspTP9_11+seg
                if seg < tempEspTP9_11Min:
                    tempEspTP9_11Min = seg
                if seg > tempEspTP9_11Max:
                    tempEspTP9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerTP11_13 = numWearerTP11_13 + 1
                tempEspTP11_13 = tempEspTP11_13 + seg
                if seg < tempEspTP11_13Min:
                    tempEspTP11_13Min = seg
                if seg > tempEspTP11_13Max:
                    tempEspTP11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerTP13_15 = numWearerTP13_15 + 1
                tempEspTP13_15 = tempEspTP13_15 + seg
                if seg < tempEspTP13_15Min:
                    tempEspTP13_15Min = seg
                if seg > tempEspTP13_15Max:
                    tempEspTP13_15Max = seg
            if inter >= 15:
                numWearerTP15_17 = numWearerTP15_17 + 1
                tempEspTP15_17 = tempEspTP15_17 + seg
                if seg < tempEspTP15_17Min:
                    tempEspTP15_17Min = seg
                if seg > tempEspTP15_17Max:
                    tempEspTP15_17Max = seg
        else:
            numWearerT = numWearerT + 1
            tempEspT = tempEspT + seg
            if seg < tempEspTMin:
                tempEspTMin = seg
            if seg > tempEspTMax:
                tempEspTMax = seg
            if inter >= 9 and inter < 11:
                numWearerT9_11 = numWearerT9_11 + 1
                tempEspT9_11 = tempEspT9_11 + seg
                if seg < tempEspT9_11Min:
                    tempEspT9_11Min = seg
                if seg > tempEspT9_11Max:
                    tempEspT9_11Max = seg
            if inter >= 11 and inter < 13:
                numWearerT11_13 = numWearerT11_13 + 1
                tempEspT11_13 = tempEspT11_13 + seg
                if seg < tempEspT11_13Min:
                    tempEspT11_13Min = seg
                if seg > tempEspT11_13Max:
                    tempEspT11_13Max = seg
            if inter >= 13 and inter < 15:
                numWearerT13_15 = numWearerT13_15 + 1
                tempEspT13_15 = tempEspT13_15 + seg
                if seg < tempEspT13_15Min:
                    tempEspT13_15Min = seg
                if seg > tempEspT13_15Max:
                    tempEspT13_15Max = seg
            if inter >= 15:
                numWearerT15_17 = numWearerT15_17 + 1
                tempEspT15_17 = tempEspT15_17 + seg
                if seg < tempEspT15_17Min:
                    tempEspT15_17Min = seg
                if seg > tempEspT15_17Max:
                    tempEspT15_17Max = seg

def printEstatisticas():
    global tempEspRF
    global tempEspA
    global tempEspB
    global tempEspC
    global tempEspT
    global tempEspRFP
    global tempEspAP
    global tempEspBP
    global tempEspCP
    global tempEspTP
    global tempEspRFMin
    global tempEspAMin
    global tempEspBMin
    global tempEspCMin
    global tempEspTMin
    global tempEspRFPMin
    global tempEspAPMin
    global tempEspBPMin
    global tempEspCPMin
    global tempEspTPMin
    global tempEspRFMax
    global tempEspAMax
    global tempEspBMax
    global tempEspCMax
    global tempEspTMax
    global tempEspRFPMax
    global tempEspAPMax
    global tempEspBPMax
    global tempEspCPMax
    global tempEspTPMax
    global tempEspRF9_11
    global tempEspA9_11
    global tempEspB9_11
    global tempEspC9_11
    global tempEspT9_11
    global tempEspRFP9_11
    global tempEspAP9_11
    global tempEspBP9_11
    global tempEspCP9_11
    global tempEspTP9_11
    global tempEspRF11_13
    global tempEspA11_13
    global tempEspB11_13
    global tempEspC11_13
    global tempEspT11_13
    global tempEspRFP11_13
    global tempEspAP11_13
    global tempEspBP11_13
    global tempEspCP11_13
    global tempEspTP11_13
    global tempEspRF13_15
    global tempEspA13_15
    global tempEspB13_15
    global tempEspC13_15
    global tempEspT13_15
    global tempEspRFP13_15
    global tempEspAP13_15
    global tempEspBP13_15
    global tempEspCP13_15
    global tempEspTP13_15
    global tempEspRF15_17
    global tempEspA15_17
    global tempEspB15_17
    global tempEspC15_17
    global tempEspT15_17
    global tempEspRFP15_17
    global tempEspAP15_17
    global tempEspBP15_17
    global tempEspCP15_17
    global tempEspTP15_17
    global tempEspRF9_11Max
    global tempEspRFP9_11Max
    global tempEspRF9_11Min
    global tempEspRFP9_11Min
    global tempEspRF11_13Max
    global tempEspRFP11_13Max
    global tempEspRF11_13Min
    global tempEspRFP11_13Min
    global tempEspRF13_15Max
    global tempEspRFP13_15Max
    global tempEspRF13_15Min
    global tempEspRFP13_15Min
    global tempEspRF15_17Max
    global tempEspRFP15_17Max
    global tempEspRF15_17Min
    global tempEspRFP15_17Min
    global tempEspA9_11Max
    global tempEspAP9_11Max
    global tempEspA9_11Min
    global tempEspAP9_11Min
    global tempEspA11_13Max
    global tempEspAP11_13Max
    global tempEspA11_13Min
    global tempEspAP11_13Min
    global tempEspA13_15Max
    global tempEspAP13_15Max
    global tempEspA13_15Min
    global tempEspAP13_15Min
    global tempEspA15_17Max
    global tempEspAP15_17Max
    global tempEspA15_17Min
    global tempEspAP15_17Min
    global tempEspB9_11Max
    global tempEspBP9_11Max
    global tempEspB9_11Min
    global tempEspBP9_11Min
    global tempEspB11_13Max
    global tempEspBP11_13Max
    global tempEspB11_13Min
    global tempEspBP11_13Min
    global tempEspB13_15Max
    global tempEspBP13_15Max
    global tempEspB13_15Min
    global tempEspBP13_15Min
    global tempEspB15_17Max
    global tempEspBP15_17Max
    global tempEspB15_17Min
    global tempEspBP15_17Min
    global tempEspC9_11Max
    global tempEspCP9_11Max
    global tempEspC9_11Min
    global tempEspCP9_11Min
    global tempEspC11_13Max
    global tempEspCP11_13Max
    global tempEspC11_13Min
    global tempEspCP11_13Min
    global tempEspC13_15Max
    global tempEspCP13_15Max
    global tempEspC13_15Min
    global tempEspCP13_15Min
    global tempEspC15_17Max
    global tempEspCP15_17Max
    global tempEspC15_17Min
    global tempEspCP15_17Min
    global tempEspT9_11Max
    global tempEspTP9_11Max
    global tempEspT9_11Min
    global tempEspTP9_11Min
    global tempEspT11_13Max
    global tempEspTP11_13Max
    global tempEspT11_13Min
    global tempEspTP11_13Min
    global tempEspT13_15Max
    global tempEspTP13_15Max
    global tempEspT13_15Min
    global tempEspTP13_15Min
    global tempEspT15_17Max
    global tempEspTP15_17Max
    global tempEspT15_17Min
    global tempEspTP15_17Min
    global numWearerRF
    global numWearerRFP
    global numWearerA
    global numWearerAP
    global numWearerB
    global numWearerBP
    global numWearerC
    global numWearerCP
    global numWearerT
    global numWearerTP
    global numWearerRF9_11
    global numWearerRFP9_11
    global numWearerA9_11
    global numWearerAP9_11
    global numWearerB9_11
    global numWearerBP9_11
    global numWearerC9_11
    global numWearerCP9_11
    global numWearerT9_11
    global numWearerTP9_11
    global numWearerRF11_13
    global numWearerRFP11_13
    global numWearerA11_13
    global numWearerAP11_13
    global numWearerB11_13
    global numWearerBP11_13
    global numWearerC11_13
    global numWearerCP11_13
    global numWearerT11_13
    global numWearerTP11_13
    global numWearerRF13_15
    global numWearerRFP13_15
    global numWearerA13_15
    global numWearerAP13_15
    global numWearerB13_15
    global numWearerBP13_15
    global numWearerC13_15
    global numWearerCP13_15
    global numWearerT13_15
    global numWearerTP13_15
    global numWearerRF15_17
    global numWearerRFP15_17
    global numWearerA15_17
    global numWearerAP15_17
    global numWearerB15_17
    global numWearerBP15_17
    global numWearerC15_17
    global numWearerCP15_17
    global numWearerT15_17
    global numWearerTP15_17

    tempEspRFMin = 0 if tempEspRFMin==999999 else tempEspRFMin
    tempEspAMin = 0 if tempEspAMin == 999999 else tempEspAMin
    tempEspBMin = 0 if tempEspBMin == 999999 else tempEspBMin
    tempEspCMin = 0 if tempEspCMin == 999999 else tempEspCMin
    tempEspTMin = 0 if tempEspTMin == 999999 else tempEspTMin
    tempEspRFPMin = 0 if tempEspRFPMin == 999999 else tempEspRFPMin
    tempEspAPMin = 0 if tempEspAPMin == 999999 else tempEspAPMin
    tempEspBPMin = 0 if tempEspBPMin == 999999 else tempEspBPMin
    tempEspCPMin = 0 if tempEspCPMin == 999999 else tempEspCPMin
    tempEspTPMin = 0 if tempEspTPMin == 999999 else tempEspTPMin
    tempEspT15_17Min = 0 if tempEspT15_17Min == 999999 else tempEspT15_17Min
    tempEspTP15_17Min = 0 if tempEspTP15_17Min == 999999 else tempEspTP15_17Min
    tempEspT13_15Min = 0 if tempEspT13_15Min == 999999 else tempEspT13_15Min
    tempEspTP13_15Min = 0 if tempEspTP13_15Min == 999999 else tempEspTP13_15Min
    tempEspT11_13Min = 0 if tempEspT11_13Min == 999999 else tempEspT11_13Min
    tempEspTP11_13Min = 0 if tempEspTP11_13Min == 999999 else tempEspTP11_13Min
    tempEspT9_11Min = 0 if tempEspT9_11Min == 999999 else tempEspT9_11Min
    tempEspTP9_11Min = 0 if tempEspTP9_11Min == 999999 else tempEspTP9_11Min
    tempEspC15_17Min = 0 if tempEspC15_17Min == 999999 else tempEspC15_17Min
    tempEspCP15_17Min = 0 if tempEspCP15_17Min == 999999 else tempEspCP15_17Min
    tempEspC13_15Min = 0 if tempEspC13_15Min == 999999 else tempEspC13_15Min
    tempEspCP13_15Min = 0 if tempEspCP13_15Min == 999999 else tempEspCP13_15Min
    tempEspC11_13Min = 0 if tempEspC11_13Min == 999999 else tempEspC11_13Min
    tempEspCP11_13Min = 0 if tempEspCP11_13Min == 999999 else tempEspCP11_13Min
    tempEspC9_11Min = 0 if tempEspC9_11Min == 999999 else tempEspC9_11Min
    tempEspCP9_11Min = 0 if tempEspCP9_11Min == 999999 else tempEspCP9_11Min
    tempEspB15_17Min = 0 if tempEspB15_17Min == 999999 else tempEspB15_17Min
    tempEspBP15_17Min = 0 if tempEspBP15_17Min == 999999 else tempEspBP15_17Min
    tempEspB13_15Min = 0 if tempEspB13_15Min == 999999 else tempEspB13_15Min
    tempEspBP13_15Min = 0 if tempEspBP13_15Min == 999999 else tempEspBP13_15Min
    tempEspB11_13Min = 0 if tempEspB11_13Min == 999999 else tempEspB11_13Min
    tempEspBP11_13Min = 0 if tempEspBP11_13Min == 999999 else tempEspBP11_13Min
    tempEspB9_11Min = 0 if tempEspB9_11Min == 999999 else tempEspB9_11Min
    tempEspBP9_11Min = 0 if tempEspBP9_11Min == 999999 else tempEspBP9_11Min
    tempEspA15_17Min = 0 if tempEspA15_17Min == 999999 else tempEspA15_17Min
    tempEspAP15_17Min = 0 if tempEspAP15_17Min == 999999 else tempEspAP15_17Min
    tempEspA13_15Min = 0 if tempEspA13_15Min == 999999 else tempEspA13_15Min
    tempEspAP13_15Min = 0 if tempEspAP13_15Min == 999999 else tempEspAP13_15Min
    tempEspA11_13Min = 0 if tempEspA11_13Min == 999999 else tempEspA11_13Min
    tempEspAP11_13Min = 0 if tempEspAP11_13Min == 999999 else tempEspAP11_13Min
    tempEspA9_11Min = 0 if tempEspA9_11Min == 999999 else tempEspA9_11Min
    tempEspAP9_11Min = 0 if tempEspAP9_11Min == 999999 else tempEspAP9_11Min
    tempEspRF15_17Min = 0 if tempEspRF15_17Min == 999999 else tempEspRF15_17Min
    tempEspRFP15_17Min = 0 if tempEspRFP15_17Min == 999999 else tempEspRFP15_17Min
    tempEspRF13_15Min = 0 if tempEspRF13_15Min == 999999 else tempEspRF13_15Min
    tempEspRFP13_15Min = 0 if tempEspRFP13_15Min == 999999 else tempEspRFP13_15Min
    tempEspRF11_13Min = 0 if tempEspRF11_13Min == 999999 else tempEspRF11_13Min
    tempEspRFP11_13Min = 0 if tempEspRFP11_13Min == 999999 else tempEspRFP11_13Min
    tempEspRF9_11Min = 0 if tempEspRF9_11Min == 999999 else tempEspRF9_11Min
    tempEspRFP9_11Min = 0 if tempEspRFP9_11Min == 999999 else tempEspRFP9_11Min

    if numWearerRF!=0:
        print("Tempo Médio de Espera Fila Triagem: "+ str(((tempEspRF+tempEspRFP)/(numWearerRF+numWearerRFP))))
    else:
        print("Tempo Médio de Espera Fila Triagem: 0")

    if numWearerRF9_11!=0:
        print("Tempo Médio de Espera Fila Triagem das 9 às 11: " + str((tempEspRF9_11+tempEspRFP9_11) / (numWearerRF9_11+numWearerRFP9_11)))
    else:
        print("Tempo Médio de Espera Fila Triagem das 9 às 11: 0")


    if numWearerRF11_13!=0:
        print("Tempo Médio de Espera Fila Triagem das 11 às 13: "+str(((tempEspRF11_13+tempEspRFP11_13)/(numWearerRF11_13+numWearerRFP11_13))))
    else:
        print("Tempo Médio de Espera Fila Triagem das 11 às 13: 0")


    if numWearerRF13_15!=0:
        print("Tempo Médio de Espera Fila Triagem das 13 às 15: "+str(((tempEspRF13_15+tempEspRFP13_15)/(numWearerRF13_15+tempEspRFP13_15))))
    else:
        print("Tempo Médio de Espera Fila Triagem das 13 às 15: 0")


    if numWearerRF15_17!=0:
        print("Tempo Médio de Espera Fila Triagem das 15 às 17: "+str(((tempEspRF15_17+tempEspRFP15_17)/(numWearerRF15_17+numWearerRFP15_17))))
    else:
        print("Tempo Médio de Espera Fila Triagem das 15 às 17: 0")


    print("Tempo Máximo de Espera Fila Triagem: " + str(max(tempEspRFMax,tempEspRFPMax)))
    print("Tempo Minimo de Espera Fila Triagem: " +str(min(tempEspRFMin,tempEspRFPMin)))
    print("Tempo Máximo de Espera Fila Triagem das 9 às 11: " + str(max(tempEspRF9_11Max,tempEspRFP9_11Max)))
    print("Tempo Minimo de Espera Fila Triagem das 9 às 11: " +str(min(tempEspRF9_11Min,tempEspRFP9_11Min)))
    print("Tempo Máximo de Espera Fila Triagem das 11 às 13: " + str(max(tempEspRF11_13Max,tempEspRFP11_13Max)))
    print("Tempo Minimo de Espera Fila Triagem das 11 às 13: " +str(min(tempEspRF11_13Min,tempEspRFP11_13Min)))
    print("Tempo Máximo de Espera Fila Triagem das 13 às 15: " + str(max(tempEspRF13_15Max,tempEspRFP13_15Max)))
    print("Tempo Minimo de Espera Fila Triagem das 13 às 15: " +str(min(tempEspRF13_15Min,tempEspRFP13_15Min)))
    print("Tempo Máximo de Espera Fila Triagem das 15 às 17: " + str(max(tempEspRF15_17Max,tempEspRFP15_17Max)))
    print("Tempo Minimo de Espera Fila Triagem das 15 às 17: " +str(min(tempEspRF15_17Min,tempEspRFP15_17Min)))



    if numWearerA!=0:
        print("Tempo Médio de Espera Fila Certidões/Registos: " + str(((tempEspA+tempEspAP) / (numWearerA+numWearerAP))))
    else:
        print("Tempo Médio de Espera Fila Certidões/Registos: 0")

    if numWearerA9_11!=0:
        print("Tempo Médio de Espera Fila Certidões/Registos das 9 às 11: " + str(((tempEspA9_11+tempEspAP9_11) / (numWearerA9_11+numWearerAP9_11))))
    else:
        print("Tempo Médio de Espera Fila Certidões/Registos das 9 às 11: 0")

    if numWearerA11_13!=0:
        print("Tempo Médio de Espera Fila Certidões/Registos das 11 às 13: " + str(((tempEspA11_13+tempEspAP11_13) / (numWearerA11_13+numWearerAP11_13))))
    else:
        print("Tempo Médio de Espera Fila Certidões/Registos das 11 às 13: 0")


    if numWearerA13_15!=0:
        print("Tempo Médio de Espera Fila Certidões/Registos das 13 às 15: " + str(((tempEspA13_15+tempEspAP13_15) / (numWearerA13_15+numWearerAP13_15))))
    else:
        print("Tempo Médio de Espera Fila Certidões/Registos das 13 às 15: 0")


    if numWearerA15_17!=0:
        print("Tempo Médio de Espera Fila Certidões/Registos das 15 às 17: " + str(((tempEspA15_17+tempEspAP15_17) / (numWearerA15_17+numWearerAP15_17))))
    else:
        print("Tempo Médio de Espera Fila Certidões/Registos das 15 às 17: 0")


    print("Tempo Máximo de Espera Fila Certidões/Registos: " + str(max(tempEspAMax,tempEspAPMax)))
    print("Tempo Minimo de Espera Fila Certidões/Registos: " + str(min(tempEspAMin,tempEspAPMin)))
    print("Tempo Máximo de Espera Fila Certidões/Registos das 9 às 11: " + str(max(tempEspA9_11Max,tempEspAP9_11Max)))
    print("Tempo Minimo de Espera Fila Certidões/Registos das 9 às 11: " + str(min(tempEspA9_11Min,tempEspAP9_11Min)))
    print("Tempo Máximo de Espera Fila Certidões/Registos das 11 às 13: " + str(max(tempEspA11_13Max,tempEspAP11_13Max)))
    print("Tempo Minimo de Espera Fila Certidões/Registos das 11 às 13: " + str(min(tempEspA11_13Min,tempEspAP11_13Min)))
    print("Tempo Máximo de Espera Fila Certidões/Registos das 13 às 15: " + str(max(tempEspA13_15Max,tempEspAP13_15Max)))
    print("Tempo Minimo de Espera Fila Certidões/Registos das 13 às 15: " + str(min(tempEspA13_15Min,tempEspAP13_15Min)))
    print("Tempo Máximo de Espera Fila Certidões/Registos das 15 às 17: " + str(max(tempEspA15_17Max,tempEspAP15_17Max)))
    print("Tempo Minimo de Espera Fila Certidões/Registos das 15 às 17: " + str(min(tempEspA15_17Min,tempEspAP15_17Min)))


    if numWearerB!=0:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA: " + str(((tempEspB+tempEspBP) / (numWearerB+numWearerBP))))
    else:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA: 0")

    if numWearerB9_11!=0:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA das 9 às 11: " + str(((tempEspB9_11+tempEspBP9_11) / (numWearerB9_11+numWearerBP9_11))))
    else:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA das 9 às 11: 0")


    if numWearerB11_13!=0:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA das 11 às 13: " + str(((tempEspB11_13+tempEspBP11_13) / (numWearerB11_13+numWearerBP11_13))))
    else:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA das 11 às 13: 0")

    if numWearerB13_15!=0:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA das 13 às 15: " + str(((tempEspB13_15+tempEspBP13_15) / (numWearerB13_15+numWearerBP13_15))))
    else:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA das 13 às 15: 0")

    if numWearerB15_17!=0:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA das 15 às 17: " + str(((tempEspB15_17+tempEspBP15_17) / (numWearerB15_17+numWearerBP15_17))))
    else:
        print("Tempo Médio de Espera Fila IRS/IRC/IVA das 15 às 17: 0")


    print("Tempo Máximo de Espera Fila IRS/IRC/IVA: " + str(max(tempEspBMax,tempEspBPMax)))
    print("Tempo Minimo de Espera Fila IRS/IRC/IVA: " + str(min(tempEspBMin,tempEspBPMin)))
    print("Tempo Máximo de Espera Fila IRS/IRC/IVA das 9 às 11: " + str(max(tempEspB9_11Max,tempEspBP9_11Max)))
    print("Tempo Minimo de Espera Fila IRS/IRC/IVA das 9 às 11: " + str(min(tempEspB9_11Min,tempEspBP9_11Min)))
    print("Tempo Máximo de Espera Fila IRS/IRC/IVA das 11 às 13: " + str(max(tempEspB11_13Max,tempEspBP11_13Max)))
    print("Tempo Minimo de Espera Fila IRS/IRC/IVA das 11 às 13: " + str(min(tempEspB11_13Min,tempEspBP11_13Min)))
    print("Tempo Máximo de Espera Fila IRS/IRC/IVA das 13 às 15: " + str(max(tempEspB13_15Max,tempEspBP13_15Max)))
    print("Tempo Minimo de Espera Fila IRS/IRC/IVA das 13 às 15: " + str(min(tempEspB13_15Min,tempEspBP13_15Min)))
    print("Tempo Máximo de Espera Fila IRS/IRC/IVA das 15 às 17: " + str(max(tempEspB15_17Max,tempEspBP15_17Max)))
    print("Tempo Minimo de Espera Fila IRS/IRC/IVA das 15 às 17: " + str(min(tempEspB15_17Min,tempEspBP15_17Min)))

    if numWearerC!=0:
        print("Tempo Médio de Espera Fila Contencioso: " + str(((tempEspC+tempEspCP) / (numWearerC+numWearerCP))))
    else:
        print("Tempo Médio de Espera Fila Contencioso: 0")


    if numWearerC9_11!=0:
        print("Tempo Médio de Espera Fila Contencioso das 9 às 11: " + str(((tempEspC9_11+tempEspCP9_11) / (numWearerC9_11+numWearerCP9_11))))
    else:
        print("Tempo Médio de Espera Fila Contencioso das 9 às 11: 0")


    if numWearerC11_13!=0:
        print("Tempo Médio de Espera Fila Contencioso das 11 às 13: " + str(((tempEspC11_13+tempEspCP11_13) / (numWearerC11_13+numWearerCP11_13))))
    else:
        print("Tempo Médio de Espera Fila Contencioso das 11 às 13: 0")


    if numWearerC13_15!=0:
        print("Tempo Médio de Espera Fila Contencioso das 13 às 15: " + str(((tempEspC13_15+tempEspCP13_15) / (numWearerC13_15+numWearerCP13_15))))
    else:
        print("Tempo Médio de Espera Fila Contencioso das 13 às 15: 0")


    if numWearerC15_17!=0:
        print("Tempo Médio de Espera Fila Contencioso das 15 às 17: " + str(((tempEspC15_17+tempEspCP15_17) / (numWearerC15_17+numWearerCP15_17))))
    else:
        print("Tempo Médio de Espera Fila Contencioso das 15 às 17: 0")


    print("Tempo Máximo de Espera Fila Contencioso: " + str(max(tempEspCMax,tempEspCPMax)))
    print("Tempo Minimo de Espera Fila Contencioso: " + str(min(tempEspCMin,tempEspCPMin)))
    print("Tempo Máximo de Espera Fila Contencioso das 9 às 11: " +str( max(tempEspC9_11Max,tempEspCP9_11Max)))
    print("Tempo Minimo de Espera Fila Contencioso das 9 às 11: " + str(min(tempEspC9_11Min,tempEspCP9_11Min)))
    print("Tempo Máximo de Espera Fila Contencioso das 11 às 13: " + str(max(tempEspC11_13Max,tempEspCP11_13Max)))
    print("Tempo Minimo de Espera Fila Contencioso das 11 às 13: " + str(min(tempEspC11_13Min,tempEspCP11_13Min)))
    print("Tempo Máximo de Espera Fila Contencioso das 13 às 15: " + str(max(tempEspC13_15Max,tempEspCP13_15Max)))
    print("Tempo Minimo de Espera Fila Contencioso das 13 às 15: " + str(min(tempEspC13_15Min,tempEspCP13_15Min)))
    print("Tempo Máximo de Espera Fila Contencioso das 15 às 17: " + str(max(tempEspC15_17Max,tempEspCP15_17Max)))
    print("Tempo Minimo de Espera Fila Contencioso das 15 às 17: " + str(min(tempEspC15_17Min,tempEspCP15_17Min)))


    if numWearerT!=0:
        print("Tempo Médio de Espera Fila Tesouraria: " + str(((tempEspT+tempEspTP) / (numWearerT+numWearerTP))))
    else:
        print("Tempo Médio de Espera Fila Tesouraria: 0")

    if numWearerT9_11!=0:
        print("Tempo Médio de Espera Fila Tesouraria das 9 às 11: " + str(((tempEspT9_11+tempEspTP9_11) / (numWearerT9_11+numWearerTP9_11))))
    else:
        print("Tempo Médio de Espera Fila Tesouraria das 9 às 11: 0")

    if numWearerT11_13 !=0:
        print("Tempo Médio de Espera Fila Tesouraria das 11 às 13: " + str(((tempEspT11_13+tempEspTP11_13) / (numWearerT11_13+numWearerTP11_13))))
    else:
        print("Tempo Médio de Espera Fila Tesouraria das 11 às 13: 0")

    if numWearerT13_15!=0:
        print("Tempo Médio de Espera Fila Tesouraria das 13 às 15: " + str(((tempEspT13_15+tempEspTP13_15) / (numWearerT13_15+numWearerTP13_15))))
    else:
        print("Tempo Médio de Espera Fila Tesouraria das 13 às 15: 0")

    if numWearerT15_17!=0:
        print("Tempo Médio de Espera Fila Tesouraria das 15 às 17: " + str(((tempEspT15_17+tempEspTP15_17) / (numWearerT15_17+numWearerTP15_17))))
    else:
        print("Tempo Médio de Espera Fila Tesouraria das 15 às 17: 0")

    print("Tempo Máximo de Espera Fila Tesouraria: " + str(max(tempEspTMax,tempEspTPMax)))
    print("Tempo Minimo de Espera Fila Tesouraria: " + str(min(tempEspTMin,tempEspTPMin)))
    print("Tempo Máximo de Espera Fila Tesouraria das 9 às 11: " + str(max(tempEspT9_11Max,tempEspTP9_11Max)))
    print("Tempo Minimo de Espera Fila Tesouraria das 9 às 11: " + str(min(tempEspT9_11Min,tempEspTP9_11Min)))
    print("Tempo Máximo de Espera Fila Tesouraria das 11 às 13: " + str(max(tempEspT11_13Max,tempEspTP11_13Max)))
    print("Tempo Minimo de Espera Fila Tesouraria das 11 às 13: " + str(min(tempEspT11_13Min,tempEspTP11_13Min)))
    print("Tempo Máximo de Espera Fila Tesouraria das 13 às 15: " + str(max(tempEspT13_15Max,tempEspTP13_15Max)))
    print("Tempo Minimo de Espera Fila Tesouraria das 13 às 15: " + str(min(tempEspT13_15Min,tempEspTP13_15Min)))
    print("Tempo Máximo de Espera Fila Tesouraria das 15 às 17: " + str(max(tempEspT15_17Max,tempEspTP15_17Max)))
    print("Tempo Minimo de Espera Fila Tesouraria das 15 às 17: " + str(min(tempEspT15_17Min,tempEspTP15_17Min)))


def primeiraIteração():
    clockLST.append(clock)
    eventoLST.append("-")
    UtenteLST.append("-")
    proxChegadaLST.append(proxChegada)
    filaRFLST.append([])
    filaRFPLST.append([])
    estadoRFLST.append(estadoRF)
    partidaRFLST.append(partidaRF)
    filaALST.append([])
    filaAPLST.append([])
    estadoA1LST.append(estadoA1)
    estadoA2LST.append(estadoA2)
    partidaA1LST.append(partidaA1)
    partidaA2LST.append(partidaA2)
    filaBLST.append([])
    filaBPLST.append([])
    estadoB1LST.append(estadoB1)
    estadoB2LST.append(estadoB2)
    partidaB1LST.append(partidaB1)
    partidaB2LST.append(partidaB2)
    filaCLST.append([])
    filaCPLST.append([])
    estadoCLST.append(estadoC)
    partidaCLST.append(partidaC)
    filaTLST.append([])
    filaTPLST.append([])
    estadoTLST.append(estadoT)
    partidaTLST.append(partidaT)

def returnClockEntradaTuplo(x):
    return x[1]

def actualizaListasFolhaExcel(evento): #Cheg -> chegadaRF; PRF -> partidaRF; A1 -> partida A1; A2, B1, B2, C, T
    global clockLST,clockLST,eventoLSTUtenteLST,proxChegadaLST,filaRFLST,estadoRFLST
    global partidaRFLST,filaALST,filaAPLST,estadoA1LST,estadoA2LST,partidaA1LST,partidaA2LST
    global filaBLST,filaBPLST,estadoB1LST,estadoB2LST,partidaB1LST,partidaB2LST,filaCLST,filaCPLST,estadoCLST,partidaCLST,filaTLST,filaTPLST,estadoTLST,partidaTLST
    global UtenteRF, UtenteA1, UtenteA2, UtenteB1, UtenteB2, UtenteC, UtenteT
    global filaRF, filaRFP, filaA, filaAP, filaB,filaBP,filaC,filaCP,filaT,filaTP

    clockLST.append(clock)
    if evento == "Cheg":
        eventoLST.append("Chegada")
        UtenteLST.append(nrUltimoUtente)
    if evento == "PRF":
        eventoLST.append("Partida RF")
        UtenteLST.append(Utentequepartiu) #nr Utente
    if evento == "A1":
        eventoLST.append("Partida A1")
        UtenteLST.append(Utentequepartiu)
    if evento == "A2":
        eventoLST.append("Partida A2")
        UtenteLST.append(Utentequepartiu)
    if evento == "B1":
        eventoLST.append("Partida B1")
        UtenteLST.append(Utentequepartiu)
    if evento == "B2":
        eventoLST.append("Partida B2")
        UtenteLST.append(Utentequepartiu)
    if evento == "C":
        eventoLST.append("Partida C")
        UtenteLST.append(Utentequepartiu)
    if evento == "T":
        eventoLST.append("Partida T")
        UtenteLST.append(Utentequepartiu)

    proxChegadaLST.append(proxChegada)
    aux123 = list(map(returnClockEntradaTuplo,filaRF))
    filaRFLST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo,filaRFP))
    filaRFPLST.append(aux123)
    estadoRFLST.append(estadoRF)
    partidaRFLST.append(partidaRF)
    aux123 = list(map(returnClockEntradaTuplo, filaA))
    filaALST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaAP))
    filaAPLST.append(aux123)
    estadoA1LST.append(estadoA1)
    estadoA2LST.append(estadoA2)
    partidaA1LST.append(partidaA1)
    partidaA2LST.append(partidaA2)
    aux123 = list(map(returnClockEntradaTuplo, filaB))
    filaBLST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaBP))
    filaBPLST.append(aux123)
    estadoB1LST.append(estadoB1)
    estadoB2LST.append(estadoB2)
    partidaB1LST.append(partidaB1)
    partidaB2LST.append(partidaB2)
    aux123 = list(map(returnClockEntradaTuplo, filaC))
    filaCLST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaCP))
    filaCPLST.append(aux123)
    estadoCLST.append(estadoC)
    partidaCLST.append(partidaC)
    aux123 = list(map(returnClockEntradaTuplo, filaT))
    filaTLST.append(aux123)
    aux123 = list(map(returnClockEntradaTuplo, filaTP))
    filaTPLST.append(aux123)
    estadoTLST.append(estadoT)
    partidaTLST.append(partidaT)

def desenharGraficos():
    # gráfico 1D chegadas
    fig = plt.figure()
    ar = list(map(lambda x: x[1], Utentes))
    plt.xlabel('Clock (s)')
    plt.title('Eventos de Chegada\nao Sistema.')
    plt.plot(ar, len(ar) * [0], "x")
    fig.savefig("plot_Chegadas.png")

    # limpar figura feita, fazer outra
    plt.clf()

    # grafico de barras, tempo médio de espera por posto
    objects = ('Triagem', 'Posto A', 'Posto B', 'Posto C', 'Posto T')
    y_pos = np.arange(len(objects))
    auxRF = ((tempEspRF + tempEspRFP) / (numWearerRF + numWearerRFP)) if (numWearerRF + numWearerRFP) != 0 else 0
    auxA = ((tempEspA + tempEspAP) / (numWearerA + numWearerAP)) if (numWearerA + numWearerAP) != 0 else 0
    auxB = ((tempEspB + tempEspBP) / (numWearerB + numWearerBP)) if (numWearerB + numWearerBP) != 0 else 0
    auxC = ((tempEspC + tempEspCP) / (numWearerC + numWearerCP)) if (numWearerC + numWearerCP) != 0 else 0
    auxT = ((tempEspT + tempEspTP) / (numWearerT + numWearerTP)) if (numWearerT + numWearerTP) != 0 else 0
    performance = [auxRF,auxA,auxB,auxC,auxT]
    plt.figure(figsize=(6, 5))
    plt.bar(y_pos, performance, align='center', alpha=1)
    plt.xticks(y_pos, objects)
    plt.ylabel('Segundos')
    plt.xlabel('Posto Atendimento')
    plt.title('Tempo Médio Total de Espera')
    plt.savefig("bar_TempoEsperaMedio.png")

def main():
    global proxChegada, partidaRF, partidaA1, partidaA2, partidaB1, partidaB2, partidaC, partidaT
    global filaRFLST, filaRFPLST, filaAPLST, filaALST, filaBPLST, filaBLST, filaCPLST, filaCLST, filaTPLST, filaTLST
    global nrUltimoUtente
    criaUtentes()
    proxChegada = Utentes[0][1]
    primeiraIteração() ##variaveis para criar excel da tabela, clock a 0, onde só aparece a proxchegada
    while 1:
        tempo()
        if proxChegada==999999 and partidaRF==999999 and partidaA1==999999 and partidaA2==999999 and partidaB1==999999 and partidaB2==999999 and partidaC==999999 and partidaT==999999:
            break
        if clock==proxChegada:
            #print ("eventoChegada")
            eventoChegada()
            if(nrUltimoUtente <= len(Utentes)): #se não existisse, criava uma linha no excel de um Utente que não existe
                actualizaListasFolhaExcel("Cheg")
        elif clock==partidaRF:
            #print ("eventoPartidaRF")
            eventoPartidaRF()
            actualizaListasFolhaExcel("PRF")
        elif clock==partidaA1:
            #print ("eventoPartidaA1")
            eventoPartidaA1()
            actualizaListasFolhaExcel("A1")
        elif clock==partidaA2:
            #print ("eventoPartidaA2")
            eventoPartidaA2()
            actualizaListasFolhaExcel("A2")
        elif clock==partidaB1:
            #print ("eventoPartidaB1")
            eventoPartidaB1()
            actualizaListasFolhaExcel("B1")
        elif clock==partidaB2:
            #print ("eventoPartidaB2")
            eventoPartidaB2()
            actualizaListasFolhaExcel("B2")
        elif clock==partidaC:
            #print ("eventoPartidaC")
            eventoPartidaC()
            actualizaListasFolhaExcel("C")
        elif clock==partidaT:
            #print ("eventoPartidaT")
            eventoPartidaT()
            actualizaListasFolhaExcel("T")

    printEstatisticas()

    df = DataFrame({'Clock': clockLST, 'TipoEvento':eventoLST, 'Utente':UtenteLST, 'ProxChegada':proxChegadaLST, 'FilaRF':filaRFLST, 'FilaRFP':filaRFPLST, 'EstadoRF':estadoRFLST, 'PartidaRF':partidaRFLST, 'FilaA':filaALST, 'FilaAP':filaAPLST, 'EstadoA1':estadoA1LST, 'EstadoA2':estadoA2LST, 'PartidaA1':partidaA1LST, 'PartidaA2':partidaA2LST, 'FilaB':filaBLST, 'FilaBP':filaBPLST, 'EstadoB1':estadoB1LST, 'EstadoB2':estadoB2LST, 'PartidaB1':partidaB1LST, 'PartidaB2':partidaB2LST, 'FilaC':filaCLST, 'FilaCP':filaCPLST, 'EstadoC':estadoCLST, 'PartidaC':partidaCLST, 'FilaT':filaTLST, 'FilaTP':filaTPLST, 'EstadoT':estadoTLST, 'PartidaT':partidaTLST})
    df.to_excel('trabalho.xlsx', sheet_name='tabela', index=False, columns=['Clock','TipoEvento','Utente','ProxChegada','FilaRF', 'FilaRFP','EstadoRF','PartidaRF','FilaA','FilaAP','EstadoA1','EstadoA2','PartidaA1','PartidaA2','FilaB','FilaBP','EstadoB1','EstadoB2','PartidaB1','PartidaB2','FilaC','FilaCP','EstadoC','PartidaC','FilaT','FilaTP','EstadoT','PartidaT'])

    printUtentes(Utentes) ##escrever para um ficheiro

    desenharGraficos()

    print("\n\nFicheiros e gráficos criados e escritos com sucesso.")

#inicializar o sistema
main()
