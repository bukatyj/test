from pages.MainPageHelpers.second_helper import SecondHelper
import pytest
import random
from time import sleep


class SecondSuite:
    @pytest.mark.test_scenario_task
    @pytest.mark.parametrize('num_city', [random.choice([i for i in range(9)])])
    def test_second_scenario(self, browser, num_city):
        booking_main_page = SecondHelper(browser)
        booking_main_page.go_to_site()
        booking_main_page.city_selection(num_city)
        sleep(5)
        assert booking_main_page.check_calendar().is_displayed()
        assert booking_main_page.check_room_detail_is_false()

        booking_main_page.empty_click()
        booking_main_page.price_button()
        sleep(5)
        assert booking_main_page.check_calendar().is_displayed()

        booking_main_page.day_go_in()
        booking_main_page.click_on_search_button()
        sleep(5)
        assert booking_main_page.check_room_detail_is_true()
