import requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").text

if __name__ == '__main__':
    print(get_proxy())