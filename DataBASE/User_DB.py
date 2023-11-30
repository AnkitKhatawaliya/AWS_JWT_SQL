from DataBASE.DB_Conn import execute_on_database, insert_on_database
from Schemas import SignupModel, LoginModel


def check_table(table_name):
    query = f"""
             CREATE TABLE IF NOT EXISTS {table_name} (
                Name VARCHAR(30),
                Email VARCHAR(30),
                Age INTEGER,
                Username VARCHAR(20),
                Password VARCHAR(300)
             )
             """
    execute_on_database(query)


def add_a_user(User: SignupModel):
    Table_name = "Users"
    check_table(Table_name)
    query = f"""INSERT INTO {Table_name} ( Name, Email, Age, Username, Password) VALUES (%s, %s, %s, %s, %s)"""
    values = (User.Name, User.Email, User.Age, User.Username, User.Password)
    insert_on_database(query, values)


def Check_user(User: LoginModel):
    Table_name = "Users"
    query = f"""SELECT Username, Password FROM {Table_name} WHERE Username = %s AND Password = %s"""
    values = (User.Username, User.Password)
    result = insert_on_database(query, values)
    if result:
        return True
    else:
        return False
