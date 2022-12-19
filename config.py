import os
basedir = os.path.abspath(os.path.dirname(__file__))


def get_db_url():
    user = os.environ['DATABASE_USER']
    password = os.environ['DATABASE_PASSWORD']
    host = os.environ['DATABASE_HOST']
    db_name = os.environ['DATABASE_DB']
    return f"postgresql://{user}:{password}@{host}/{db_name}"


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = get_db_url()


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
