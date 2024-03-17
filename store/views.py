from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from pprint import pprint
from store.filters import ProductFilter
from store.models import Collection, OrderItem, Product, Review
from store.serializers import CollectionSerializer, ProductSerializer, ReviewSerializer 



# learning and working with viewsets 

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# generic filtering methods
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def  get_context_data(self, **kwargs):
        context = {'request': self.request}
        return context
    # performing the filtering handdy 
    # def get_queryset(self):
    #     queryset  = Product.objects.all()
    #     collection_id = self.request.query_params.get('collection_id')
    #     if collection_id is not None:
    #         queryset =  queryset.filter(collection_id=collection_id)
    #     return queryset
    
      
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



# creating the reivew view for a product
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
# getting all the reviews for a particular product 
    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])

# read the id of the product and use this method below to pass it to the serializer 
    def get_serializer_context(self):
      
        return {'product_id': self.kwargs['product_pk']}

