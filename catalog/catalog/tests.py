from pdb import set_trace as st

from django.test import TestCase

from django.test.client import Client
from django.utils.unittest import TestSuite
from django.utils.unittest import defaultTestLoader

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


class CreateTest(LoginTest):

    CREATE_URL = '/item_add'

    def test_create_nopic(self):
        print("create test unimplemented")
        # self.c.post(self.CREATE_URL, {


class ReadTest(LoginTest):
    pass

class UpdateTest(LoginTest):
    pass

class DeleteTest(LoginTest):
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
