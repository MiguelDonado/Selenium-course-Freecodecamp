# This file is going to include methods that will parse
# The specific data that we need from each one of the deal boxes
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, deal_boxes: WebElement):
        self.deal_boxes = deal_boxes

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="title"]'
            ).text

            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]'
            ).text

            hotel_score = deal_box.find_element(
                By.CSS_SELECTOR, 'div[data-testid="review-score"]>div:first-child'
            ).text.split("\nPuntuación:")[0]

            collection.append([hotel_name, hotel_price, hotel_score])
        return collection
