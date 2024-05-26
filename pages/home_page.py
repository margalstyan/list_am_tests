from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config_reader import get_config_value


class HomePage(BasePage):
    # selectors
    SELECT_LANG_DLG = By.ID, "dlgLangSel"
    WELCOME_MSG_ARM_TEXT = By.ID, "idli2"
    ARMENIAN_LANG_LINK = By.CSS_SELECTOR, "[href='/am/']"
    BABY_AND_KIDS_LINK = By.LINK_TEXT, "Մանկական աշխարհ"
    PAGE_TITLE = By.ID, "pt"
    PRICE_LABEL = By.XPATH, "//*[@id='idprice1']/../preceding-sibling::div"
    PRICE_FROM_INPUT = By.ID, "idprice1"
    PRICE_TO_INPUT = By.ID, "idprice2"
    PRICE_SAVE_BTN = By.CSS_SELECTOR, ".btn[href='#']"
    ITEM_PRICE_DIV = By.CLASS_NAME, "p"

    base_url = get_config_value("base_url")

    def load(self):
        self.driver.get(self.base_url)

    def select_armenian_language(self):
        self.click(self.ARMENIAN_LANG_LINK)

    def click_baby_and_kids(self):
        self.click(self.BABY_AND_KIDS_LINK)

    def set_price_range(self, price_from, price_to):
        self.type_text(self.PRICE_FROM_INPUT, price_from)
        self.type_text(self.PRICE_TO_INPUT, price_to)

    def submit_price_range(self):
        self.click(self.PRICE_SAVE_BTN)

    def get_item_prices(self):
        prices = self.find_elements(self.ITEM_PRICE_DIV)
        return [price.text for price in prices]

    def ensure_lang_dlg_opened(self):
        return self.wait_for_visibility(self.SELECT_LANG_DLG)

    def get_lang_dlg_welcome_text(self):
        return self.find_element(self.WELCOME_MSG_ARM_TEXT).text

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_price_placeholders(self):
        return self.get_placeholder_text(self.PRICE_FROM_INPUT), self.get_placeholder_text(self.PRICE_TO_INPUT)

    def get_price_label_text(self):
        return self.get_text(self.PRICE_LABEL)
