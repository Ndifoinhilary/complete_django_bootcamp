from rest_framework import serializers
from decimal import Decimal
from store.models import Collection, Product, Review




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_stax', 'collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_with_stax = serializers.SerializerMethodField(method_name='calculate_price')
    # collection = serializers.HyperlinkedRelatedField(queryset=Collection.objects.all(), view_name='collection-detail')


    def calculate_price(self, product:Product):
        return product.price * Decimal(1.5)



class CollectionSerializer(serializers.ModelSerializer):
    total_product = serializers.SerializerMethodField(method_name='product_count', read_only = True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'total_product']
    

    def product_count(self, collection:Collection):
        return collection.products.count()




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review

        fields = ['id', 'name', 'description']


    def create(self, validated_data):
        # getting it from the views 
        product_id = self.context['product_id']
       
        return  Review.objects.create(product_id=product_id, **validated_data)
