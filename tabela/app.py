from flask import Flask, render_template, request, redirect


app = Flask(__name__)

# Restante do código...

@app.route('/adicionar_numero/<int:id>', methods=['POST'])
def adicionar_numero(id):
    # Lógica para adicionar um número ao cliente com o ID fornecido
    # ...

    return redirect('/')

import sqlite3

app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect('cadastros.db')

@app.route('/')
def index():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cadastros')
    clientes = cursor.fetchall()
    conn.close()
    return render_template('index.html', clientes=clientes)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        endereco = request.form['endereco']

        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO cadastros (nome, cpf, endereco) VALUES (?, ?, ?)', (nome, cpf, endereco))
        conn.commit()
        conn.close()

    return redirect('/')

@app.route('/deletar/<int:id>')
def deletar(id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cadastros WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

# Restante do código...

@app.route('/adicionar_numero/<int:id>', methods=['POST'])
def adicionar_numero(id):
    # Lógica para adicionar um número ao cliente com o ID fornecido
    # ...

    return redirect('/')

