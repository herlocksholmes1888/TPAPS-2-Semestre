from hashlib import sha256
import pandas as pd

USER_LIMIT = 10
names = []
roles = []
dates = []
emails = []
passwords = []

def user_verification(name):
    for i in names:
        if i == name:
            return True
    return False

def dataframe_creation(names, roles, dates, emails, passwords):
    f = names, roles, dates, emails, passwords
    df = pd.DataFrame(f, index=['Nome', 'Cargo', 'DT Nascimento', 'Email', 'Senha']).T
    df = df.to_csv('usuarios.csv', index=False)

while len(names) <= USER_LIMIT:
    name = input("Informe o nome do usuário (ou digite 'sair' para sair do programa): ")

    if user_verification(name) == True:
        print("Esse usuário já está cadastrado!")
        choice = input("Gostaria de entrar como este usuário? S/N: ")
        if choice.upper() == 'S':
            password_verification = input("Por favor, informe sua senha: ")
            password_verification = sha256(password_verification.encode())
            password_verification = password_verification.digest()
            for i in passwords:
                if i == password_verification:
                    print("Bem-vindo(a), {}!".format(name))
                else:
                    print("Você digitou a senha errada. Reinicie o programa e tente novamente.")
            break
        elif choice.upper() == 'N':
            dataframe_creation(names, roles, dates, emails, passwords)
            break
        else:
            print("Opção inválida! Reinicie o programa e tente novamente.")
            break

    if name.lower() == 'sair': 
        dataframe_creation(names, roles, dates, emails, passwords)
        break

    role = input("Informe o seu cargo na empresa: ")
    date = input("Informe a sua data de aniversário: ")
    email = input("Informe o email que será associado à sua conta: ")
    password = input("Informe a senha que será associada à sua conta: ")
    
    hash_code = sha256(password.encode())
    hash_password = hash_code.digest()

    names.append(name)
    roles.append(role)
    dates.append(date)
    emails.append(email)
    passwords.append(hash_password)

    if len(names) >= USER_LIMIT:
        print("O sistema atingiu seu limite de cadastramentos.")
        dataframe_creation(names, roles, dates, emails, passwords)
        break
