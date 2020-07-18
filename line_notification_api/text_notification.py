import requests
url = 'https://notify-api.line.me/api/notify'
token = 'your token'


def text(token, text):
    LINE_HEADERS = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    try:
        session_post = requests.post(url, headers=LINE_HEADERS , data = {'message':text})
        print(session_post.text)
    except:
        print("Network is not connected")

if __name__ == '__main__':
    text(token, "Hello")