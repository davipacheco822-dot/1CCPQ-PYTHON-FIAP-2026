from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    stage = input("Etapa no funil: ")

    #depois de validado, precisamos modelar o lead como um dict
    print(model_lead(name, email, stage))
    #usar o control agora, ja que temos que enviar esse lead para o leads.json
    control.create_lead(model_lead(name, email, stage))

    print("Lead adicionado (func)")



def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do Programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            print("Lead adicionado")
            add_lead()
        elif opt == "2":
            print("Lister leads")
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()