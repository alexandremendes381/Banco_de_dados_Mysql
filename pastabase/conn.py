import mysql.connector


class DbConnection:
    def connect(self):
        mydb = mysql.connector.connect(
            host="localhost", user="root", password="96828255axz", database="cadastro")
        return mydb

    def select(self):
        db = self.connect()
        mycursor = db.cursor()
        mycursor.execute("select * from pessoas")
        myresult = mycursor.fetchall()
        print(myresult)

    def insert(self, nome:str, sexo:str, idade:int, altura:float, peso:float, nacionalidade:str ):
        db = self.connect()
        mycursor = db.cursor()
        sql = "INSERT INTO pessoas (nome, idade, sexo, peso, altura, nacionalidade) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nome, idade, sexo, peso, altura, nacionalidade )
        mycursor.execute(sql,val)
        db.commit()

#app = DbConnection()
#app.insert(nome, idade, sexo, peso, altura, nacionalidade)
#app.select()

    def delete(self, nome):
        db = self.connect()
        mycursor = db.cursor()
        sql = "DELETE FROM pessoas WHERE nome = %s"
        adr = (nome,)
        mycursor.execute(sql, adr)
        db.commit()
        mycursor = db.cursor()
#app = DbConnection()
#app.select()

