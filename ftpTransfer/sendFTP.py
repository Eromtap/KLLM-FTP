# -*- coding: utf-8 -*-


from ftplib import FTP

ftp = FTP('test.rebex.net')
ftp.login("demo", "password")
print(ftp.dir())
ftp.cwd('pub')
print(ftp.dir())
ftp.cwd('example')
print(ftp.dir())
