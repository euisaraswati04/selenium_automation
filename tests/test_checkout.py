
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_and_add_product(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Login
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Menunggu halaman inventory
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # 3. Tambahkan produk ke cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
        )
    ).click()

    # 4. Buka shopping cart
    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()

    # 5. Menunggu halaman cart
    wait.until(EC.url_contains("cart.html"))

    # 6. Klik checkout
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()


def test_checkout_requires_first_name(driver):
    login_and_add_product(driver)

    wait = WebDriverWait(driver, 10)

    # Tidak mengisi First Name untuk menguji validasi
    wait.until(
        EC.visibility_of_element_located((By.ID, "last-name"))
    ).send_keys("Saraswati")

    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Validasi error message
    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "First Name is required" in error.text


def test_complete_checkout_successfully(driver):
    login_and_add_product(driver)

    wait = WebDriverWait(driver, 10)

    # Mengisi informasi checkout
    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Euis")

    driver.find_element(By.ID, "last-name").send_keys("Saraswati")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    # Klik Continue
    driver.find_element(By.ID, "continue").click()

    # Menunggu halaman checkout overview
    finish_button = wait.until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )

    # Menyelesaikan pesanan
    finish_button.click()

    # Validasi konfirmasi pesanan
    confirmation = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    assert confirmation.text == "Thank you for your order!"
