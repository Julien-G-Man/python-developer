class Student:
   # the __init__ method allows us to instantiate the object right before usage
   def __init__(self, name, age, grade):
      self.name = name
      self.age = age
      self.grade = grade
      
   def get_grade(self):
      return self.grade 
   
class Course:
   def __init__(self, name, max_students):
      self.name = name
      self.max_students = max_students 
      self.students = []
      
   def add_student(self, student):
      if len(self.students) < self.max_students:
         self.students.append(student)
         return True
      return False
   
   def get_average_grade(self):
      value = 0
      for student in self.students:
         value += student.get_grade()
      
      return value /  len(self.students)
   
   def list_students(self):
      for student in self.students:
         print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
      return None   
   
s1 = Student("Jay", 20, 85)
s2 = Student("Belle", 22, 92)
s3 = Student("Caleb", 25, 85)

course = Course("Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
average_grade = course.get_average_grade()

print(course.add_student(s3))
print("The average grade is: ", average_grade)
print(course.students[0].name)
print(course.list_students())