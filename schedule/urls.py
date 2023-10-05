from django.urls import path
from .views import loginView,signupView,taskView

urlpatterns = [
    path('login/', loginView, name='loginView'),
    path('signup/', signupView, name='signupView'),
    path('task/',taskView, name="taskView")
]