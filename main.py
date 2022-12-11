import pymssql
from fastapi import FastAPI

constr = "server='46.39.232.190',user='TestUser',password='vag!nA228##',database='Agronomic_App_TestUser"

app = FastAPI()


@app.get("/api/GetAgriculturalMachineries")
def ebera():
    with pymssql.connect("46.39.232.190", "TestUser", "vag!nA228##", "Agronomic_App_TestUser") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('select * from agricultural_machinery FOR JSON AUTO')
            for row in cursor:
                return row


@app.get("/api/GetAgriculturalMachineryById")
def bebra(id):
    with pymssql.connect("46.39.232.190", "TestUser", "vag!nA228##", "Agronomic_App_TestUser") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(f'select * from agricultural_machinery where id_agricultural_machinery = {id} FOR JSON AUTO')
            for row in cursor:
                return row


@app.get("/api/DeleteAgriculturalMachinery")
def bebra_delete(id):
    with pymssql.connect("46.39.232.190", "TestUser", "vag!nA228##", "Agronomic_App_TestUser") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(f'delete from agricultural_machinery where id_agricultural_machinery = {id}')



def convert(sql_result):
    result = []
    for i in sql_result:
        result.append({"id": i[0], "type": i[1], "title": i[2], "content": i[3], "lastSentAt": i[4]})
    return result


if __name__ == '__main__':
    bebra(1)

