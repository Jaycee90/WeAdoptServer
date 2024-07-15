from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('adopt', views.AdoptViewSet, basename='adopt')

urlpatterns = [
   
]

urlpatterns += router.urls