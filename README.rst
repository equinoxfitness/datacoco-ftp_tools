datacoco-ftp_tools
=======================

.. image:: https://img.shields.io/pypi/v/datacoco-ftp_tools.svg
   :target: https://pypi.python.org/pypi/datacoco-ftp_tools
   :alt: Pypi Version
.. image:: https://travis-ci.org/readthedocs/datacoco-ftp_tools.svg?branch=master
   :target: https://travis-ci.org/readthedocs/datacoco-ftp_tools
   :alt: Build Status
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

datacoco-ftp_tools provides basic interaction for FTP (File-Transfer-Protocol)
Standard Internet protocol for transmitting files between computers on the Internet over TCP/IP connections
This module has FTP and SFTP support

Installation
------------

datacoco-ftp_tools requires Python 3.6+

::

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install datacoco_ftp_tools

Quickstart
----------

SFTP and write file to remote server using FTP
::

    from datacoco_ftp_tools import FTPInteraction


    # Sample Code for FTP Interaction

    ftp = FTPInteraction('ftp',ftp_site,ftp_user,ftp_password)

    ftp.conn()

    ftp.curr_dir() # outputs '/web_analytics'

    ftp.call_dir('Monitoring') # outputs '/web_analytics/Monitoring'

    ftp.write_file('test.txt', 'test')

    ftp.quit()


SFTP and write file to remote server using SFTP
::

    from datacoco_ftp_tools import FTPInteraction


    # Sample Code for SFTP Interaction

    sftp = FTPInteraction('sftp',sftp_site,sftp_user,sftp_password)

    sftp.conn()

    sftp.curr_dir() outputs '/web_analytics'

    sftp.call_dir('Monitoring') outputs '/web_analytics/Monitoring'

    sftp.write_file('test.txt', 'test')

    sftp.quit()


SFTP and write file to remote server using SFTP
::

    from datacoco_ftp_tools import SFTPInteraction


    # Sample Code for SFTP Interaction

    sftp = SFTPInteraction(sftp_site, user, None, key_file='key.ppk')

    sftp.conn()

    sftp.call_dir('Monitoring') outputs '/web_analytics/Monitoring'

    sftp.write_file(schema[table], remote_path=path)

    sftp.quit()






Contributing
~~~~~~~~~~~~

Contributions to datacoco\_ftp_tools are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/datacoco-ftp_tools/blob/master/CONTRIBUTING.md>`__.
