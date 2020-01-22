datacoco-ftp_tools
=======================

.. image:: https://badge.fury.io/py/datacoco-ftp-tools.svg
    :target: https://badge.fury.io/py/datacoco-ftp-tools
    :alt: PyPI Version

.. image:: https://readthedocs.org/projects/datacoco-ftp-tools/badge/?version=latest
    :target: https://datacoco-ftp-tools.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://api.codacy.com/project/badge/Grade/18451ba755734b5da30575516b87cb93
    :target: https://www.codacy.com/manual/equinoxfitness/datacoco-ftp_tools?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinoxfitness/datacoco-ftp_tools&amp;utm_campaign=Badge_Grade
    :alt: Code Quality Grade

.. image:: https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg
    :target: https://github.com/equinoxfitness/datacoco-email_tools/blob/master/CODE_OF_CONDUCT.rst
    :alt: Code of Conduct

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

Development
-----------

Getting Started
~~~~~~~~~~~~~~~

It is recommended to use the steps below to set up a virtual environment for development:

::

    python3 -m venv <virtual env name>
    source <virtual env name>/bin/activate
    pip install -r requirements.txt

Testing
~~~~~~~

::

    pip install -r requirements-dev.txt

To run the testing suite, simply run the command: ``tox`` or ``python -m unittest discover tests``

Contributing
~~~~~~~~~~~~

Contributions to datacoco\_ftp_tools are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/datacoco-ftp_tools/blob/master/CONTRIBUTING.md>`__.
