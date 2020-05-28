import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import constants
import texts

def greeting_button(vk, event):

    keyboard = VkKeyboard(inline=True)

    keyboard.add_button('Хочу быть отвечающим!', color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_openlink_button('Информация о сообществе', link=constants.GROUP_MENU)
    keyboard.add_line()
    keyboard.add_button('Связь с администрацией', color=VkKeyboardColor.POSITIVE) 


    vk.messages.send(
                user_id = event.message.from_id,
                random_id = get_random_id(),
                message = texts.STARTING_MESSAGE,
                keyboard = keyboard.get_keyboard()
                )

def redirect_to_admins(vk, event):
    # Sends message to user
    vk.messages.send(
        user_id = event.message.from_id,
        random_id = get_random_id(),
        message = texts.CONTACT_ADMINS,
    )
    """
    # Sends message to admin group chat
    vk.messages.send(
        random_id = get_random_id(),
        message = f'{event.message.user_id} хочет связаться с администрацией',
        #chat_id = 84,
        peer_id = -195480573,
    )
    """

def wanna_answer_too(vk, event):
    vk.messages.send(
        user_id = event.message.from_id,
        random_id = get_random_id(),
        message = texts.ASK_FOR_PORTFOLIO,
    )