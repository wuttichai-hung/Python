import requests
token = 'your token'
url = 'https://notify-api.line.me/api/notify'


def image(token, text, path_img):
    file_img = {'imageFile': open(path_img, 'rb')}
    LINE_HEADERS = {"Authorization": "Bearer "+ token}
    try:
        session_post = requests.post(url, headers=LINE_HEADERS, files=file_img, data= {'message': text})
        print(session_post.text)
    except:
        print("Internet is not connected")

if __name__ == '__main__':
    text = "oh!"
    image_path = "myimage.jpg"
    image(token, text, image_path)