from task import Task
from db import insertTask, getAllTasks, updateFinishTaskById, getTaskById, getPendingTasks


class TodoListApp:
    def __init__(self) -> None:
        print("iniciando la instancia...")
        self.menuItems = {
            " 0": "tarea nueva",
            " 1": "mostrar todas las tareas no terminadas",
            " 2": "mostrar todas las tareas",
            " 3": "terminar tarea",
            "-1": "exit",
        }

    def run(self):
        while True:
            self.showMenu()
            option = int(input("option: "))
            if option == -1:
                break
            elif option == 0:
                self.createNewTask()
            elif option == 1:
                self.showPendingTasks()
            elif option == 2:
                self.showAllTasks()
            elif option == 3:
                self.finishTaskById()
            else:
                print("la aplicacion continua...")

    def showMenu(self):
        print()
        print()
        for item, value in self.menuItems.items():
            print(f"{item}: {value}")
        print()

    def createNewTask(self):
        print()
        print()
        description = input("description: ")
        newTask = Task(description)
        insertTask(newTask)

    def showAllTasks(self):
        print()
        print()
        """ lista de diccionarios """
        taskList = getAllTasks()
        for task in taskList:
            print(task)

    def finishTaskById(self):
        print()
        print()
        id = int(input("id: "))
        updateFinishTaskById(id)
        finishedTask = getTaskById(id)
        print()
        print()
        print(finishedTask)

    def showPendingTasks(self):
        print()
        print()
        pendingTaskList = getPendingTasks()
        for task in pendingTaskList:
            print(task)
