import pyodbc
import sqlalchemy


class AccessDatabaseSqlServer:
    host = ''  # Hostname o IP server
    database = ''  # name database
    user = ''  # user hostname or ip server
    password = ''  # password hostname or ip server

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        print(f"Parameter access database: ({self.host}, {self.database}, {self.user}, {self.password})")

    def open_conection(self):
        cnx = pyodbc.connect("DRIVER={ODBC Driver 13 for SQL Server}; SERVER=" +
                             self.host +
                             ";DATABASE=" +
                             self.database +
                             ";UID=" +
                             self.user +
                             ";PWD=" +
                             self.password)

        if cnx:
            print("Conexion Aperturada : ", cnx)
        return cnx

    def insert(self, io, schema, table_name, driver_string):
        engine = sqlalchemy.create_engine("mssql+pyodbc://" + self.user + ":" + self.password + "@" + self.host
                                          + ":1433/" + self.database + "?driver=" + driver_string, pool_size=0,
                                          max_overflow=-1, )

        io.to_sql(table_name, engine, schema=schema, if_exists='append', chunksize=50, index=False)

    def __del__(self):
        print("El espacio a sido liberado")


ac = AccessDatabaseSqlServer('PEJCB933SQL', 'Rimac', 'sa_Desarrollo', 'Desa_BI++2019')
ac.insert("DataFrame", "dbo", "Table", "Driver 13 SQLServer")


