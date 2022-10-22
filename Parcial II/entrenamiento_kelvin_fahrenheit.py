
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#obtencion de los datos de entrenamiento
kelvin_k = pd.read_csv("temperaturak.csv", sep=";")
#print(kelvin_k)

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
f= modelo_k_f.predict([900])
print("Conversion de kelvin a Farehrenheit: ",f)


