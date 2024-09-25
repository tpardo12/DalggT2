from math import inf
from scipy.optimize import linear_sum_assignment  # Solo necesitamos esta parte de scipy


def maximo(m):
    #Personajes de arriba
    largo_fila=len(m[0])
    ancho=len(m[0])
    valor=0
    m2=[[0 for _ in range(largo_fila)] for _ in range(len(m))]
    m3=[[0 for _ in range(largo_fila)] for _ in range(len(m)//2+1)]
    A=[0 for _ in range(largo_fila)]
    B=[0 for _ in range(largo_fila)]
    for i in range(0,len(m)//2+1):
        r=len(m[0])
        if valor+1<=ancho:
            valor= valor+1
        for a in range(valor):
            if m[i][a]!=-1:
                if i !=0:
                    if a!=(len(m)//2) and i!=len(m)//2:
                        if a!=(len(m)+valor) and a!=(0):
                            m2[i][a]=max(m2[i-1][a]+m[i][a], m2[i-1][a-1]+m[i][a], m2[i+1][a+1]+m[i][a])
                        elif a==0:
                            m2[i][a]=max(m2[i-1][a]+m[i][a], m2[i-1][a+1]+m[i][a])
                        elif a==(len(m)+valor):
                            m2[i][a]=max(m2[i-1][a]+m[i][a], m2[i-1][a-1]+m[i][a])
                    else:
                        if a!=(len(m)+valor) and a!=(0):
                            A[a]=max(m2[i-1][a]+m[i][a], m2[i-1][a-1]+m[i][a], m2[i+1][a+1]+m[i][a])
                        elif a==0:
                            A[a]=max(m2[i-1][a]+m[i][a], m2[i-1][a+1]+m[i][a])
                        elif a==(len(m)+valor):
                            A[a]=max(m2[i-1][a]+m[i][a], m2[i-1][a-1]+m[i][a])

            else:
                m2[i][a]=-inf
    valor=0
    for i in range(0, len(m)//2+1):
        if valor+1<=len(m[0]):
            valor= valor+1
        if i !=0:
            
            for b in range (largo_fila-1, largo_fila-valor-1, -1):
                    r=len(m[0])
                    if m[i][b]!=-1:
                        if  i!=len(m)//2:
                            if (b!=largo_fila-valor) and b!=(largo_fila-1):
                                m3[i][b]=max(m3[i-1][b]+m[i][b], m3[i-1][b-1]+m[i][b], m3[i+1][b+1]+m[i][b])
                            elif (b==largo_fila-valor):
                                m3[i][b]=max(m3[i-1][b]+m[i][b], m3[i-1][b+1]+m[i][b])
                            elif b==(largo_fila-1):
                                m3[i][b]=max(m3[i-1][b]+m[i][b], m3[i-1][b-1]+m[i][b])
                        else:
                                if b!=b!=(largo_fila-1) and b!=(len(m)-valor):
                                    B[b]=max(m3[i-1][b]+m[i][b], m3[i-1][b-1]+m[i][b], m3[i+1][b+1]+m[i][b])
                                elif b==(len(m)-valor):
                                    B[b]=max(m3[i-1][b]+m[i][b], m3[i-1][b+1]+m[i][b])
                                elif b==b!=(largo_fila-1):
                                    B[b]=max(m3[i-1][b]+m[i][b], m3[i-1][b-1]+m[i][b])
                    elif m[i][b]==-1:
                        m3[i][b]=-inf


    #Personaje de abajo
    valor=-1
    l=len(m[0])//2
    
    for i in range(len(m)-1, len(m)//2-1, -1):
        if valor+1<=len(m[0])//2:
            valor= valor+1
        if i !=len(m)-1:
            medio = l
            for c in range(medio-valor, medio+valor+1):
                if m[i][c]!=-1:
                    if c!=(medio-valor)and c!=(medio+valor):
                        m2[i][c]=max(m2[i+1][c]+m[i][c], m2[i+1][c-1]+m[i][c], m2[i+1][c+1]+m[i][c])
                    elif c==(medio-valor):
                        m2[i][c]=max(m2[i+1][c]+m[i][c], m2[i+1][c+1]+m[i][c])
                    elif c==(medio+valor):
                        m2[i][c]=max(m2[i+1][c]+m[i][c], m2[i+1][c-1]+m[i][c])
                else:
                    m2[i][c]=-inf
    #centro, donde se encuentran los personajes
    
    valores_tomados= None
    
    C=m2[len(m)//2]
    maxc=max(C)
    #find the indices of the maximum value
    indices = [i for i, x in enumerate(C) if x == maxc]

    

    # Construimos la matriz de beneficios como una lista de listas
    tesoros_matrix = [A, B, C]

    # Convertimos la matriz de listas a la forma que espera `linear_sum_assignment`
    # Como queremos maximizar, le pasamos los valores negativos
    neg_tesoros_matrix = [[-x for x in row] for row in tesoros_matrix]

    # Aplicamos el algoritmo de asignación óptima (algoritmo húngaro)
    fila, columna = linear_sum_assignment(neg_tesoros_matrix)

    # Calculamos el máximo de tesoros recogidos
    max_tesoros = sum(tesoros_matrix[fila[i]][columna[i]] for i in range(len(fila)))

    return max_tesoros
    

matriz = [[ 0,  7,  2, -1,  0],
    [ 6,  1,  8,  9,  3],
    [-1,  4,  7,  5,  2],
    [ 2,  1,  9, -1,  4],
    [ 5,  6,  3,  8,  7],
    [ 9,  2,  1,  4, -1],
    [ 8, -1,  3,  6,  5],
    [ 4,  7,  2,  1,  9],
    [ 3,  5,  6,  7,  8],
    [-1,  1,  2,  3,  4],
    [ 5,  8,  7, -1,  6],
    [ 6,  9,  3,  2,  1],
    [ 7,  4, -1,  5,  8],
    [ 2,  1,  6,  7,  3],
    [ 9,  4,  5,  8,  2],
    [ 8,  3,  2,  1, -1],
    [ 4,  6,  9,  5,  7],
    [ 1,  2,  8,  3,  9],
    [ 5,  6,  4,  9,  1],
    [-1,  3,  2,  8,  7],
    [ 1,  9,  0,  6,  2]
]
print(maximo(matriz))