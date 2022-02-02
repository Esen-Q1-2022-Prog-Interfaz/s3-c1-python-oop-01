from task import Task
from db import insertTask


class TodoListApp:
    def __init__(self) -> None:
        print("iniciando la instancia...")
        self.menuItems = {
            " 0": "tarea nueva",
            " 1": "terminar tarea",
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
