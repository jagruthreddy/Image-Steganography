from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='AAA'
    app.config['UPLOAD_FOLDER'] = 'static/files'

    from .hcode import hcode
    from .code import code
    app.register_blueprint(hcode, url_prefix='/')
    app.register_blueprint(code, url_prefix='/')
    
    return app