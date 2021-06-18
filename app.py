from flask import Flask, render_template, request, redirect, url_for
import session_items
import pdb
from datetime import datetime, timedelta
from view_model import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object("flask_config.Config")


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


    @app.route("/delete_item", methods=["POST"])
    def delete_item():
        new_dict = request.form.to_dict(flat=False)
        for id in new_dict.keys():
            item = session_items.get_item(id)
            session_items.delete_item(item)

        return redirect("/")


    @app.route("/update_status", methods=["POST"])
    def update_status():
        new_dict = request.form.to_dict(flat=False)
        string_select_update = new_dict["select_update"][0]
        if "item_id" in new_dict:
            item = session_items.get_item(int(new_dict["item_id"][0]))
            session_items.update_status(item, string_select_update)

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


if __name__ == "__main__":
    create_app().run()