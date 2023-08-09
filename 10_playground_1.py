#https://platzi.com/clases/7967-python-21-dias/63840-playground-crea-un-task-manager-usando-closures/

def createTaskPlanner():
    tareas = []

    def addTask(task):
        task['completed'] = False
        tareas.append(task)
        

    def removeTask(value):
        i = -1
        found = False
        while not found and i < len(tareas):
            i += 1
            if tareas[i]['id'] == value or tareas[i]['name'] == value:
                found = True
        tareas.pop(i)

    def getTasks():
        return tareas
        
    
    def getPendingTasks():
        return list(filter(lambda x: x['completed'] == False, tareas))
        
    
    def getCompletedTasks():
        return list(filter(lambda x: x['completed'] == True, tareas))

    
    def markTaskAsCompleted(value):
        i = -1
        found = False
        while not found and i < len(tareas):
            i += 1
            if tareas[i]['id'] == value or tareas[i]['name'] == value:
                found = True
        
        tareas[i]['completed'] = True
    
    def getSortedTasksByPriority():
        return sorted(tareas, key= lambda x: x['priority'])
    
    def filterTasksByTag(tag):
        return list(filter(lambda x: tag in x['tags'], tareas))
    
    def updateTask(taskId, updates):
        # Get index of task
        i = -1
        found = False
        while not found and i < len(tareas):
            i += 1
            if tareas[i]['id'] == taskId:
                found = True
        
        # Actualization
        tareas[i] = tareas[i] | updates
        
    
    return {'addTask': addTask, 'removeTask': removeTask, 'getTasks': getTasks,
            'getPendingTasks': getPendingTasks, 'getCompletedTasks': getCompletedTasks,
            'markTaskAsCompleted': markTaskAsCompleted, 'getSortedTasksByPriority': getSortedTasksByPriority,
            'filterTasksByTag': filterTasksByTag, 'updateTask':updateTask}


# planner = createTaskPlanner()
# planner['addTask']({
#     'id': 1,
#     'name': 'Comprar leche',
#     'priority': 1,
#     'tags': ['shopping', 'home']
# })

# planner['addTask']({
#     'id': 2,
#     'name': 'Llamar a Juan',
#     'priority': 3,
#     'tags': ['personal']
# })

# planner['markTaskAsCompleted']('Llamar a Juan')

# print(planner['getCompletedTasks']())


# planner = createTaskPlanner()

# planner['addTask']({
#     'id': 1,
#     'name': 'Comprar leche',
#     'priority': 1,
#     'tags': ['shopping', 'home']
# })

# planner['addTask']({
#     'id': 2,
#     'name': 'Llamar a Juan',
#     'priority': 3,
#     'tags': ['personal']
# })

# print(planner['filterTasksByTag']('shopping'))