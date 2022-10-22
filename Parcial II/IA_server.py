#IMPORTAR LAS LIBRERIAS 
from urllib import parse
from http.server import BaseHTTPRequestHandler, HTTPServer
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import math
import tensorflow_datasets as tfds
import pandas as pd

#Codigo de entrenamiento de IA
#obtencion de los datos de entrenamiento
Kelvin_k = pd.read_csv("convertido de kelvin a fahrenheit.csv", sep=";")
#print(Kelvin_k)

#datos de entrada y salida
k = kelvin_f ['kelvin']
f = kelvin_f['fahrenheit']

#modelo de entrenamiento
modelo_k_f= tf.keras.Sequential()
modelo_k_f.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compliar modelo
modelo_k_f.compile(optimizer=tf.keras.optimizers.Adam(1),loss='mean_squared_error')

hisotiral_k_f = modelo_k_f.fit(k,f, epochs=525, verbose=0)

#convertir de metros a yardas
f= modelo_k_f.predict([10])
print("Conversion de kelvin a Farehrenheit: ",f)

#servidor en Python
class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Peticion recibida por GET")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hola Mundo, GRUPO 10".encode())

    def do_POST(self):
        print("Peticion recibida por POST")
        #obtenemos los datos enviados por AJAX => Asincrono JavaScript y XML
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode('utf-8')
        print(data)

        prediccion = modelo_k_f.predict([data])
        print("Predicción:", prediccion)
        
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(str(prediccion[0][0]).encode())
 
       
print("Iniciando el servidor de Python")
servidor = HTTPServer(("localhost", 3010), servidorBasico)
servidor.serve_forever()