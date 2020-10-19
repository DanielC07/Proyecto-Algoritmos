import json
import random
from datetime import date
import datetime
import win32com.client
import os

qinfo = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')
qinfo.FormatName = "direct=os:"+computer_name+"\\private$\\ALACOLAPP"
queue = qinfo.Open(2,0)   # Open a ref to queue
msg = win32com.client.Dispatch("MSMQ.MSMQMessage")

fecha = datetime.datetime.now()
d = int(fecha.day)
m = int(fecha.month)
y = int(fecha.year)
fecha = str(d)+"/"+"/"+str(m)+"/"+str(y)
dato = ""

def generador(dato):
    print("""1. CAJA
2. SAC
""")
    opi = int(input("Ingresa una opcion disponible: "))
    if opi == 1:
        num_tick = int(random.randrange(0,1000))
        cero = ""
        dato = "CAJ-" +str(y)+str(m)+str(d)+str(num_tick)
        tamaño = len(dato)
        if(tamaño<16):
            ceros = 16-tamaño
            for i in range(ceros):
                cero += "0"
        dato = "CAJ-" +str(y)+str(m)+str(d)+cero+str(num_tick)
    elif opi == 2:
        num_tick = int(random.randrange(0,1000))
        cero = ""
        dato = "SAC-" +str(y)+str(m)+str(d)+str(num_tick)
        tamaño = len(dato)
        if(tamaño<16):
            ceros = 16-tamaño
            for i in range(ceros):
                cero += "0"
        dato = "SAC-" +str(y)+str(m)+str(d)+cero+str(num_tick)
    else:
        print("Opción no disponible")
    return dato
ini = True
while ini:
    print("""1. Generador de Tickets
2. Llamada Cliente
3. Salir
""")
    op = int(input("Ingresa una opcion disponible: "))
    if op == 1:
        generador(dato)
    elif op == 3:
        ini = False
    else:
        print("Opcion no disponible")
j = generador(dato)
class Base:
    def __init__(self):
        self.generador = j
        self.operacion = j[0:3]
        self.date = fecha
        self.agente = "null"

ticket = Base()


print(ticket.generador+"\n"+ticket.operacion+"\n"+ticket.date+"\n"+ticket.agente)

#serializar = json.dumps(ticket)
#msg.Label = "El Pepe - Ete Sech"
#msg.Body = serializar
#msg.send(queue)
#queue.close()