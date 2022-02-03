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
            sql = "INSERT INTO `todolistdb`.`tasks`(`id`,`description`,`is_finished`) VALUES(%s,%s,%s);"
            data = (task.id, task.description, int(task.isFinished))
            cursor.execute(sql, data)
        connection.commit()


def getAllTasks() -> list:
    connection = createConnectionToDB()
    result = []
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `tasks`.`id`, `tasks`.`description`, `tasks`.`is_finished` FROM `todolistdb`.`tasks`;"
            cursor.execute(sql)
            result = cursor.fetchall()
    return result


def updateFinishTaskById(id):
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `todolistdb`.`tasks` SET `is_finished` = %s WHERE `id` = %s;"
            data = (1, id)
            cursor.execute(sql, data)
        connection.commit()


def getTaskById(id) -> dict:
    connection = createConnectionToDB()
    result = None
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `tasks`.`id`, `tasks`.`description`, `tasks`.`is_finished` FROM `todolistdb`.`tasks` where `tasks`.`id`= %s;"
            data = (id,)
            cursor.execute(sql, data)
            result = cursor.fetchone()
    return result


def getPendingTasks() -> list:
    connection = createConnectionToDB()
    result = []
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `tasks`.`id`, `tasks`.`description`, `tasks`.`is_finished` FROM `todolistdb`.`tasks` where `tasks`.`is_finished` = 0;"
            cursor.execute(sql)
            result = cursor.fetchall()
    return result
