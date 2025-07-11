import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

# Cargar datasets con manejo de excepciones
try:
    df1 = pd.read_csv("C:/Users/benja/Documents/IA/PremierLeague2324.csv")
    df2 = pd.read_csv("C:/Users/benja/Documents/IA/PremierLeague2223.csv")
except FileNotFoundError as e:
    print("❌ No se encontró uno de los archivos CSV. Asegúrate de que los archivos existan en la ruta correcta.")
    exit()

# Normalizar nombres de columnas si es necesario
df2.rename(columns={
    'fecha': 'starting_at',
    'local': 'home_team_name',
    'visitante': 'away_team_name',
    'goles_local': 'home_team_goals',
    'goles_visitante': 'away_team_goals'
}, inplace=True)

# Convertir fechas con manejo de excepciones
try:
    df1['starting_at'] = pd.to_datetime(df1['starting_at'])  # PremierLeague2324.csv (ya está bien)
    df2['starting_at'] = pd.to_datetime(df2['starting_at'], dayfirst=True)  # PremierLeague2223.csv con formato día/mes/año
except ValueError as e:
    print("❌ Error al convertir las fechas. Verifica el formato de las fechas en el archivo.")
    exit()

# Unir ambos dataframes
df = pd.concat([df1, df2], ignore_index=True)

# Asegurar consistencia de nombres de equipos
df['home_team_name'] = df['home_team_name'].astype(str)
df['away_team_name'] = df['away_team_name'].astype(str)

# Obtener lista limpia de equipos
equipos = sorted(set(df['home_team_name'].unique()) | set(df['away_team_name'].unique()))

# Calcular promedios de goles por equipo (local y visitante)
avg_goles = df.groupby('home_team_name').agg({'home_team_goals': 'mean'}).rename(columns={'home_team_goals': 'avg_home_goals'})
avg_goles['avg_away_goals'] = df.groupby('away_team_name').agg({'away_team_goals': 'mean'})['away_team_goals']

# Función para mostrar historial entre dos equipos
def mostrar_historial(equipo1, equipo2, df):
    historial = df[((df['home_team_name'] == equipo1) & (df['away_team_name'] == equipo2)) |
                   ((df['home_team_name'] == equipo2) & (df['away_team_name'] == equipo1))]

    if historial.empty:
        print(f"\n❌ No se encontraron partidos entre {equipo1} y {equipo2}.")
        return

    print(f"\n📊 Historial entre {equipo1} y {equipo2}:")
    historial = historial.sort_values(by='starting_at')

    tabla = []
    g1, g2 = 0, 0
    w1 = w2 = draws = 0

    for _, row in historial.iterrows():
        h, a = row['home_team_name'], row['away_team_name']
        gh, ga = row['home_team_goals'], row['away_team_goals']
        ganador = 'Empate'
        if gh > ga:
            ganador = h
        elif ga > gh:
            ganador = a

        if ganador == equipo1:
            w1 += 1
        elif ganador == equipo2:
            w2 += 1
        else:
            draws += 1

        if h == equipo1:
            g1 += gh
            g2 += ga
        else:
            g1 += ga
            g2 += gh

        tabla.append([
            row['starting_at'].strftime("%d/%m/%Y"),
            f"{h} {gh} - {ga} {a}",
            f"Ganador: {ganador}"
        ])

    print(tabulate(tabla, headers=["Fecha", "Marcador", "Resultado"], tablefmt="fancy_grid"))
    print(f"\n🔢 Resumen:")
    print(f"{equipo1} ganó {w1} veces, {equipo2} ganó {w2} veces, Empates: {draws}")
    print(f"Goles de {equipo1}: {g1}, Goles de {equipo2}: {g2}")

    # Predicción basada en historial
    print("\n🧠 Predicción básica:")
    if w1 > w2:
        print(f"✅ Predicción: {equipo1} ganará")
    elif w2 > w1:
        print(f"✅ Predicción: {equipo2} ganará")
    else:
        print("✅ Predicción: Empate")

    # Predicción de goles utilizando promedios
    prediccion_goles_1 = avg_goles.loc[equipo1, 'avg_home_goals']
    prediccion_goles_2 = avg_goles.loc[equipo2, 'avg_away_goals']
    print(f"\n📊 Predicción de goles: {equipo1} {prediccion_goles_1:.2f} - {prediccion_goles_2:.2f} {equipo2}")

    return prediccion_goles_1, prediccion_goles_2

# Visualización de estadísticas de goles
def visualizar_estadisticas(equipo1, equipo2, df):
    equipo1_historial = df[df['home_team_name'] == equipo1]
    equipo2_historial = df[df['away_team_name'] == equipo2]

    equipo1_goles = equipo1_historial['home_team_goals'].mean()
    equipo2_goles = equipo2_historial['away_team_goals'].mean()

    equipos = [equipo1, equipo2]
    goles = [equipo1_goles, equipo2_goles]

    plt.bar(equipos, goles, color=['blue', 'red'])
    plt.title(f"Promedio de goles de {equipo1} y {equipo2}")
    plt.ylabel("Promedio de goles")
    plt.show()

# Menú interactivo con historial de predicciones
predicciones = []

while True:
    print("\n📌 Menú principal")
    print("1. Ver lista de equipos")
    print("2. Predecir enfrentamiento")
    print("3. Visualizar estadísticas de goles")
    print("4. Ver historial de predicciones")
    print("5. Salir")

    opcion = input("Selecciona una opción (1/2/3/4/5): ").strip()

    if opcion == '1':
        print("\n📋 Equipos disponibles:")
        for equipo in sorted(equipos):
            print("-", equipo)

    elif opcion == '2':
        equipo1 = input("🔎 Ingresa el nombre del primer equipo: ").strip()
        equipo2 = input("🔎 Ingresa el nombre del segundo equipo: ").strip()

        if equipo1 not in equipos or equipo2 not in equipos:
            print("❌ Uno o ambos equipos no están en la base de datos.")
        else:
            prediccion_goles_1, prediccion_goles_2 = mostrar_historial(equipo1, equipo2, df)
            # Guardar predicción en el historial
            predicciones.append({
                'equipo1': equipo1,
                'equipo2': equipo2,
                'prediccion': "Ganará " + (equipo1 if prediccion_goles_1 > prediccion_goles_2 else equipo2),
                'goles_equipo1': prediccion_goles_1,
                'goles_equipo2': prediccion_goles_2
            })

    elif opcion == '3':
        equipo1 = input("🔎 Ingresa el nombre del primer equipo: ").strip()
        equipo2 = input("🔎 Ingresa el nombre del segundo equipo: ").strip()
        
        if equipo1 not in equipos or equipo2 not in equipos:
            print("❌ Uno o ambos equipos no están en la base de datos.")
        else:
            visualizar_estadisticas(equipo1, equipo2, df)

    elif opcion == '4':
        print("\n📜 Historial de predicciones:")
        for pred in predicciones:
            print(f"{pred['equipo1']} vs {pred['equipo2']} => {pred['prediccion']}, Goles: {pred['goles_equipo1']:.2f} - {pred['goles_equipo2']:.2f}")

    elif opcion == '5':
        print("👋 ¡Hasta luego!")
        break

    else:
        print("❌ Opción no válida. Intenta de nuevo.")
