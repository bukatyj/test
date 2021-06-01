from BaseApp import BasePage
from Locators.locator_to_first_sc import LocatorFirstScenario


class FirstHelper(BasePage):
    def click_add_child(self):
        return self.find_element(LocatorFirstScenario.LOCATOR_CHILD_BUTTON, time=2).click()

    def num_child(self, count_child):
        num_child = self.find_elements(LocatorFirstScenario.LOCATOR_ADD_CHILD, time=2)
        for i in range(count_child):
            num_child[1].click()

    def num_field_child(self):
        fields = self.find_elements(LocatorFirstScenario.LOCATOR_NUM_FIELD_CHILD, time=2)
        return len(fields)

    def click_clean_child(self, count_child):
        clean_child = self.find_element(LocatorFirstScenario.LOCATOR_CLEAN_CHILD, time=2)
        for i in range(count_child):
            clean_child.click()
