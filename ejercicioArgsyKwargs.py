import threading
import json

jsonPersonas = {
    "personas": [
        {"nombre": "Juan", "edad": 24},
        {"nombre": "Maria", "edad": 16},
        {"nombre": "Rodrigo", "edad": 36},
        {"nombre": "Ivan", "edad": 20},
        {"nombre": "Javier", "edad": 60},
    ]
}


def procesar_usuario(id, nombre, edad):
    print(f"Usuario ID: {id}, Nombre: {nombre}, Edad: {edad}")


def main():
    threads = []
    for index, persona in enumerate(jsonPersonas["personas"]):
        t = threading.Thread(
            target=procesar_usuario,
            args=(index + 1,),
            kwargs={"nombre": persona["nombre"], "edad": persona["edad"]},
        )
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("Todos los usuarios han sido procesados")


if __name__ == "__main__":
    main()
