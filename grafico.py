import numpy as np
from matplotlib import pyplot as plt
import csv
import datetime

tiempo=[]
temperatura=[]
with open("temperaturas.csv") as archivo_csv:
    lectura=csv.reader(archivo_csv,delimiter=",")
    for row in lectura:
        datetime=row[0]

        tiempo.append(datetime)
        temperatura.append(int(row[1]))

plt.title("Prueba")
plt.xlabel("Temperatura")
plt.ylabel("Tiempo")
plt.plot(tiempo,temperatura)
plt.savefig("temperatura.png")
plt.show()


print(tiempo, temperatura)
