from flet import *
from pytonconnect import TonConnect
import asyncio



def main(page: Page):
    page.title = "TestProject"
    page.theme_mode = 'light'
    page.vertical_alignment = MainAxisAlignment
    page.horizontal_alignment = CrossAxisAlignment
    page.window_width = 385
    page.window_height = 660
    page.padding = 0
    BG = '#FFFFFF'
    ScrollbarTheme = 'dark'


    Climb_page = Row(
        [
            Column(
                [
                    Text("Soon...")
                ]
            )
        ],
        alignment=MainAxisAlignment.CENTER
    )


    Equip_page = Row(
        [
            Column(
                [
                    Text("Soon...")
                ]
            )
        ],
        alignment=MainAxisAlignment.CENTER
    )

    # wallet_page = Row(
    #     [
    #         Container(          
    #                 Image(src='/images/wallet.png'),
    #                 ImageFit.COVER,
    #                 expand=True,
    #                 width=350,
    #                 height=550,
    #                 alignment=MainAxisAlignment.CENTER,
    #         )
    #     ]
    # )

    wallet_page = Container(
        bgcolor= BG,
        width = 400,
        height= 560,
        padding=0,

        content=Row(
            [
            Container(
                content=Image(src='/images/wallet.png'),
                alignment=alignment.center,
                width=400,
                height=560,
                padding=0
            ),
            ]
        )
    )

    award_page = Container(
        bgcolor= BG,
        width = 400,
        height= 560,
        padding=0,

        content=Row(
            [
            Container(
                content=Image(src='/images/award.png'),
                alignment=alignment.center,
                width=400,
                height=560,
                padding=0
            ),
            ]
        )
    )

    main_page = Container(
        bgcolor= BG,
        border_radius=35,
        width = 350,
        height= 540,

        content=Row(
            [
            Container(
                content=Image(src='/images/Everest.png'),
                margin=10,
                padding=padding.only(left=25, right=25),
                alignment=alignment.center,
                width=350,
                height=440,
            ),
            Container(
                content=Image(src='/images/Kili.png'),
                margin=10,
                padding=padding.only(left=25, right=25),
                alignment=alignment.center,
                width=350,
                height=440,
            ),
            Container(
                content=Image(src='/images/Fitz.png'),
                margin=10,
                padding=padding.only(left=25, right=25),
                alignment=alignment.center,
                width=350,
                height=440,
            ),
            Container(
                content=Image(src='/images/Altai.png'),
                margin=10,
                padding=padding.only(left=25, right=25),
                alignment=alignment.center,
                width=350,
                height=440,
            ),
            Container(
                content=Image(src='/images/Fudzi.png'),
                margin=10,
                padding=padding.only(left=25, right=25),
                alignment=alignment.center,
                width=350,
                height=440,
            ),
            ],
            scroll='always'
        )
    )

    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0: page.add(award_page)
        elif index == 1: page.add(Equip_page)
        elif index == 2: page.add(main_page)
        elif index == 3: page.add(Climb_page)
        elif index == 4: page.add(wallet_page)

    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.TASK_ALT_OUTLINED, label="Award"),
            NavigationDestination(icon=icons.BACKPACK_OUTLINED, label="Equip'm"),
            NavigationDestination(icon=icons.HOME, label="Main"),
            NavigationDestination(icon=icons.SNOWSHOEING, label="Climb"),
            NavigationDestination(icon=icons.WALLET, label="Wallet"),
        ], on_change=navigate
    )

    page.add(main_page)

app(target=main, assets_dir='assets', port=8000, view=WEB_BROWSER)