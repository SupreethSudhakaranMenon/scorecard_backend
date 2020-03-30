import pymysql


def databaseOperation(sqlQuery):
    db = pymysql.connect("localhost", "root", "password", "mifostenant")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        cursor.execute(sqlQuery)
        return cursor.fetchall()
    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()


def databaseOperationSave(sqlQuery):
    db = pymysql.connect("localhost", "root", "password", "mifostenant")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        cursor.execute(sqlQuery)
        id = cursor.lastrowid
        db.commit()
        # return id
        # return cursor.fetchall()
    except:
        print("Error: unable to insert data")
        return False

    # disconnect from server
    db.close()
    return id