from django.urls import path
from someapp import views



urlpatterns = [
    path('index/',views.index),
    path('profile/',views.profile),
    path('add/',views.add),
    path('submit/',views.submit),
    path('addcomment/',views.addComment),
    path('viewcomments/',views.showComments),
    path('deletecomment/',views.delComment),



]
