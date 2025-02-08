from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo_items = []
notes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Cannot divide by zero'
    return render_template('calculator.html', result=result)

@app.route('/todo', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        if 'add' in request.form:
            todo_items.append(request.form['item'])
        elif 'remove' in request.form:
            idx = int(request.form['index']) - 1
            if 0 <= idx < len(todo_items):
                todo_items.pop(idx)
    return render_template('todo.html', todo_items=todo_items)

@app.route('/notes', methods=['GET', 'POST'])
def note_taking():
    if request.method == 'POST':
        if 'add' in request.form:
            notes.append(request.form['note'])
        elif 'remove' in request.form:
            idx = int(request.form['index']) - 1
            if 0 <= idx < len(notes):
                notes.pop(idx)
    return render_template('notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
