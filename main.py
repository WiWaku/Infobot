from aiogram.utils import executor

from telegram import dp, bot, scheduler
from env import *
from router import *
from aiogram.dispatcher.webhook import *


def run():
    executor.start_polling(dp, skip_updates=True, allowed_updates=types.update.AllowedUpdates.all())


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    loop.create_task(run())
    loop.run_forever()


# async def on_startup(_app: web.Application):
#     asyncio.create_task(scheduler())
#     webhook = await bot.get_webhook_info()
#     if not webhook.url:
#         await bot.delete_webhook()
#     await bot.set_webhook(
#         url=f"{ENV.WEBHOOK_URL}/webhook/bot/infobot",
#         drop_pending_updates=True, allowed_updates=types.update.AllowedUpdates.all()
#     )
#
#
# async def on_shutdown(_app: web.Application):
#     await bot.delete_webhook()
#     await dp.storage.close()
#     await dp.storage.wait_closed()
#
#
# if __name__ == '__main__':
#     app = get_new_configured_app(dispatcher=dp, path="/webhook/bot/infobot")
#     app.add_routes(routes=route)
#     app.on_startup.append(on_startup)
#     app.on_shutdown.append(on_shutdown)
#     web.run_app(
#         app=app, host="0.0.0.0", port=6000
#     )
