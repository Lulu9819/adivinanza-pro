import random

print("🎲 Bienvenida al juego de adivinanza, Lulu 🎲")
print("Estoy pensando en un número del 1 al 20...")

numero_secreto = random.randint(1, 20)
intentos = 0

while True:
    # Pedimos número y controlamos si no es válido
    entrada = input("Adivina el número (1-20): ")
    try:
        intento = int(entrada)
    except ValueError:
        print("Por favor, escribe un número válido 😊")
        continue

    if not 1 <= intento <= 20:
        print("Debe estar entre 1 y 20.")
        continue

    intentos += 1

    if intento < numero_secreto:
        print("Es más grande ⬆️")
    elif intento > numero_secreto:
        print("Es más pequeño ⬇️")
    else:
        print(f"🎉 ¡Correcto, Lulu! Lo lograste en {intentos} intentos.")
        break
