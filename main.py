import random

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("\n" + "="*50)
    print("¡Bienvenido al juego de Adivinar el Número!")
    print("="*50 + "\n")
    
    while True:
        try:
            guess = int(input("Adivina un número entre 1 y 100: "))
            
            if guess < 1 or guess > 100:
                print("⚠️ Por favor, ingresa un número entre 1 y 100.\n")
                continue
            
            intentos += 1
            
            if guess < numero_secreto:
                diferencia = numero_secreto - guess
                print(f"📉 ¡Muy bajo! (Diferencia: {diferencia})\n")
            elif guess > numero_secreto:
                diferencia = guess - numero_secreto
                print(f"📈 ¡Muy alto! (Diferencia: {diferencia})\n")
            else:
                print(f"\n🎉 ¡GANASTE! ¡Adivinaste el número {numero_secreto}!\")
                print(f"📊 Total de intentos: {intentos}")
                return intentos
        
        except ValueError:
            print("❌ Error: Por favor ingresa un número válido.\n")

def main():
    estadisticas = []
    
    while True:
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL")
        print("="*50)
        print("1. Jugar")
        print("2. Ver estadísticas")
        print("3. Salir")
        print("="*50)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            intentos = jugar()
            estadisticas.append(intentos)
        
        elif opcion == "2":
            if estadisticas:
                print("\n📊 ESTADÍSTICAS DE JUEGOS:")
                print(f"  - Juegos jugados: {len(estadisticas)}")
                print(f"  - Intentos promedio: {sum(estadisticas) / len(estadisticas):.1f}")
                print(f"  - Mejor juego: {min(estadisticas)} intentos")
                print(f"  - Peor juego: {max(estadisticas)} intentos")
            else:
                print("\n⚠️ Aún no has jugado ninguna partida.")
        
        elif opcion == "3":
            print("\n👋 ¡Gracias por jugar! ¡Hasta pronto!")
            break
        
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()