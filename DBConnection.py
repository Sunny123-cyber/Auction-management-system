import pyodbc
conn_str = (
                "DRIVER={MySQL ODBC 8.4 ANSI Driver};"
                "SERVER=localhost;"
                "DATABASE=registration;"
                "USER=root;"
                "PASSWORD=Sunny@12345;"
                "PORT=3306;"
            )

conn = pyodbc.connect(conn_str)