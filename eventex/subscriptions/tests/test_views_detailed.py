#coding utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Gabriel Cortes', cpf='000000000012', email='gaco@gaco.com', phone='11-91210021')
        self.resp = self.client.post('/inscricao/%d/' % s.pk)

    def test_get(self):
        """GET /inscricao/1/ should return status 200. """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        """Context must have a subscription instance."""
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.resp,'Gabriel Cortes')


class DetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)