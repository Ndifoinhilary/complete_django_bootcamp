from django.urls import path, re_path
from rest_framework.routers import SimpleRouter
from .views import CollectionViewSet, ProductViewSet

routers = SimpleRouter()
routers.register("products", ProductViewSet)
routers.register("collection", CollectionViewSet)
urlpatterns = routers.urls

app_name = "store"

# urlpatterns = [
#     path('products/', ProductListView.as_view()),
#     path('products/<int:pk>/', ProductDetailView.as_view()),
#     path('collection/<int:pk>/', CollectionDetailsView.as_view(), name='collection-detail'),
#     path('collections/', CollectionCreateListView.as_view()),
# ]