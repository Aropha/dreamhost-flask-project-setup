from flask import Flask, render_template, request, make_response, Response

app = Flask(__name__)


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')


#Starting the Flask Server 
if __name__ == '__main__':
    app.debug = True
    app.run()
