from flask import Flask, request, render_template, redirect, url_for

from forms import TodoForm
from models import todos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/")
def home():
    todos_list=todos.all() #pobranie zapisanych książek
    return render_template("index.html", todos=todos_list)

@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""

    if request.method == "POST":
        if form.validate_on_submit():
            todos.create(form.data)
            todos.save_all()
        return redirect(url_for("todos_list"))

    #Pobranie listy książek
    todos_list = todos.all()

    #Pobranie parametru sortowania z URL
    sort_by = request.args.get("sort_by")

    #Sortowanie według autora lub oceny
    if sort_by == "author":
        todos_list = sorted(todos_list, key=lambda x: x["author"].lower())  # Sortowanie alfabetycznie według autora
    elif sort_by == "rating":
        todos_list = sorted(todos_list, key=lambda x: int(x["bookrating"]), reverse=True)  # Sortowanie według oceny (malejąco)

    return render_template("todos.html", form=form, todos=todos_list, error=error)


@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos.get(todo_id - 1)
    form = TodoForm(data=todo)

    if request.method == "POST":
        if form.validate_on_submit():
            todos.update(todo_id - 1, form.data)
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, todo_id=todo_id)

@app.route("/todos/<int:todo_id>/delete", methods=["POST"])
def delete_todo(todo_id):
    todos.delete(todo_id - 1)  # Usuwanie książki z listy
    todos.save_all()  # Zapisanie zmian
    return redirect(url_for("todos_list"))


if __name__ == "__main__":
    app.run(debug=True)