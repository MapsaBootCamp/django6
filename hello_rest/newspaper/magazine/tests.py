from os import name
from django import views
from django.http import response
from django.test import TestCase
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient


from .models import Category, Magazine, Author
from .views import AuthorList

#  view (api), form, model, functinality


def summm(numbers: list) -> float:
    return sum(numbers)


# class SumTest(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         print("in setup class")

#     def setUp(self) -> None:
#         print("in setUp")

#     def tearDown(self) -> None:
#         print("in tear Down")

#     def test_khnade(self):
#         numbers = [2, 4, 2, 3]   # Arrange
#         result = summm(numbers)  # Act
#         return self.assertEqual(result, 12, "sum should be 11")        

#     def test_sum(self):
#         print("in tesst sum")
#         numbers = [2, 4, 2, 3]   # Arrange
#         result = summm(numbers)  # Act
#         return self.assertEqual(result, 11, "sum should be 11")



class MagazineModelTest(TestCase):

    def setUp(self):
        self.magazine = Magazine()
        self.category = Category.objects.create(name="hi")

    def test_magazine_name_field(self):
        name_field = self.magazine._meta.get_field('name')
        self.assertIsInstance(name_field, models.CharField, "name should be charfield")

    def test_magazine_number_field(self):
        number_field = self.magazine._meta.get_field('number')
        self.assertIsInstance(number_field, models.SmallIntegerField, "number should be small integer")


    def test_magazine_has_slug(self):
        """Magazine are given slugs correctly when saving"""
        magazine = Magazine(name="My first post", )

        magazine.number = 3
        magazine.category = self.category
        magazine.content = 1
        magazine.save()
        self.assertEqual(magazine.slug, slugify(magazine.name))



class AuthorModelTest(TestCase):
    
    def setUp(self) -> None:
        self.author = Author(name="ashkan")
    
    def test_author_name_field(self):
        name_field = self.author._meta.get_field('name')
        self.assertEqual(name_field.max_length, 100)
        self.assertIsInstance(name_field, models.CharField)
    
    def test_get_full_name(self):
        self.assertEqual(self.author.get_author_full_name(), "ashkan hi")


class AuthorTestAPI(TestCase):
    
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="ashkan", password="1234")
        self.get_request = self.factory.get("api/authors/", format="json")


    def test_view_authors(self):
        view = AuthorList.as_view()
        response = view(self.get_request)
        self.assertEqual(401, response.status_code)

    def test_view_authors_without_login_client(self):
        client = APIClient()
        response = client.get("/api/authors/", format="json")
        self.assertEqual(401, response.status_code)

    def test_view_authors_with_login_client(self):
        client = APIClient()
        client.login(username="ashkan", password="1234")
        response = client.get("/api/authors/", format="json")

        self.assertEqual(200, response.status_code)
