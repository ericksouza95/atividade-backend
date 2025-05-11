from flask import Flask, render_template, request, redirect, url_for, session, flash
import json

app = Flask(__name__)
app.secret_key = 'chave_secreta_simples'  # para gerenciar sessão

# Carregar usuários do JSON
def load_users():
    with open('users.json', 'r') as f:
        return json.load(f)

# Carregar músicas do JSON
def load_musicas():
    try:
        with open('musicas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Salvar músicas no JSON
def save_musicas(musicas):
    with open('musicas.json', 'w') as f:
        json.dump(musicas, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Usuário ou senha inválidos!')
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('home.html', username=session['username'])

@app.route('/musicas', methods=['GET', 'POST'])
def musicas_page():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    musicas = load_musicas()

    if request.method == 'POST':
        action = request.form.get('action')
        musica = request.form.get('musica')

        if action == 'add' and musica:
            musicas.append(musica)
        elif action == 'remove' and musica in musicas:
            musicas.remove(musica)
        save_musicas(musicas)

    search_query = request.args.get('search')
    if search_query:
        musicas_filtradas = [m for m in musicas if search_query.lower() in m.lower()]
    else:
        musicas_filtradas = musicas

    return render_template('musicas.html', musicas=musicas_filtradas)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)