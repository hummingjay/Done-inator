"""
My sidebar for the done-inator
"""

import flet
from flet import *
from functools import partial
import time

class Sidebar(UserControl):
    """
    This is the sidebar for the to-do app

    Args:
        UserControl (_type_): _description_
    """
    def __init__(self, func):
        self.func=func
        super().__init__()
    
    # highlighting when hovering
    def Highlight(self, e):
        if e.data == 'true':
            e.control.bgcolor = 'white10'
            e.control.update()
            
            # highlighted text and icons to turn white
            
            # .controls[0] index for Button
            e.control.content.controls[0].icon_color = "white"
            # .controls[1] index for text
            e.control.content.controls[1].color = "white"
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()
            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].color = "white54"
            e.control.content.update()

    def UserData(self, initials: str, name: str, description: str):
        # first row with user details
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor='bluegrey900',
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=20,
                            weight='bold'
                        ),
                    ),
                   Column(
                       spacing=1,
                       alignment='center',
                       controls=[
                           Text(
                               value=name,
                               size=11,
                               weight='bold',
                               # animation details
                               opacity=1,
                               animate_opacity=200 # animation speed
                           ),
                           Text(
                               value=description,
                               size=11,
                               weight='w400',
                               color="white54",
                               # animation details
                               opacity=1,
                               animate_opacity=200 # animation speed
                           ),
                       ],
                   ),
                ]
            )
        )

    #  main sidebar row and icons
    def ContainedIcon(self, icon_name:str, text:str):
        return Container(
            width=200,
            height=45,
            border_radius=10,
            on_hover=lambda e:self.Highlight(e),
            content=Row(
                    controls=[
                        IconButton(
                            icon=icon_name,
                            icon_size=21,
                            icon_color='White54',
                            style=ButtonStyle(
                                shape={
                                    "": RoundedRectangleBorder(radius=10),
                                },
                                overlay_color={"": "transparent"},
                            ),
                        ),
                        Text(
                            value=text,
                            color="White56",
                            size=11,
                            opacity=1,
                            animate_opacity=200,
                        ),
                    ]
                ),
        )
    
    def build(self):
        return Container(
            # dimensions and xtics of returned container
            width=200,
            height=500,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                # horizontal_alignment="center",
                controls=[
                    # adding sidebar icons
                    self.UserData("Di", "Done-inator", "The To-do app"),
                    # clickable menu icon expand and mini sidebar
                    Row(
                        controls=[
                            IconButton(
                                icon=icons.MENU,
                                on_click=partial(self.func)
                            ),
                            Text(
                                value=" Menu",
                                color="White56",
                                size=11,
                                opacity=1,
                                animate_opacity=200,
                            ),
                        ]
                        ),
                    # divider
                    Divider(height=5, color="transparent"),
                    self.ContainedIcon(icons.HOME, "Home"),
                    self.ContainedIcon(icons.SEARCH, "Search"),
                    self.ContainedIcon(icons.CALENDAR_MONTH_ROUNDED, "Calendar"),
                    self.ContainedIcon(icons.PIE_CHART_OUTLINE_ROUNDED, "Stats"),
                    self.ContainedIcon(icons.SETTINGS, "Settings"),
                    Divider(height=5, color="white24"),
                    self.ContainedIcon(icons.LOGIN_OUTLINED, "Login"),
                ]
            ),
        )

# Main Function
def main(page: Page):
    # App Title
    page.title = "Done-inator"
    
    # Alignment of app
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    
    # AnimateSidebar
    def AnimateSidebar(e):
        """
        Defines the animation of the sidebar in and out of the page

        Args:
            e (data): checks if interacted with
        """
        # reduce opacity of title text
        if page.controls[0].width != 62:
            # first reduce opacity by iterating through rows
            for item in (
                # position of class
                page.controls[0]
                # content of the container
                .content.controls[0]
                # row controls
                .content.controls[0]
                # layer at the top
                .content.controls[1]
                # position of the text
                .controls[:] # all controls
            ):
                item.opacity = (
                    0
                )
                item.update()
        
            # reduce opacity of menu items
            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 0
                    items.content.update()
        
            time.sleep(0.2)
        
            # minimize sidebar
            page.controls[0].width = 62
            page.controls[0].update()
        
        # doing the opposite
        else:
            # maximize sidebar
            page.controls[0].width = 200
            page.controls[0].update()
            
            time.sleep(0.2)
            
            for item in (
                # position of class
                page.controls[0]
                # content of the container
                .content.controls[0]
                # row controls
                .content.controls[0]
                # layer at the top
                .content.controls[1]
                # position of the text
                .controls[:] # all controls
            ):
                item.opacity = 1
                item.update()
        
            # reduce opacity of menu items
            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 1
                    items.content.update()
    
    # Adding class to page
    page.add(
        Container(
            width=200,
            height=580,
            bgcolor='black',
            border_radius=10,
            animate=animation.Animation(500, 'decelerate'),
            alignment=alignment.center,
            padding=10,
            content=Sidebar(AnimateSidebar),
        )
    )
    
    page.update()

# Run app
if __name__ == '__main__':
    flet.app(target=main)