def calculate(a , b):
    """
    Calculates the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b
def greet_user(name: str) -> None:
            """
            Greets the user with a personalized message.

            Args:
                name (str): The name of the user.

            Returns:
                None
            """
            print(f"¡Hola, {name}! Bienvenido/a al programa.")
while True:
    print("=== Menú ===")
    print("1. Saludar")
    print("2. Calcular")
    print("3. Salir")
    eleccion = int(input("Ingrese su una opcion: "))
    if eleccion == 1:
        nombre = input("Ingrese su nombre: ")
        greet_user(nombre)
    elif eleccion == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = calculate(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif eleccion == 3:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
print("Gracias por usar el programa. ¡Hasta luego!")


