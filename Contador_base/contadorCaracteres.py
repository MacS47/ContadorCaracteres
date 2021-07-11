#
#           Autor: Alexsandre Macaulay (MS47)
#           Data: 28/05/2021
#           Versão: 0.0.1
#
#-------------------------------------------------------------------------------------------
#
# 1ª - Etapa
# Consiste em informar ao usuário o que o programa deseja receber (palavra, frase ou texto)
# 

print("\nEsse programa tem por objetivo realizar uma contagem do número de caracteres utlizados em uma palavra, frase ou texto.")
print("Essa é a primeira versão do programa\n")

entrada = input("Palavra | Frase | Texto: ")

print(f"\n{entrada}")


#-------------------------------------------------------------------------------------------
#
# 2ª - Etapa
# Realizar a contagem do número de caracteres
# 

indice = 0
numeroCaracteres = 0

for x in entrada:
    numeroCaracteres += 1

print(f"\nA sua frase possui {numeroCaracteres} de carcacteres.")

#-------------------------------------------------------------------------------------------
#
# 3ª - Etapa
# 
# 

