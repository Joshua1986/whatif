from flask import Flask
import os
import sys

app = Flask(__name__, instance_relative_config=True)

if "win" in sys.platform:
    app.config.from_pyfile('local.py')
elif app.config["BETA_HOST"] in os.popen("ifconfig").read():
    app.config.from_pyfile('beta.py')
else:
    app.config.from_pyfile('prod.py')

app.config.from_pyfile('config.py')


import logging
from logging.handlers import TimedRotatingFileHandler

# 普通日志及格式设定
LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir) + "/logs/app.log")
handler = TimedRotatingFileHandler(LOG_FILE, when='H', interval=1, backupCount=40)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'))
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


# 增加邮件日志设置
from logging.handlers import SMTPHandler
mail_handler = SMTPHandler(app.config["SMTP_HOST"],
                           app.config["SMTP_SENDER"],
                           app.config["SMTP_RECEIVER"],
                           app.config["SMTP_TITLE"])
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'))
app.logger.addHandler(mail_handler)

# 路由
from .routes.common import *
from .routes.html import *
from .routes.interface import *
