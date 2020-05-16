import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import urllib.request
from constants import BOT_TOKEN, GROUP_ADRESS 
from vk_api.utils import get_random_id
import texts
import button


vk_session = vk_api.VkApi(token=BOT_TOKEN)

vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, GROUP_ADRESS)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.message.text == 'Начать': 
            if event.from_user:  
                """              
                vk.messages.send(
                        user_id = event.message.from_id,
                        random_id = get_random_id(),
                        message = texts.STARTING_MESSAGE,
                        keyboard = 
                        )
                        """
                button.test_button(vk, event)