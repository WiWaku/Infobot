import os
import logging as log
from os import environ
from logging.handlers import *


if not os.path.exists("log"):
    os.mkdir("log")


class Environment:
    # ADMIN_API_URL: str = str(environ.get(
    #     "ADMIN_API_URL", default="https://vm3707648.43ssd.had.wf/api/"
    # ))
    ADMIN_API_URL: str = str(environ.get(
        "ADMIN_API_URL", default="http://127.0.0.1:8000/api/"
    ))

    # BOT_TOKEN: str = str(environ.get(
    #     "BOT_TOKEN", default="5311291326:AAG1zR2vMgk6m7sSsXRvx6Voec4RS358E50"
    # #     5089695436:AAGcdENF4gKzpJ7NB_H6F7Oah3qNCFG0i40
    # ))
    BOT_TOKEN: str = str(environ.get(
        "BOT_TOKEN", default='6125819127:AAGOe2cnY25FG-cVBJFzL9O0OMXml_x35d4'
    )) #Мой тг бот
    BOT_ID: int = int(environ.get(
        "BOT_ID", default="6125819127"
    ))

    WEBHOOK_URL: str = str(environ.get(
        "WEBHOOK_URL", default="https://4763-178-155-5-135.eu.ngrok.io"
    ))


    API_KEY: str = str(environ.get(
        "API_KEY", default="3RS0MTQ-9E0MQM1-K4K7HDW-YGB6RR5"
    ))

    NAME_INFO: str = str(environ.get(
        "NAME_INFO", default="bananacrypto_bot"
    ))

    ADMIN_CHAT: str = int(environ.get(
        "ADMIN_CHAT", default=-1001967223905
    ))


log.basicConfig(
    level=log.DEBUG,
    format='[%(asctime)s.%(msecs)03d] [%(levelname)-6s] [%(filename)-24s] : %(message)s',
    handlers=[
        log.StreamHandler(),
        TimedRotatingFileHandler(filename="log/application.log", when="D", backupCount=14)
    ]
)


ENV = Environment()
