from django.test import TestCase
from . models import bookdineinmodel
# Create your tests here.
class TablesTestCase(TestCase):
    def setUp(self):
        bookdineinmodel.objects.create(email="tanujandhavarapu123@gmail.com",table_no='11',time="7:30pm",space='6')
    def test_data_added(self):
        x = bookdineinmodel.objects.get(email="tanujandhavarapu123@gmail.com",table_no='11',time="7:30pm",space='6')
        self.assertEqual(x.email, 'tanujandhavarapu123@gmail.com')
        self.assertEqual(x.table_no,'11')
    def createbooking(self,email="default@gmail.com",table_no='0',time="6:00pm",space='2'):
        return bookdineinmodel.objects.create(email=email,table_no=table_no,time=time,space=space)
    def testcreatebooking(self):
        email="tanujandhavarapu123@gmail.com"
        table_no='11'
        time="7:30pm"
        space='6'
        x1=self.createbooking(email=email,table_no=table_no,time=time,space=space)
        x2=self.createbooking(email=email,table_no=table_no,time=time,space=space)
        x3=self.createbooking(email=email,table_no=table_no,time=time,space=space)
        qs=bookdineinmodel.objects.filter(email=email)
        self.assertEqual(qs.count(),4)