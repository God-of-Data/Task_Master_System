
from flask import request, jsonify, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid

from database import task_master_database


class User():

    ERROR_STATUS   = 400
    SUCCESS_STATUS = 200


    def sign_in(self):

        GENERAL_EMAIL_ERROR = {"error": "Sign In has failed."}


        user = {            
                    "email": request.form.get("email"),            
                    "password": request.form.get("password")       
               }  

        query_parameters = {"email": user["email"]}

        query_result = task_master_database.users.find_one(query_parameters)

        if (query_result):

            password_is_correct = pbkdf2_sha256.verify(user["password"], query_result["password"])

            if(password_is_correct):

                return self.start_session(query_result)


        error_message = jsonify(GENERAL_EMAIL_ERROR)

        return error_message, User.ERROR_STATUS 


    def sign_up(self):

        GENERAL_EMAIL_ERROR = {"error": "Sign Up has failed."}
        UNIQUE_EMAIL_ERROR  = {"error": "Email address is already in use."}


        new_user = {
                        "_id": uuid.uuid4().hex,
                        "name": request.form.get("name"),
                        "email": request.form.get("email"),
                        "password": request.form.get("password")
                   }   

        new_user["password"] = pbkdf2_sha256.encrypt(new_user["password"])


        query_parameters = {"email": new_user["email"]}

        query_result = task_master_database.users.find_one(query_parameters)


        if (query_result):

            error_message = jsonify(UNIQUE_EMAIL_ERROR)

            return error_message, User.ERROR_STATUS


        query_parameters = new_user

        query_result = task_master_database.users.insert_one(query_parameters)

        if (query_result):

            return self.start_session(new_user)


        error_message = jsonify(GENERAL_EMAIL_ERROR)

        return error_message, User.ERROR_STATUS 


    def sign_out(self):

        User.end_session()

        return redirect("/")


    @staticmethod
    def start_session(user):

        temp_user = user

        del temp_user["password"]

        session["logged_in"] = True
        session["user"] = temp_user

        temp_user = jsonify(user)

        return temp_user, User.SUCCESS_STATUS


    @staticmethod
    def end_session():

        session.clear()
