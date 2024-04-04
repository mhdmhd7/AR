from django.urls import path
from .views import SignUpAPIView, LoginAPIView
urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
