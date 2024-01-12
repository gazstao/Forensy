# File signature magic bytes Gazstao 19 OCT 23
# Forensy
# Gazstao 12 JAN 24

import pathlib
import json

# Read file magic number database
from db_load_file_signatures import load_database
file_signatures = load_database()

# Test if is a dir.
# If it is, call it recursively
# If it is a file, call the function to test it
def test_dir(_path):
    for child in pathlib.Path(_path).glob("*"):
        try:
            if child.is_file():
                if test_file(child) != None:
                    print(test_file(child))
            elif child.is_dir():
                test_dir(child)
        except Exception as e:
            print(f'Erro {e} no arquivo {child}')


# Test magic number of file
def test_file(file_path):
    try:
        print(f"[*] Testing {file_path}: ", end="")

        # Leitura dos primeiros bytes do arquivo
        with open(file_path, 'rb') as file:
            file_header = file.read(5)  # Leitura dos primeiros 5 bytes

        # Converta file_header para bytes
        file_header = bytes(file_header)

        # Verifique se as assinaturas correspondem
        for signature, file_type in file_signatures.items():
            if file_header.startswith(signature.encode('latin-1')):
                return file_type

        string = 'Unknown type: '+str(file_header)
        return string

    except Exception as e:
        print(f"Erro {e}")

# testa_dir('c:')
#
# implementações futuras:
# - criar um arquivo com uma lista de arquivos que possuem extensão diferente do tipo
# - obter o hash dos arquivos suspeitos (e eventualmente dos ok tbem) e criar outro arquivo com eles
# - testar hashes suspeitos em algum serviço online
#


# IMPLEMENTAR COMPARAÇÃO DA EXTENSÃO VERIFICADA COM A FORNECIDA
test_dir("c:\\")