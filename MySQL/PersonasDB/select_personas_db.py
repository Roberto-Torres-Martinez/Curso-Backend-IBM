import MySQLdb

try:
    print("Intentando conectar con mysqlclient...")
    conn = MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        passwd='admin',
        db='personas_db',
        port=3306
    )
    print("Conexión exitosa")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas")
    resultado = cursor.fetchall()
    print(f"Registros: {resultado}")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("Conexión cerrada")
