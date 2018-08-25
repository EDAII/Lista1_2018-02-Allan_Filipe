import os
import sys
import time


all_data = []
columns_descriptions = []


def initialMenu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Seja Bem Vindo!\n")
    print("---------------------------------------------------------------")
    print("Regras de Uso:")
    print("A primeira linha do seu arquivo '.csv' deve conter os títulos das colunas.")
    print("A primeira coluna do seu arquivo '.csv' deve ser a informação que será o parâmetro de busca e deve ser um número.")
    print("O Dado que servirá de parâmetro de busca não deve se repetir, ou seja, tem de ser uma Chave Primária.")
    print("OBS: O Tempo de Execução da Busca Binária está levando em conta o tempo de ordenação do vetor sempre que uma nova busca é feita.")
    print("---------------------------------------------------------------\n")


def readCsv():
    global all_data
    global columns_descriptions

    file_path = input("Insira o caminho do seu arquivo '.csv' referente aos dados que serão alvos de buscas: ")

    # Treating error while opening the file.
    try:
        file = open(file_path, "r")
    except IOError:
        print("\nNão foi possível abrir o arquivo com o caminho indicado:", file_path)
        sys.exit()

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            line_splitted = line.split(",")
            line_splitted[-1] = line_splitted[-1].strip("\n")
            all_data.append(line_splitted)

    file.close()


def searchValues():
    search = True

    while search:
        requested_value = input("Insira um valor para a busca: ")

        print("\n===== Resultado para busca Sequencial com Sentinela =====")

        sentinelSearch(requested_value)

        print("\n===== Resultado para busca Binária =====")

        binarySearch(requested_value)

        search = input("\nDeseja buscar um novo registro? (s/n): ")

        if search == 's' or search == 'S':
            search = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            search = False
            print("\n===== Fim da Execução =====")


def sentinelSearch(requested_value):
    time_initial = time.time()
    time_final_not_found = []
    time_final_found = []
    result = False
    sentinel = []
    sentinel.append(requested_value)
    all_data.append(sentinel)
    i = 0

    while all_data[i][0] != requested_value:
        i += 1
    all_data.pop()

    if i == len(all_data):
        time_final_not_found.append(time.time() - time_initial)
        printResult(result, all_data, time_final_not_found)
    else:
        time_final_found.append(time.time() - time_initial)
        result = True
        printResult(result, all_data[i], time_final_found)


def binarySearch(requested_value):
    time_initial_with_sort = time.time()
    time_final_not_found = []
    time_final_found = []
    all_data_sorted = sorted(all_data, key=getKey)
    time_initial_without_sort = time.time()

    left_position, right_position = 0, len(all_data_sorted)-1

    result = False

    while left_position <= right_position and not result:
        current_position = (left_position + right_position)//2

        if int(all_data_sorted[current_position][0]) == int(requested_value):
            time_final_found.append(time.time() - time_initial_with_sort)
            time_final_found.append(time.time() - time_initial_without_sort)
            result = True
            printResult(result, all_data_sorted[current_position], time_final_found)
        else:
            if int(all_data_sorted[current_position][0]) < int(requested_value):
                left_position = current_position + 1
            else:
                right_position = current_position - 1

    if not result:
        time_final_not_found.append(time.time() - time_initial_with_sort)
        time_final_not_found.append(time.time() - time_initial_without_sort)
        printResult(result, all_data_sorted, time_final_not_found)


def printResult(result, value_found, time):
    if result:
        print("\nPara o índice ", value_found[0], ", o registro encontrado foi: \n")
        i = 0
        for description in columns_descriptions:
            print(description, ":", value_found[i])
            i += 1

        print("")
        if len(time) == 2:  # Binary Print
            print("Tempo de Execução (Contando o Tempo de Ordenação):", round(time[0], 9), "segundos")
            print("Tempo de Execução (Sem o Tempo de Ordenação):", round(time[1], 9), "segundos")
        else:  # Sequencial Print
            print("Tempo de Execução (Sem necessidade de Ordenação):", round(time[0], 9), "segundos")
    else:
        print("\nO Registro correspondente ao índice indicado não foi encontrado.")

        print("")
        if len(time) == 2:  # Binary Print
            print("Tempo de Execução (Contando o Tempo de Ordenação):", round(time[0], 9), "segundos")
            print("Tempo de Execução (Sem o Tempo de Ordenação):", round(time[1], 9), "segundos")
        else:  # Sequencial Print
            print("Tempo de Execução (Sem necessidade de Ordenação):", round(time[0], 9), "segundos")


def getKey(item):
    return int(item[0])


if __name__ == "__main__":
    initialMenu()
    readCsv()
    searchValues()
