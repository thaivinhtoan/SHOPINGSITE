from importlib import import_module
from django.conf import settings
from unittest import skip
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from store.models import Category, Product
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from store.views import product_all

# @skip('demonstrating skipping')
# class TestSkip(TestCase):
#     def test_skip_exmaple(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='djangos')

    def test_url_allowed_hosts(self):
        '''
        Test allowed hosts
        '''
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        '''
        Test Product response status 
        '''
        response = self.c.get(
            reverse('store:product_detail', args=['django-beginners']))

    def test_category_detail_url(self):
        '''
        Test Category response status 
        '''
        response = self.c.get(
            reverse('store:category_list', args=['django']))

    def test_homepage_html(self):
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Book Store</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_url_allowed_hosts(self):
        response = self.c.get('/', HTTP_HOST='haha.com')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)
