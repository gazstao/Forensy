# This file tests the database.
# It is also used to load the database from the file and return a dictionary array as a result.

import json

# ChatGPT suggested function to convert string to byte
def bytes_decoder(obj):
    if '__bytes__' in obj:
        return obj['data'].encode('latin-1')
    return obj

# Load the database from the file
def load_database(file='db_file_signatures.json'):
    try:
        # Lendo o dicionário de um arquivo JSON com a função de decodificação personalizada
        with open(file, 'r') as arquivo:
            file_signatures = json.load(arquivo, object_hook=bytes_decoder)

        itens = len(file_signatures)
        print(f'DB OK!\nREADED. {itens} signatures detected.')
        return file_signatures

    except:
        print("No database found.")
        return None