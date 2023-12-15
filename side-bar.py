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
    def __init__(self):
        super().__init__()
    
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
            width=100,
            height=45,
            border_radius=10,
            content=None,
        )
    
    def build(self):
        return Container(
            # dimensions and xtics of returned container
            width=200,
            height=500,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                controls=[
                    # adding sidebar icons
                    self.UserData("Di", "Done-inator", "The To-do app"),
                    # divider
                    Divider(height=5, color="transparent")
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
            content=Sidebar(),
        )
    )
    
    page.update()

# Run app
if __name__ == '__main__':
    flet.app(target=main)