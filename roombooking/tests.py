from django.test import TestCase
from . models import bookroommodel
# Create your tests here.
class RoomsTestCase(TestCase):
    def setUp(self):
        bookroommodel.objects.create(email="tanujandhavarapu123@gmail.com",room_no="1",room_type="king guestroom",price=100,start_date="2020-05-01",end_date="2020-05-05")
    def test_data_added(self):
        x = bookroommodel.objects.get(email="tanujandhavarapu123@gmail.com",room_no="1",room_type="king guestroom",price=100,start_date="2020-05-01",end_date="2020-05-05")
        self.assertEqual(x.email, 'tanujandhavarapu123@gmail.com')
        self.assertEqual(x.room_no,'1')
        self.assertEqual(x.room_type,'king guestroom')
        self.assertEqual(x.price,100)
    def createbooking(self,email="dummy@gmail.com",room_no="0",room_type="king guestroom",price=10,start_date="2020-00-01",end_date="2020-00-02"):
        return bookroommodel.objects.create(email=email,room_no=room_no,room_type=room_type,price=price,start_date=start_date,end_date=end_date)
    def testcreatebooking(self):
        email="tanujandhavarapu123@gmail.com"
        room_no="4"
        room_type="king guestroom"
        price=100
        start_date="2020-05-01"
        end_date="2020-05-05"
        x1=self.createbooking(email=email,room_no=room_no,room_type=room_type,price=price,start_date=start_date,end_date=end_date)
        x2=self.createbooking(email=email,room_no='2',room_type=room_type,price=price,start_date=start_date,end_date=end_date)
        x3=self.createbooking(email=email,room_no='3',room_type=room_type,price=price,start_date=start_date,end_date=end_date)
        qs=bookroommodel.objects.all()
        self.assertEqual(qs.count(),4)