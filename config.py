import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ('SECRET_KEY') or 'asdfonq298fhxapn9ewfhx'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ('DEV_DB_URI') or 'sqlite:///' + os.path.join(basedir, 'dev_db.sqlite')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ('TEST_DB_URI') or 'sqlite:///' + os.path.join(basedir, 'test_db.sqlite')


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'test': TestConfig
}
