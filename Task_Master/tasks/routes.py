
from flask import Blueprint, render_template, redirect, session
from functools import wraps

from tasks.task import Task


tasks = Blueprint("tasks", __name__)


def make_login_repuired(func):

    @wraps(func)
    def wrap(*args, **kwargs):

        if ("logged_in" in session):

            return func(*args, **kwargs)

        else:

            return redirect("/")

    return wrap


@tasks.route("/tasks/user/dashboard/")
@make_login_repuired
def show_user_dashboard_page():

    connected_user_tasks = Task.fetch_all_tasks()

    return render_template("user_dashboard.html", tasks = connected_user_tasks)


@tasks.route("/tasks/user/add/", methods = ["POST"])
@make_login_repuired
def add_task():

    new_task = Task()

    return new_task.add_task()


@tasks.route("/tasks/user/delete/<_id>/", methods = ["GET"])
@make_login_repuired
def delete_task(_id):

    task_to_delete = Task()

    return task_to_delete.delete_task(_id)
