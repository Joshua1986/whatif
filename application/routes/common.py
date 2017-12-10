from flask import request, jsonify, redirect, session, send_from_directory
from application.models import *
from application import app
import os


@app.before_request
def before_request():
    app.logger.info("request:\t{}".format(request.path))
    app.logger.info("session:\t{}".format(session))
    if request.method == 'POST':
        app.logger.info("post args:\t{}".format(request.get_json()))
    elif request.method == 'GET':
        app.logger.info("get args:\t{}".format(request.args))
    else:
        redirect("/permission_denied"), 405

'''
通用响应参数解释：

resCode - 响应码：
0 - 成功
-1 - 必输项参数校验失败
-2 - 参数格式校验失败
-3 - 逻辑错误
-4 - 未知错误，重定向至unhandled_exception

desc - 响应详情
data - 响应数据
'''


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'icon.png')


@app.route("/test", methods=["GET"])
def test():
    res = query_cases_id_by_tag(["A"])
    return jsonify("{}".format(res))


@app.errorhandler(404)
def page_not_found():
    return "page not found!", 404


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', error)
    return "Error", 500
