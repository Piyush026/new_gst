# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database='scraper'
# )
#
# mycursor = mydb.cursor()

import psycopg2

conn = psycopg2.connect(database="gst_scrapper_db", user="uplauds_dev", password="uPLAUDS!@126",
                        host="uplauds-dev-lr7.c1h7mjd0doow.ap-south-1.rds.amazonaws.com", port="5432")

print("Opened database successfully")
cur = conn.cursor()


# mycursor.execute("CREATE DATABASE scraper")
# mycursor.execute("CREATE TABLE gst (cin VARCHAR(255), cmp_name VARCHAR(255), gstin VARCHAR(255))")

def insert_row(val):
    sql = "INSERT INTO public.uplauds_corp_gst (cin, c_name,gstin) VALUES (%s, %s, %s)"

    cur.execute(sql, val)

    conn.commit()

    print("record inserted.")


# data = ("abc", "abc", "abc")
# insert_row(data)
