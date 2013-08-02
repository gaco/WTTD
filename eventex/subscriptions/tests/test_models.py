# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Gabriel Cortes',
            cpf='12345678901',
            email='gaco@gaco.com',
            phone='11-91219955'
        )

    def test_create(self):
        # Subscription must have name, cpf, email, phone
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        #Subscription must have automatic created_at
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Gabriel Cortes', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the collision
        Subscription.objects.create(name='Gabriel Cortes', cpf='12345678901',
                                    email='gaco@gaco.com', phone='11-91219955')

    def test_cpf_unique(self):
        """CPF must be unique"""
        s = Subscription(name='Gabriel Cortes', cpf='12345678901',
                         email='outro@email.com', phone='11-91219955')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        """Email must be unique"""
        s = Subscription(name='Gabriel Cortes', cpf='00000000011',
                         email='gaco@gaco.com', phone='11-91219955')
        self.assertRaises(IntegrityError, s.save)