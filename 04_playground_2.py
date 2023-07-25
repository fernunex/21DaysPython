# Obtén el promedio de los estudiantes
# https://platzi.com/clases/7967-python-21-dias/63508-obten-el-promedio-de-los-estudiantes/

def get_student_average(students):
    student_average = [round(sum(student['grades'])/len(student['grades']), 2) for student in students]
    class_average = round(sum(student_average) / len(student_average), 2)
    
    lst_students = [{
            "name": student['name'],
            "average": grade
            } 
            for student, grade in zip(students, student_average)]
    
    output = {
        "class_average": class_average,
        "students": lst_students
    }

    return output


my_dict = [{
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
    },
{
    "name": "Jose",
    "grades": [99, 71, 88, 96],
    },
{
    "name": "Maria",
    "grades": [92, 81, 80, 96],
    },
]

grades = get_student_average(my_dict)
print(grades)