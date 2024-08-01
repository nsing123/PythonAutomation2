import pymysql
def database_connection():
    connection=None
    try:
        connection=pymysql.connect(host='localhost',
                                 user='root',
                                 password='Root@123',
                                 database='fitness',
                                 cursorclass=pymysql.cursors.DictCursor) # this connection for retriving data from sql in form of dictionary
        #print("MySQL datyabase is connected suscessfully")
    except Exception as err:
        print(f"Error :{err}")
    return connection