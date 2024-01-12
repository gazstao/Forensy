# File signature magic bytes Gazstao 19 OCT 23
# Forensy
# Gazstao 12 JAN 24

import pathlib


# Lendo o dicionário de um arquivo JSON com a função de decodificação personalizada
with open(nome_arquivo, 'r') as arquivo:
    file_signatures_lido = json.load(arquivo, object_hook=bytes_decoder)

print('Dicionário lido do arquivo:', file_signatures_lido)

file_signatures = file_signatures_lido
# IMPLEMENTAR COMPARAÇÃO DA EXTENSÃO VERIFICADA COM A FORNECIDA


def testa_dir(_path):

    for child in pathlib.Path(_path).glob("*"):
        try:
            if child.is_file():
                print(testa_arquivo(child))
            elif child.is_dir():
                testa_dir(child)
        except Exception as e:
            print(f'Erro {e} no arquivo {child}')


def testa_arquivo(file_path):

#    if (keyboard.is_pressed("enter") | keyboard.is_pressed(" ")):
#        exit(0)

    try:
        print(f"[*] testa_arquivo {file_path}: ", end="")
        # Defina as assinaturas de arquivo para os tipos que você deseja identificar

        # Leitura dos primeiros bytes do arquivo
        with open(file_path, 'rb') as file:
            file_header = file.read(5)  # Leitura dos primeiros 5 bytes

        # Verifique se as assinaturas correspondem
        for signature, file_type in file_signatures.items():
            if file_header.startswith(signature):
                return file_type
        string = 'Desconhecido: '+str(file_header)
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

