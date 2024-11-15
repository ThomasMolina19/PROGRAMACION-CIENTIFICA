while True:
                if (numero < Lista_primos[indice]):
                    pi_x= indice
                    List_pix.append(pi_x)
                    List_aprox.append(numero/math.log(numero))
                    List_Error.append(f'{100*abs(pi_x - (numero/math.log(numero)) ) / pi_x}' )
                    break
                else:
                    indice+=1
            return List_pix,List_aprox,List_Error#Lista que almacena la cantidad de números primos al aplicarle la función Pi(x) 