from flask import Flask, render_template, redirect, flash
app = Flask('app')

app.config['SECRET_KEY'] = 'Luiz$uza2904'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
  flash(f'Bem-vindo, {name}!', 'info')
  return render_template('flashing.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)