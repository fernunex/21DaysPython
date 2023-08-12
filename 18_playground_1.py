# https://platzi.com/clases/7967-python-21-dias/63841-playground-implementacion-de-una-singly-linked-lis/

from node import PatientNode
# use 'from Node import PatientNode' in playground 

class PatientList:
    def __init__(self, max_beds):
        self.max_beds = max_beds
        self.avaible_beds = {x for x in range(1, max_beds + 1)}
        self.length = 1
        self.head = None
        self.tail = None

    def addPatient(self, name, age):
        """agrega un nuevo paciente a la lista, asignándole la próxima 
        cama disponible. Si no hay camas disponibles, debe lanzar un 
        error con el mensaje 'No hay camas disponibles'"""

        if self.head is None:
            # print("first")
            new_patient = PatientNode(name, age, 1)
            self.head = new_patient
            self.tail = new_patient
            self.avaible_beds.discard(1)
            return
        elif self.length < self.max_beds:
            next_bed = min(self.avaible_beds)
            self.avaible_beds.discard(next_bed)
            new_patient = PatientNode(name, age, next_bed)

            if next_bed == 1:
                new_patient.next = self.head
                self.head = new_patient
            
            else:
                current_patient = self.head
                while current_patient and (current_patient.value[2] != next_bed - 1):
                    # print("into")
                    current_patient = current_patient.next
                
                new_patient.next = current_patient.next
                current_patient.next = new_patient
        else:
            raise Exception("No hay camas disponibles")
        
        self.length += 1

    def removePatient(self, name):
        """remueve al paciente con el nombre especificado de la lista y libera su cama. 
        Si el paciente no se encuentra en la lista, debe lanzar un error con el mensaje 
        'Paciente no encontrado'."""
        # Esta vacia
        if self.head is None:
            raise Exception('Paciente no encontrado')
        
        # Es el primer nodo
        if self.head.value[0] == name:
            self.avaible_beds.add(self.head.value[2])
            self.head = self.head.next
            self.length -= 1
        
        # Es cualquier otro nodo
        else:
            current_patient = self.head
            while current_patient.next.next and current_patient.next.value[0] != name:
                    current_patient = current_patient.next
            if current_patient.next.value[0] == name:
                self.avaible_beds.add(current_patient.next.value[2])
                current_patient.next = current_patient.next.next
                self.length -= 1
            else:
                raise Exception('Paciente no encontrado')

                


    def getPatient(self, name):
        """retorna la información del paciente con el nombre especificado en el 
        siguiente formato {name, age, bedNumber}. Si el paciente no se encuentra en la lista, 
        debe lanzar un error con el mensaje 'Paciente no encontrado'"""
        current_node = self.head
        while current_node:
            if current_node.value[0] == name:
                return {'name': current_node.value[0],
                        'age': current_node.value[1],
                        'bedNumber': current_node.value[2]}
            current_node = current_node.next

        raise Exception('Paciente no encontrado')


    def getPatientList(self):
        """retorna una lista con la información de todos los pacientes en la lista, 
        cada paciente deberá tener el siguiente formato {name, age, bedNumber}."""
        list_info = []
        current = self.head
        while current:
            info_patient = current.value
            list_info.append({'name': info_patient[0],
                        'age': info_patient[1],
                        'bedNumber': info_patient[2]})
            current = current.next
        return list_info

    def getAvailableBeds(self):
        """Retorna un número con el total de camas disponibles."""
        return len(self.avaible_beds)

if __name__ == '__main__':
    single_L = PatientList(4)
    single_L.addPatient("Paciente 1", 20)
    single_L.addPatient("Paciente 2", 30)
    single_L.addPatient("Paciente 3", 50)
    single_L.addPatient("Paciente 4", 99)
    # print("****"*20)
    # single_L.addPatient("Paciente 5", 919)
    single_L.removePatient('Paciente 4')
    single_L.addPatient("Richi", 919)
    print(single_L.getPatientList())
    print(single_L.getPatient('Paciente 3'))
    print(single_L.getAvailableBeds())
    print(single_L.length)
    print(single_L.avaible_beds)
    # print(single_L.head.value)
    # print(single_L.head.next.value)
    # print(single_L.head.next.next.value)
    # print(single_L.head.next.next.next.value)
    #print(single_L.head.next.next.next.next.value) # NONE



