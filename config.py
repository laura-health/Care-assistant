"""REST Web Service configuration file.

Common configuration between environments.
"""

DEBUG = False
TESTING = False
PORT = 80
LOCALE = 'pt-br'
SQLALCHEMY_DATABASE_URI = 'oracle://user:password@server_ip/database_name'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQL_DATE_FORMAT = '%d/%m/%Y %H:%M:%S'
USERNAME = 'laura'
PASSWORD = 'laura'
MAIL_SERVER = 'example.com'
MAIL_PORT = 000
MAIL_USE_SSL = True
MAIL_USERNAME = 'example@example.com'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"Web Server" <example@example.com>'
ADMINS = ['Someone <example@example.com>']
