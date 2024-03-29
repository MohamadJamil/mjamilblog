import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 25
    RECAPTCHA_PUBLIC_KEY='6LcCmMQUAAAAAO6SKhd8XIaipQqTQkJThW2up2WA'
    RECAPTCHA_PRIVATE_KEY='6LcCmMQUAAAAAPOpqMWXD2cSLhGjt0OBbc-nBgPa'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('GMAIL_EMAIL')
    MAIL_PASSWORD = os.environ.get('GMAIL_PASS')
    ADMINS = ['your-email@example.com']
