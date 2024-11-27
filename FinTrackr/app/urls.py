from django.urls import path, include
from .views import SignUpView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('sign', SignUpView, basename = 'sign')

urlpatterns = [
    path('', include('routers.urls'))
]