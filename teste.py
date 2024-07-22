import os
import re


def extract_number(filename):
    # Extrai o número do nome do arquivo original
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')  # Retorna infinito se nenhum número for encontrado


def rename_pdfs(directory, names_file):
    if not os.path.exists(directory):
        print(f"O diretório '{directory}' não existe.")
        return

    try:
        with open(names_file, 'r', encoding='utf-8') as file:
            new_names = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"O arquivo de nomes '{names_file}' não foi encontrado.")
        return
    except UnicodeDecodeError:
        print(f"Erro ao decodificar o arquivo de nomes '{names_file}'. Verifique a codificação do arquivo.")
        return

    files = os.listdir(directory)
    pdf_files = [file for file in files if file.endswith('.pdf')]

    if len(pdf_files) != len(new_names):
        print("A quantidade de novos nomes não corresponde à quantidade de arquivos PDF.")
        return

    # Ordena os arquivos PDF com base nos números extraídos dos nomes originais
    pdf_files_sorted = sorted(pdf_files, key=extract_number)

    for old_name, new_name in zip(pdf_files_sorted, new_names):
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name + '.pdf')

        try:
            os.rename(old_path, new_path)
            print(f'Renomeado: {old_name} -> {new_name}.pdf')
        except Exception as e:
            print(f"Erro ao renomear {old_name} para {new_name}.pdf: {e}")


directory = r'C:\Users\x545208\Desktop\Renamer\pdfs'
names_file = r'C:\Users\x545208\Desktop\Renamer\lista-de-nomes.txt'
rename_pdfs(directory, names_file)
