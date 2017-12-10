import json
import requests
import time
from application import app


# 重试机制做成装饰器
def send_request(method, url, headers=None, params=None, retry_time_max=3):
    retry_times = 0

    r = requests.request(method, url, params=params, headers=headers)
    app.logger.info(r.url)
    app.logger.info(r.status_code)
    try:
        s = r.json()
        app.logger.info(s)
    except ValueError as e:
        app.logger.info("request error happens: " + e.args)
        while retry_times < retry_time_max:
            try:
                time.sleep(2)
                retry_times += 1
                s = requests.request(method, url, params=params, headers=headers).json()
            except ValueError as e:
                app.logger.error(e.args)
                continue
            return s
        return {}
    return s


# 弃用的方法
# def send_post_request(url, params=None, headers=None, retry_time_max=2):
#     return send_request("POST", url, params, retry_time_max)
#
#
# def send_get_request(url, params=None, headers=None, retry_time_max=2):
#     return send_request("GET", url, params, retry_time_max)

# def send_post_json_request(url, params, headers=None):
#     r = requests.get(url, data=json.dumps(params))
#     app.logger.info(r.url)
#     app.logger.info(r.status_code)
#     s = r.json()
#     app.logger.info(s)
#     return s


# 发送raw格式的post请求，请求的参数使用纯字符串，并设置header的Content-Type
# 判断header、payload格式方法封装装饰器
def send_post_raw_request(url, headers={}, payload=""):
    if not isinstance(headers, dict):
        app.logger.error("Wrong type of raw post request's header: [url:{0}, header:{1}, payload:{2}]".format(
            url, headers, payload))
        raise RuntimeError("The raw post request's header should be dictionary.")

    headers["content-type"] = "application/json"
    response = requests.request("POST", url, data=payload, headers=headers)
    app.logger.debug(
        "Sending raw post request: [url:{0}, header:{1}, payload:{2}], the response is [code: {3}, res_body: {4}]".format(
            url, headers, payload, response.status_code, response.json()))
    return response.text


# 发送x_www_form_urlencoded格式的post请求，请求的参数使用类似于get请求中的参数格式字符串，例如："a=1&b=2"
def send_post_x_www_form_request(url, headers={}, payload=""):
    if not isinstance(headers, dict):
        app.logger.error("Wrong type of www-form request's header: [url:{0}, header:{1}, payload:{2}]".format(
            url, headers, payload))
        raise RuntimeError("The www-form post request's header should be dictionary.")

    headers["content-type"] = "application/x-www-form-urlencoded"
    response = requests.request("POST", url, data=payload, headers=headers)
    app.logger.debug(
        "Sending www-form request: [url:{0}, header:{1}, payload:{2}], the response is [code: {3}, res_body: {4}]".format(
            url, headers, payload, response.status_code, response.json()))
    return response.text


# 发送表单格式的post请求，请求的参数使用dictionary格式，例如：{"a":1, "b":2}
def send_post_form_request(url, headers={}, payload=None):
    if not isinstance(payload, dict):
        app.logger.error("Wrong type of form request's payload: [url:{0}, header:{1}, payload:{2}]".format(
            url, headers, payload))
        raise RuntimeError("The form post request's payload should be dictionary.")

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    app.logger.debug(
        "Sending form request: [url:{0}, header:{1}, payload:{2}], the response is [code: {3}, res_body: {4}]".format(
            url, headers, payload, response.status_code, response.json()))
    return response.text


# 发送get请求，请求的参数使用字符串格式，例如："a=1&b=2"
def send_get_request(url, headers=None, params=''):

    response = requests.request("GET", url+"?"+params, headers=headers)
    app.logger.debug(
        "Sending get form request: [url:{0}, header:{1}, payload:{2}], the response is [code: {3}, res_body: {4}]".format(
            url, headers, params, response.status_code, response.json()))
    return response.text


# 发送get请求，请求的参数使用dictionary格式，例如：{"a":1, "b":2}
def send_get_form_request(url, headers={}, params=None):
    if not isinstance(params, dict):
        app.logger.error("Wrong type of get form request's params: [url:{0}, header:{1}, payload:{2}]".format(
            url, headers, params))
        raise RuntimeError("The form get request's params should be dictionary.")

    response = requests.request("GET", url, params=params, headers=headers)
    app.logger.debug(
        "Sending get form request: [url:{0}, header:{1}, payload:{2}], the response is [code: {3}, res_body: {4}]".format(
            url, headers, params, response.status_code, response.json()))
    return response.text


def del_tag(del_column, iterator):
    if isinstance(iterator, dict):
        for tag in del_column:
            del iterator[tag]
    elif isinstance(iterator, list):
        for l in iterator:
            for tag in del_column:
                del l[tag]
    else:
        raise AssertionError("The type of iterator is incorrect!")
    return iterator


def show_tag(show_column, iterator):
    if isinstance(iterator, dict):
        for tag in iterator.keys():
            if tag not in show_column:
                del iterator[tag]
    elif isinstance(iterator, list):
        for l in iterator:
            for tag in l.keys():
                if tag not in show_column:
                    del l[tag]
    else:
        raise AssertionError("The type of iterator is incorrect!")
    return iterator
