import json
import os

def carregar_dados(nome_arquivo):
    """Carrega dados de arquivo JSON. Retorna lista vazia se o arquivo não existir."""
    caminho = os.path.join("data", nome_arquivo)
    if not os.path.exists(caminho):
        return []
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(nome_arquivo, dados):
    """Salva dados em arquivo JSON."""
    caminho = os.path.join("data", nome_arquivo)
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)