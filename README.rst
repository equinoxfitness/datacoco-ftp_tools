datacoco-ftp_tools
=======================

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


::

    from datacoco_ftp_tools import FTPInteraction


    # Sample Code for FTP Interaction

    ftp = FTPInteraction('ftp',ftp_site,ftp_user,ftp_password)

    ftp.conn()

    ftp.curr_dir() # outputs '/web_analytics'

    ftp.call_dir('Monitoring') # outputs '/web_analytics/Monitoring'

    ftp.write_file('test.txt', 'test')

    ftp.quit()


::

    from datacoco_ftp_tools import FTPInteraction


    # Sample Code for SFTP Interaction

    sftp = FTPInteraction('sftp',sftp_site,sftp_user,sftp_password)

    sftp.conn()

    sftp.curr_dir() outputs '/web_analytics'

    sftp.call_dir('Monitoring') outputs '/web_analytics/Monitoring'

    sftp.write_file('test.txt', 'test')

    sftp.quit()



Contributing
~~~~~~~~~~~~

Contributions to datacoco\_ftp_tools are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/datacoco-ftp_tools/blob/master/CONTRIBUTING.md>`__.
