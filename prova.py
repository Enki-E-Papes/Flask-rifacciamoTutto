from flask import Flask,render_template
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])
def hello_world():
    return ('<h1>Hello, world!</h1>')

@app.route('/it', methods=['GET'])
def ciao_mondo():
    return ('<h1>Ciao, mondo!</h1>')

@app.route('/ben', methods=['GET'])
def inserHtml():
    return render_template('benvenuto.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma