#
#           Autor: Alexsandre Macaulay (MS47)
#           Data: 28/05/2021
#           Versão: 0.0.1
#
#           Versão do Programa
#  Para determinar a versão vou me atentar às seguintes
#  regras: ano, mes, dia, data desde a última alteração
#
#-------------------------------------------------------------------------------------------
#
# Área de Importação de pacotes
#  

import funcoes as f


#-------------------------------------------------------------------------------------------
#
# 1ª Etapa - Entrada de dados
#
# Consiste em informar ao usuário o que o se deseja receber (palavra, frase ou texto)
# 

print("\nEsse programa tem por objetivo realizar uma contagem do número de caracteres utlizados em uma palavra, frase ou texto.")
print("Essa é a primeira versão do programa\n")

userText = input("Palavra | Frase | Texto: ")

print(f"\n{userText}")


#-------------------------------------------------------------------------------------------
#
# 2ª Etapa - Processamento dos dados
#
# Realizar a contagem do número de caracteres, com ou sem a utilização do espaço
# Esse espaço também é destinado para chamada de outras funções ou qualquer chamada
# que envolva o processamento da informação.
# 


caracterNumbers = f.count_all(userText)

statistic = f.count_wtt_spc(userText)

#-------------------------------------------------------------------------------------------
#
# 3ª Etapa - Saída de dados
#
# Exibir os dados obtidos na 2ª Etapa, onde foi realizado o processamento.
# 

print(f"\nA sua frase possui {caracterNumbers} carcacteres.")
print(f"Sendo {statistic[0]} letras, sinais de pontuação ou caracteres especiais")
print(f"e {statistic[1]} espaços.\n")
