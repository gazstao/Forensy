
import json
import os

# Nome do arquivo para salvar os dados
nome_arquivo = 'db_file_signatures.json'

file_signatures = {
    b'GIF89a': 'GIF',  # Exemplo de assinatura para arquivos GIF
    b'%PDF': 'PDF',  # Exemplo de assinatura para arquivos PDF
    b'\x89PNG\r': 'PNG',
    b'PK\x03\x04': 'ZIP',
    b'\xFF\xFB': 'MP3',
    b'{\n': 'JSON',
    b'IRPF ': 'IRPF',
    b'<?xml': 'XML',
    b'<!DOC': 'HTML',
    b'MZ\x90\x00\x03': 'EXE/DLL',
    b'{\\rtf': 'RTF',
    b'\x00\x01\x00\x00\x00': 'TTF',
    b'GIF89': 'GIF',
    b'\xff\xd8\xff\xe0\x00': 'JPEG',
    b"7z\xbc\xaf'":'7zip'
# Adicione outras assinaturas conforme necessário
}

# ChatGPT suggested function to encode bytes
def bytes_encoder(obj):
    if isinstance(obj, bytes):
        return {'__bytes__': True, 'data': obj.decode('latin-1')}
    return obj

def save_database(file_path='db_file_signatures.json', data=None):
    if data is None:
        print("No data provided to save.")
        return

    if os.path.isfile(file_path):
        user_response = input(f"File '{file_path}' already exists. Do you want to overwrite it? (y/n): ").lower()
        if user_response != 'y':
            print("Database not saved.")
            return

    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, default=bytes_encoder)

        print(f'Database saved to {file_path}.')
    except Exception as e:
        print(f"Error occurred while saving the database: {str(e)}")

# Converter chaves de bytes para strings
file_signatures_str_keys = {key.decode('latin-1'): value for key, value in file_signatures.items()}

# Gravando o dicionário em um arquivo JSON com a função de codificação personalizada
save_database(file_path=nome_arquivo, data=file_signatures_str_keys)

print(f'Database created successfully: {nome_arquivo}.')
