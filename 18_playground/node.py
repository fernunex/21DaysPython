class PatientNode:
    def __init__(self, name, age, bed_number):
        self.value = (name, age, bed_number)
        self.next = None