from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

# Global list
todo_list = []

# Email validation
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# MAIN PAGE
@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

# SUBMIT
@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # Validation
    if not task or not email or not is_valid_email(email):
        return redirect('/')

    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # Add to list
    todo_list.append({
        "task": task,
        "email": email,
        "priority": priority
    })

    return redirect('/')

# CLEAR
@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)