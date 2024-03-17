from django.urls import path, re_path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from .views import CollectionViewSet, ProductViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet, basename='products')
router.register("collection", CollectionViewSet)

product_router =  routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", ReviewViewSet, basename='reviews-list')
urlpatterns = router.urls + product_router.urls

app_name = "store"

# urlpatterns = [
#     path('products/', ProductListView.as_view()),
#     path('products/<int:pk>/', ProductDetailView.as_view()),
#     path('collection/<int:pk>/', CollectionDetailsView.as_view(), name='collection-detail'),
#     path('collections/', CollectionCreateListView.as_view()),
# ]