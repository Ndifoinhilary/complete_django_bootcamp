from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from store.models import Collection, OrderItem, Product
from store.serializers import CollectionSerializer, ProductSerializer 



# learning and working with viewsets 

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def  get_context_data(self, **kwargs):
        context = {'request': self.request}
        return context
    
      
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id = kwargs['pk']).count() > 0:
            return Response( {'error': "Can not delete this collection since it has some product assoiciated with it."} ,  status=status.HTTP_403_FORBIDDEN)
        
        return super().destroy(request, *args, **kwargs)





# learning and working with viewsets 

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
    def get_context_data(self, **kwargs):
        context = {'request':self.request}
        return context
    

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response( {'error': "Can not delete this collection since it has some product assoiciated with it."} ,  status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
  


# Working with genenrict views 
class CollectionCreateListView(ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_context_data(self, **kwargs):
        context = {'request':self.request}
        return context
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response( {'error': "Can not delete this collection since it has some product assoiciated with it."} ,  status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)






# Working with genenrict views 

class CollectionDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response( {'error': "Can not delete this collection since it has some product assoiciated with it."} ,  status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)



