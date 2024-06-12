import json
import aiohttp
from env import *
import requests

import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


async def check_status(id_pay):
    """

    :param id_pay:
    :return:
    """
    url = f"https://api.nowpayments.io/v1/payment/{id_pay}"

    payload = {}
    headers = {
        'x-api-key': ENV.API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


async def monthly_subscription(user_id):
    """

    :param user_id:
    :return:
    """
    url = "https://api.nowpayments.io/v1/invoice"

    payload = json.dumps({
        "price_amount": 100,
        "price_currency": "usd",
        "pay_currency": "USDTTRC20",
        "ipn_callback_url": "https://nowpayments.io",
        "order_id": user_id,
        "order_description": "Донат. Подписка на 1 месяц."
    })
    headers = {
        'x-api-key': ENV.API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


async def two_monthly_subscription(user_id):
    """

    :param user_id:
    :return:
    """
    url = "https://api.nowpayments.io/v1/invoice"

    payload = json.dumps({
        "price_amount": 170,
        "price_currency": "usd",
        "pay_currency": "USDTTRC20",
        "ipn_callback_url": "https://nowpayments.io",
        "order_id": user_id,
        "order_description": "Донат. Подписка на 2 месяца."
    })
    headers = {
        'x-api-key': ENV.API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


async def meeting_pay(user_id, title, cost):
    """

    :param cost:
    :param title:
    :param user_id:
    :return:
    """
    url = "https://api.nowpayments.io/v1/invoice"

    payload = json.dumps({
        "price_amount": cost,
        "price_currency": "usd",
        "pay_currency": "USDTTRC20",
        "ipn_callback_url": "https://nowpayments.io",
        "order_id": user_id,
        "order_description": title
    })
    headers = {
        'x-api-key': ENV.API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


async def subscription_three_months(user_id):
    url = "https://api.nowpayments.io/v1/invoice"

    payload = json.dumps({
        "price_amount": 220,
        "price_currency": "usd",
        "pay_currency": "USDTTRC20",
        "order_id": user_id,
        "order_description": "Донат. Подписка на 3 месяца.",
        "ipn_callback_url": "https://nowpayments.io",
        "success_url": "https://nowpayments.io",
        "cancel_url": "https://nowpayments.io"
    })
    headers = {
        'x-api-key': ENV.API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response


async def get_payment_id(user_id, data_invoice):

    url = "https://api.nowpayments.io/v1/invoice-payment"

    data = json.dumps({
        'iid': data_invoice['id'],
        'pay_currency': data_invoice['pay_currency'],
        'order_description': data_invoice['order_description']
    })
    headers = {
        'x-api-key': ENV.API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=data)
    data_payment = json.loads(response.text)

    url = f'https://nowpayments.io/payment/?iid={data_invoice["id"]}&paymentId={data_payment["payment_id"]}'
    data = {'user_id': user_id,
            'payment_id': data_payment["payment_id"],
            'invoice_id': data_invoice["id"],
            'name_payment': data_invoice['order_description']
            }
    await payment_post(data)
    return url


async def payment_all_get():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/payment/') as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def payment_get(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/payment/{user_id}') as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def payment_post(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{ENV.ADMIN_API_URL}v1/bot/user/payment/', data=data) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def payment_delete(user_id, data):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f'{ENV.ADMIN_API_URL}v1/bot/user/payment/{user_id}', data=data) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def user(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/users/' + str(user_id)) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def user_create(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{ENV.ADMIN_API_URL}v1/bot/user/users/', data=data) \
                as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def user_create1(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'https://vm3707648.43ssd.had.wf/api/v1/bot/guard/user', data=data) \
                as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def user_update(user_id, update_key, update_val):
    async with aiohttp.ClientSession() as session:
        async with session.put(f'{ENV.ADMIN_API_URL}v1/bot/user/users/' + str(user_id) + '/',
                               data={'user_id': user_id, update_key: update_val}) \
                as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def check_rec():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/recruitment/0') as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def reviews(num):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/review/rev/' + str(num)) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def ref_check(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/referal/' + str(user_id)) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def all_users():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/users/') as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def sub_users():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/sub/') as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def chat_create(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{ENV.ADMIN_API_URL}v1/bot/user/chats/', data=data) \
                as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def chats():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/chats/') as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def channel_create(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{ENV.ADMIN_API_URL}v1/bot/user/channels/', data=data) \
                as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def channels():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/user/channels/') as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def meeting():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}meeting/') as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def meeting_detail(title):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}meeting/' + title) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def meeting_update(data):
    response = requests.post(f'{ENV.ADMIN_API_URL}meeting/add_user/', data=data)
    status = response.status_code
    if status == 200:
        return response.json()
    return None


async def feedback_api(num):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/feedback/' + str(num)) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def feedback_create(data):
    response = requests.post(f'{ENV.ADMIN_API_URL}v1/bot/user/feedback_user/add_feedback/', data=data)
    status = response.status_code
    if status == 200:
        return response.json()
    return None


async def feedback_update_answer(data):
    response = requests.post(f'{ENV.ADMIN_API_URL}v1/bot/user/feedback_user/add_answer_feedback/', data=data)
    status = response.status_code
    if status == 200:
        return response.json()
    return None


async def add_purchase(data):
    response = requests.post(f'{ENV.ADMIN_API_URL}v1/bot/user/purchase/', data=data)
    status = response.status_code
    if status == 200:
        return response.json()
    return None


async def feedback_api_unpaid(num):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{ENV.ADMIN_API_URL}v1/bot/feedback/unpaid/' + str(num)) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def feedback_create_unpaid(data):
    response = requests.post(f'{ENV.ADMIN_API_URL}v1/bot/user/feedback_user_unpaid/add_feedback/', data=data)
    status = response.status_code
    if status == 200:
        return response.json()
    return None


async def feedback_update_answer_unpaid(data):
    response = requests.post(f'{ENV.ADMIN_API_URL}v1/bot/user/feedback_user_unpaid/add_answer_feedback/', data=data)
    status = response.status_code
    if status == 200:
        return response.json()
    return None


class GoogleSheet:
    # SPREADSHEET_ID = '1zeM1LaOCQlUcQrcHROkxjdHp96Rbh-7GZ5uV6QRnWhE'
    FINANCE_SPREADSHEET_ID = ''
    NOTION_SPREADSHEET_ID = ''
    GRADUATES_SPREADSHEET_ID = ''
    TEST = '1lRTgtCG9NMTRxo2GG1nBxbg0WrtWtb1pQdZKN5906SA'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GoogleSheet, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValuesFinance(self, values, range):

        result = self.service.spreadsheets().values().append(spreadsheetId=self.FINANCE_SPREADSHEET_ID,
                                                             range=range,
                                                             valueInputOption='USER_ENTERED',
                                                             body={'values': values}).execute()
        return result

    def updateRangeValuesNotion(self, values, range):

        result = self.service.spreadsheets().values().append(spreadsheetId=self.NOTION_SPREADSHEET_ID,
                                                             range=range,
                                                             valueInputOption='USER_ENTERED',
                                                             body={'values': values}).execute()
        return result

    def getGoogle(self):

        ranges = f'Лист3!D3:D162'
        result = self.service.spreadsheets().values().batchGet(spreadsheetId=self.GRADUATES_SPREADSHEET_ID,
                                                               ranges=ranges,
                                                               valueRenderOption='FORMATTED_VALUE',
                                                               dateTimeRenderOption='FORMATTED_STRING').execute()
        return result

    def postGoogle(self, values, ranges):

        result = self.service.spreadsheets().values().append(spreadsheetId=self.GRADUATES_SPREADSHEET_ID,
                                                             range=ranges,
                                                             valueInputOption='USER_ENTERED',
                                                             body={'values': values}).execute()
        return result













