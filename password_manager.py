import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, "r") as archivo:
        contraseña = archivo.read().strip()
    contraseña_encriptada = caesar_encrypt(contraseña)
    with open(filename, "w") as archivo:
        archivo.write(contraseña_encriptada)


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    with open(filename, mode="r") as file:
        data= []
        linea = csv.reader(file)
        for fila in linea:
            if fila:
                data.append(fila)
        for fila in data:
            if "password" not in fila:
                fila[2] = caesar_encrypt(fila[2])
        with open(filename, mode="w", newline = "") as file:
            escritor = csv.writer(file)
            escritor.writerows(data)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    with open(filename, mode="r") as file:
        data= []
        website_existente = False
        linea = csv.reader(file)
        for fila in linea:
            if fila:
                data.append(fila)
        for fila in data:
            if fila[0] == website:
                website_existente = True
                fila[2] = caesar_encrypt(password)
                break
            else:
                website_existente = False
        with open(filename, mode="w", newline = "") as file:
            escritor = csv.writer(file)
            escritor.writerows(data)
        return website_existente

def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    contraseña_encriptada = caesar_encrypt(password)
    with open(filename, mode="a") as file:
        escritor = csv.writer(file)
        escritor.writerow(website_name, username, contraseña_encriptada)
