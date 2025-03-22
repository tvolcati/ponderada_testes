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

