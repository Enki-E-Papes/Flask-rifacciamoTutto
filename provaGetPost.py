from flask import Flask,render_template,request
app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/')  #sono tutte le possibili richieste del utente
def hello_world():
    return render_template('./postGet/GetPost.html')


@app.route('/login')  #sono tutte le possibili richieste del utente
def Login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == 'xxx123##':
         return render_template('./postGet/login.html',username=username)
    else:  
        return render_template('./postGet/errore.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma