import requests


def custom_text(chat_id, text):
    url = "http://api.telegram.org/bot"
    bot_key = "1339449529:AAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0"
    method = "/SendMessage?chat_id="
    message = "&text=" + str(text) + "\nregards, \nBhavik patel's Chemistry tuitions.\nPowered by markOS from Aexior."
    message_request = url + bot_key + method + str(chat_id) + message
    requests.get(message_request)

def admission_successful(chat_id, name):
    url = "http://api.telegram.org/bot"
    bot_key = "1339449529:AAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0"
    method = "/SendMessage?chat_id="
    text = f"Congratulations! {name}'s admission to Bhavik Patel's chemistry tuitions is successful. We will be sending texts through this Telegram account.\nHave a nice day," + "\nBhavik patel's Chemistry tuitions.\nPowered by markOS from Aexior."
    message = "&text=" + str(text)
    message_request = url + bot_key + method + str(chat_id) + message
    requests.get(message_request)

def send_them_scores(name, score, maxscore, subject, date, g_cid, s_cid):
    url = "http://api.telegram.org/bot"
    bot_key = "1339449529:AAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0"
    method = "/SendMessage?chat_id="
    text = f"{name} has scored {score} out of {maxscore} in {subject} test taken on {date}\nScore = {score}/{maxscore}.\nHave a nice day," + "\nBhavik patel's Chemistry tuitions.\nPowered by markOS from Aexior."
    message = "&text=" + str(text)
    message_request_g = url + bot_key + method + str(g_cid) + message
    message_request_s = url + bot_key + method + str(s_cid) + message
    requests.get(message_request_g)
    requests.get(message_request_s)
