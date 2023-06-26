from rest_framework import routers, permissions
from .views import CategoryViewSet, PostViewSet


router = routers.DefaultRouter()

router.register('api/category', CategoryViewSet, basename='category')
router.register('api/post', PostViewSet, basename='post')

urlpatterns = router.urls