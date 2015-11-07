from pdb import set_trace as st

from django.test import TestCase

from django.test.client import Client
from django.utils.unittest import TestSuite
from django.utils.unittest import defaultTestLoader

from bs4 import BeautifulSoup as BS

from capp.models import Item
from capp.models import lots_of_items
# although this import is unused, it must be included to avoid errors
# when initializing Item objects b/c of the foreign key relation
from cauth.models import User


def _get_first_item(test, xs):
    """utility to get first item in list 'xs' in which function
    'test' is true, None otherwise"""
    filtered_xs = list(filter(test, xs))
    if len(filtered_xs) == 0:
        return None
    else:
        return filtered_xs[0]

def setUpModule():
    lots_of_items()

# todo: check parsed html
#       rather than using 'in' operator on str(resp.content)

class LoginTest(TestCase):
    # todo: make class properties
    LOGIN_URL = '/login'
    SIGNUP_URL = '/login'
    EMAIL = "a@a.org"
    PASSWORD = "pass"
    NAME = "alice"

    def _login(self):
        resp = self.c.post(self.LOGIN_URL, {
            'email': self.EMAIL,
            'password': self.PASSWORD,
            'sign-in': ''
        }, follow=True)
        return (
            resp.status_code == 200 and
            'Errors' not in str(resp.content))

    def _signup(self):
        resp = self.c.post(self.LOGIN_URL, {
            'email': self.EMAIL,
            'password': self.PASSWORD,
            'password_confirm': self.PASSWORD,
            'name': self.NAME,
            'sign-up': ''
        }, follow=True)
        return (
            resp.status_code == 200 and
            'Catalog App' in str(resp.content))

    def setUp(self):
        self.c = Client()
        if not self._login():
            self.assertTrue(self._signup())


class ItemTest(LoginTest):
    TITLE = "soccer ball"
    DESC = "world cup 2014 edition"
    CAT_NAME = "Soccer"

    def _get_read_url(self):
        resp = self.c.get('/')
        soup = BS(resp.content)
        return _get_first_item(lambda t: self.TITLE in t.text,
                               soup.find_all('ul')[2].find_all('li')
                           ).find('a')['href']

    def _get_edit_url(self):
        resp = self.c.get(self._get_read_url())
        soup = BS(resp.content)
        return _get_first_item(lambda t: 'Edit' in t.text,
                               soup.find_all('a'))['href']


class CreateTest(ItemTest):

    CREATE_URL = '/catalog/item/new'

    def test_create(self):
        resp = self.c.get(self.CREATE_URL)
        soup = BS(resp.content)
        cat_tag = _get_first_item(lambda t: t.text == self.CAT_NAME,
                                  soup.find_all('option'))
        cat_val = cat_tag['value']
        post_resp = self.c.post(self.CREATE_URL, {
            'title': self.TITLE,
            'description': self.DESC,
            'category': cat_val
        }, follow=True)
        self.assertTrue(post_resp.status_code == 200)


class ReadTest(CreateTest):

    def test_read(self):
        self.test_create() # django clears database between tests...
        resp = self.c.get(self._get_read_url())
        soup = BS(resp.content)
        self.assertEqual(soup.find('h3').text, self.TITLE)

class UpdateTest(CreateTest):

    def test_update(self):
        self.test_create()
        self._get_edit_url()


class DeleteTest(ItemTest):
    pass


def crud_suite():
    suite = TestSuite()
    suite.addTest(defaultTestLoader.loadTestsFromTestCase(CreateTest))
    suite.addTest(defaultTestLoader.loadTestsFromTestCase(ReadTest))
    suite.addTest(defaultTestLoader.loadTestsFromTestCase(UpdateTest))
    suite.addTest(defaultTestLoader.loadTestsFromTestCase(DeleteTest))
    return suite

def suite():
    suite = TestSuite()
    suite.addTest(crud_suite())
    return suite
