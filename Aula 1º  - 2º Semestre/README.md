Como Fazer um Code Review no GitHub 
Passo 1: Recebendo e Acessando o Pull Request (PR) 
1. No repositório no GitHub, clique na aba Pull requests. 
2. Clique no PR que foi atribuído a você ou que precisa de revisão. 
3. Leia primeiro a descrição e o título do PR: Entenda o contexto. O autor deve ter explicado o que foi feito, por que foi feito e como testar. 

Passo 2: Navegando até a aba "Files changed" 
1. Clique na aba Files changed (Arquivos alterados) na parte superior do PR. 
2. É aqui que você verá a visualização em Diff: o Lado esquerdo / Vermelho: Como o código era antes (removerá/substituirá). o Lado direito / Verde: Como o código ficou agora (código novo). 

Passo 3: Adicionando Comentários e Sugestões nas Linhas 
Ao analisar o código linha por linha: 
1. Fazer um comentário simples: 
- Passe o cursor sobre o número da linha no código e clique no ícone azul de mais (+). 
- Escreva seu comentário apontando a melhoria ou dúvida. 

2. Propor uma mudança de código direta: 
- Em vez de dizer "mude a variável X para Y", clique no ícone de folha com sinais de mais e menos (+-) na barra de ferramentas do comentário.
- O GitHub criará um bloco com o código atual. Edite o código diretamente ali com a sua sugestão.
- Vantagem: O autor do PR poderá aceitar sua sugestão com um único clique! 

3. Iniciando a Revisão em Rascunho: 
- No seu primeiro comentário, clique no botão Start a review (Iniciar revisão), em vez de "Add single comment".
- Nos comentários seguintes do mesmo PR, clique em Add review comment. 

Passo 4: Finalizando e Submetendo o Veredito
1. Clique no botão verde Review changes no canto superior direito da tela.
2. Escreva uma mensagem geral de resumo (ex: "Excelente trabalho! Deixei apenas alguns pontos menores de atenção em relação ao tratamento de erros."). 
3. Escolha uma das 3 opções de veredito: 
- Comment: Envia suas observações gerais sem aprovar nem bloquear o PR.
- Approve: Aprova o PR. O código está pronto e validado para ser mesclado (merge) na branch principal.
- Request changes: Bloqueia o merge e exige que o autor corrija os problemas críticos que você apontou antes que o código vá para produção. 

Passo 5: Last step
4. Clique em Submit review. 