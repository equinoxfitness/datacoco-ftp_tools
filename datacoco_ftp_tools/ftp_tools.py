"""
Module provides basic interaction for FTP (File-Transfer-Protocol)
Standard Internet protocol for transmitting files between
computers on the Internet over TCP/IP connections
This module has FTP and SFTP support
"""
import pysftp
from io import BytesIO, StringIO

from ftplib import FTP_TLS  # nosec
from ftplib import FTP  # nosec


class FTPInteraction:
    """
    Currently supports sftp and ftp connecting, listing directories and files,
    entering a directory, writing to a directory, and closing the connection
    """

    def __init__(self, protocol, host, user, password):
        """
        Initializes the FTP object and decides the port number
        based on the protocol that is passed
        """
        if not protocol or not host or not user or password is None:
            raise RuntimeError("%s request all __init__ arguments" % __name__)
        if protocol == "ftp":
            self.host = host
            self.user = user
            self.password = password
            self.port = 21
        elif protocol == "sftp":
            self.host = host
            self.user = user
            self.password = password
            self.port = 22
        else:
            raise RuntimeError("Please define an appropriate protocol.")

    def conn(self):
        """
        Connects to ftp or sftp based on the protocol
        """
        try:
            if self.port == 22:
                ftp_conn = FTP_TLS(self.host)
                ftp_conn.login(self.user, self.password)
                ftp_conn.auth()
                ftp_conn.prot_p()
            else:
                ftp_conn = FTP(self.host)
                ftp_conn.login(self.user, self.password)
            self.con = ftp_conn
        except Exception as e:
            raise e

    def list(self):
        """
        Lists all files and folders in a given directory
        """
        return self.con.retrlines("LIST")

    def call_dir(self, pathname):
        """
        Enters the specified directory
        DO NOT START WITH A "/"
        """
        curr_dir = self.con.pwd()
        if pathname == curr_dir:
            return
        else:
            self.con.cwd(pathname)
            return self.con.pwd()

    def curr_dir(self):
        """
        Returns the name of the current directory.
        """
        return self.con.pwd()

    def write_file(self, filename, contents):
        """
        Writes file to the current directory.
        If this function won't work for you. You can call con from this class
        and use it according to your preference. i.e read a file
        and store directly
        ftp.con.storbinary(command, open(self.ftp_pgp_file, 'rb'))
        """
        command = "STOR " + filename
        self.con.storbinary(command, StringIO(contents))

    def quit(self):
        """
        Tries to close the connection gracefully unless the command
        fails. If it fails it will force the connection to close.
        """
        try:
            self.con.quit()
        except Exception as e:
            print(e)
            self.con.close()


class SFTPInteraction:
    def __init__(
        self, host, user, password, hostkeys=None, key_file=None, port=None
    ):
        self.host = host
        self.user = user
        self.password = password

        self.cnopts = pysftp.CnOpts()
        self.cnopts.hostkeys = hostkeys
        self.key_file = key_file

        if port is not None:
            self.port = port
        else:
            self.port = 22

    def conn(self):
        """
        Connects to sftp
        """
        self.sftp_conn = pysftp.Connection(
            self.host,
            username=self.user,
            password=self.password,
            cnopts=self.cnopts,
            private_key=self.key_file,
            port=self.port,
        )

    def call_dir(self, remote_path):
        """
        Switch to remote path if provided.
        """
        curr_dir = self.sftp_conn.pwd
        if remote_path == curr_dir:
            return
        else:
            self.sftp_conn.cwd(remote_path)

    def write_file(self, filename, remote_path=None):
        """
        Saves file to sftp.
        """
        if remote_path:
            # Currently, bug in paramiko requires filename in destination
            remote_directory = "{}/{}".format(remote_path, filename)

            self.sftp_conn.put(filename, remote_directory)
            print("File saved to sftp remote path")
        else:
            self.sftp_conn.put(filename)
            print("File saved to sftp")

    def quit(self):
        self.sftp_conn.close()

    def get_file_data_as_string(self, filename, remote_path=None):
        """
        Grabs content of file on FTP as string
        """
        flo = BytesIO()

        if remote_path:
            # This command does not work and not needed
            # self.call_dir(remote_path)
            remote_directory = "{}/{}".format(remote_path, filename)
            num_bytes = self.sftp_conn.getfo(remote_directory, flo)
        else:
            num_bytes = self.sftp_conn.getfo(filename, flo)
        print("Created file-like object with {} bytes".format(num_bytes))

        return flo.getvalue()  # return the data as string for s3 upload
