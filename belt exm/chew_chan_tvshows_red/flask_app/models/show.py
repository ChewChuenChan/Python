from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,request,redirect,session,flash, get_flashed_messages
import re
from flask_app.models import user

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class Show:
    db = "tvshow_schema"

    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data ['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        # self.users_ids_who_favorited =[]
        # self.users_who_favorited=[]
        

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

    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM shows;"
    #     result = connectToMySQL(cls.db).query_db(query)
    #     all_shows = []
    #     if len(result) <1:
    #         return all_shows
    #     else:
    #         for row in result:
    #             all_shows.append(cls(row))
    #         return all_shows

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows JOIN users ON shows.user_id = users.id;"        
        result = connectToMySQL(cls.db).query_db(query)
        shows_list =[]
        if len(result) <1:
            return shows_list
        else:
            for row in result:
                #create the review object
                show_ob = cls(row)
                #create the creators object
                users_data ={
                    'id':row['users.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                user_ob = user.User(users_data)
                #associate the two objects together
                show_ob.user = user_ob
                #Add review object to list of reviews
                shows_list.append(show_ob)
        return shows_list

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
        query = """
        SELECT * FROM shows 
        JOIN users ON 
        shows.user_id = users.id
        WHERE
        shows.id = %(id)s;"""
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        if len(result) < 1:
            return False
        row = result[0]
        #create the review object
        show = cls(row)
        #create the user object
        user_data ={
            'id':row['users.id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'password': row['password'],
            'created_at': row['users.created_at'],
            'updated_at': row['users.updated_at']
            }
        user_ob = user.User(user_data)
        #associate the two objects together
        show.user = user_ob
        return show

    # @classmethod
    # def like(cls,data):
    #     query ="INSERT INTO liked_show(user_id, review_id) VALUES (%(user_id)s, %(id)s);"
    #     result = connectToMySQL(cls.db).query_db(query,data)
    #     return result


    # @classmethod
    # def unlike(cls,data):
    #     query = "DELETE FROM liked_show WHERE user_id = %(user_id)s AND review_id = %(id)s ;"
    #     result = connectToMySQL(cls.db).query_db(query,data)
    #     return result 