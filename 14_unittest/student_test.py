import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.ex_student1 = Student('Bilbo', 'Baggins', 4.99, None)
        self.ex_student2 = Student('Jon', 'Snow', 4.5, None)
        print('Set up')

    def tearDown(self):
        print('Tear down')



    def test_email(self):

        self.assertEqual(self.ex_student1.email, 'bilbo.baggins@university.com')
        self.ex_student1.last = 'Bagginss'
        self.assertEqual(self.ex_student1.email, 'bilbo.bagginss@university.com')

        self.assertEqual(self.ex_student2.email, 'jon.snow@university.com')
        self.ex_student2.last = 'Targaryan'
        self.assertEqual(self.ex_student2.email, 'jon.targaryan@university.com')

    def test_fullname(self):

        self.assertEqual(self.ex_student1.fullname, 'Bilbo Baggins')
        self.ex_student1.last = 'Bagginss'
        self.assertEqual(self.ex_student1.fullname, 'Bilbo Bagginss')

        self.assertEqual(self.ex_student2.fullname, 'Jon Snow')
        self.ex_student2.last = 'Targaryan'
        self.assertEqual(self.ex_student2.fullname, 'Jon Targaryan')

    def test_grant_scholarship_succes(self):

        self.ex_student1.grant_scholarship()
        self.assertTrue(self.ex_student1.scholarship)

        self.ex_student2.grant_scholarship()
        self.assertTrue(self.ex_student2.scholarship)

    def test_grant_scholarship_unsucces(self):
        self.ex_student1.student_avg = 3.0
        self.ex_student1.grant_scholarship()
        self.assertFalse(self.ex_student1.scholarship)

        self.ex_student2.student_avg = 3.5
        self.ex_student2.grant_scholarship()
        self.assertFalse(self.ex_student2.scholarship)

if __name__ == '__main__':
    unittest.main()