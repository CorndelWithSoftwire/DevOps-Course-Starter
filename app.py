from flask import Flask, render_template, request, redirect, url_for
import session_items
import pdb
from datetime import datetime, timedelta


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        todo_items = []
        for item in self._items:
            if item["status"] == "To Do":
                todo_items.append(item)
            else:
                continue
        return todo_items

    @property
    def in_progress_items(self):
        in_progress_items = []
        for item in self._items:
            if item["status"] == "In Progress":
                in_progress_items.append(item)
            else:
                continue
        return in_progress_items

    @property
    def complete_items(self):
        complete_items = []
        for item in self._items:
            if item["status"] == "Complete":
                complete_items.append(item)
            else:
                continue
        return complete_items

    @property
    def show_all_done_items(self):
        if len(self.complete_items) <= 5:
            return True
        else:
            return False

    @property
    def recent_done_items(self):
        datetime_yesterday = datetime.now() - timedelta(minutes=1)
        recent_done_items = []
        for item in self._items:
            if (item["status"] == "Complete") and (
                item["last_edited"] > datetime_yesterday
            ):
                recent_done_items.append(item)
            else:
                continue

        return recent_done_items

    @property
    def older_done_items(self):
        datetime_yesterday = datetime.now() - timedelta(minutes=1)
        older_done_items = []
        for item in self._items:
            if (item["status"] == "Complete") and (
                item["last_edited"] < datetime_yesterday
            ):
                older_done_items.append(item)
            else:
                continue

        return older_done_items


def create_app():
    app = Flask(__name__) 
    app.config.from_object('flask_config.Config')

    @app.route("/")
    def index():
        items = session_items.get_items()
        item_view_model = ViewModel(items)


        return render_template("index.html", view_model=item_view_model)


    @app.route("/create_item", methods=["POST"])
    def create_item():
        new_dict = request.form.to_dict(flat=False)
        for item_name in new_dict["newitem"]:
            session_items.add_item(item_name)

        return redirect("/")


    # @app.route("/mark_in_progress", methods=["POST"])
    # def mark_in_progress():
    #     new_dict = request.form.to_dict(flat=False)
    #     for id in new_dict.keys():
    #         item = session_items.get_item(id)
    #         session_items.mark_in_progress(item)

    #     return redirect("/")


    # @app.route("/mark_as_complete", methods=["POST"])
    # def mark_as_complete():
    #     new_dict = request.form.to_dict(flat=False)
    #     for id in new_dict.keys():
    #         item = session_items.get_item(id)
    #         session_items.mark_complete(item)

    #     return redirect("/")


    @app.route("/update_status", methods=["POST"])
    def update_status():
        new_dict = request.form.to_dict(flat=False)
        string_select_update = new_dict["select_update"][0]
        if "item_id" in new_dict:
            item = session_items.get_item(int(new_dict["item_id"][0]))
            session_items.update_status(item, string_select_update)

        return redirect("/")


    @app.route("/delete_item", methods=["POST"])
    def delete_item():
        new_dict = request.form.to_dict(flat=False)
        for id in new_dict.keys():
            item = session_items.get_item(id)
            session_items.delete_item(item)

        return redirect("/")

    @app.route("/due_date", methods=["POST"])
    def due_date(): 
        new_dict = request.form.to_dict(flat=False)
        due_date_update = new_dict["duedate"][0]
        if "item_id" in new_dict:
            item = session_items.get_item(int(new_dict["item_id"][0]))
            session_items.due_date(item, due_date_update)
        
        return redirect("/")

    return app