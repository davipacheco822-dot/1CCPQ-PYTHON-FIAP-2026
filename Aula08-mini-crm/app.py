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

def list_leads():
    leads = control.read_leads()

    print(f"## | {"Nome": <12} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]: <12} |{lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    #validar query

    search_results = control.read_leads_search(query)
    print(f"## | {"Nome": <12} | E-mail")
    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]: <12} |{lead["email"]}")

    print(search_results)

def export_leads():
    path_csv = control.export_csv()
    if path_csv is None:
        print("Não foi possivel exportar para CSV")
    else:
        print(f"Exportando para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/email)")
        print("[4] Exportar para CSV")
        print("[0] Sair do Programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            print("Lead adicionado")
            add_lead()
        elif opt == "2":
            print("Lister leads")
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()