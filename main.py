import flet as ft


def main(page: ft.Page):

    page.title="cord"
    page.bgcolor="black"
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.colors.TRANSPARENT,
        inactive_color=ft.colors.GREY,
        active_color="#d3d3d3",
        on_change=lambda e: print("Selected tab:", e.control.selected_index),
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.PERSON, label="Profile")
        ]
    )

    title=ft.SafeArea(ft.Text("cord", size=20, color="#d3d3d3"))

    serverlist=[]

    for i in range(0,30):
        serverlist.append(ft.Text('i'))

    servers=ft.ListView(serverlist)

    servercont=ft.Column([servers], 
                         scroll=ft.ScrollMode.HIDDEN, 
                         expand=True, 
                         width=50
                         )

    page.add(title, servercont)

ft.app(main)