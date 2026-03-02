import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_next_email():
    return f"test{int(time.time())}@gmail.com"
class UserPage:

    PROFILE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(10)"
    )

    SEE_ALL_OPTIONS = (
        AppiumBy.ACCESSIBILITY_ID, "See all Options"
    )
    CONTINUE_WITH_EMAIL = (AppiumBy.ACCESSIBILITY_ID, "Continue with Email and OTP")
    EMAIL_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    SEND_OTP = (AppiumBy.ACCESSIBILITY_ID, "Send OTP")
    VERIFY_OTP = (AppiumBy.ACCESSIBILITY_ID, "Verify OTP")
    YES_I_AM = (AppiumBy.ACCESSIBILITY_ID, "Yes, I am.")
    MALE = (AppiumBy.ACCESSIBILITY_ID, "Male")
    CITY_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(15)")
    CITY_SEARCH_ICON = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    CITY_SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    ADD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Add")
    CONTINUE = (AppiumBy.ACCESSIBILITY_ID, "Continue")
    AS_A_BUYER = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(1)")
    UPLOAD_PROFILE_PICTURE = (AppiumBy.ACCESSIBILITY_ID, "Upload profile picture")
    PHOTO_INSTANCE_26 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(26)")
    CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(6)")
    CROP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Crop")
    JOIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Join the Future of Shopping")
    PROFILE_BUTTON_POST_ONBOARD = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(25)")
    EDIT_PROFILE = (AppiumBy.ACCESSIBILITY_ID, "Edit profile")
    CHANGE_PROFILE_PICTURE = (AppiumBy.ACCESSIBILITY_ID, "change profile picture")
    EDIT_PHOTO_INSTANCE_30 = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(30)")
    EDIT_CONFIRM_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(6)")
    FIRST_NAME_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    LAST_NAME_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    DISPLAY_NAME_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(2)")
    USERNAME_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(3)")
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "save")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_BUTTON)).click()

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

    def wait_for_otp(self):
        time.sleep(3)

    def click_verify_otp(self):
        self.wait.until(EC.element_to_be_clickable(self.VERIFY_OTP)).click()

    def click_yes_i_am(self):
        self.wait.until(EC.element_to_be_clickable(self.YES_I_AM)).click()

    def select_gender_male(self):
        self.wait.until(EC.element_to_be_clickable(self.MALE)).click()

    def select_city(self, city):
        self.wait.until(EC.element_to_be_clickable(self.CITY_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.CITY_SEARCH_ICON)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.CITY_SEARCH_INPUT))
        field.click()
        field.send_keys(city)
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def click_as_a_buyer(self):
        self.wait.until(EC.element_to_be_clickable(self.AS_A_BUYER)).click()

    def upload_profile_picture(self):
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_PROFILE_PICTURE)).click()
        self.wait.until(EC.element_to_be_clickable(self.PHOTO_INSTANCE_26)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.CROP_BUTTON)).click()

    def click_join(self):
        self.wait.until(EC.element_to_be_clickable(self.JOIN_BUTTON)).click()

    def click_profile_button_post_onboard(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_BUTTON_POST_ONBOARD)).click()

    def click_edit_profile(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_PROFILE)).click()

    def change_profile_picture(self):
        self.wait.until(EC.element_to_be_clickable(self.CHANGE_PROFILE_PICTURE)).click()
        self.wait.until(EC.element_to_be_clickable(self.EDIT_PHOTO_INSTANCE_30)).click()
        self.wait.until(EC.element_to_be_clickable(self.EDIT_CONFIRM_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.CROP_BUTTON)).click()

    def enter_first_name(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT))
        field.click()
        field.clear()
        field.send_keys(text)

    def enter_last_name(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_INPUT))
        field.click()
        field.clear()
        field.send_keys(text)

    def enter_display_name(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.DISPLAY_NAME_INPUT))
        field.click()
        field.clear()
        field.send_keys(text)

    def enter_username(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        field.click()
        field.clear()
        field.send_keys(text)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()