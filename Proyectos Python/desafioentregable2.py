texto = input("Ingrese un texto: ")
letras = input("Ingrese tres letras: ")
letras = letras.lower()
cantidad_letras = [texto.lower().count(letra) for letra in letras]
palabras = texto.split()
print("Cantidad de palabras:", len(palabras))
primera_letra = texto[0]
ultima_letra = texto[-1]
print("Primera letra:", primera_letra)
print("Última letra:", ultima_letra)
print("Cantidad de veces que aparece cada letra:")
for i in range(len(letras)):


        

    print(letras[i], cantidad_letras[i])
  
   
    texto_inverso = texto[::-1]
    print("Texto en orden inverso:", texto_inverso)
    python_aparece = "python" in texto.lower()
    print("¿Python aparece en el texto?", "Sí" if python_aparece else "No")




