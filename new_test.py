""" Main app page of the Done-inator"""

import flet
from flet import *
import sqlite3
from tsidebar import Sidebar
import loginator

conn = sqlite3.connect("to-do.db")
c = conn.cursor()

c.execute(
    '''
    CREATE TABLE IF NOT EXISTS 'to-do'(
        id INTEGER PRIMARY KEY,
        Task VARCHAR(255) NOT NULL,
        Task_status INTEGER DEFAULT 0
    )
    '''
)

conn.commit()
conn.close()

class Task(UserControl):
    """
    This class represents a single task item in the to-do list.
    It holds the task's name, completion status and ref to functions for
    manipulating the task (change status, edit, and deleting)
    """
    def __init__(self, task_name: str, task_status: bool, task_delete):
        """_summary_

        Args:
            task (_str_): _Filled in text field and becomes name of task_
            task_status (_bool_): _True or false to tell if the task is edited_
            task_delete (_none_): _deletes the task when needed_
        """
        super().__init__()
        self.completed = task_status
        self.task_name = task_name
        self.task_status = task_status
        self.task_delete = task_delete

    def build(self):
        self.display_task = Checkbox(
            value=self.task_status,
            label=self.task_name,
            on_change=lambda value: self.status_changed(self, value),
        )
        self.edit_name = TextField(on_submit=self.save_clicked ,expand=1)
          
        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_ROUNDED,
                            tooltip="Edit task",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_ROUNDED,
                            tooltip="Delete Task",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )
        
        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update Task",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return Column(controls=[self.display_view, self.edit_view])
    
    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()
    
    def save_clicked(self, e):
        old = self.task_name
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
        loginator.TaskDatabase.update_task(self, self.display_task.label, old)
    
    def status_changed(self, e, value):
        self.completed = self.display_task.value
        self.task_status
        loginator.TaskDatabase.update_status(self, value ,self.task_name)
    
    def delete_clicked(self, e):
        self.task_delete(self.task_name)
        # loginator.TaskDatabase.DeleteTask(self, self.task_name)


class Done_inator(UserControl):
    """
    This is the main Class of the app containing the app's root control(i.e the view)
    containing all other controls
    """
    def build(self):
        self.new_task =TextField(hint_text="Whatchu doing?", on_submit=self.add_clicked ,expand=True)
        self.tasks = Column()

        self.filter = Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="My Tasks"), Tab(text="Active"), Tab(text="completed")],
        )
        return Column(
            controls=[
                Row(
                    controls=[
                        IconButton(
                            icon=icons.MENU_ROUNDED,
                            icon_size=35,
                            on_click=None,
                        ),
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                    ],
                ),
            ],
        )

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_status, self.task_delete)
        loginator.TaskDatabase.add_task(self, self.new_task.value)
        self.tasks.controls.insert(0, task)
        self.new_task.value = ""
        self.update()

    def task_status(self):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        loginator.TaskDatabase.DeleteTask(self, task)
        self.update()
    
    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status =="My Tasks"
                or (status == "Active" and task.completed == False)
                or (status == "completed" and task.completed)
            )
        super().update()
        
    def tabs_changed(self, e):
        self.update()


def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = 'top'
    page.scroll = "hidden"
    page.appbar = AppBar(
        title=Text("Done-inator",
                   size=49,
                   weight="bold",
                   font_family="playbill",
                   ),
        center_title=True
    )
    page.add(Done_inator())
    
    page.update()

    db = loginator.TaskDatabase.connectToDb()
    
    result = loginator.TaskDatabase.ReadData(db)[::-1]

    for task in result:
        if task["Task_status"] == 1:
            status = True
        elif task["Task_status"] == 0:
            status = False
            
        page.controls[0].controls[0].controls[1].controls[1].controls.append(
            Task(
                task["Task"],
                status,
                Done_inator.task_delete,
            )
        )
    page.controls[0].controls[0].controls[1].controls[1].update()


if __name__ == '__main__':
    flet.app(target=main)