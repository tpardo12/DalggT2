import sys

def max_reliquias(R, C, matriz):
    central_row = R // 2
    if R == 1:
        return 0

    def dp_indiana_marion(R, C, matriz, central_row):
        """
        Calcula el máximo de reliquias que Indiana y Marion pueden recolectar juntos
        sin compartir ninguna celda en su camino hacia la fila central.
        
        :param R: Número de filas de la matriz.
        :param C: Número de columnas de la matriz.
        :param matriz: Matriz de reliquias y maldiciones.
        :param central_row: Índice de la fila central.
        :return: La cantidad máxima de reliquias recolectadas por Indiana y Marion.
        """
        steps = central_row
        # Inicializar DP
        dp_prev = [[-1 for _ in range(C)] for _ in range(C)]
        if matriz[0][0] != -1 and matriz[0][C-1] != -1 and 0 != (C-1):
            dp_prev[0][C-1] = matriz[0][0] + matriz[0][C-1]
        else:
            return -1  # Al menos uno de los personajes no puede comenzar
        no_sigue_I=False
        no_sigue_M=False
        for s in range(1, steps + 1):
            dp_next = [[-1 for _ in range(C)] for _ in range(C)]
            row = s
            
            
            for ci_prev in range(C):
                
                
                for cm_prev in range(C):
                    conteoI=0
                    
                    if dp_prev[ci_prev][cm_prev] == -1:
                        continue
                    for di in [-1, 0, 1]:
                        conteoM=0
                        ci_new = ci_prev + di
                        if not (0 <= ci_new < C):
                            conteoI+=1
                            if conteoI==3:
                                no_sigue_I=True
                            continue
                        if matriz[row][ci_new] == -1:
                            conteoI+=1
                            if conteoI==3:
                                no_sigue_I=True
                        for dm in [-1, 0, 1]:
                            cm_new = cm_prev + dm
                            if not (0 <= cm_new < C):
                                conteoM+=1
                                if conteoM==3:
                                    no_sigue_M=True
                                continue
                            if matriz[row][cm_new] == -1:
                                conteoM+=1
                                if conteoM==3:
                                    no_sigue_M=True
                            if ci_new == cm_new:
                                continue  # Evitar que Indiana y Marion estén en la misma celda
                            total=-1
                            if not(no_sigue_I) and not(no_sigue_M)and(matriz[row][ci_new] != -1 and matriz[row][cm_new] != -1) :
                                total = dp_prev[ci_prev][cm_prev] + matriz[row][ci_new] + matriz[row][cm_new]
                            elif no_sigue_I and matriz[row][cm_new] != -1:
                                total = dp_prev[ci_prev][cm_prev] + matriz[row][cm_new]
                            elif no_sigue_M and matriz[row][ci_new] != -1:
                                total = dp_prev[ci_prev][cm_prev] + matriz[row][ci_new]
                            elif matriz[row][ci_new] == -1 or matriz[row][cm_new] == -1:
                                continue
                            if total > dp_next[ci_new][cm_new]:
                                dp_next[ci_new][cm_new] = total
            dp_prev = dp_next

        # Obtener el máximo relics recolectados por Indiana y Marion
        max_relics = -1
        ubicacion=None
        for ci in range(C):
            for cm in range(C):
                if ci != cm and dp_prev[ci][cm] > max_relics:
                    max_relics = dp_prev[ci][cm]
                    ubicacion = (ci, cm)
        return max_relics, ubicacion, dp_prev

    def dp_sallah(R, C, matriz, central_row):
        """
        Calcula el máximo de reliquias que Sallah puede recolectar al llegar a la fila central.
        
        :param R: Número de filas de la matriz.
        :param C: Número de columnas de la matriz.
        :param matriz: Matriz de reliquias y maldiciones.
        :param central_row: Índice de la fila central.
        :return: La cantidad máxima de reliquias recolectadas por Sallah.
        """
        steps = R - 1 - central_row
        # Inicializar DP
        dp_prev = [-1 for _ in range(C)]
        start_col = C // 2
        if matriz[R-1][start_col] != -1:
            dp_prev[start_col] = matriz[R-1][start_col]
        else:
            return -1  # Sallah no puede comenzar

        for s in range(1, steps + 1):
            dp_next = [-1 for _ in range(C)]
            row = R - 1 - s
            for c_prev in range(C):
                if dp_prev[c_prev] == -1:
                    continue
                for dc in [-1, 0, 1]:
                    c_new = c_prev + dc
                    if not (0 <= c_new < C):
                        continue
                    if matriz[row][c_new] == -1:
                        continue
                    total = dp_prev[c_prev] + matriz[row][c_new]
                    if total > dp_next[c_new]:
                        dp_next[c_new] = total
            dp_prev = dp_next

        # Obtener el máximo relics recolectados por Sallah
        max_relics = max(dp_prev)
        max_relics = max_relics if max_relics != -1 else -1
        ubicacion = dp_prev.index(max_relics)
        return max_relics,ubicacion, dp_prev

    # Calcular reliquias de Indiana y Marion
    relics_im, ubicacion_im, dp_im = dp_indiana_marion(R, C, matriz, central_row)
    if relics_im == -1:
        relics_im = 0  # Si Indiana o Marion no pueden llegar

    # Calcular reliquias de Sallah
    relics_s, ubicacion_s, dp_s = dp_sallah(R, C, matriz, central_row)
    if relics_s == -1:
        relics_s = 0  # Si Sallah no puede llegar

    #Calcular mayor suma de reliquias en caso de que se cuzen
    total_relics = relics_im + relics_s
    if ubicacion_im is not None and ubicacion_s is not None:
        if ubicacion_s in ubicacion_im:
            mayor = 0
            for i in range(C):
                for s in range(C):
                    for m in range(C):
                        if dp_im[i][m] + dp_s[s] > mayor and i!=s and m!=s:
                            mayor = dp_im[i][m] + dp_s[s]
            total_relics = mayor
    # Sumar las reliquias de Indiana, Marion y Sallah
    

    return total_relics if total_relics > 0 else -1

# matriz =[[0,9,1,10,0],
# [-1,5,5,25,5],
# [1,5,1,5,7],
# [5,5,5,15,2],
# [55,3,0,4,1]]

# print(max_reliquias(5,5,matriz))

# matriz =[[0,9,1,10,0],
# [-1,-1,5,-1,5],
# [1,5,1,5,7],
# [5,5,5,15,2],
# [55,3,0,4,1]]

# print(max_reliquias(5,5,matriz))

# matriz = [
#     [0, 7, 2, -1, 0],
#     [2, 1, 9, -1, 4],
#     [9, 2, 1, 4, -1],
#     [3, 5, 6, 7, 8],
#     [-1, 1, 2, 3, 4],
#     [5, 8, 7, -1, 6],
#     [6, 9, 3, 2, 1],
#     [9, 4, 5, 8, 2],
#     [8, 3, 2, 1, -1],
#     [7, 4, -1, 5, 8],
#     [5, 6, 4, 9, 1],
#     [-1, 3, 2, 8, 7],
#     [1, 9, 0, 6, 2]
# ]

# print(max_reliquias(13, 5, matriz))

#Main function to handle input and output from command line arguments
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python archivo.py input.txt output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f:
        num_cases = int(f.readline().strip())
        results = []
        for i in range(num_cases):
            R, C = map(int, f.readline().strip().split())
            matriz = [list(map(int, f.readline().strip().split())) for _ in range(R)]
            result = max_reliquias(R, C, matriz)
            results.append(result)
    
    with open(output_file, 'w') as f:
        for result in results:
            f.write(f"{result}\n")
