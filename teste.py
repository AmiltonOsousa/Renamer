import os


def rename_pdfs(directory, names_file):
    if not os.path.exists(directory):
        print(f"O diretório '{directory}' não existe.")
        return

    try:
        with open(names_file, 'r') as file:
            new_names = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"O arquivo de nomes '{names_file}' não foi encontrado.")
        return

    files = os.listdir(directory)
    pdf_files = [file for file in files if file.endswith('.pdf')]

    if len(pdf_files) != len(new_names):
        print("A quantidade de novos nomes não corresponde à quantidade de arquivos PDF.")
        return

    for old_name, new_name in zip(pdf_files, new_names):
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name + '.pdf')

        os.rename(old_path, new_path)
        print(f'Renomeado: {old_name} -> {new_name}.pdf')

directory = r'C:\Users\amilt\PycharmProjects\Teste\pdfs'
names_file = r'C:\Users\amilt\PycharmProjects\Teste\lista-de-nomes.txt'
rename_pdfs(directory, names_file)
