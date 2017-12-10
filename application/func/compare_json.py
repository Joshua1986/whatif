# /usr/bin/python
# -*- coding: utf-8 -*-
from tags import exp_res_tags, form_tags, method_tags
import json
import requests


class CompareJson:
    def __init__(self, title, url, method, form, exp_res):
        self.title = title
        self.url = url
        self.error_desc = []

        # 判断请求方式在枚举值之间
        if method.upper() not in method_tags:
            raise RuntimeError("method 参数格式错误！")
        else:
            self.method = method

        # 判断form格式必须可以转换json，以后会支持TAG
        for i in form_tags:
            form = form.replace('$'+i, '"${0}"'.format(i))
        try:
            self.form = json.loads(form)
        except:
            raise RuntimeError("form 参数格式错误！")

        # exp_res参数必须是string，而且在替换TAG后必须可以转json
        if not isinstance(exp_res, str):
            raise RuntimeError("exp_res数据类型错误！\n错误数据：" + self.title)
        for i in exp_res_tags:
            exp_res = exp_res.replace('$'+i, '"${0}"'.format(i))
        try:
            self.exp_res = json.loads(exp_res)
        except:
            raise RuntimeError("exp_res Json 格式转换出错，请检查预期返回数据结果。\n错误数据：" + self.title)

        # 根据method参数区别请求方式
        if method.upper() == "POST_FORM":
            self.act_res = requests.post(self.url, data=self.form).json()
        elif method.upper() in ["POST_RAW", "POST"]:
            self.act_res = requests.post(self.url, self.form).json()
        else:
            paras = "&".join(["{0}={1}".format(k1, v1) for k1, v1 in self.form.items()])
            self.act_res = requests.get(self.url + "?" + paras).json()

        # 打印日志区域
        # app.logger.info("Got title: {0}".format(self.title))
        # app.logger.info("Got url: {0}".format(self.url))
        # app.logger.info("Got form: {0}".format(self.form))
        # app.logger.info("Got method: {0}".format(self.method))
        # app.logger.info("Got exp_res: {0}".format(self.exp_res))
        # app.logger.info("Got act_res: {0}".format(self.act_res))

    # 发送请求，并处理请求参数中的TAG
    @property
    def generate_act_res(self):
        # todo
        return True

    # 核对self.act_res和self.exp_res的区别，返回diff后的区别，append进self.error_desc
    @property
    def compare(self):
        # todo
        return self.act_res == self.exp_res

    def __repr__(self):
        result = False if self.compare else True
        return "Case {0} 执行结果：{1} \nDetail：{1}".format(self.title, result)
