import unittest
import datetime
from rpaste import rpaste


class RpasteTestCase(unittest.TestCase):
    """
    Test  case for paste push and pull
    """

    def test_pushpull(self):
        paste = rpaste()
        now = datetime.datetime.now()
        content = "RPTEST - " + str(now)

        paste.set_content(content)
        paste.set_title(content)

        paste.push_paste("TEST")

        newpaste = rpaste()
        newpaste.set_url_slug(paste.get_slug())
        newpaste.pull_paste()

        self.assertEqual(newpaste.get_title(), paste.get_title())
        self.assertEqual(newpaste.get_content(), paste.get_content())

    def test_password(self):
        password = "samplepassword"
        paste = rpaste()
        now = datetime.datetime.now()
        content = "RPTEST - " + str(now)

        paste.set_content(content)
        paste.set_password(password)
        paste.set_title(content)

        paste.push_paste("TEST")

        newpaste = rpaste()
        newpaste.set_url_slug(paste.get_slug())

        # Since no password given
        with self.assertRaises(Exception):
            newpaste.pull_paste()

        newpaste.set_password(password)

        newpaste.pull_paste()

        self.assertEqual(newpaste.get_title(), paste.get_title())
        self.assertEqual(newpaste.get_content(), paste.get_content())
