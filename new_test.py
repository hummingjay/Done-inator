import flet
from flet import *
from sideinator import SideBar
import loginator
import sqlite3

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
    pass

class Doneinator(UserControl):
    pass

def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = 'top'
    page.scroll = ScrollMode.ADAPTIVE
    
    
    page.appbar = AppBar(
        leading = IconButton(
            icons.MENU_ROUNDED,
            # add controls later
        ),
        leading_width=70,
        title=Text(
            "Done-inator",
            size=49,
            weight="bold",
            font_family="playbill",
        ),
        center_title=True
        
    )
    new_task = TextField(hint_text="Whatchu doing?", expand=True)
    
    def status_changed():
        pass
    
    def edit_clicked():
        pass
    
    def delete_clicked():
        pass
    
    def edit_name():
        pass
    
    def save_clicked():
        pass
    
    def add_tasK():
        pass

    def Task():
        task_display = Checkbox(
            value = value,
            label=new_task,
            on_change=status_changed(),
        )

        display_view =Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                task_display,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_ROUNDED,
                            tooltip="Edit Task",
                            on_click=edit_clicked(),
                        ),
                        IconButton(
                            icons.DELETE_ROUNDED,
                            tooltip="Delete Task",
                            on_click=delete_clicked(),
                        ),
                    ],
                ),
            ],
        )
        
        edit_view = Row(
            visivle=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                edit_name(),
                IconButton(
                    icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN_100,
                    tooltip="Update Task",
                    on_click=save_clicked()
                ),
            ],
        )
        return Column(controls=[display_view, edit_view])
        
    page.add(
        Column(
            controls= [
                Row(
                    controls=[
                        new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=add_tasK),
                    ]
                )
            ]
        )
    )

if __name__ == '__main__':
    flet.app(target=main)