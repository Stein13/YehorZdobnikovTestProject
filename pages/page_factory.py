from pages.top_bar import TopBar
from pages.registration import Registration
from pages.mp3_player import Mp3Players


class PageFactory:

    def __init__(self, driver, logger):
        self.top_bar = TopBar(driver, logger)
        self.registration = Registration(driver, logger)
        self.mp3_players = Mp3Players(driver, logger)
