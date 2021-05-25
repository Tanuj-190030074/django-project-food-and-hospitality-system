from django import forms
from . models import DineInTables,Rooms,meetingrooms
class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)

class addroomform(forms.ModelForm):
    class Meta:
        model=Rooms
        exclude=('bookcount',)
        labels={
            "room_no":"enter room number",
            "room_type":"enter room type",
            "is_available":"is it available?",
            "description":"describe about room",
            "price":"enter price",
            "start_date":"Enter available start date",
            "room_image":"upload room image",
        }
        widgets = {
            'start_date':XYZ_DateInput(format=["%Y-%m-%d"],),
        }

class addtableform(forms.ModelForm):
    class Meta:
        model=DineInTables
        fields="__all__"
        labels={
            "table_no":"enter table number",
            "is_available":"is it available?",
            "capacity":"What is the capacity?"
        }

class addmeetingroomform(forms.ModelForm):
    class Meta:
        model=meetingrooms
        fields="__all__"
        labels={
            "room_no":"enter room number",
            "room_type":"enter room type",
            "is_available":"is it available?",
            "start_date":"Enter available start date",
        }
        widgets = {
            'start_date':XYZ_DateInput(format=["%Y-%m-%d"],),
        }

