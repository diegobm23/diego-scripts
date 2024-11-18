# -*- coding: utf-8 -*-
import pandas as pd
import logging as log

print("**************")
print("| INSTRUÇÕES |")
print("**************")

print("- Adicionar o arquivo do dataset na mesma pasta deste script.")
print("- Seguir as instruções do passadas aqui para análise dos dados.")
print("- digite FIM a qualquer momento para sair.\n")


def main():
    dataset = ler_arquivo()
    menu_opcoes(dataset)


def ler_arquivo():
    try:
        nome_arquivo = input("$ Informe o nome do arquivo com a estenção -> ")
        verificar_fim(nome_arquivo)
        return pd.read_csv(nome_arquivo, low_memory=False)
    except Exception:
        log.error(" Ops, arquivo não encontrado ou com extensão não compatível :(")
        exit()


def menu_opcoes(dataset):
    opcao = ""

    while not is_fim(opcao):
        colunas = dataset.columns.values
        print("O arquivo possui as seguintes colunas:")
        print(colunas)
        print("\nEscolha as opções a seguir:")
        print("1 - Operações com colunas numéricas")
        print("2 - Operações com colunas NÃO numéricas")
        print("3 - Exibição parcial\n")

        opcao = input("$ Informe a opção desejada -> ")

        match opcao:
            case "1":
                menu_numericos(dataset)
            case "2":
                menu_nao_numericos(dataset)
            case "3":
                exibir_parcial(dataset)
            case _:
                opcao = "fim"

    verificar_fim(opcao)


def menu_numericos(dataset):
    coluna = input("$ Informe a coluna -> ")
    print("média [avg], mínimo [min], máximo [max], desvio padrão [dsv]")
    funcao = input("$ Informe qual função gostaria de aplicar dentre as opções acima -> ")

    try:
        match funcao:
            case "avg":
                print(dataset[coluna].mean())
            case "min":
                print(dataset[coluna].min())
            case "max":
                print(dataset[coluna].max())
            case "dsv":
                print(dataset[coluna].std())
            case _:
                print("Ops, opção inválida :(")
    except Exception:
        log.error(" Ops, essa coluna não é numérica :(")

    voltar()


def menu_nao_numericos(dataset):
    coluna = input("$ Informe a coluna -> ")
    print("1 - Quantidade de valores de cada elemento da coluna")
    print("2 - Elemento com a maior quantidade de caracteres")
    print("3 - Elemento com a menor quantidade de caracteres")

    opcao = input("$ Informe o número da opção que gostaria de aplicar -> ")

    try:
        match opcao:
            case "1":
                coluna_zero = dataset.columns.values[0]
                print(dataset[[coluna, coluna_zero]].groupby(coluna).count())
            case "2":
                dataset["diegobm23_len"] = dataset[coluna].str.len()
                print(dataset["diegobm23_len"].max())
            case "3":
                dataset["diegobm23_len"] = dataset[coluna].str.len()
                print(dataset["diegobm23_len"].min())
            case _:
                print("Ops, opção inválida :(")
    except Exception:
        log.error(" Ops, essa coluna é numérica :(")

    voltar()


def exibir_parcial(dataset):
    linhas = int(input("$ Infrome a quantidade de linhas -> "))
    colunas = int(input("$ Informe a quantidade de colunas -> "))
    print(dataset.iloc[:linhas, :colunas])
    voltar()



def verificar_fim(opcao):
    if is_fim(opcao):
        print("Até logo ;) - by diegobm23")
        exit()

def is_fim(opcao):
    return str.lower(opcao) == "fim"


def voltar():
    input("\n$ Informe qualquer tecla para voltar... ")

main()
