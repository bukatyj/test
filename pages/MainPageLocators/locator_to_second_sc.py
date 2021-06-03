from selenium.webdriver.common.by import By


class LocatorSecondScenario:
    LOCATOR_CITY_SELECTION = (
        By.XPATH, "//div[@class='bui-spacer--largest popular-destinations-carousel-block']/div[@role='region']/ul/li"
    )
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, 'sb-searchbox__button')
    LOCATOR_PRICE_BUTTON = (By.XPATH, "//div[@class='sr-cta-button-row sr-cta-button-top-spacing']/a")
    LOCATOR_DAY = (By.XPATH, "//div[@class='bui-calendar__content']/div[2]/table/tbody/tr[2]/td[2]")
    LOCATOR_EMPTY = (By.CLASS_NAME, 'sorth1')
    LOCATOR_CALENDAR = (By.CLASS_NAME, 'bui-calendar')
    LOCATOR_ROOM_DETAIL = (By.XPATH, "//div[@class='room_details ']/div")
