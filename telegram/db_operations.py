import mysql.connector


def apply_register(pers_name, pers_surname, pers_phone, pers_value, pers_photo, pers_user_id):
    connection = mysql.connector.connect(host='localhost',
                                         database='telegram',
                                         user='telegram_bot',
                                         password='bot_telegram',
                                         auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    print(pers_name, pers_surname, pers_phone, pers_value, pers_photo, pers_user_id)
    mysql_insert_query = """INSERT INTO apply_table (name, surname, phone, value, photo, user_id) VALUES (%s, %s, %s, %s, %s, %s) """
    data = (pers_name, pers_surname, pers_phone, pers_value, pers_photo, pers_user_id)
    cursor.execute(mysql_insert_query, data)
    connection.commit()
    cursor.close()
    connection.close()