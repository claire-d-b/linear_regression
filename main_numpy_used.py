import numpy as np
import matplotlib.pyplot as plt

# Données
km = np.array([240000, 139800, 150500, 185530, 176000, 114800, 166800, 89000,
               144500, 84000, 82029, 63060, 74000, 97500, 67000, 76025,
               48235, 93000, 60949, 65674, 54000, 68500, 22899, 61789])
price = np.array([3650, 3800, 4400, 4450, 5250, 5350, 5800, 5990,
                  5999, 6200, 6390, 6390, 6600, 6800, 6800, 6900,
                  6900, 6990, 7490, 7555, 7990, 7990, 7990, 8290])

# Calcul de la droite de régression
a, b = np.polyfit(km, price, 1)
print("a", a)
print("b", b)
# Tracer
plt.scatter(km, price, color='blue', label='Données')
plt.plot(km, a*km + b, color='red', label='Droite de régression')
plt.xlabel('Kilomètres')
plt.ylabel('Prix')
plt.title('Relation entre km et prix')
plt.legend()
plt.grid()
plt.show()
