from fastapi import FastAPI
import libsql_experimental as libsql
from pydantic import BaseModel


app = FastAPI()


url = ''
auth_token = ''
con = libsql.connect(database=url, auth_token=auth_token)
cur = con.cursor()



class User(BaseModel):
    name: str


app = FastAPI()

#create
@app.post("/users/")
async def create_user(usuario: User):
    try:
        # Executar a consulta SQL com placeholders
        con.execute("BEGIN")
        cur.execute("INSERT INTO users (name) VALUES (?)", (usuario.name,))
        #con.commit()  # Comitar a transação

        # Fechar a conexão com o banco de dados
        cur.close()

        # Retornar uma resposta
        return {"message": "Usuário criado com sucesso"}
    except Exception as e:
        # Se ocorrer algum erro, reverta a transação
        con.rollback()
        return {"error": str(e)}
    finally:
        # Sempre feche a conexão com o banco de dados
        cur.close()

#read
@app.get("/users")
def read():
    rows = cur.execute("SELECT * FROM users").fetchall()
    cur.close()
    return rows

#update
@app.put("/users/{user_id}")
async def update_user(user_id: int, new_name: User):
    try:
        # Começar uma transação
        con.execute("BEGIN")

        # Executar a consulta SQL para atualizar o nome do usuário pelo ID
        cur.execute("UPDATE users SET name = ? WHERE id = ?", (new_name.name, user_id))
        
        # Comitar a transação
        #con.commit()

           # Retornar uma resposta
        return {"message": f"Usuário com ID {user_id} atualizado com sucesso"}
    except Exception as e:
        # Se ocorrer algum erro, reverta a transação
        con.rollback()
        return {"error": str(e)}
    finally:
        # Sempre feche a conexão com o banco de dados
        cur.close()

#delete
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    try:
        # Começar uma transação
        con.execute("BEGIN")

        # Executar a consulta SQL para deletar o usuário pelo ID
        cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
        
        # Comitar a transação
        #con.commit()

        # Retornar uma resposta
        return {"message": f"Usuário com ID {user_id} deletado com sucesso"}
    except Exception as e:
        # Se ocorrer algum erro, reverta a transação
        con.rollback()
        return {"error": str(e)}
    finally:
        # Sempre feche a conexão com o banco de dados
        cur.close()

'''
#create
@app.post("/products")
def create(product: Products, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

#read
@app.get("/products")
def read(db: Session = Depends(get_db)):
    allproducts = db.query(models.Product).all()
    return allproducts

#delete
@app.delete("/delete/{id}")
def delete(id: int, Session: Depends(get_db)):
    delete_post = db.query(models.Product).filter(models.Product.id == id)
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NO_CONTENT, detail="Product not found")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#update
@app.put("/update/{id}")
def update(id: int, product: Products, db: Session = Depends(get_db)):
    update_post = db.query(models.Product).filter(models.Product.id == id)
    if update_post == None:
        raise HTTPException(status_code=status.HTTP_404_NO_CONTENT, detail="Product not found")
    else:
        update_post.update(product.dict(), synchronize_session=False)
        db.commit()
        db.refresh(update_post)
    return update_post
    
'''