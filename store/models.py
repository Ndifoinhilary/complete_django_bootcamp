from django.db import models

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


    def __str__(self):
        return self.discount



class Product(models.Model):
    """ 
    Product models that gives details for each product
    """
    title = models.CharField(max_length = 255)
    description = models.TextField()
    slug = models.SlugField()
    price = models.DecimalField(max_digits =6, decimal_places =2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)

    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name = "products")

    promotions = models.ManyToManyField(Promotion)
    

    def __str__(self) -> str:
        return self.title



class Customer(models.Model):
    """
    for customers creation 
    """
    MEMEBERSHIP_BRONZE = 'B'
    MEMEBERSHIP_SILVER = 'S'
    MEMEBERSHIP_GOLD = 'G'

    MEMEBERSHIP_CHOICES = (
        (MEMEBERSHIP_BRONZE, 'Bronze'),
        (MEMEBERSHIP_SILVER, 'Silver'),
        (MEMEBERSHIP_GOLD, 'Gold'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null = False, blank=False)

    membership = models.CharField(max_length=1 , choices = MEMEBERSHIP_CHOICES, default = MEMEBERSHIP_BRONZE)

    def __str__(self):
        return self.first_name



class Order(models.Model):
    """
    order models for placing orders 
    """
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETED = 'C'
    PAYMENT_FAILED = 'F'
    PAYMENT_STATUS = (
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETED, 'Completed'),
        (PAYMENT_FAILED, 'Failed')
    )
    place_at = models.DateTimeField(auto_now_add=True)

    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_PENDING)

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return self.customer.first_name



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name = 'orderItems')

    quantity = models.PositiveSmallIntegerField()

    unity_price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.product.title




class Address(models.Model):
    stress = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


    def __str__(self):
        return self.stress


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product.title  