import django.contrib.auth.models
from django.db import models

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


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

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
#     # category_name = models.CharField(max_length=255)
#     # category_news = models.Choices(unique=True)
#     pass
#
#
# class Post(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     # поле с выбором — «статья» или «новость»;
#     post_datetime = models.DateTimeField(auto_now_add=True)
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
