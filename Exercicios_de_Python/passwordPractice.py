def check_password(user_id: int | str ,password: str ) -> str | dict:
  """ Função que verifica se a senha tem seus requisitos mínimos.
  
      Args:
        user_id (int | str): ID de usuário.
        password (int | str): senha do usuário.
    
    
      Returns:
        str: Print de sucesso ou de negação apontando o que precisar mudar.
        dict: Dicionário salvando as senhas e o id do usuário.
  """
  data_base = {}
  
  achou_maiuscula = False
  achou_numero = False
  if len(password) >= 8 and len(password) < 20:
    for x in password:
      if x.isdigit():
        achou_numero = True
      if x.isupper():
        achou_maiuscula = True
      
    if achou_maiuscula == True and achou_numero == True:
      data_base.update({'user_id' : user_id, 'password' : password})
      print(f'Pronto, sua senha "{data_base['password']}" foi salva com sucesso no seu ID: {data_base['user_id']}')

    else:
        print('Sua senha precisa ter letras, mínimo 1 número, e mínimo 1 letra maiúscula')
        
  else:
    print('Senha necessita ter entre 8 a 20 caracteres!')
    
check_password(1,'TesteSenha06.') # sucesso
check_password(2,'TesteSenhaCompridaa06.') # Senha muito comprida
check_password(3,'Curta06.') # Senha muito curta
check_password(4,'senhanormal06.') # senha sem letra maiúscula
check_password(4,'senhaSemNum.') # senha sem número

def user_valid_username ():
  """Variável que valida se o username tem somente letras"""
  while true: 
    username = input("Crie o seu usuário (O seu nome de usuário só pode ter letras):  ").strip()

    if username.isalpha():
      return username
    
data_base = {}

userID = user_valid_username

banco_usuarios["username"] = userID

print("\nDados salvos no nosso banco de dados!")
print(banco_usuarios)

