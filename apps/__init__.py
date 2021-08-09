from flask import Flask

def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object('web_config')
    return app