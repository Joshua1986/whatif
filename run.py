from application import app
import sys


if __name__ == "__main__":
    sys.path.append(app.config['PROJECT_HOME'])
    app.debug = app.config['DEBUG']
    app.testing = app.config['TESTING']
    # 加上use_reloader防止出现logger重复打开的windows报错
    app.run(host=app.config['HOST'], port=app.config['PORT'], use_reloader=False)
