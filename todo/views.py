from flask import (
    redirect,
    request,
    url_for,
    Blueprint,
    render_template
)
from flask_sqlalchemy import model
from sqlalchemy.orm import session

from . import models

todo = Blueprint("todo", __name__)


def get_entry(id):
    return models.Entry.query.filter(models.Entry.id == id).first()


def get_entries():
    return models.db.session.query(models.Entry).order_by(models.Entry.is_done)


@todo.route("/", methods=["GET"])
def index():
    return render_template("todo/index.html", entries=get_entries())


@todo.route("/new", methods=["POST"])
def new():
    entry = models.Entry(request.form["body"])
    models.db.session.add(entry)
    models.db.session.commit()

    return redirect("/")


@todo.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    models.db.session.delete(get_entry(id))
    models.db.session.commit()

    return redirect("/")


@todo.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    entry = get_entry(id)

    if request.method == "POST" and entry is not None:
        entry.body = request.form["body"]
        models.db.session.commit()

        return redirect("/")

    return render_template("todo/edit.html", entry=entry)


@todo.route("/done/<int:id>", methods=["GET", "POST"])
def done(id):
    entry = get_entry(id)

    if request.method == "POST" and entry is not None:
        entry.is_done = not entry.is_done
        models.db.session.commit()

        return redirect("/")

    return render_template("todo/edit.html", entry=entry)