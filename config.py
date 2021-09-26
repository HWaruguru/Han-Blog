import os


class Config:
    # email configurations
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    

class ProdConfig(Config):
    db_url = os.environ.get('DATABASE_URL')
    if db_url.startswith('postgres:'):
        SQLALCHEMY_DATABASE_URI = db_url.replace("://", "ql://", 1)
    else:
        SQLALCHEMY_DATABASE_URI = db_url


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://hannahnjoroge:password@localhost/blogs_test"
    )


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://hannahnjoroge:password@localhost/blogs"
    )
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
}
