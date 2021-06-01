from Helpers.first_helper import FirstHelper
import pytest


class FirstSuite:
    @pytest.mark.parametrize('count_child', [i for i in range(1, 11)])
    @pytest.mark.scenario_test_task
    def test_first_scenario(self, browser, count_child):
        booking_main_page = FirstHelper(browser)
        booking_main_page.go_to_site()
        booking_main_page.click_add_child()
        booking_main_page.num_child(count_child)
        fields = booking_main_page.num_field_child()
        assert fields == count_child
        booking_main_page.click_clean_child(count_child)
