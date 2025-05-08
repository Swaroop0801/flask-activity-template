from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store tasks as a list of dictionaries
tasks = []

@app.route('/')
def home():
    return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form['task']
    tasks.append({'text': task_text, 'done': False})
    return redirect(url_for('home'))

@app.route('/complete/<int:index>')
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
