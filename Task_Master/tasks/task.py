

from flask import jsonify, session, request, redirect
import uuid


from database import task_master_database


class Task():

    ERROR_STATUS   = 400
    SUCCESS_STATUS = 200

    GENERAL_ERROR = {"error": "operation failed."}


    def add_task(self): 

        new_task = {
                     "_id": uuid.uuid4().hex,
                     "content": request.form.get("content"),
                     "user_id": session["user"]["_id"] 
                   }


        query_parameters = new_task

        query_result = task_master_database.tasks.insert_one(query_parameters)

        if(query_result):

            return redirect("/tasks/user/dashboard/")


        error_message = jsonify(Task.GENERAL_ERROR)

        return error_message, Task.ERROR_STATUS


    def delete_task(self, task_id): 

        query_parameters = {"_id": task_id, "user_id": session["user"]["_id"]}

        query_result = task_master_database.tasks.delete_one(query_parameters)

        if(query_result):

            return redirect("/tasks/user/dashboard/")


        error_message = jsonify(Task.GENERAL_ERROR)

        return error_message, Task.ERROR_STATUS


    @staticmethod
    def fetch_all_tasks(): 

        query_parameters = {"user_id": session["user"]["_id"]}

        query_result = task_master_database.tasks.find(query_parameters)

        query_result = list(query_result)

        return query_result
