from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,request,redirect,session,flash, get_flashed_messages
import re
from flask_app.models import user

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class Show:
    db = "tvshow"

    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data ['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        self.users_who_liked_ids =[]
        self.users_who_liked=[]
        

    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO shows
        (title, network, release_date, description, user_id)
        Values 
        (%(title)s,%(network)s,%(release_date)s,%(description)s,%(user_id)s);
        """
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query ="""
        SELECT * FROM shows 
        JOIN users AS creators
        ON shows.user_id = creators.id
        LEFT JOIN likes
        ON shows.id = likes.show_id
        LEFT JOIN users AS users_who_liked
        ON users_who_liked.id = likes.user_id;"""
        result = connectToMySQL(cls.db).query_db(query)
        show_list =[]
        for row in result:
            new_show = True
            #create the users_who_liked_data object
            users_who_liked_data = {
                'id':row['users_who_liked.id'],
                'first_name': row['users_who_liked.first_name'],
                'last_name': row['users_who_liked.last_name'],
                'email': row['users_who_liked.email'],
                'password': row['users_who_liked.password'],
                'created_at': row['users_who_liked.created_at'],
                'updated_at': row['users_who_liked.updated_at']
            }
            #Check to see if previously processed show belong to the same as current row
            number_of_show = len(show_list)

            #We have processed a row already
            if number_of_show > 0:
                #Check to see if the last show is the same as th current row's 
                last_show = show_list[number_of_show -1]
                if last_show.id == row['id']:
                    last_show.users_who_liked_ids.append(row['users_who_liked.id'])
                    last_show.users_who_liked.append(user.User(users_who_liked_data))
                    new_show = False

            #Create new show object if show has not been created and added to the list
            if new_show:
                #create the show object
                show_ob = cls(row)
                #create the creators object
                creators_data ={
                    'id':row['creators.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['creators.created_at'],
                    'updated_at': row['creators.updated_at']
                }
                creator_ob = user.User(creators_data)
                #associate the two objects together
                show_ob.creators = creator_ob
                #Check to see if anyone like this show
                if row['users_who_liked.id']:
                    show_ob.users_who_liked_ids.append(row['users_who_liked.id'])
                    show_ob.users_who_liked.append(user.User(users_who_liked_data))
                
                #Add show object to list of shows
                show_list.append(show_ob)
        return show_list

    @classmethod
    def update(cls,data):
        query = "UPDATE shows SET title = %(title)s, network=%(network)s ,release_date = %(release_date)s, description=%(description)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @staticmethod
    def validate_show( show_data ):
        is_valid = True
        if len(show_data['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters ","show")
        if len(show_data['network']) < 3:
            is_valid = False
            flash("Network must be at least 3 characters","show")
        if show_data['release_date'] == "":            
            is_valid = False
            flash("Date must be select.","show")
        if len(show_data['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","show")
        return is_valid
    

    @classmethod
    def get_one(cls,data):
        query ="""
        SELECT * FROM shows 
        JOIN users AS creators
        ON shows.user_id = creators.id
        LEFT JOIN likes
        ON shows.id = likes.show_id
        LEFT JOIN users AS users_who_liked
        ON users_who_liked.id = likes.user_id
        WHERE
        shows.id = %(id)s;"""

        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        if len(result) < 1:
            return False

        new_show = True
        for row in result:
            #If this is the first row being processed
            #Create new show object if show has not been created and added to the list
            if new_show:
                #create the show object
                show_ob = cls(row)
                #create the creators object
                creators_data ={
                    'id':row['creators.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['creators.created_at'],
                    'updated_at': row['creators.updated_at']
                }
                creator_ob = user.User(creators_data)
                #associate the two objects together
                show_ob.creators = creator_ob
                new_show=False

            if row['users_who_liked.id']:
                #create the users_who_liked_data object
                users_who_liked_data = {
                    'id':row['users_who_liked.id'],
                    'first_name': row['users_who_liked.first_name'],
                    'last_name': row['users_who_liked.last_name'],
                    'email': row['users_who_liked.email'],
                    'password': row['users_who_liked.password'],
                    'created_at': row['users_who_liked.created_at'],
                    'updated_at': row['users_who_liked.updated_at']
                }
                show_ob.users_who_liked_ids.append(row['users_who_liked.id'])
                show_ob.users_who_liked.append(user.User(users_who_liked_data))
        return show_ob

    @classmethod
    def like(cls,data):
        query ="INSERT INTO likes(user_id, show_id) VALUES (%(user_id)s, %(id)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result


    @classmethod
    def unlike(cls,data):
        query = "DELETE FROM likes WHERE user_id = %(user_id)s AND show_id = %(id)s ;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result 