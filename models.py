from django.db import models


class CreatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Producer(CreatedAt):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        name = models.CharField(max_length=100)
        db_table = 'bank_producer'


class Product(CreatedAt):
    name = models.CharField(max_length=100)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bank_product'


class Contract(CreatedAt):

    class Meta:
        db_table = 'bank_contract'


class CreditApplication(CreatedAt):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='credit_application')
    products = models.ManyToManyField(Product, through='CreditProduct', related_name='credit_product')

    class Meta:
        db_table = 'bank_creditapplication'


class CreditProduct(models.Model):
    credit = models.ForeignKey(CreditApplication, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('credit', 'product')
        db_table = 'bank_credit_product'


