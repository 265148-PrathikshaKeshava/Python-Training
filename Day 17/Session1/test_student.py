import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_student_initialization(self):
        name = "Anil"
        age = 12
        grade = "6"
        student = Student(name, age, grade)
        self.assertEqual(student.name, name)
        self.assertEqual(student.age, age)
        self.assertEqual(student.grade, grade)
        self.assertTrue(student.id) 

    def test_to_dict(self):
        name = "Prathiksha"
        age = 12
        grade = "6"
        student = Student(name, age, grade)
        student_dict = student.to_dict()
        self.assertEqual(student_dict['name'], name)
        self.assertEqual(student_dict['age'], age)
        self.assertEqual(student_dict['grade'], grade)
        self.assertTrue(student_dict['id'])  # Ensure ID is included in the dictionary

    def test_from_dict(self):
        data = {
            "id": "12345",
            "name": "Anil",
            "age": 12,
            "grade": "6"
        }
        student = Student.from_dict(data)
        self.assertEqual(student.id, data['id'])
        self.assertEqual(student.name, data['name'])
        self.assertEqual(student.age, data['age'])
        self.assertEqual(student.grade, data['grade'])
