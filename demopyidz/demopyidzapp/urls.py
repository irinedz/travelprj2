from. import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('',views.pj,name='pj'),
    #path('add/',views.addition,name="addition"),
    #path('contact/',views.contact,name="contact"),
    #path('details/',views.details,name="details"),
    #path('thanks/',views.thanks,name="thanks")
]
