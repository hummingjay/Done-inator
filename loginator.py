import sqlite3

class TaskDatabase:
    """
    This class controls connection, editing, saving and deleting from the
    app's database
    """
    def add_task(self, Task):
        try:
            """
            Function that adds a task to the database
            """
            conn = sqlite3.connect("to-do.db")
            c = conn.cursor()
            
            insert_task = "INSERT INTO 'to-do' (Task) VALUES (?)"
            c.execute(insert_task, (Task, ))
            
            conn.commit()
            c.close()
            conn.close()
        except sqlite3.Error as e:
            print("The error here is: ", e)
            return[]
    
    def update_task(self, New, Old):
        try:
            """
            Update a task in the database
            """
            conn = sqlite3.connect("to-do.db")
            c = conn.cursor()
            
            Update_task = "UPDATE 'to-do' SET Task=? WHERE Task=?"
            c.execute(Update_task, (New, Old))
            
            conn.commit()
            c.close()
            conn.close()
        except sqlite3.Error as e:
            print("The error here is: ", e)
            return[]
    
    def update_status(self, status, Task):
        try:
            """
            Update the staus between done and not done
            """
            conn = sqlite3.connect("to-do.db")
            c = conn.cursor()
            
            Update_status = "UPDATE 'to-do' SET Task_status=? WHERE Task=?"
            
            new_status = 0 if not status else 1
            
            c.execute(Update_status, (new_status, Task))
            
            conn.commit()
            c.close()
            conn.close()
        except sqlite3.Error as e:
            print("The error here is: ", e)
            return[]
    
    def DeleteTask(self, Task):
        try:
            """
            Deletes task from the database
            """
            conn = sqlite3.connect("to-do.db")
            c = conn.cursor()
            
            delete_task = "DELETE FROM 'to-do' WHERE Task=?"
            
            c.execute(delete_task, (Task, ))
            
            conn.commit()
            c.close()
            conn.close()
        except sqlite3.Error as e:
            print("The error here is: ", e)
            return[]
            
    
    def ReadData(self):
        try:
            conn = sqlite3.connect("to-do.db")
            c = conn.cursor()
            
            c.execute("SELECT Task, Task_status FROM 'to-do'")

            tasks = [{'Task':value[0], 'Task_status':value[1]}for value in c.fetchall()]

            c.close()
            conn.close()
            
            return tasks
        except sqlite3.Error as e:
            print("The error here is: ", e)
            return[]