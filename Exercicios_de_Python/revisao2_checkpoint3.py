Exercícios Complementares - Funções
Desafio: Validador de Cadastro
Contexto: Você foi contratado por uma empresa que atende clientes brasileiros, mas o sistema deles é global. 
Sua missão é criar uma função que valide o estado de nascimento de um usuário antes de salvá-lo no banco de dados.

O que deve ser feito: Crie uma função chamada get_user_location que siga os requisitos abaixo:

Parâmetros: A função deve receber o user_id (id do usuário) e o state_code (texto, que seria a sigla do estado).
Tratamento de Dados: Remova espaços em branco extras (ex: " SP " vira "SP"). Converta a sigla para letras maiúsculas (ex: "rs" vira "RS").

Regras de Validação:
- Tamanho: A sigla deve ter exatamente 2 caracteres.
- Existência: A sigla deve ser de um estado brasileiro real (crie uma tupla interna com as siglas: SP, RJ, MG, etc.).
- Retorno (Output): Se tudo estiver correto: Retorne um dicionário com o formato: {"client_id": user_id, "birth_state": state_code}. 
Se houver erro (tamanho errado ou estado inexistente): Retorne uma mensagem de erro amigável (string).

Documentação (Docstring): Escreva o que a função faz e o que ela recebe (parâmetros) e o que ela retorna.

Adicione ao código anotação de tipo ao definir a função e tratamento de exceção.

