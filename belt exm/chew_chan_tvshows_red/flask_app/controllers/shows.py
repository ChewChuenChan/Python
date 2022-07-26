from flask_app import app
from flask import render_template,request,redirect,session,flash, get_flashed_messages
from datetime import datetime
from flask_app.models import user
from flask_app.models.show import Show


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Must be logged in to do that!", "error")
        return redirect("/logout")
    else:
        return render_template("dashboard.html", 
        user = user.User.get_by_id({"id" : session["user_id"]}),
        all_shows = Show.get_all(),
        error = get_flashed_messages(category_filter="error"))


@app.route('/show/new')
def new_show():
    return render_template("add_show.html", 
                show_msg = get_flashed_messages(category_filter="show"),
                error = get_flashed_messages(category_filter="error"))

@app.route('/show/create', methods =['POST'])
def create_show():
    if "user_id" not in session:
            flash("Must be logged in to do that!", "error")
            return redirect("/logout")
    if not Show.validate_show(request.form):
            return redirect('/show/new')
    else:
        data ={
                "user_id": session['user_id'],
                "title" : request.form['title'],
                "network" : request.form['network'],
                "release_date" : request.form['release_date'],
                "description" : request.form['description']
        }
        show_id = Show.create(data)
        return redirect('/dashboard')


@app.route('/show/edit/<int:id>')
def edit_show(id):
    data={
        'id':id
    }
    show = Show.get_one(data)
    return render_template('edit_show.html', 
    show=show, 
    show_msg = get_flashed_messages(category_filter="show"), 
    error = get_flashed_messages(category_filter="error"))

@app.route('/show/update/<int:id>', methods =['POST'])
def update_show(id):
    if "user_id" not in session:
        flash("Must be logged in to do that!", "error")
        return redirect("/logout")
    if not Show.validate_show(request.form):
        return redirect('/show/new')
    else:
        show = Show.update(request.form)
        return redirect ('/dashboard')

@app.route('/show/<int:id>')
def view_show(id):
    data={
        'id':id
    }
    show = Show.get_one(data)
    return render_template('show.html', show=show)


@app.route('/show/delete/<int:id>')
def delete(id):
        if 'user_id' not in session:
                return redirect ('/logout')
        data={
                "id": id
        }
        Show.delete(data)
        return redirect ('/dashboard')

# @app.route('/show/like/<int:id>', methods=['POST'])
# def like(id):
#     Show.like(request.form)
#     return redirect('/dashboard')

# @app.route('/show/unlike/<int:id>', methods=['POST'])
# def unlike(id):
#     Show.unlike(request.form)
#     return redirect('/dashboard')