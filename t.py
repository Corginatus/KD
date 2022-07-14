import vk_api
from config import token
import re


def getUserIdByUrl(url):

    username = re.split('https://vk.com/', url)[1]
    session = vk_api.VkApi(token=token)
    x = session.method('users.get', {'user_ids': username})

    return x[0]['id']


result = getUserIdByUrl('https://vk.com/atamacer')
print(result)