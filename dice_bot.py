import requests, pprint, random

token = '2053819400:AAFav9zWTsALzdr49fE53VT3GSFRP4puJsg'
base_url = 'https://api.telegram.org/bot' + token

offset = 0


while True:
    response = requests.post(url=base_url + '/getUpdates', data={
        'offset': offset,
        'timeout': 120
    })
    updates = response.json() # Достать json тело из ответа
    result = updates['result']
    for update in result:
        if 'message' not in update:
            continue

        # pprint.pp(update)
        update_id = update['update_id']
        offset = update_id + 1

        message = update['message']
        if 'text' not in message:
            continue

        message_text = message['text']
        message_id = message['message_id']
        chat_id = message['chat']['id']
        numeric1 = message_text.split(' ')
        if len(numeric1) == 3:
            if numeric1[0] == 'roll':
                random_number = random.randint(int(numeric1[1]), int(numeric1[2]))
                requests.post(url=base_url + '/sendMessage', data={
                    'text': str(random_number),
                    'chat_id': chat_id,
                    'reply_to_message_id': message_id
                })
        else:
            requests.post(url=base_url + '/sendMessage', data={
                    'text': 'неверный формат',
                    'chat_id': chat_id,
                    'reply_to_message_id': message_id
                })