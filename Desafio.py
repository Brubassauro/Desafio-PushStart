
                                                             ## Desafio PushStart ##


# =================================================================================================================================== #
                                  
import numpy as np

# =================================================================================================================================== #
# Faz o input para o arquivo de entrada e passa para as variáveis do programa.

def Entrada():

    # Pergunta o arquivo de entrada
    print('Entre com o nome do arquivo:')
    nome=input()
    print()
    try: txt=open(nome,'r')
    except:
        print('Arquivo não encontrado!')
        print()
        return Entrada()
        
    cont=0 # Contador
    peças=[] # Lista de peças do jogo

    # Lê o arquivo txt
    for line in txt:
        
        # Lê as dimensões de entrada e verifica a validade
        if cont==0:
            dim = line.split('x') # Dimensoes da matriz
            try:
                for i in range(2): dim[i]=int(dim[i])
            except:
                print('Entrada para as dimensões da matriz inválida!')
                print()
                return Entrada()
            cont+=1
            
        elif cont==1: cont+=1 # Pula linha
        
        # Lê as peças de entrada e verifica a validade
        elif line!='\n':
            try:
                line=line.split(' ')
                line[1]=line[1].split('x')
                peças+=[[int(line[0]),int(line[1][0]),int(line[1][1])]]
            except:
                print('Entrada para as peças inválida!')
                print()
                return Entrada()
            
    # Checa a entrada com a função ChecaEntrada
    # Retorna dim (dimsões da matriz) e peças (peças do jogo)
    if ChecaEntrada(dim,peças)=='y': return dim,peças
    return Entrada()

# =================================================================================================================================== #
# Verifica se a área da matriz é a mesma área da soma das peças
# Verifica se alguma peça possui uma dimensão inválida

def ChecaEntrada(dim,peças):

    # Verifica se alguma peça possui uma das dimensões maior que a matriz
    for i in range(len(peças)):
        if peças[i][1]>dim[0] or peças[i][2]>dim[1]:
            print('Entrada inválida!')
            print('Uma das peças possui dimensão inválida!')
            print()
            return 'n'
        
    # Verifica se a área da matriz é igual a área da soma das peças
    Amatriz=dim[0]*dim[1] # Area da matriz
    Apeças=0 # Area somada das peças
    for i in range(len(peças)): Apeças+=peças[i][0]*peças[i][1]*peças[i][2]
    if Amatriz==Apeças: return 'y'
    
    print('Entrada inválida!')
    if Amatriz>Apeças: print('A matriz possui espaço maior que conjunto de peças.')
    else: print('O conjunto de peças possui espaço maior que a matriz.')
    print()
    return 'n'

# =================================================================================================================================== #
# Verifica se existe espaço para colocar a peça na posição x,y da matriz (x,y sendo o canto superior esquerdo da peça)

def Disponibilidade(x,y,peça,matriz):

    # Verifica se a peça cabe no espaço da matriz
    if x+peça[1]>len(matriz[0]): return 'n'
    if y+peça[2]>len(matriz):return 'n'

    # Verifica se todos espaços necessários não foram preenchidos
    for i in range(peça[1]):
        for j in range(peça[2]):
            if matriz[y+j][x+i]!=0: return 'n'

    return 'y'

# =================================================================================================================================== #
# Printa a matriz 

def PrintaMatriz(Matriz):
    
    for i in range(len(Matriz)):
        linha='  '
        for j in range(len(Matriz[0])):
            linha+=str(Matriz[i][j])
            if len(str(Matriz[i][j]))<=2: linha+=' '*(3-len(str(Matriz[i][j])))
            else:linha+='  '
        print(linha)
    print()

# =================================================================================================================================== #
# Coloca a peça na posição x,y da matriz (x,y sendo o canto superior esquerdo da peça)

def ColocaPeça(x,y,n,Peça,matriz):

    for i in range(Peça[1]):
        for j in range(Peça[2]):
            matriz[j+y][i+x]=n

    return matriz

# =================================================================================================================================== #
# Copia dada lista ou matriz

def Copia(matriz):

    # Copia para o caso de matriz
    if type(matriz[0])==list:
        nova=[[0]*len(matriz[0]) for i in range(len(matriz))]
        for i in range(len(matriz)):
            for j in range(len(matriz[0])): nova[i][j]=matriz[i][j]

    # Copia para o caso de lista
    else:
        nova=[0 for i in range(len(matriz))]
        for i in range(len(matriz)): nova[i]=matriz[i] 

    return nova

# =================================================================================================================================== #
# Inicializa o programa e chama as funções Entrada, Encaixe e Retorna

def Main():

    # Chama a função de entrada
    dim,peças=Entrada()

    # Salva as variáveis do arquivo de entrada
    Dim=Copia(dim)
    Peças=Copia(peças)
    
    # Reseta a contagem de tentativas
    global Contagem
    Contagem=0

    # Executa o algoritmo de encaixe das peças
    Encaixe(dim,peças)
    
    # Menu de execução
    Retorna(Dim,Peças)
    
# =================================================================================================================================== #
# Função para um menu de execução que permite:
# 1- Executar novamente o algoritmo para a mesma entrada
# 2- Executar novamente o algoritmo para um novo arquivo de entrada
# 3- Sair: Fecha o programa

def Retorna(dim,peças):

    # Reseta a contagem de tentativas
    global Contagem
    Contagem=0
    
    # Salva as variáveis do arquivo de entrada
    Dim=Copia(dim)
    Peças=Copia(peças)

    # Prints do menu
    print('Digite o número da alternativa de interesse:')
    print('1- Tentar novamente com o mesmo arquivo')
    print('2- Tentar novamente com outro arquivo')
    print('3- Sair')

    # Caixa de resposta
    resp=input()
    print()

    # Repete a mesma entrada
    if resp=='1':
      Encaixe(dim,peças)
      Retorna(Dim,Peças)

    # Chama a Main para um novo arquivo de entrada
    elif resp=='2': Main()
    
    # Fecha o programa
    elif resp=='3': return

    # Mensagem de erro para resposta inválida
    else:
      ('Resposta inválida!')
      print()
      Retorna(Dim,Peças)

# =================================================================================================================================== #
# Função para gerar uma afirmação aleatória do desafio

def Afirmação(matriz):
    
    # Gera aleatoriamente uma direção
    # 0 para cima, 1 para baixo, 2 para esquerda, 3 para direita 
    if len(matriz[0])>=2 and len(matriz)>=2: direção=int(np.random.rand(1)[0]*4)
    elif len(matriz)==1: direção=int(2+np.random.rand(1)[0]*2)
    elif len(matriz[0])==1: direção=int(np.random.rand(1)[0]*2)
    
    # Escolhe uma posição aleatória baseada na direção escolhida
    if direção==0: # Para cima
        x=int(np.random.rand(1)[0]*(len(matriz[0])))
        y=1+int(np.random.rand(1)[0]*(len(matriz)-1))
        if matriz[y][x]!=matriz[y-1][x]: print('A peça de ID %s está acima da peça de ID %s' %(matriz[y-1][x],matriz[y][x]))
        else: Afirmação(matriz)
        
    elif direção==1: # Para baixo
        x=int(np.random.rand(1)[0]*(len(matriz[0])))
        y=int(np.random.rand(1)[0]*(len(matriz)-1))
        if matriz[y][x]!=matriz[y+1][x]: print('A peça de ID %s está abaixo da peça de ID %s' %(matriz[y+1][x],matriz[y][x]))
        else: Afirmação(matriz)
        
    elif direção==2: # Para esquerda
        x=1+int(np.random.rand(1)[0]*(len(matriz[0])-1))
        y=int(np.random.rand(1)[0]*(len(matriz)))
        if matriz[y][x]!=matriz[y][x-1]: print('A peça de ID %s está a esquerda da peça de ID %s' %(matriz[y][x-1],matriz[y][x]))
        else: Afirmação(matriz)
        
    elif direção==3: # Para direita
        x=int(np.random.rand(1)[0]*(len(matriz[0])-1))
        y=int(np.random.rand(1)[0]*(len(matriz)))
        if matriz[y][x]!=matriz[y][x+1]: print('A peça de ID %s está a direita da peça de ID %s' %(matriz[y][x+1],matriz[y][x]))
        else: Afirmação(matriz)

    return
# =================================================================================================================================== #
# Algoritmo de encaixe das peças

def Encaixe(dim,peças):
    
    # Contagem do número de tentativas
    # Caso o programa tente encaixar as peças 1000 vezes sem sucesso retorna que não foi encontrada solução
    global Contagem
    Contagem+=1
    
    # Salva as peças de entrada
    Peças=Copia(peças)

    # Cria matriz de 0 nas dimensões de entrada
    matriz=[[0]*dim[0] for i in range(dim[1])]

    # Laço while para colocar todas as peças
    while peças!=[0]*len(Peças) and Contagem<=1000:

        # Seleciona uma das peças remanescentes aleatoriamente
        Chave=0
        while Chave==0:
            peça=int(np.random.rand(1)[0]*len(peças))
            if peças[peça]!=0: Chave=1

        # Percorre a matriz procurando disponibilidade para colocar a peça
        for i in range(dim[1]):
            if Chave==0:break
            for j in range(dim[0]):           
                if Disponibilidade(j,i,peças[peça],matriz)=='y': # Checa disponibilidade
                    matriz=ColocaPeça(j,i,peça+1,peças[peça],matriz) # Coloca a peça
                    # Subtrai a peça da lista de peças
                    peças[peça][0]-=1 
                    if peças[peça][0]==0: peças[peça]=0
                    Chave=0
                    break
                
        # Caso não tenha encontrado espaço pra uma peça começa de novo do 0
        if Chave==1:
            Encaixe(dim,Peças)
            return

    # Caso foi encontrada solução retorna a solução
    if Contagem<=1000:
        print('Solução aleatória:')
        print()
        PrintaMatriz(matriz)
        
        # Chama as afirmações do desafio
        Afirmação(matriz)
        Afirmação(matriz)
        Afirmação(matriz)

        print()
    
    # Caso tenha excedido 1000 tentativas retorna que não foi encontrada solução
    else:
        print('Não foi encontrada solução para o problema!')
        print()
                
# =================================================================================================================================== #

Main()
        
