# https://platzi.com/clases/7967-python-21-dias/63737-playground-crea-un-task-manager-con-maps/

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def addTask(self, task, tags):
        """Se encargará de agregar tareas al Map.
        Es importante convertir todas las letras de
        la tarea a minúsculas usando lower() para verificar 
        si la tarea ya existe. En caso de que exista, se agregarán 
        las nuevas etiquetas al Set correspondiente. Si la tarea no 
        existe, se creará una nueva entrada en el Map con un Set de 
        etiquetas inicializado con las etiquetas proporcionadas."""
        if task.lower() in self.tasks:
            self.tasks[task.lower()] = self.tasks[task.lower()].union((set(tags)))
        else:
            self.tasks[task.lower()] = set(tags)

    def printTasks(self):
        """Se encargará de retornar todas las tareas creadas con sus etiquetas."""
        return self.tasks

if __name__ == '__main__':
    # myTaskManager = TaskManager()
    # myTaskManager.addTask("Comprar leche", ["compras", "urgente"])
    # myTaskManager.addTask("Sacar al perro", ["mascotas"])
    # myTaskManager.addTask("Hacer ejercicio", ["salud"])
    # print(myTaskManager.printTasks())

    myTaskManager = TaskManager()
    myTaskManager.addTask("Comprar leche", ["compras", "urgente"])
    myTaskManager.addTask("Sacar al perro", ["mascotas"])
    myTaskManager.addTask("Hacer ejercicio", ["salud"])
    myTaskManager.addTask("Comprar leche", ["lacteos"])

    print(myTaskManager.printTasks())
