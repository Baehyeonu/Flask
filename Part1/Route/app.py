from flask import Flask, request, Response
import test

app = Flask(__name__)

@app.route('/')
def home():
    return "hello this is main page"

@app.route('/about')
def about():
    return "hello this is about page"

@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

# psot 요청 날리는 법
# (1) postman
# (2) requestrs
import requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    date = 'test data'
    response = requests.post(url=url, data=data)

    return response

@app.route('/submit', methods=['GET','POST','PUT','DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST method***", request.data)

    return Response("success submitted", status=200)

if __name__ == "__main__":
    app.run(debug=True)