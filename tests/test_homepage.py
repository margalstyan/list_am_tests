from pages.home_page import HomePage
from utils.config_reader import get_config_value


def test_baby_and_kids_price_range(driver):
    homepage = HomePage(driver)
    homepage.load()

    # Ensure that language dialog is opened
    homepage.ensure_lang_dlg_opened()
    assert homepage.get_lang_dlg_welcome_text() == get_config_value("lang_dlg_welcome_text")

    # Select Armenian language
    homepage.select_armenian_language()

    # Click on Baby and Kids link
    homepage.click_baby_and_kids()

    # Ensure the page title is "Մանկական աշխարհ"
    assert homepage.get_page_title() == get_config_value("baby_and_kids_page_title")

    # Check price section
    assert homepage.get_price_placeholders() == (get_config_value("price_from_placeholder"),
                                                 get_config_value("price_to_placeholder"))
    assert homepage.get_price_label_text() == get_config_value("price_label")

    # Set price range to 3000-3001
    homepage.set_price_range(get_config_value("price_from"), get_config_value("price_to"))

    # Submit price range
    homepage.submit_price_range()

    # Get all item prices and ensure they are all 3,000
    item_prices = homepage.get_item_prices()
    for price in item_prices:
        assert "3,000 " in price
