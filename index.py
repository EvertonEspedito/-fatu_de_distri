import json

# Função para carregar dados do arquivo JSON
def carregar_dados(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        dados = json.load(file)
    return dados

# Função para calcular o menor, maior valor e dias acima da média
def analisar_faturamento(dados):
    valores = [item['valor'] for item in dados['faturamento'] if item['valor'] > 0]
    
    if not valores:
        return {
            "menor_valor": None,
            "maior_valor": None,
            "dias_acima_media": 0
        }
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media)
    
    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_media": dias_acima_media
    }

def main():
    nome_arquivo = 'faturamento.json'
    dados = carregar_dados(nome_arquivo)
    resultado = analisar_faturamento(dados)
    
    print(f"Menor valor de faturamento: {resultado['menor_valor']}")
    print(f"Maior valor de faturamento: {resultado['maior_valor']}")
    print(f"Número de dias acima da média mensal: {resultado['dias_acima_media']}")

if __name__ == "__main__":
    main()
