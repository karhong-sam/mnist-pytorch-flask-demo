import requests

resp = requests.post("https://flask-pytorch-test01.herokuapp.com/predict", files={"file": open("nine.png", "rb")})

print(resp.text)