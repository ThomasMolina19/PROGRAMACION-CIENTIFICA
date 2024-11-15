import math
import pandas as pd

# Este algoritmo recrea el Teorema de los Números Primos al seleccionar cada número natural entre 0 y 1000,
# calculando la cantidad de números primos que existen hasta ese número. Luego, compara este conteo con 
# la aproximación asintótica del teorema de los números primos, dada por x/ln(x).
# Los resultados se muestran en columnas que contienen respectivamente:
# - El número natural.
# - La cantidad de números primos menores o iguales a él.
# - La estimación del teorema.
# - El error relativo entre el conteo real y la estimación.
# Finalmente, el algoritmo imprime estos valores para todos los números de 0 a 1000.

#Lista de primos entre 0 y 1009
Lista_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]


List_pix=[0,0] #Lista que almacena la cantidad de números primos que hay antes de cada número x natural entre 0 y 1000. 

List_aprox=[0,0] #Lista que almacena la cantidad de números primos que hay antes de cada número x natural usando entre 0 y 1000, usando la aproximación del teorema de números primos. 

List_Error = [0,0] #Lista que almacena el error relativo en porcentaje entre el conteo real y la estimación.

# Convierte la lista 'Lista_primos' en una estructura de datos tipo Series de pandas.
df = pd.Series(Lista_primos)

# Muestra todas las filas sin truncamiento
pd.set_option('display.max_rows', None)  # Declarlo en None para que muestre todas las filas


# indice = 0 Se va a usar como el contador de primos antes de un número X, el cual se va ir actualizando a medida que se vaya iterando sobre los numero de 1 a mil
indice = 0  

# Iteramos sobre cada número en el rango de 2 a 1000, que serán los valores de x en la función Pi(x).
for numero in range(2, 1001):  
    while True:
        # Verificamos si el número actual es menor que el número primo en la posición `indice`.
        # Si es así, significa que `indice` representa el conteo de números primos menores o iguales a `numero`.
        if numero < Lista_primos[indice]:
            pi_x = indice  # Asignamos el conteo actual de primos a pi(x) para este número.
            
            # Guardamos el conteo real de números primos en List_pix.
            List_pix.append(pi_x)
            
            # Calculamos y guardamos la aproximación de pi(x) usando la fórmula del teorema de los números primos.
            List_aprox.append(numero / math.log(numero))
            
            # Calculamos el error relativo entre el conteo real y la aproximación asintótica,
            # usando el valor absoluto de la diferencia dividido por el conteo real.
            List_Error.append(100 * abs(pi_x - (numero / math.log(numero))) / pi_x)
            
            # Salimos del bucle `while` ya que hemos terminado con el número actual.
            break
        else:
            # Si el número es mayor o igual al primo en `Lista_primos[indice]`,
            # incrementamos el índice para verificar el siguiente primo.
            indice += 1


# Crea un diccionario con los datos calculados para generar un DataFrame en pandas.
# Las claves representan los nombres de las columnas y cada lista asociada a ellas contiene los valores calculados.
data = {
    'x': range(0, 1001),           # Columna 'x' que contiene cada número natural entre 0 y 1000.
    'pi(x)': List_pix,             # Columna 'pi(x)' con los valores reales de la función pi(x), es decir, la cantidad de primos hasta x.
    'pi(x) Approx': List_aprox,    # Columna 'pi(x) Approx' con la aproximación de pi(x) según el teorema de los números primos (x/ln(x)).
    'Error relativo': List_Error   # Columna 'Error relativo' que contiene el error relativo entre el valor real y la aproximación.
}


# Convierte el diccionario 'data' en un DataFrame de pandas
df = pd.DataFrame(data)

# Redondea las columnas 'pi(x) Approx' y 'Error relativo' a dos cifras decimales.
df['pi(x) Approx'] = df['pi(x) Approx'].round(2)
df['Error relativo'] = df['Error relativo'].round(2)

# Imprime el DataFrame como una cadena de texto, mostrando todos los valores sin incluir los índices de las filas.
# La opción `index=False` asegura que no se muestre la columna del índice, que generalmente es innecesaria para este tipo de salida.
print(df.to_string(index=False))

