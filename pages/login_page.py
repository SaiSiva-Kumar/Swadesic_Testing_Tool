# login_page.py
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    IMAGE_ENTRY = (AppiumBy.XPATH,
                   '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView')
    SEE_ALL_OPTIONS = (AppiumBy.ACCESSIBILITY_ID, "See all Options")
    CONTINUE_WITH_EMAIL = (AppiumBy.ACCESSIBILITY_ID, "Continue with Email and OTP")
    EMAIL_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    SEND_OTP = (AppiumBy.ACCESSIBILITY_ID, "Send OTP")
    VERIFY_OTP = (AppiumBy.ACCESSIBILITY_ID, "Verify OTP")
    HOME_SCREEN_ELEMENT = (AppiumBy.XPATH,
                           '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.ImageView[1]')
    EMAIL_ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "Please enter an email")
    SETTINGS = (AppiumBy.ACCESSIBILITY_ID, "Settings")
    APP_AND_SECURITY = (AppiumBy.ACCESSIBILITY_ID, "App & Security")
    LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Logout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(self.IMAGE_ENTRY)).click()

    def click_see_all_options(self):
        self.wait.until(EC.element_to_be_clickable(self.SEE_ALL_OPTIONS)).click()

    def click_continue_with_email(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_WITH_EMAIL)).click()

    def enter_email(self, email):
        field = self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
        field.click()
        field.send_keys(email)

    def click_send_otp(self):
        self.wait.until(EC.element_to_be_clickable(self.SEND_OTP)).click()

    def click_verify_otp(self):
        self.wait.until(EC.element_to_be_clickable(self.VERIFY_OTP)).click()

    def is_home_screen_visible(self):
        self.wait.until(EC.presence_of_element_located(self.HOME_SCREEN_ELEMENT))

    def is_email_error_displayed(self):
        self.wait.until(EC.presence_of_element_located(self.EMAIL_ERROR_MESSAGE))

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.IMAGE_ENTRY)).click()
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS)).click()
        self.wait.until(EC.element_to_be_clickable(self.APP_AND_SECURITY)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()