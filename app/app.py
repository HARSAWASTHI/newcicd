from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Devops and CICD Jenkins Application for Demo Purpose DO14WD -E batch'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
