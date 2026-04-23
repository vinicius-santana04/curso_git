from datetime import datetime

def saudacao_atleta(nome: str, equipe: str, posicao_tática: str) -> dict:
    """
    Retorna uma mensagem de boas-vindas e um payload de dados do atleta.
    """
    mensagem = f"Olá, {nome}! Bem-vindo ao sistema de análise da equipe {equipe}."
    
    payload = {
        "atleta": nome,
        "equipe": equipe,
        "posicao": posicao_tática,
        "mensagem_boas_vindas": mensagem,
        "timestamp_registro": datetime.now().isoformat()
    }
    
    return payload

# Testando a função
dados_jogador = saudacao_atleta(nome="Camisa 10", equipe="Time Principal", posicao_tática="Meio-Campo")

print(dados_jogador["mensagem_boas_vindas"])
print(f"Payload gerado: {dados_jogador}")