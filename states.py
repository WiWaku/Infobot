from aiogram.dispatcher.filters.state import State, StatesGroup


class InfoBotStates(StatesGroup):
    id_pay = State()
    upgrade_notion = State()
    meeting_state = State()
    feedback_state = State()
    unpaid_state = State()
    detailed_response_state = State()
    new_message_state = State()
    message_send_state = State()
    promo_state = State()
    mailing_state = State()


