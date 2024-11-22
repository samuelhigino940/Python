def somaLista(valores=[]):
    """
    A função somaLista,recebe uma lista de números e faz a soma de todos os números
    da Lista e retorna o resultado da somaLista

    parameters
    -------------------
    valores: int[]
    Lista de números para a Lista

    Returns
    -------------------
    Retorna a soma de uma Lista
    """
    [1,3,52,78,15]
    resultado=0
    for i in valores:
        resultado+=i

    return resultado

def maiorValor(lista=[]):
    """
    A função maiorValor encontra o maior valor
    em uma lista númerica.
    
    Parameters
    ------------
         lista: int[]

    returns
    ------------
    Retorna o maior valor da lista
    """
    m=lista[0]
    for i in lista:
        if i>m:
            m=i
    return m

def inverter(palavra=""):
    #Vamos utilizar o comando 
    #len(length-comprimento) para obter
    #a quantidade de caracteres da palavra
    qtd=len(palavra)
    invertida=""
    for i in range(qtd-1,-1,-1):
        invertida+=palavra[i]
    return invertida

def palindromo(palavra=""):
    org=inverter(palavra).lower()
    if palavra.lower()==org:
        return"É um palindromo"
    else:
        return "Não é um palindromo"
