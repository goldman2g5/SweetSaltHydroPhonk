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


def bebra_put(id):
    with pymssql.connect("46.39.232.190", "TestUser", "vag!nA228##", "Agronomic_App_TestUser") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(f'delete from agricultural_machinery where id_agricultural_machinery = {id}')


####

@app.get("/api/GetTasks")
def get_tasks():
    with pymssql.connect("46.39.232.190", "TestUser", "vag!nA228##", "Agronomic_App_TestUser") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute('select * from ttasks FOR JSON AUTO')
            for row in cursor:
                return row


@app.get("/api/GetTasksById")
def get_tasksId(id):
    with pymssql.connect("46.39.232.190", "TestUser", "vag!nA228##", "Agronomic_App_TestUser") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(f'select * from ttasks where id_task_type = {id} FOR JSON AUTO')
            for row in cursor:
                return row


@app.get("/api/DeleteTasksById")
def post_deleteById(id):
    return 0


@app.post("/api/DeleteTasks")
def post_delete():
    return 0


@app.get("/api/GetChemicalsById")
def get_chemicalsById(id):
    with pymssql.connect("46.39.232.190", "TestUser", "vag!nA228##", "Agronomic_App_TestUser") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(f'select * from chemicals where id_chemical = {id} FOR JSON AUTO')
            for row in cursor:
                return row


@app.get("/api/GetChemicalsById")
def get_chemicals():
    with pymssql.connect("46.39.232.190", "TestUser", "vag!nA228##", "Agronomic_App_TestUser") as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(f'select * from chemicals FOR JSON AUTO')
            for row in cursor:
                return row


if __name__ == '__main__':
    bebra(1)
