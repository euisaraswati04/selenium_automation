
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


def login(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )


def test_add_product_to_cart(driver):
    wait = WebDriverWait(driver, 10)

    login(driver)

    # Add product
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
        )
    ).click()

    # Verify cart badge
    badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge.text == "1"

    # Open cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    # Verify product in cart
    product = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert product.text == "Sauce Labs Backpack"


def test_remove_product_from_cart(driver):
    wait = WebDriverWait(
        driver,
        10,
        ignored_exceptions=(StaleElementReferenceException,)
    )

    login(driver)

    # Add product to cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
        )
    ).click()

    # Open shopping cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    # Wait until product appears in cart
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    # Click remove button
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']")
        )
    ).click()

    # Wait until product disappears
    wait.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    # Verify cart is empty
    cart_items = driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )

    assert len(cart_items) == 0
