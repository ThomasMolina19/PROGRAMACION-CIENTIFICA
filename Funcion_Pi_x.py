import math
import pandas as pd
import matplotlib.pyplot as plt


Lista_primos= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]
List_pix=[]
List_aprox=[]
# Convert it into a pandas DataFrame or Series
df = pd.Series(Lista_primos)

# Show all rows without truncation
pd.set_option('display.max_rows', None)  # Set this to None to show all rows

for indice in range(len(Lista_primos)):
    for numero in range(2,1001): #Este for va a recorrer cada número al cual se le quiere aplicar la función Pi(x)

        while True:
            if (numero < Lista_primos[indice]):
                pi_x = indice
                List_pix.append(pi_x)
                List_aprox.append(numero/math.log(numero))
                break
            else:
                indice+=1
    break #Para no volver a iterar sobre la lista de primeros y haber tenido un solo for

# Create a DataFrame for easy manipulation and visualization
data = {
    'x': range(2, 1001),
    'pi(x)': List_pix,  # True pi(x)
    'pi(x) Approx': List_aprox  # Approximate pi(x)
}

df = pd.DataFrame(data)
print(df.to_string(index=False))

# # Plot the results using matplotlib
# plt.figure(figsize=(10, 6))

# # Plot the true pi(x)
# plt.plot(df['x'], df['pi(x)'], label='π(x) (True)', color='blue', linewidth=2)

# # Plot the approximate pi(x)
# plt.plot(df['x'], df['pi(x) Approx'], label='π(x) Approx (x / log(x))', color='red', linestyle='dashed', linewidth=2)

# # Customize the plot
# plt.title('Prime Counting Function π(x) and its Approximation')
# plt.xlabel('x')
# plt.ylabel('π(x)')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()

# # Show the plot
# plt.show()

