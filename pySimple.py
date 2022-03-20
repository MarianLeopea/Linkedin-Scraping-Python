import PySimpleGUI as sg


def pySimple(layout):
    sg.theme("DarkTeal9")


    frame_layout1 = [
        [
            sg.Text("Email addres or phone:", size=(15, 1)),
            sg.InputText(key="address"),
        ],
        [sg.Text("Password:", size=(15, 1)), sg.InputText(key="password")],
    ]

    frame_layout2 = [
        [
            sg.Radio("Jobs:", "RADIO1", key="Jobs"),
            sg.Radio("Groups:", "RADIO1", key="Groups"),
            sg.Radio("Posts:", "RADIO1", key="Posts"),
            sg.Radio("Companies:", "RADIO1", key="Companies"),
            sg.Radio("People:", "RADIO1", key="People"),
            sg.Radio("Schools:", "RADIO1", key="Schools"),
            sg.Radio("Events:", "RADIO1", key="Events"),
            sg.Radio("Services:", "RADIO1", key="Services"),
            sg.Radio("Courses:", "RADIO1", key="Courses"),
        ],
        # [sg.Text("Keyword for search:", size=(15, 1)), sg.InputText(key="Search_Categories")],
        [sg.Text("Keyword for search:", size=(15, 1)), sg.InputText(key="Keyword")],
    ]
    frame_layout3 = [
        [sg.Text("Location for search:", size=(15, 1)), sg.InputText(key="Location")],
    ]
    frame_layout4 = [
        [sg.Text("Number of pages for scraping:", size=(5, 1)), sg.InputText(key="NrPages")],
    ]


    layout = [
        [
            sg.Frame(
                "Email addres or phone:", frame_layout1, font="Any 12", title_color="red"
            )
        ],
        [sg.Frame("Keyword for search:", frame_layout2, font="Any 12", title_color="red")],
        [
            sg.Frame(
                "Enter location for Search", frame_layout3, font="Any 12", title_color="red"
            )
        ],
                [
            sg.Frame(
                "Number of pages for scrapingh", frame_layout4, font="Any 12", title_color="red"
            )
        ],
        [
            sg.Text("Save format:", size=(15, 1)),
            sg.Combo([".css", ".json"], key="Favorite Colour"),
        ],
        [sg.Submit(), sg.Button("Clear"), sg.Exit()],
    ]
    return layout



