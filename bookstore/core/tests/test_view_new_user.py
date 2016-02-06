from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from bookstore.core.forms import UserForm


class UserNewGet(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('adduser'))

    def test_get(self):
        ''' GET /adduser/ must return status code 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        ''' Must use adduser.html '''
        self.assertTemplateUsed(self.resp, 'adduser.html')

    def test_html(self):
        ''' Html must contain input tags '''
        tags = (('<form', 1),
                ('<input', 4),
                ('type="text"', 1),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        ''' Html must contain csrf '''
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        ''' Context must have subscription form '''
        form = self.resp.context['form']
        self.assertIsInstance(form, UserForm)


class UserNewPostValid(TestCase):

    def setUp(self):
        data = dict(
            name='regis',
            email='regis@example.com',
            password='1')
        self.resp = self.client.post(r('adduser'), data)

    def test_post(self):
        ''' Valid POST should redirect to /index/ '''
        self.assertRedirects(self.resp, r('home'))

    def test_save_user(self):
        self.assertTrue(User.objects.exists())


class UserNewPostInvalid(TestCase):

    def setUp(self):
        self.resp = self.client.post(r('adduser'), {})

    def test_post(self):
        ''' Invalid POST should not redirect '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'adduser.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, UserForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_user(self):
        self.assertFalse(User.objects.exists())


class TemplateRegressionTest(TestCase):

    def test_template_has_non_field_errors(self):
        invalid_data = dict(name='regis', email='regis')
        response = self.client.post(r('adduser'), invalid_data)
        self.assertContains(response, '<ul class="errorlist nonfield">')
