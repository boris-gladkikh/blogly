from unittest import TestCase
from app import app



class BloglyTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_users_show(self):
        """Test that form appears."""
        resp = self.client.get("/")
        self.assertIn(b'<form', resp.data)
    def test_form_failures(self):
        """Test conversion failures."""
        resp = self.client.get("/users",
                               query_string={"first_name": "MUPPET",
                                             "last_name": "BLARGH",
                                             "image_url": "glumph"})
        self.assertIn(b'Not a valid amount', resp.data)
        self.assertIn(b'Not a valid code: MUPPET', resp.data)
        self.assertIn(b'Not a valid code: BLARGH', resp.data)