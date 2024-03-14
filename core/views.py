from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count
from store.models import *
# Create your views here. 


def HomeView(request):
    # gives all the product that have been ordered in the system
    # products = Product.objects.filter(id__in = OrderItem.objects.values('product_id')).distinct().order_by('title')

#   to get the collection title by going through the products tabla if just used .all()  the query will be slow
    # that's  we use select_related() whe the other end of the relationship has one instance 
    # lke in the case below a product just have one collection 
    # ForeignKey relationship is an example 
    # products = Product.objects.select_related('collection').all()
    # prefech_related() when the other end has many instance for example below promotion that's one product can have many promotion 
    # ManyTOMany relationship is and example or the other instance has many items to get from 
    # products = Product.objects.prefetch_related('promotions').all()
    # we can complain all this query to form a more complex one that is 
    # products = Product.objects.prefetch_related('promotions').select_related('collection').all()

    products = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-place_at')[:5]

    #  to count the order for each custmors 
    # orders_total = Order.objects.annotate(orders_count = Count('order))
    context = {'products':products}
    return render(request, 'core/index.html', context)