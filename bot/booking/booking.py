from types import TracebackType
from typing import Type
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        super(Booking, self).__init__(
            options=options
        )  # succesfully instantiate an instance of the webdriver.chrome class
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_cookies(self):
        try:
            accept_btn = self.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_btn.click()
        except:
            print("The cookies window hasn`t appear")

    def close_genius_pop_up(self):
        try:
            close_btn = self.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Ignorar información sobre el inicio de sesión."]',
            )
            close_btn.click()
        except:
            print("The genius pop-up hasn't appear")

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Precios en Euro"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.XPATH, f"//button[.//div[contains(text(), '{currency}')]]"
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.CSS_SELECTOR, "input[name='ss']")
        search_field.clear()
        search_field.send_keys(place_to_go)

        time.sleep(5)

        first_result = self.find_element(By.ID, "autocomplete-result-0")
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]'
        )
        selection_element.click()

        adults_value_element = self.find_element(
            By.CSS_SELECTOR,
            "input#group_adults",
        )

        while True:
            decrease_adults_element = self.find_element(
                By.CSS_SELECTOR,
                "input#group_adults ~ :nth-child(3) > button:first-child",
            )
            decrease_adults_element.click()
            adults_value_element = self.find_element(
                By.CSS_SELECTOR,
                "input#group_adults",
            )
            adults_value = adults_value_element.get_attribute(
                "value"
            )  # Should give back the adults count
            if int(adults_value) == 1:
                break

        increase_adults_element = self.find_element(
            By.CSS_SELECTOR,
            "input#group_adults ~ :nth-child(3) > button:nth-of-type(2)",
        )

        for _ in range(count - 1):
            increase_adults_element.click()
        # print(adults_element.get_attribute("outerHTML"))

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        time.sleep(5)
        filtration.close_map()
        filtration.apply_star_rating(3, 4, 5)
        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )
        report = BookingReport(hotel_boxes)
        table = PrettyTable(field_names=["Hotel Name", "Hotel Price", "Hotel Score"])
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
