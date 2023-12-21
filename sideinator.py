import flet
from flet import *

class SideBar(UserControl):
    def __init__(self):
        super().__init__()
    
    def ContainedIcon(self, icon_name, text):
        return Container(
            width=210,
            border_radius=10,
            ink=True,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=21,
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transarent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color=Theme,
                        size=14,
                        opacity=1,
                        animate_opacity=200,
                    ),
                ],
            ),
        )
    
    def build(self):
        return Container(
            alignment=alignment.center,
            padding=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                expand=True,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.START,
                spacing=5,
                controls=[
                    self.ContainedIcon(icons.HOME, "Home"),
                    self.ContainedIcon(icons.SEARCH, "Search"),
                    self.ContainedIcon(icons.CALENDAR_MONTH_ROUNDED, "Calendar"),
                    self.ContainedIcon(icons.PIE_CHART_OUTLINE_ROUNDED, "Stats"),
                    self.ContainedIcon(icons.SETTINGS, "Settings"),
                    Divider(height=5, color=Theme),
                    self.ContainedIcon(icons.LOGIN_OUTLINED, "Login"),
                ],
            ),
        )