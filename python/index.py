# -*- coding: utf8 -*-
from serverless_db_sdk import database

def main_handler(event, context):
    print('Start Serverlsess DB SDK function')

    connection = database().connection(autocommit=False)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM name')
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
