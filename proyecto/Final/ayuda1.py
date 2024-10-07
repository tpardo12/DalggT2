def dp_indiana_marion(R, C, matriz, central_row):
    """
    Calcula el máximo de reliquias que Indiana y Marion pueden recolectar juntos,
    permitiendo que ambos pasen por la misma casilla y sigan recolectando reliquias
    aunque uno de los dos no pueda moverse en algún paso.
    
    :param R: Número de filas de la matriz.
    :param C: Número de columnas de la matriz.
    :param matriz: Matriz de reliquias y maldiciones.
    :param central_row: Índice de la fila central.
    :return: La cantidad máxima de reliquias recolectadas por Indiana y Marion.
    """
    steps = central_row
    # Inicializar DP
    dp_prev = [[-1 for _ in range(C)] for _ in range(C)]
    
    # Condición inicial: ambos empiezan en las esquinas
    if matriz[0][0] != -1 and matriz[0][C-1] != -1:
        dp_prev[0][C-1] = matriz[0][0] + matriz[0][C-1]
    else:
        return -1  # Al menos uno de los personajes no puede comenzar

    # Recorrer cada fila hasta la fila central
    for s in range(1, steps + 1):
        dp_next = [[-1 for _ in range(C)] for _ in range(C)]
        row = s
        
        # Para cada combinación de posiciones previas
        for ci_prev in range(C):
            for cm_prev in range(C):
                if dp_prev[ci_prev][cm_prev] == -1:
                    continue
                
                # Movimientos posibles de Indiana
                for di in [-1, 0, 1]:
                    ci_new = ci_prev + di
                    if not (0 <= ci_new < C) or matriz[row][ci_new] == -1:
                        continue
                    
                    # Movimientos posibles de Marion
                    for dm in [-1, 0, 1]:
                        cm_new = cm_prev + dm
                        if not (0 <= cm_new < C) or matriz[row][cm_new] == -1:
                            continue
                        
                        # Recolectar reliquias si ambos están en la misma celda
                        if ci_new == cm_new:
                            total = dp_prev[ci_prev][cm_prev] + matriz[row][ci_new]
                        else:
                            total = dp_prev[ci_prev][cm_prev] + matriz[row][ci_new] + matriz[row][cm_new]
                        
                        # Actualizar el DP con el valor máximo
                        if total > dp_next[ci_new][cm_new]:
                            dp_next[ci_new][cm_new] = total
        
        # Actualizamos la fila previa a la siguiente
        dp_prev = dp_next

    # Obtener el máximo de reliquias recolectadas por Indiana y Marion
    max_relics = -1
    for ci in range(C):
        for cm in range(C):
            if dp_prev[ci][cm] > max_relics:
                max_relics = dp_prev[ci][cm]
    
    return max_relics

matriz = [[0, 9, 1, 10, 0,],
[-1, -1, 5, -1, 5],
[1, 5, 1, 5, 7],
[5, 5, 5, 15, 2],
[55, 3, 0, 4, 1]
]
print(dp_indiana_marion(5,5, matriz, 3))