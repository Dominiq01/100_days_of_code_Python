import os
import time
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

ACCOUNT_EMAIL = "dominik@test2.com"  # The email you registered with
ACCOUNT_PASSWORD = "Janoisk45!"
GYM_URL = "https://appbrewery.github.io/gym/"
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
all_new_bookings = []
booking_summary = {
    "Classes booked": 0,
    "Waitlists joined": 0,
    "Already booked/waitlisted": 0,
    "Total Tuesday 6pm & Thursday classes processed": 0
}


def print_summary():
    print("\n")
    print("-" * 3 + " BOOKING SUMMARY " + "-" * 3)
    for key, value in booking_summary.items():
        print(f"  {key}: {value}")
    print("\n")
    if len(all_new_bookings) > 0:
        print("-" * 3 + " DETAILED CLASS LIST " + "-" * 3)
        for text in all_new_bookings:
            print(f"  - {text}")


def verify_bookings():
    my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
    my_bookings_link.click()

    all_my_bookings = driver.find_elements(By.CSS_SELECTOR, "[id^='booking-class-name-booking']")
    all_my_waitlists = driver.find_elements(By.CSS_SELECTOR, "[id^='waitlist-class-name-waitlist']")
    all_classes_num = booking_summary['Total Tuesday 6pm & Thursday classes processed']
    found_bookings_num = len(all_my_bookings) + len(all_my_waitlists)

    print(f"--- VERIFYING ON MY BOOKINGS PAGE ---")
    for booking in all_my_bookings:
        print(f"  Verified: {booking.text}")

    for waitlist in all_my_waitlists:
        print(f"  Verified: {waitlist.text}")
    print("\n")
    print(f"--- VERIFICATION RESULT ---")
    print(f"  Expected: {all_classes_num}")
    print(f"  Found: {found_bookings_num}")

    if all_classes_num == found_bookings_num:
        print("✅ SUCCESS: All bookings verified!")
    else:
        print(
            f"❌ MISMATCH: Missing {all_classes_num - found_bookings_num} bookings")

book_retries = 7
def book_or_waitlist(time_el, container):
    parent = time_el.find_element(By.XPATH, "ancestor::div[2]")
    container_date = container.find_element(By.TAG_NAME, "h2")
    title_class = parent.find_element(By.TAG_NAME, "h3")
    btn = parent.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

    if btn.text == "Booked":
        print(f"✓ Already booked: {title_class.text} on {container_date.text}")
        booking_summary["Already booked/waitlisted"] = booking_summary["Already booked/waitlisted"] + 1
    elif btn.text == "Waitlisted":
        print(f"✓ Already on waitlist: {title_class.text} on {container_date.text}")
        booking_summary["Already booked/waitlisted"] = booking_summary["Already booked/waitlisted"] + 1
    elif btn.text == "Join Waitlist":
        btn.click()
        print(f"✓ Joined waitlist for: {title_class.text} on {container_date.text}")
        booking_summary["Waitlists joined"] = booking_summary["Waitlists joined"] + 1
        all_new_bookings.append(f"[NEW WAITLIST] {title_class.text} on {container_date.text}")
    else:
        btn.click()
        print(f"✓ Booked: {title_class.text} on {container_date.text}")
        booking_summary["Classes booked"] = booking_summary["Classes booked"] + 1
        all_new_bookings.append(f"[NEW BOOKING] {title_class.text} on {container_date.text}")

    booking_summary["Total Tuesday 6pm & Thursday classes processed"] = booking_summary[
                                                                            "Total Tuesday 6pm & Thursday classes processed"] + 1


login_retries = 7
def login():
    global login_retries
    login_btn = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.ID, "login-button")))
    login_btn.click()
    email_input = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)
    password_input = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.ID, "password-input")))
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)
    submit_btn = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.ID, "submit-button")))
    submit_btn.click()
    error = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.ID, "error-message")))
    print(error.text)
    if error.text == "Network request failed. Please try again.":
        login_retries-= 1
        retry(login, login_retries, error)
        print(f"Current number of retries: {login_retries}")

def check_classes():
    class_containers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//p[starts-with(@id, 'class-time-')]/ancestor::div[4]"))
    )

    for container in class_containers:
        if "Tue" in container.text or "Thu" in container.text:
            time_elements = container.find_elements(By.CSS_SELECTOR, "p[id^='class-time-']")
            for time_el in time_elements:
                if time_el.text == "Time: 6:00 PM":
                    book_or_waitlist(time_el, container)

def retry(func, retries=7, description=None):
    if retries > 0:
        print(description)
        func()
    else:
        print("Too many attempts. Please try again later.")
        return


driver.get(GYM_URL)
login()
check_classes()
print_summary()
verify_bookings()
# driver.quit()
