def ferry_loading(ferry_length, cars):
    ferry_length *= 100  # Convertimos la longitud del ferry a centímetros
    n = len(cars)  # Número de coches
    
    # DP: Usamos un diccionario en lugar de una lista para hacer la búsqueda más eficiente
    dp = [{} for _ in range(n + 1)]
    dp[0][0] = True  # Inicialmente, no hay coches cargados y no se ha usado espacio
    
    # Variable para guardar el número máximo de coches cargados y la longitud usada en babor
    max_cars = 0
    max_length_babor = 0
    
    # Para guardar las decisiones tomadas en cada paso (port o starboard)
    parent = [{} for _ in range(n + 1)]
    
    # Procesar los coches en orden
    for i in range(n):
        car_length = cars[i]
        for length_babor in dp[i]:
            length_estribor = sum(cars[:i + 1]) - length_babor
            # Decidir en qué lado cargar el coche, balanceando las longitudes
            if abs((length_babor + car_length) - length_estribor) < abs(length_babor - (length_estribor + car_length)):
                # Cargar el coche en babor si esto equilibra mejor la carga
                if length_babor + car_length <= ferry_length:
                    dp[i + 1][length_babor + car_length] = True
                    parent[i + 1][length_babor + car_length] = ('port', length_babor)
            else:
                # Cargar el coche en estribor si esto equilibra mejor la carga
                if length_estribor + car_length <= ferry_length:
                    dp[i + 1][length_babor] = True
                    parent[i + 1][length_babor] = ('starboard', length_babor)
        
        # Actualizamos el número máximo de coches cargados
        for length_babor in dp[i + 1]:
            total_length = sum(cars[:i + 1])
            length_estribor = total_length - length_babor
            if length_babor <= ferry_length and length_estribor <= ferry_length:
                max_cars = i + 1
                max_length_babor = length_babor

    # Reconstruir la solución
    result = []
    length_babor = max_length_babor
    for i in range(max_cars, 0, -1):
        side, prev_length_babor = parent[i][length_babor]
        result.append(side)
        length_babor = prev_length_babor
    result.reverse()  # Invertimos el resultado para mostrarlo en orden

    return max_cars, result

# Función principal que usa entrada estándar (stdin) y salida estándar (stdout)
def main():
    # Leer la cantidad de casos (n)
    n = int(input().strip())
    #espacio= input().strip()
    
    for _ in range(n):

        ferry_length = int(input().strip())  # Leer la longitud del ferry en metros
        cars = []
        while True:
            car_length = int(input().strip())  # Leer la longitud de cada coche en cm
            if car_length == 0:
                break  # La entrada de coches termina con un 0
            cars.append(car_length)
        
        # Llamar a la función ferry_loading
        max_cars, result = ferry_loading(ferry_length, cars)
        
        # Imprimir los resultados en salida estándar
        print(max_cars)
        for side in result:
            print(side)

# Ejecutar el programa
if __name__ == "__main__":
    main()

