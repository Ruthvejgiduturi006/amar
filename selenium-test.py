from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Test Started")

# Connect to Selenium Chrome container
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=webdriver.ChromeOptions()
)

driver.get("http://host.docker.internal:8000")

try:
    # Click "Get started"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "get-started"))
    ).click()

    # Enter email & password
    driver.find_element(By.ID, "user_email_login").send_keys("abc@gmail.com")
    driver.find_element(By.ID, "user_password").send_keys("password")
    driver.find_element(By.NAME, "commit").click()

    # Check login success/failure
    try:
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.ID, "error-message"))
        )
        print("Login Failed!")
    except:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "dashboard"))
        )
        print("Login Successful!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
    print("Test Finished")
