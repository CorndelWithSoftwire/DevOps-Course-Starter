from flask import Flask, render_template, request, redirect, url_for
import todo_app.data.session_items as session_items
from datetime import datetime, timedelta
from todo_app.view_model import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object("todo_app.flask_config.Config")

    @app.route("/")
    def index():
        items = session_items.get_items()
        item_view_model = ViewModel(items)

        return render_template("index.html", view_model=item_view_model)

    @app.route("/create_item", methods=["POST"])
    def create_item():
        new_item_name = request.form["newitem"]
        session_items.add_item(new_item_name)

        return redirect("/")

    @app.route("/delete_item", methods=["POST"])
    def delete_item():
        new_dict = request.form.to_dict(flat=False)
        item_id = new_dict["item_id"][0]
        session_items.delete_item(item_id)

        return redirect("/")

    @app.route("/update_status", methods=["POST"])
    def update_status():
        new_dict = request.form.to_dict(flat=False)
        string_select_update = new_dict["select_update"][0]
        item_id = new_dict["item_id"][0]
        session_items.update_status(string_select_update, item_id)

        return redirect("/")

    @app.route("/due_date", methods=["POST"])
    def due_date():
        new_dict = request.form.to_dict(flat=False)
        due_date_update = new_dict["duedate"][0]
        item_id = new_dict["item_id"][0]
        session_items.due_date(item_id, due_date_update)

        return redirect("/")

    return app


if __name__ == "__main__":
    create_app().run()

