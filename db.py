from task import Task
import pymysql.cursors


def createConnectionToDB():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="todolistdb",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def insertTask(task):
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            """INSERT INTO `todolistdb`.`tasks`(`id`,`description`,`is_finished`) VALUES(0,'t',0);"""
            print(task)
            sql = "INSERT INTO `todolistdb`.`tasks`(`id`,`description`,`is_finished`) VALUES(%s,%s,%s);"
            data = (task.id, task.description, int(task.isFinished))
            print(data)
            print(type(data))
            cursor.execute(sql, data)
        connection.commit()
