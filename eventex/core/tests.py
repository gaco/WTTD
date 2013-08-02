"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

# coding utf-8

from django.test import TestCase


class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        # GET MUST return 200
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        # Homepage must use template index.hml
            self.assertTemplateUsed(self.resp, 'index.html')
