from aiogram.dispatcher.filters.state import State, StatesGroup

class TestStates(StatesGroup):
    START_STATE        = State()
    END_STATE          = State()
    SETTINGS_STATE     = State()
    SETTINGS_STATE_MY  = State()
    SETTINGS_STATE_MM  = State()
    SETTINGS_STATE_AU  = State()
    ADD_PHONE_STATE    = State()
    SAVE_PHONE_STATE   = State()
    SEARCH_PHONE_STATE = State()
    DEL_PHONE_STATE    = State()
    ADD_AUTO_STATE     = State()
    SAVE_AUTO_STATE    = State()
    SEARCH_AUTO_STATE  = State()
    DEL_AUTO_STATE     = State()
    ADD_MM_STATE       = State()
    SAVE_MM_STATE      = State()
    SEARCH_MM_STATE    = State()
    DEL_MM_STATE       = State()
    SEND_MESSAGE_STATE = State()
    SEND_MESSAGE_STATE_MM = State()
    SEND_MESSAGE_STATE_AU = State()
    SEND_MESSAGE_STATE_MY = State()
    SEND_MESSAGE_STATE_MM_CNT = State()
    SEND_MESSAGE_STATE_MM_CNT_DIRECT = State()
    SEND_MESSAGE_STATE_AU_CNT = State()
    SEND_MESSAGE_STATE_AU_CNT_DIRECT = State()
    SEND_MESSAGE_STATE_MY_CNT = State()
    SEND_MESSAGE_STATE_MY_CNT_DIRECT = State()
    GET_DIALOG_MESSAGE_STATE = State()
    DIALOG_MESSAGE_STATE = State()
    DIALOG_MESSAGE_STATE_REPLY = State()
    DIALOG_MESSAGE_STATE_FORWARD = State()
    DIALOG_MESSAGE_STATE_FORWARD_REPLY = State()
    INFO_STATE = State()
    INFO_STATE_COUNTERS = State()

# if __name__ == '__main__':
#     print(TestStates.all())