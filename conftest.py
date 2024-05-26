import pytest
import undetected_chromedriver as uc


@pytest.fixture
def driver():
    driver = uc.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
