import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import main
    from . import upload_data2excel
    from . import passage2excel
    
    app.register_blueprint(main.bp)
    app.register_blueprint(upload_data2excel.bp)
    app.register_blueprint(passage2excel.bp)
    
    # app.register_blueprint(after_upload.bp)
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/upload_data2excel/', endpoint='upload_data2excel')
    app.add_url_rule('/after_upload//', endpoint='upload')
    app.add_url_rule('/passage2excel/', endpoint='passage2excel')
    return app