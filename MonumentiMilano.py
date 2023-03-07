from flask import Flask,render_template
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])  #sono tutte le possibili richieste del utente
def hello_world():
    return render_template('./MonumentiMilano/index.html')

#@app.route('/', methods=['GET'])
#def ciao_mondo():
#    return render_template('')

#@app.route('/', methods=['GET'])
#def inserHtml():
#    return render_template('')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma