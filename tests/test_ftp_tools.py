import pysftp
import unittest
from unittest import mock

from datacoco_ftp_tools.ftp_tools import SFTPInteraction


class Connection:
    def __init__(self):
        self.pwd = "/path/to/file"
        self.cwd_path = None
        self.put_result = None

    def cwd(self, path):
        self.cwd_path = path

    def put(self, filename, path_to_remote=None):
        self.put_result = path_to_remote

    def close(self):
        return True

    def getfo(self, filename, flo):
        """
        @param: filename string
        @param: flo object
        @return: bytes
        """
        return 1000  # bytes


class TestFtp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = dict(
            host="test.ftp.com", user="user", password="password"
        )
        cls.testClass = SFTPInteraction(**cls.config)

    def test_connection(self):
        print("--------------test connection")

        with mock.patch(
            "datacoco_ftp_tools.ftp_tools.pysftp"
        ) as MockPysftpConn:
            config = (
                MockPysftpConn.return_value.Connection._tconnect
            ) = self.config
            self.testClass.conn()
            resp = self.testClass.sftp_conn
            method = self.testClass.sftp_conn._mock_new_parent._mock_name
            obj = (
                self.testClass.sftp_conn._mock_new_parent._mock_parent._mock_name
            )

            # Test connection object
            self.assertEqual("pysftp.Connection", f"{obj}.{method}")

            # Test connection args
            self.assertEqual(config, self.config)

    def test_call_dir(self):
        with mock.patch(
            "datacoco_ftp_tools.ftp_tools.pysftp"
        ) as MockPysftpConn:
            MockPysftpConn.Connection.return_value = Connection()
            with mock.patch(
                "datacoco_ftp_tools.ftp_tools.SFTPInteraction"
            ) as MockSFTPInteraction:
                self.testClass.conn()

                # Test call_dir() if current working direcotry is same as set path, it should do nothing or return none
                resp = self.testClass.call_dir("/path/to/file")
                self.assertEqual(resp, None)

                # Test call_dir() if it was able to point to new working directory
                cwd = "/path/to/remote/folder"
                self.testClass.call_dir(cwd)
                self.assertEqual(self.testClass.sftp_conn.cwd_path, cwd)

    def test_write_file(self):
        with mock.patch(
            "datacoco_ftp_tools.ftp_tools.pysftp"
        ) as MockPysftpConn:
            MockPysftpConn.Connection.return_value = Connection()
            with mock.patch(
                "datacoco_ftp_tools.ftp_tools.SFTPInteraction"
            ) as MockSFTPInteraction:
                self.testClass.conn()
                # Given
                filename = "filename.txt"
                remote_path = "/path/to/folder"

                # When
                self.testClass.write_file(filename, remote_path)

                # Then: Test save to remote path
                self.assertEqual(
                    self.testClass.sftp_conn.put_result,
                    f"{remote_path}/{filename}",
                )

                # Then: Test save to sftp
                self.testClass.write_file(filename)
                self.assertEqual(self.testClass.sftp_conn.put_result, None)

    def test_quit(self):
        with mock.patch(
            "datacoco_ftp_tools.ftp_tools.pysftp"
        ) as MockPysftpConn:
            MockPysftpConn.Connection.return_value = Connection()
            with mock.patch(
                "datacoco_ftp_tools.ftp_tools.SFTPInteraction"
            ) as MockSFTPInteraction:
                self.testClass.conn()
                self.assertEqual(self.testClass.sftp_conn.close(), True)

    def test_get_file_data_as_string(self):
        with mock.patch(
            "datacoco_ftp_tools.ftp_tools.pysftp"
        ) as MockPysftpConn:
            MockPysftpConn.Connection.return_value = Connection()
            with mock.patch(
                "datacoco_ftp_tools.ftp_tools.SFTPInteraction"
            ) as MockSFTPInteraction:
                self.testClass.conn()
                resp = self.testClass.get_file_data_as_string("filename.txt")
                self.assertEqual(isinstance(resp, bytes), True)
