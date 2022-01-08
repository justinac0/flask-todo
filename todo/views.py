from flask import (
    redirect,
    request,
    url_for,
    Blueprint,
    render_template
)

from . import models

todo = Blueprint("todo", __name__)


def get_entries():
    return models.Entry.query.all()


@todo.route("/", methods=["GET"])
def index():
    return render_template("todo/index.html", entries=get_entries())


@todo.route("/new", methods=["POST"])
def new():
    entry = models.Entry(request.form["body"])
    models.db.session.add(entry)
    models.db.session.commit()

    return redirect("/")


@todo.route("/delete", methods=["POST"])
def delete():
    models.db.session.delete(
        models.Entry.query.filter(
            models.Entry.id == request.form['id']
        ).first()
    )

    models.db.session.commit()

    return redirect("/")


@todo.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    return None


@todo.route("/get/<int:id>", methods=["GET"])
def get(id):
    entries = get_entries()
    print(entries)
    return None
