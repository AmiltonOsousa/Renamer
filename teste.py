import os
import re

def extract_number(filename):
    match = re.findall(r'\d+', filename)
    if match:
        full_number = ''.join(match)
        return int(full_number)
    else:
        return float('inf')

def clean_filename(filename):
    # Remove espaços extras e caracteres especiais
    filename = filename.strip()
    filename = re.sub(r'[^\w\s-]', '', filename)  # Remove caracteres que não são alfanuméricos, underscore (_) ou hífen (-)
    filename = re.sub(r'\s+', ' ', filename)  # Substitui múltiplos espaços por um único espaço
    return filename

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

    pdf_files_sorted = sorted(pdf_files, key=extract_number)

    for old_name, new_name in zip(pdf_files_sorted, new_names):
        old_path = os.path.join(directory, old_name)
        new_name_clean = clean_filename(new_name)
        new_path = os.path.join(directory, new_name_clean + '.pdf')

        try:
            os.rename(old_path, new_path)
            print(f'Renomeado: {old_name} -> {new_name_clean}.pdf')
        except Exception as e:
            print(f"Erro ao renomear {old_name} para {new_name_clean}.pdf: {e}")

# Exemplo de utilização:
directory = r'C:\Users\d829574\Desktop\Renamer-master\pdfs'
names_file = r'C:\Users\d829574\Desktop\Renamer-master\lista-de-nomes.txt'
rename_pdfs(directory, names_file)