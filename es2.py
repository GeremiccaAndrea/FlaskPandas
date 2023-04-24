from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep = ';')

@app.route('/')
def search():
  lingua = request.args('lingua')
  return render_template('es2.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)