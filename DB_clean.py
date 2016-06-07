# -*- coding:utf-8 -*-  
from __future__ import print_function
import psycopg2

__author__ = "JOHNKYON"

connection = psycopg2.connect(database="mydb", user="postgres", password="postgres", host="127.0.0.1", port="5432")

cursor = connection.cursor()
cursor2 = connection.cursor()

select_sql = "SELECT * FROM person"
update_sql = "INSERT INTO clean_person (id, \"major\", \"edu_intr\", \"work_title\", \"work_intr\") VALUES (%s, %s, %s, %s, %s)"

cursor.execute(select_sql)

counter = 0

update_array = []

text = cursor.fetchone()
while text:
    try:
        text = list(text)
        for a in range(1,5):
            text[a] = text[a].decode('utf8')
        n1 = len(text[3])
        n2 = len(text[4])
        if text[4][0:((n2 / 3) - 1)] and text[4][(n2 / 3):((2 * n2 / 3) - 1)] and text[4][((2 * n2 / 3) - 1):n2 - 1]:
            text[4] = text[4][0:(n2 / 3)]
        if text[3][0:((n1 / 3) - 1)] and text[3][(n1 / 3):((2 * n1 / 3) - 1)] and text[3][((2 * n1 / 3) - 1):n1 - 1]:
            text[3] = text[3][0:(n1 / 3)]
            update_array.append(text)
    except:
        text = cursor.fetchone()
        continue
    text = cursor.fetchone()

connection.commit()

# print update_array

for ele in update_array:
    # try:
    cursor2.execute(update_sql, ele)
    counter += 1
    print(counter)
    # except:
    #     continue

connection.commit()
connection.close()
