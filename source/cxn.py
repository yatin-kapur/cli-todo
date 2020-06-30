import pymysql

def get_cxn():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='wplqsym',
                                db='todo')

    return connection