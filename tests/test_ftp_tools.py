import unittest

from datacoco_ftp_tools.ftp_tools import SFTPInteraction


class TestFtp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testClass = SFTPInteraction( # nosec
            host="ftp.x.com", user="user", password="password"
        )

    def test_connection(self):
        print("--------------test")
        self.testClass.conn()
        self.testClass.call_dir("./")
        self.testClass.quit()
