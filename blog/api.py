from rest_framework import routers
from posts import views

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'posts', views.PostViewSet)