from flask import Flask, render_template, request, redirect, url_for
import todo_app.data.session_items as session_items
from todo_app.view_model import ViewModel
from datetime import datetime, timedelta


def create_app():
    app = Flask(__name__)
    app.config.from_object("todo_app.flask_config.Config")

    @app.route("/")
    def index():
        items = session_items.get_items()
        item_view_model = ViewModel(items)

        return render_template("index.html", view_model=item_view_model)

    @app.route("/add_item", methods=["POST"])
    def add_item():
        new_item = request.form.get("name")
        session_items.add_item(new_item)

        return redirect("/")

    @app.route("/mark_complete", methods=["POST"])
    def mark_complete():
        new_dict = request.form.to_dict(flat=False)
        for id in new_dict.keys():
            item = session_items.get_item(id)
            session_items.mark_complete(item)

        return redirect("/")

    @app.route("/mark_in_progress", methods=["POST"])
    def mark_in_progress():
        new_dict = request.form.to_dict(flat=False)
        for id in new_dict.keys():
            item = session_items.get_item(id)
            session_items.mark_in_progress(item)

        return redirect("/")

    @app.route("/delete_item", methods=["POST"])
    def delete_item():
        new_dict = request.form.to_dict(flat=False)
        for id in new_dict.keys():
            item = session_items.get_item(id)
            session_items.delete_item(item)

        return redirect("/")

    return app


if __name__ == "__main__":
    create_app().run()
