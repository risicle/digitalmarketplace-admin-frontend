import os
import jinja2

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    S3_DOCUMENT_BUCKET = os.getenv('DM_S3_DOCUMENT_BUCKET')
    DOCUMENTS_URL = 'https://assets.dev.digitalmarketplace.service.gov.uk'
    API_URL = os.getenv('DM_API_URL')
    API_AUTH_TOKEN = os.getenv('DM_ADMIN_FRONTEND_API_AUTH_TOKEN')
    SECRET_KEY = os.getenv('DM_ADMIN_FRONTEND_COOKIE_SECRET')
    PASSWORD_HASH = os.getenv('DM_ADMIN_FRONTEND_PASSWORD_HASH')

    STATIC_URL_PATH = '/admin/static'
    ASSET_PATH = STATIC_URL_PATH + '/'
    BASE_TEMPLATE_DATA = {
        'asset_path': ASSET_PATH,
        'header_class': 'with-proposition'
    }

    @staticmethod
    def init_app(app):
        repo_root = os.path.abspath(os.path.dirname(__file__))
        template_folders = [
            os.path.join(repo_root,
                         'bower_components/govuk_template/views/layouts'),
            os.path.join(repo_root, 'app/templates')
        ]
        jinja_loader = jinja2.FileSystemLoader(template_folders)
        app.jinja_loader = jinja_loader


class Test(Config):
    DEBUG = True
    AUTHENTICATION = True
    DOCUMENTS_URL = 'https://assets.test.digitalmarketplace.service.gov.uk'
    SECRET_KEY = "test_secret"
    PASSWORD_HASH = "JHA1azIkMjcxMCQwYmZiN2Y5YmJlZmI0YTg4YmNkZjQ1ODY0NWUzOGEwNCRoeDBwbUpHZVhSalREUFBGREFydmJQWnlFYnhWU1g1ag=="  # noqa


class Development(Config):
    DEBUG = True
    AUTHENTICATION = True


class Live(Config):
    DEBUG = False
    AUTHENTICATION = True
    DOCUMENTS_URL = 'https://assets.digitalmarketplace.service.gov.uk'


config = {
    'development': Development,
    'preview': Development,
    'staging': Live,
    'production': Live,
    'test': Test,
}
