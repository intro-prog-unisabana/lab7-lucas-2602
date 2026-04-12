from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
    nombre_archivo = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(nombre_archivo)
    while True:
        entrada = input("Options: (1) Change Password, (2) Add Password, (3) Quit:\n")
        if entrada == "1":
            website_and_password = input("Enter the website and the new password:\n").split()
            if len(website_and_password) < 2:
                print("Input is in the wrong format!")
                continue
            website, password = website_and_password
            if len(password) < 12:
                print("Password is too short!")
                continue
            if change_password(nombre_archivo, website, password) == True:
                print("Password changed.")
                continue
            else:
                print("Website not found! Operation failed.")
                continue

        elif entrada == "2":
            agregar = input("Enter the website, username, and password:\n").split()
            if len(agregar) < 3:
                print("Input is in the wrong format!")
                continue
            web, username, contrasena = agregar
            if len(contrasena) < 12:
                print("Password is too short!")
                continue
            add_login(nombre_archivo, web, username, contrasena)
            print("Login added.")
            continue

        elif entrada == "3":
            break
        
        else:
            print("Invalid option selected!")
            continue


if __name__ == "__main__":
    main()
