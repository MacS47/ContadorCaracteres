#-------------------------------------------------------------------------------------------
#
# Funcões utilizadas pelo arquivo principal
# estarão nesse arquivo
# 

#
# Função retorna a quantidade de caracteres em uma string
#

def count_all(text):
    carcaterNumbers = len(text)
    return carcaterNumbers


# 
# Para esse caso, originalmente havia criado o algoritmo abaixo
# isso porque, minha base de conhecimento sempre foi C
# o método abaixo funcionaria em C e funcionaria em Python.
# Porém é muito mais útil utilizar a função len()
#
#
# numeroCaracteres = 0
# 
# for x in entrada:
#     numeroCaracteres += 1



#
# Função retorna a quantidade de caracteres em uma string
#

def count_wtt_spc(text):
    textWttSpc = text.replace(" ", "")      
    caracterNumbers = len(textWttSpc)
    spcNumbers = len(text) - caracterNumbers
    statistic = [caracterNumbers, spcNumbers]
    return statistic