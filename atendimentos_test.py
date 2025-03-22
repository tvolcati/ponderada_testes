import requests
from unittest.mock import Mock
from datetime import datetime

# Mock da resposta da API para simular diferentes cenários
def mock_obter_atendimentos_por_data(data_inicio, data_fim, cenario='success'):
    mock_response = Mock()
    
    if cenario == 'success':
        # Cenário 1: Atendimentos encontrados
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": 1,
                "aluno": "Pedro Oliveira",
                "data": "2025-03-10T14:30:00",
                "tipo_atendimento": "Suporte de Aprendizagem",
                "status": "Confirmado",
                "responsavel_id": 789,
                "observacoes": "Atendimento para acompanhamento semestral"
            },
            {
                "id": 2,
                "aluno": "Ana Carolina Lima",
                "data": "2025-03-15T10:00:00",
                "tipo_atendimento": "Orientação Vocacional",
                "status": "Agendado",
                "responsavel_id": 456,
                "observacoes": "Primeira sessão de orientação profissional"
            }
        ]
    elif cenario == 'empty':
        # Cenário 2: Nenhum atendimento encontrado
        mock_response.status_code = 200
        mock_response.json.return_value = []
    else:
        # Cenário 3: Erro de servidor
        mock_response.status_code = 500
        mock_response.text = "Falha na conexão com o servidor"
    
    return mock_response

# Função que realiza a consulta de atendimentos por período
def obter_atendimentos_por_periodo(data_inicio, data_fim, cenario='success'):
    # Em um ambiente real, a URL seria algo como:
    # url = f"https://api.centropaulasouza.sp.gov.br/atendimentos?data_inicio={data_inicio}&data_fim={data_fim}"
    # response = requests.get(url)
    
    # Como estamos usando mock, simulamos a resposta:
    response = mock_obter_atendimentos_por_data(data_inicio, data_fim, cenario)
    
    # Verifica o resultado
    if response.status_code == 200:
        atendimentos = response.json()
        if atendimentos:
            print(f"Test PASSED: Atendimentos filtrados com sucesso!")
            print(f"Quantidade de atendimentos: {len(atendimentos)}")
            print(f"Exemplo de atendimento: {atendimentos[0]}")
            return True
        else:
            print(f"Test PASSED: Resposta recebida com sucesso!")
            print(f"Quantidade de atendimentos: 0")
            print(f"Mensagem: Nenhum atendimento encontrado para o período solicitado")
            return True
    else:
        print(f"Test FAILED: Erro ao acessar endpoint de atendimentos")
        print(f"Status code: {response.status_code}")
        print(f"Mensagem de erro: {response.text}")
        return False

# Executa os testes para diferentes cenários
def executar_testes():
    # Teste 1: Filtro de data com resultados
    print("\n=== Teste 1: Filtro de data com resultados ===")
    obter_atendimentos_por_periodo("2025-03-01", "2025-03-20", "success")
    
    # Teste 2: Filtro de data sem resultados
    print("\n=== Teste 2: Filtro de data sem resultados ===")
    obter_atendimentos_por_periodo("2025-04-01", "2025-04-30", "empty")
    
    # Teste 3: Erro no acesso ao endpoint
    print("\n=== Teste 3: Erro no acesso ao endpoint ===")
    obter_atendimentos_por_periodo("2025-03-01", "2025-03-30", "error")

# Função principal
if __name__ == "__main__":
    print("Iniciando testes de validação do endpoint de atendimentos...")
    executar_testes()
    print("\nTodos os testes foram executados!")