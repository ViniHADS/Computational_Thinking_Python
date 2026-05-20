#Checkpoint 3: Computational Thinking With Python
#Você deverá desenvolver um código em Python (em formato de Notebook ou Python file)
#contendo a resolução do desafio a seguir. Como entrega, deverá enviar o arquivo Python ou
#o repositório do Github com a resolução do desafio via teams. O checkpoint será individual.
#Desafio: Validador de Grade de Estoque (E-commerce)
#Contexto: Você foi contratado por um grande e-commerce de moda que está unificando o
#inventário de suas fábricas. O sistema atual recebe entradas manuais de diversos
#fornecedores, o que gera inconsistências no banco de dados (como letras minúsculas ou
#espaços desnecessários). Sua missão é criar uma função que atue como um "filtro",
#garantindo que apenas tamanhos de roupas válidos e padronizados sejam registrados.
#O que deve ser feito:
#1. Crie a função: Escreva uma função em Python chamada check_product_size.
#2. Parâmetros: 
#- A função deve receber os parâmetros product_id (o id do produto).
#- size_label (texto correspondente ao tamanho da roupa).
#3. Tratamento de Dados:
#- Remova espaços em branco extras (ex: " g " vira "G").
#- Converta a etiqueta para letras maiúsculas (ex: "xg" vira "XG").
#4. Regras de Validação:
#- Tamanho do Texto: A etiqueta deve ter entre 1 e 2 caracteres (ex: 'P' ou 'GG').
#- Existência: O tamanho deve pertencer a grade oficial da empresa. Crie uma
#tupla com as siglas permitidas para serem validadas: P, M, G, GG, XG.
#5. Retorno (Output):
#- Sucesso: Retorne um dicionário no formato: {"product_id": product_id,
#"size_tag": size_label}.
#- Erro: Se o tamanho for inválido ou não existir na grade, retorne uma
#mensagem de erro amigável (string) explicando cada problema.
#6. Requisitos técnicos:
#- Documentação (em formato de Docstring): Escreva o que a função faz, o
#que ela recebe e o que ela retorna.
#- Tratamento de Exceções: Adicione tratamento de exceção ao longo do código.
#- Anotações de tipo: Adicione type hints na definição da função.
#Requisito de Entrega: Além da função, o código enviado deverá conter obrigatoriamente
#a chamada da função passando os diferentes cenários de testes: casos de sucesso, casos
#com espaços e letras minúsculas e casos que forcem os erros de validação. Faça essa
#chamada de função passando os argumentos dos parâmetros de forma nomeada.

# Nome: Vinicius Henrique Araujo da Silva

# typing utilizado para poder usar o método de hints no código.
from typing import Any, Dict, Tuple, Union

VALID_SIZE_TAGS: Tuple[str, ...] = ("P", "M", "G", "GG", "XG")

# product_id é configurado para possuir qualquer nomenclatura, diferente do do size_label que tem o processo de validação logo abaixo
def check_product_size(product_id: Any, size_label: str) -> Union[Dict[str, Any], str]:
    """Valida e padroniza a etiqueta de tamanho de um produto.

    Args:
        product_id: Identificador do produto. Pode ser número ou texto.
        size_label: Texto correspondente ao tamanho da roupa.

    Returns:
        Um dicionário com os dados validados quando a etiqueta for válida,
        ou uma mensagem de erro descrevendo o problema quando a validação falhar.
    """
    try:
        if not isinstance(size_label, str):
            return "Erro: o tamanho deve ser fornecido como texto (string)."

        normalized_size = size_label.strip().upper()

        if len(normalized_size) == 0:
            return "Erro: a etiqueta de tamanho está vazia após remover espaços."

        if not (1 <= len(normalized_size) <= 2):
            return (
                "Erro: a etiqueta deve ter 1 ou 2 caracteres após a normalização. "
                f"Recebido '{normalized_size}' com {len(normalized_size)} caracteres."
            )

        if normalized_size not in VALID_SIZE_TAGS:
            return (
                f"Erro: tamanho inválido '{normalized_size}'. "
                f"As opções válidas são: {', '.join(VALID_SIZE_TAGS)}."
            )

        return {"product_id": product_id, "size_tag": normalized_size}

    except Exception as error:
        return f"Erro inesperado ao validar o tamanho: {error}"


if __name__ == "__main__":
    print('Olá, seja bem-vindo ao nosso atendimento ao cliente')

    # Exemplos de possiveís erros de validação do size_label.
    exemplos = [
        {
            "description": "Sucesso com tamanho válido",
            "product_id": 12345,
            "size_label": "M",
        },
        {
            "description": "Sucesso com espaços e letras minúsculas",
            "product_id": "SKU-987",
            "size_label": " gg ",
        },
        {
            "description": "Erro: tamanho vazio após normalização",
            "product_id": 54321,
            "size_label": "   ",
        },
        {
            "description": "Erro: tamanho inválido",
            "product_id": "SKU-001",
            "size_label": "XX",            
        },
        {
            "description": "Erro: tipo inválido para size_label",
            "product_id": 99999,
            "size_label": 10,  # tipo incorreto
        },
    ]

    # Execução do loop dos exemplos para auxiliar o usuário a preencher.
    for caso in exemplos:
        resultado = check_product_size(
            product_id=caso["product_id"],
            size_label=caso["size_label"],
        )
        print(f"{caso['description']}: {resultado}")

    # Input do usuário para fazer seu teste de validação de id e size do produto.
    print('\nAgora faça sua própria validação:')
    user_product_id = input('Digite o product_id: ').strip()
    user_size_label = input('Digite o tamanho da roupa: ')
    user_resultado = check_product_size(
        product_id=user_product_id,
        size_label=user_size_label,
    )
    print(f'Resultado da validação do usuário: {user_resultado}')
