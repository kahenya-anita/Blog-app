from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    from .requests import configure_request
    configure_request(app)

    from .email import configure_email
    configure_email(app)

    # configure UploadSet
    configure_uploads(app,photos)


    # setting config
    from .requests import configure_request
    configure_request(app)

    return app