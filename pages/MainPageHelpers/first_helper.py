from pages.BaseApp import BasePage
from pages.MainPageLocators.locator_to_first_sc import LocatorFirstScenario
import selenium
from selenium.common.exceptions import TimeoutException


class FirstHelper(BasePage, TimeoutException):
    def click_add_child(self):
        return self.click_element(LocatorFirstScenario.LOCATOR_CHILD_BUTTON, time=10).click()

    # def click_add_people(self, count_child):
    #     try:
    #         num_people = self.click_element(LocatorFirstScenario.LOCATOR_ADD_CHILD, time=2)
    #         for i in range(count_child):
    #             num_people.click()
    #     except selenium.common.exceptions.TimeoutException:
    #         self.go_to_site()
    #         self.click_add_child()
    #         self.click_add_people(count_child)


    # def check_child_menu(self):
    #     if self.find_element(LocatorFirstScenario.LOCATOR_CHILD_MENU, time=7).is_enabled():
    #         pass
    #     else:
    #         self.click_add_child()

    def num_child(self, count_child):
        num_child = self.find_element(LocatorFirstScenario.LOCATOR_ADD_CHILD, time=10)
        for i in range(count_child):
            num_child.click()


    def num_field_child(self):
        fields = self.find_elements(LocatorFirstScenario.LOCATOR_NUM_FIELD_CHILD, time=2)
        return len(fields)

    def click_clean_child(self, count_child):
        clean_child = self.find_element(LocatorFirstScenario.LOCATOR_CLEAN_CHILD, time=2)
        for i in range(count_child):
            clean_child.click()
