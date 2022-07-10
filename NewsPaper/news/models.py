import django.contrib.auth.models
from django.db import models
from datetime import datetime

director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)
    labor_contract = models.BigIntegerField(default=0)

    def get_last_name(self):
        return self.full_name.split()[0]


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    composition = models.TextField(default="Состав не указан")


class Order(models.Model):  # наследуемся от класса Model
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:
            return (self.time_out - self.time_in).total_seconds() // 60
        else:
            return (datetime.now() - self.time_in).total_seconds() // 60


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    _amount = models.IntegerField(default=1, db_column='amount')

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value > 0 else 0
        self.save()

    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount

# # ______________________________________________________________________________________________________________________
# # ______________________________________________________________________________________________________________________
# # Код итогового задания
# class Author(models.Model):
#     user = models.OneToOneField(django.contrib.auth.models.User, on_delete= models.CASCADE)
#     # cвязь «один к одному» с встроенной моделью пользователей User;
#     rating = models.IntegerField(default=0)
#
#
# class Category(models.Model):
#     # Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.).
#     # Имеет единственное поле: название категории.
#     # Поле должно быть уникальным (в определении поля необходимо написать параметр unique = True).
#     category_name = models.CharField(max_length=255, unique=True)
#
#
# class Post(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     # поле с выбором — «статья» или «новость»;
#     post_create_datetime = models.DateTimeField(auto_now_add=True)
#     category = models.ManyToManyField(Category, through='PostCategory')
#     post_title = models.CharField(max_length=255)
#     post_text = models.TextField(default="Здесь должен быть текст вашей статьи или новости...")
#     post_rating = models.IntegerField(default=0)
#
#
# class PostCategory(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
#     comment_text = models.TextField()
#     comment_datetime = models.DateTimeField(auto_now_add=True)
#     comment_rating = models.IntegerField(default=0)
#
#     def like(self):
#         self.comment_rating += 1
#         self.save()
#
#     def dislike(self):
#         self.comment_rating -= 1
#         self.save()

