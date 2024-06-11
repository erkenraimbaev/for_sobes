import requests


def get_page(url: str):
    try:
        response = requests.get(url)
    except Exception:
        print('Not right')
    else:
        return f'{response.status_code}'


print(get_page('https://mail.ru'))
assert int(get_page('https://mail.ru')) == 00, 'Ytdthyj erfpfy URL'
