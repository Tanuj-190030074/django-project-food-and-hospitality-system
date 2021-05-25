from django.test import TestCase
from . models import bookmeetingroommodel
# Create your tests here.
class RoomsTestCase(TestCase):
    def setUp(self):
        bookmeetingroommodel.objects.create(email="tanujandhavarapu123@gmail.com",room_no="1",room_type="ball room",start_date="2020-05-01",end_date="2020-05-05")
    def test_data_added(self):
        x = bookmeetingroommodel.objects.get(email="tanujandhavarapu123@gmail.com",room_no="1",room_type="ball room",start_date="2020-05-01",end_date="2020-05-05")
        self.assertEqual(x.email, 'tanujandhavarapu123@gmail.com')
        self.assertEqual(x.room_no,'1')
        self.assertEqual(x.room_type,'ball room')
    def createbooking(self,email="dummy@gmail.com",room_no="0",room_type="ball room",start_date="2020-00-01",end_date="2020-00-02"):
        return bookmeetingroommodel.objects.create(email=email,room_no=room_no,room_type=room_type,start_date=start_date,end_date=end_date)
    def testcreatebooking(self):
        email="tanujandhavarapu123@gmail.com"
        room_no="4"
        room_type="ball room"
        start_date="2020-05-01"
        end_date="2020-05-05"
        x1=self.createbooking(email=email,room_no=room_no,room_type=room_type,start_date=start_date,end_date=end_date)
        x2=self.createbooking(email=email,room_no='2',room_type=room_type,start_date=start_date,end_date=end_date)
        x3=self.createbooking(email=email,room_no='3',room_type=room_type,start_date=start_date,end_date=end_date)
        qs=bookmeetingroommodel.objects.all()
        self.assertEqual(qs.count(),4)