from django.urls import path
from . import views
urlpatterns = [
    path('bigroom/',views.bigroom,name="bigroom"),
    path('ballroom/',views.ballroom,name="ballroom"),
    path('conf/',views.conf,name="conf"),
    path("bookballroom/",views.bookballroom,name="bookballroom"),
    path("bookconferenceroom/",views.bookconferenceroom,name="bookconferenceroom"),
    path("ballsuccess/",views.ballsuccess,name="ballsuccess"),
    path("consuccess/",views.consuccess,name="consuccess"),
    path("cancelmeetingroom/<str:email>/<str:roomno>/<str:roomtype>",views.cancelmeetingroom,name="cancelmeetingroom"),
]