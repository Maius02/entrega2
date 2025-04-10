def procesar_rondas(rondas):
    """rondas es una lista de diccionario de diccionario, cada elem es la partida de un jugador
        jugadores = {
            jugador1: { "kills": 0, "assists": 0, "deaths": 0, "mvp": 0, "puntos": 0 }
            jugador2:
            ...
        } """

    jugadores = {}
    
    for nro_ronda, ronda in enumerate(rondas, start=1):
        
        puntajes_ronda = {} #guardo los pares nombre:puntaje para luego calcular el mvp

        for jugador, datos in ronda.items():
            
            k = datos["kills"]   #int
            a = datos["assists"] #int
            d = datos["deaths"]  #boolean
            puntos = k * 4 + a * 1 + (-1 if not d else 0)

            puntajes_ronda[jugador] = puntos 

            #si el jugador no fue procesado, agrego nombre e inicializo valores en cero
            if jugador not in jugadores:
                jugadores[jugador] = {"kills": 0, "assists": 0, "deaths": 0, "mvp": 0, "puntos": 0}
            
            #incremento valores
            jugadores[jugador]["kills"] += k 
            jugadores[jugador]["assists"] += a
            jugadores[jugador]["deaths"] += int(d)
            jugadores[jugador]["puntos"] += puntos

        # Determinar MVP
        max_puntos = max(puntajes_ronda.values())   # puntajes_ronda = { "nombre": puntos, "nombre": puntos, ...}
        for nombre, puntaje in puntajes_ronda.items():
            if max_puntos == puntaje:
                jugadores[nombre]["mvp"] += 1

        # Imprimir ronda parcial
        print(f"Ranking ronda {nro_ronda}-------------")
        for nombre, puntaje in puntajes_ronda.items():
            print(f'   {nombre}: {puntaje} pts')
    print()
    return jugadores

def mostrar_ranking_final(jugadores):

    print("Ranking final:")
    print("Jugador  Kills  Asistencias  Muertes  MVPs  Puntos")
    print("-"*30)

    # ordena el diccionario jugadores por puntaje total, de mayor a menor (-x), para mostrar el ranking final.
    ranking = sorted(jugadores.items(), key=lambda x: -x[1]["puntos"])
    
    for nombre, stats in ranking:
        print(f"{nombre}   {stats['kills']},  {stats['assists']}, "
              f" {stats['deaths']},  {stats['mvp']}  |  {stats['puntos']} pts ")