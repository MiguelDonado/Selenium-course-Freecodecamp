# THis file will include a class with instance methods
# THat will be responsible to interact with out website
# After we have some results, to apply filtrations

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def close_map(self):
        try:
            close_btn = self.driver.find_element(
                By.CSS_SELECTOR, "button[aria-label='Cerrar el mapa']"
            )
            close_btn.click()
        except:
            print("The map hasn`t appear")

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(
            By.CSS_SELECTOR, "div[data-filters-group='class']"
        )
        star_child_elements = star_filtration_box.find_elements(
            By.CSS_SELECTOR, "div[data-filters-item^='class:class']"
        )
        for star_value in star_values:
            for star_element in star_child_elements:
                if (
                    str(star_element.get_attribute("data-filters-item"))
                    == f"class:class={star_value}"
                ):
                    star_element.click()

    def sort_price_lowest_first(self):
        sort_button_dropdown = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        sort_button_dropdown.click()

        sort_by_price = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-id="price"]'
        )
        sort_by_price.click()
