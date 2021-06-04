from pages.MainPageHelpers.first_helper import FirstHelper
import pytest
from time import sleep


class FirstSuite:
    @pytest.mark.parametrize('count_child', [i for i in range(1, 11)])
    @pytest.mark.test_scenario_task
    def test_first_scenario(self, browser, count_child):
        booking_main_page = FirstHelper(browser)
        # booking_main_page.wait(10)
        booking_main_page.go_to_site()
        # booking_main_page.wait(10)
        sleep(5)
        booking_main_page.click_add_child()
        booking_main_page.wait(5)
        # booking_main_page.check_child_menu()
        # booking_main_page.click_add_people(count_child)
        booking_main_page.num_child(count_child)
        fields = booking_main_page.num_field_child()
        assert fields == count_child
        booking_main_page.click_clean_child(count_child) 