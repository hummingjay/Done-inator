import sqlite3

class TaskDatabase:
    """
    This class controls connection, editing, saving and deleting from the
    app's database
    """
    def add_task(self, Task):
        """
        Function that adds a task to the database
        """
        conn = sqlite3.connect("to-do.db")
        c = conn.cursor()
        
        insert_task = "INSERT INTO 'to-do' (Task) VALUES (?)"
        c.execute(insert_task, (Task, ))
        
        conn.commit()
        conn.close()
    
    def update_task(self, New, Old):
        """
        Update a task in the database
        """
        conn = sqlite3.connect("to-do.db")
        c = conn.cursor()
        
        Update_task = "UPDATE 'to-do' SET Task=? WHERE Task=?"
        c.execute(Update_task, (New, Old))
        
        conn.commit()
        conn.close()
    
    def update_status(self, status, Task):
        """
        Update the staus between done and not done
        """
        conn = sqlite3.connect("to-do.db")
        c = conn.cursor()
        
        Update_status = "UPDATE 'to-do' SET Task_status=? WHERE Task=?"
        
        new_status = 0 if not status else 1
        
        c.execute(Update_status, (new_status, Task))
        
        conn.commit()
        conn.close()
    
    def DeleteTask(self, Task):
        """
        Deletes task from the database
        """
        conn = sqlite3.connect("to-do.db")
        c = conn.cursor()
        
        delete_task = "DELETE FROM 'to-do' WHERE Task=?"
        
        c.execute(delete_task, (Task, ))
        
        conn.commit()
        conn.close()
    
    def ReadData(self):
        conn = sqlite3.connect("to-do.db")
        c = conn.cursor()
        
        records = c.fetchall()
        c.execute()
        
        conn.commit()
        conn.close()