import argparse

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")

    subparsers = parser.add_subparsers(dest="command")

    #comando add
    add_parser = subparsers.add_parser("add", help="Adicionar uma despesa")
    add_parser.add_argument("--description", required=True, help="Descrição da despesa")
    add_parser.add_argument("--amount", required=True, help="Valor da despesa")

    #Comando: list
    subparsers.add_parser("List", help="Lista de todas as despesas")

    #Comando: summary
    summary_parser = subparsers.add_parser("summary", help="Resumo das despesas")
    summary_parser.add_argument("--mount", type=int, help="Mês para filtrar (1-12)")

    #Comando: delete
    delete_parser = subparsers.add_parser("delete", help="Deletar uma despesa")
    delete_parser.add_argument("--id", type=int, required=True, help="ID da despesa")

    args = parser.parse_args()

    print("Comando recebido:", args.command)
    print("Argumentos:", args)


if __name__ == "__main__":
    main()