from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
    nombre_archivo = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(nombre_archivo)


if __name__ == "__main__":
    main()
