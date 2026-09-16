from os import sleep

def cronometro(segundos_total, segundos_intervalo):
    for i in range(segundos_total, 0, -segundos_intervalo):
        print(f"Tempo restante: {i} segundos")
        sleep(segundos_intervalo)
        print(i)

cronometro(15, 5)