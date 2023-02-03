from rest_framework.routers import DefaultRouter

from API import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('products', views.ProductViewSet, basename='products')

urlpatterns = router.urls
