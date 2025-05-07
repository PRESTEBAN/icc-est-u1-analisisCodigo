import matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y,label="Linea1", color="blue")

#agregar_parametros

plt.title("primer grafico")
plt.xlabel("Datos eje X")
plt.ylabel("Datos eje Y")
plt.legend()
plt.show()

