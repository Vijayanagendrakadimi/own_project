from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Here you would typically check the username and password against a database
    if username == 'admin' and password == 'password':  # Example credentials
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)