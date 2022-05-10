help_message = f"❓ Основные команды:\n\n/start - Перезапустить бота\n/help - Вызвать помощь (это сообщение)\n\nВ остальном следует нажимать кнопки бота и вводить необходимые данные в нужном формате.\nКак минимум, добавьте номер машиноместа, чтобы вас могли находить и писать послания. \nНеобязательно, но желательно добавлять номера автомобилей и свои телефоны, так вы даете больше возможностей с вами связаться в случае чего. Эти данные я не показываю, но использую для поиска ваших телеграм-аккаунтов.\n\nНапример, если вы впишите номер автомобиля, то другие собственники смогут по нему найти ваш телеграм аккаунт или написать анонимку о том, что у вас колесо спущено или окно не закрыто итп. Но бот умеет посылать в анонимках только текст.\n\n PS: все вопросы по работе бота к @dimkanio"
start_message = f"Привет! 👋 Я бот-помощник чата парковки. \n\nВы сможете оставлять через меня сообщения соседям по паркингу, при этом вам нужен только номер машиноместа или номер автомобиля. Если эти данные есть у меня, я передам сообщение адресату. \n\nТакже я могу вам подсказывать всякое, например, на каком месте паркуется автомобиль с определенным номером, или статистику по занятым или свободным местам!\n\nПрисоединяйтесь! 😊. "
need_invite = f"Вам нужно сначала вступить в группу \n\n'Паркинг 2 блока ЖК Ясеневая 12к5' \n\nНапишите админу @andrey_barakin. \nНо будьте готовы подтвердить свое право собственности на паркинг."
nlo = f"Неопознанный пользователь! Вам точно нужен этот бот? напишите @dimkanio"

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'need_invite': need_invite,
    'nlo': nlo
}

class TgAddresses:
    tg_ids = {}