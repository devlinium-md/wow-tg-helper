import psycopg2
conn = psycopg2.connect(dbname='django', user='django',
                        password='6552', host='127.0.0.1', port='5432')


def active():
    cursor = conn.cursor()
    cursor.execute(\
        "SELECT main_page_work_request.id, name, phone_number, mail, commentary, request_date, work_name \
        FROM main_page_work_request, main_page_work_type \
        WHERE main_page_work_request.work_name_id = main_page_work_type.id \
        AND is_done = FALSE AND is_deleted = FALSE \
        ORDER BY main_page_work_request.id ASC")
    all_list = []
    records = cursor.fetchall()
    for element in records:
        all_list.append(element)
    cursor.close()
    return all_list


def done(request_id):
    cursor = conn.cursor()
    cursor.execute(\
        "UPDATE main_page_work_request SET is_done = TRUE WHERE id = %s", (request_id,))
    conn.commit()
    cursor.close()


def delete(request_id):
    cursor = conn.cursor()
    cursor.execute(\
        "UPDATE main_page_work_request SET is_deleted = TRUE WHERE id = %s", (request_id, ))
    conn.commit()
    cursor.close()


def users():
    cursor = conn.cursor()
    cursor.execute( \
        "SELECT tg_id FROM main_page_tg_user")
    all_list = []
    records = cursor.fetchall()
    for element in records:
        all_list.append(element[0])
    cursor.close()
    return all_list

