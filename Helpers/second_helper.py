from BaseApp import BasePage
from Locators.locator_to_second_sc import LocatorSecondScenario
from selenium.common.exceptions import TimeoutException


class SecondHelper(BasePage):
    def city_selection(self, num_city):
        city = self.find_elements(LocatorSecondScenario.LOCATOR_CITY_SELECTION, time=2)
        city[num_city].click()

    def empty_click(self):
        return self.find_element(LocatorSecondScenario.LOCATOR_EMPTY, time=2)

    def price_button(self):
        return self.find_element(LocatorSecondScenario.LOCATOR_PRICE_BUTTON, time=2).click()

    def day_go_in(self):
        return self.find_element(LocatorSecondScenario.LOCATOR_DAY, time=2).click()

    def click_on_search_button(self):
        return self.find_element(LocatorSecondScenario.LOCATOR_SEARCH_BUTTON, time=2).click()

    def check_calendar(self):
        return self.find_element(LocatorSecondScenario.LOCATOR_CALENDAR, time=2)

    def check_room_detail_is_true(self):
        return self.find_element(LocatorSecondScenario.LOCATOR_ROOM_DETAIL, time=2)

    def check_room_detail_is_false(self):
        try:
            self.find_element(LocatorSecondScenario.LOCATOR_ROOM_DETAIL, time=2)
        except TimeoutException:
            return True
