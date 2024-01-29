import requests

def create(url, name):
    try:
        request = requests.post(f"{url}/", json={'name' : name})

        if request.status_code == 200:
            print(f'Usuário {name} criado com sucesso!')
            return request.json()
        else:
            print("Erro ao acessar a API:", request.status_code)
            return None
    except Exception as e:
        print("Erro ao acessar a API:", str(e))
        return None

def read(url):
    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            return resposta.json()
        else:
            print("Erro ao acessar a API:", resposta.status_code)
            return None
    except Exception as e:
        print("Erro ao acessar a API:", str(e))
        return None

def put(url, user_id, new_name):
    try:
        resposta = requests.put(f"{url}/{user_id}", json={"name": new_name})
        #assert resposta.status_code == 200
        #assert resposta.json()["message"] == f"User with ID {user_id} updated ssuccessfully"
        if resposta.status_code == 200:
            print(f'Usuário {user_id} atualizado com sucesso para o nome {new_name}!')
            return resposta.json()
        else:
            print("Erro ao acessar a API:", resposta.status_code)
            return None
    except Exception as e:
        print("Erro ao acessar a API:", str(e))
        return None
    
def delete(url, user_id):
    try:
        resposta = requests.delete(f"{url}/{user_id}")
        if resposta.status_code == 200:
            print(f'Usuário {user_id} deletado com sucesso!')
            return resposta.json()
        else:
            print("Erro ao acessar a API:", resposta.status_code)
            return None
    except Exception as e:
        print("Erro ao acessar a API:", str(e))
        return None



url_da_api = "http://127.0.0.1:8000/users"

escolha = 5

while(escolha !=0):
    escolha = int(input("""
                      1 - create 
                      2 - read
                      3 - update
                      4 - delete
                      """))
    if escolha == 1:
        #create
        name = input('Digite o nome do usuario: ')
        create(url_da_api, name)
        
    elif escolha == 2:
        #read
        print(f'Usuários: \n{read(url_da_api)}')
    elif escolha == 3:
        #update
        new_name = input('Digite o novo nome do usuário: ')
        user_id = int(input('Digite o ID do usuário: '))
        put(url_da_api, user_id, new_name)
        
    elif escolha == 4:
        #delete
        user_id = int(input('Digite o ID do usuário: '))
        delete(url_da_api, user_id)
        
    else: 
        print('faça uma escolha')

