from flask import render_template, jsonify, redirect, session, send_from_directory
from application.models import *
from application import app
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


# 查看所有task的页面
@app.route("/", methods=['GET', 'POST'])
@app.route("/index.html", methods=["GET"])
@app.route("/suite_list.html", methods=["GET"])
def suite_list():
    return render_template("suite_list.html")


# cases的页面
@app.route("/cases.html", methods=["GET"])
def case_list():
    return render_template("cases.html")


# task页面
@app.route("/task.html", methods=["GET"])
def task_list():
    return render_template("task.html")


# case_result页面
@app.route("/case_result.html", methods=["GET"])
def case_result_list():
    return render_template("case_result.html")


# tag管理页面
@app.route("/tags.html", methods=["GET"])
def tags_list():
    return render_template("tags.html")


# 帮助页面
@app.route("/help.html", methods=["GET"])
def help():
    return render_template("help.html")
