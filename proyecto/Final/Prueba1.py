def max_reliquias(R, C, matriz):
    central_row = R // 2

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

        for s in range(1, steps + 1):
            dp_next = [[-1 for _ in range(C)] for _ in range(C)]
            row = s
            for ci_prev in range(C):
                for cm_prev in range(C):
                    if dp_prev[ci_prev][cm_prev] == -1:
                        continue
                    for di in [-1, 0, 1]:
                        ci_new = ci_prev + di
                        if not (0 <= ci_new < C):
                            continue
                        if matriz[row][ci_new] == -1:
                            continue
                        for dm in [-1, 0, 1]:
                            cm_new = cm_prev + dm
                            if not (0 <= cm_new < C):
                                continue
                            if matriz[row][cm_new] == -1:
                                continue
                            if ci_new == cm_new:
                                continue  # Evitar que Indiana y Marion estén en la misma celda
                            total = dp_prev[ci_prev][cm_prev] + matriz[row][ci_new] + matriz[row][cm_new]
                            if total > dp_next[ci_new][cm_new]:
                                dp_next[ci_new][cm_new] = total
            dp_prev = dp_next

        # Obtener el máximo relics recolectados por Indiana y Marion
        max_relics = -1
        for ci in range(C):
            for cm in range(C):
                if ci != cm and dp_prev[ci][cm] > max_relics:
                    max_relics = dp_prev[ci][cm]
        return max_relics

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
        return max_relics if max_relics != -1 else -1

    # Calcular reliquias de Indiana y Marion
    relics_im = dp_indiana_marion(R, C, matriz, central_row)
    if relics_im == -1:
        relics_im = 0  # Si Indiana o Marion no pueden llegar

    # Calcular reliquias de Sallah
    relics_s = dp_sallah(R, C, matriz, central_row)
    if relics_s == -1:
        relics_s = 0  # Si Sallah no puede llegar

    # Sumar las reliquias de Indiana, Marion y Sallah
    total_relics = relics_im + relics_s

    return total_relics if total_relics > 0 else -1

    # Prueba de la función con la matriz proporcionada
matriz5 = [
        [0, 0, 0]
]

R = len(matriz5)
C = len(matriz5[0])

resultado = max_reliquias(R, C, matriz5)
print(f"El máximo número de reliquias recolectadas es: {resultado}")