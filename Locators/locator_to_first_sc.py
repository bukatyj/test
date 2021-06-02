from selenium.webdriver.common.by import By


class LocatorFirstScenario:

    LOCATOR_CHILD_BUTTON = (By.XPATH, "//div[@class='xp__input-group xp__guests']")
    LOCATOR_ADD_CHILD = (By.XPATH, "//button[@class='bui-button bui-button--secondary bui-stepper__add-button ']")
    LOCATOR_NUM_FIELD_CHILD = (By.XPATH, "//div[@class='sb-group__children__field clearfix']/select")
    LOCATOR_CLEAN_CHILD = (By.XPATH, "//div[@class='sb-group__field sb-group-children ']/div/div[2]/button")
    LOCATOR_CHILD_MENU = (By.ID, 'xp__guests__inputs-container')