#! encoding='utf-8'

import requests
import re

domains = [
    'github.global.ssl.fastly.net', 'github.com', 'assets-cdn.github.com',
    'documentcloud.github.com', 'gist.github.com', 'help.github.com',
    'nodeload.github.com', 'raw.github.com', 'status.github.com',
    'training.github.com', 'www.github.com', 'github.global.ssl.fastly.net',
    'avatars0.githubusercontent.com', 'avatars1.githubusercontent.com',
    'codeload.github.com '
]
'''
IP Address</th><td><ul class="comma-separated"><li>199.232.5.194
'''


def get_ip(domain):
    url = "https://www.ipaddress.com/search/" + domain
    headers = {
        'Origin': 'https://www.ipaddress.com',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Sec-Fetch-User': "?1",
        "Sec-Fetch-Site": 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Referer': 'https://www.ipaddress.com/'
    }
    s = requests.session()
    r = s.get(url, headers=headers)
    result = re.findall(
        "IP Address(.|\n)*?comma-separated(.|\n)*?([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})",
        r.text)
    return result[0][2]


print('#github')
for i in domains:
    print(get_ip(i) + '   ' + i)
