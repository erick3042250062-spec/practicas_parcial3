import mysql.connector

try:
    conexion= mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'bd_estudiantes'
    )
    cursor = conexion.cursor(buffered=True)

except Exception as e: 
    print(f"Ocurrió un error: {e}")
