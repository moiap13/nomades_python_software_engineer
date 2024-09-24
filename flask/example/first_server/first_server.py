from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
  return '<h1>Hello</h1> <p>Flask class, The best class!</p>'

@app.route('/hello/<name>')
def hello(name):
  return f'<h1>Hello {name}</h1>'

@app.route('/allow/<int:age>')
def allow_voting(age):
    return "You are allowed to enter the voting website" if age >= 18 else "You are not allowed to enter the voting website"



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)