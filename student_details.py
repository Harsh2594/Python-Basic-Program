class Student:
    
    def __init__(self, name, roll_No, father_name):
        self.name = name
        self.roll_No = roll_No
        self.father_name = father_name
    
        
    def student_details(self):
        return f"Name:{self.name}\n,Roll_No: {self.roll_No}\n, Father's name:{self.father_name}"
students = []        
student_data = [('harsh',1,'balbir_singh'),
                 ('Balbir',2,'hukum_singh'),
                 ('kanak',3,'abhijeet')]
                 
for data in student_data:
    student = Student(data[0],data[1],data[2])
    students.append(student)
    


def find_student(student_id,students):
    for student in students:
        if student.roll_No == student_id:
            return student
    return None
    
student_id = int(input("Enter student roll no"))    
student =  find_student(student_id,students) 

print(student.student_details())  

    
    
    
    
    
    
    
    
    