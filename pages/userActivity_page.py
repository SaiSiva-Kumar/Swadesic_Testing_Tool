from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class UserActivityPage:

    PROFILE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(29)")
    SETTINGS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Settings")
    PERSONAL_INFORMATION = (AppiumBy.ACCESSIBILITY_ID, "Personal information")
    CITY_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Agartala\")")
    CITY_AGARTALA = (AppiumBy.ACCESSIBILITY_ID, "Agartala")
    PROFESSION_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(21)")
    PROFESSION_ACTOR = (AppiumBy.ACCESSIBILITY_ID, "Actor")
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "save")
    THEME_SETTINGS = (AppiumBy.ACCESSIBILITY_ID, "Theme Settings")
    DARK_MODE = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"Dark Mode\nComing soon\")")
    BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(7)")
    APP_AND_SECURITY = (AppiumBy.ACCESSIBILITY_ID, "App & Security")
    TERMS_AND_CONDITIONS = (AppiumBy.ACCESSIBILITY_ID, "Terms and conditions")
    BACK_BUTTON_IMAGE = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(0)")
    PRIVACY_AGREEMENT = (AppiumBy.ACCESSIBILITY_ID, "Privacy agreement")
    ADJUST_APP_FONT_SIZE = (AppiumBy.ACCESSIBILITY_ID, "Adjust app font size")
    FONT_SIZE_BACK_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(5)")
    SEARCH_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(6)")
    SEARCH_INPUT = (AppiumBy.XPATH,
                    "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.ImageView")
    PEOPLE_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"People\n2\")")
    USER_PROFILE = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"krishna_k\nKrishna Kanth\")")
    REPOST_BUTTON = (
    AppiumBy.XPATH, "//android.view.View[@content-desc=\"Post with author\"]/android.widget.ImageView[3]")
    SAVED_BUTTON = (
    AppiumBy.XPATH, "//android.view.View[@content-desc=\"Post with author\"]/android.widget.ImageView[4]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_BUTTON)).click()

    def click_settings_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS_BUTTON)).click()

    def click_personal_information(self):
        self.wait.until(EC.element_to_be_clickable(self.PERSONAL_INFORMATION)).click()

    def select_city(self):
        self.wait.until(EC.element_to_be_clickable(self.CITY_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.CITY_AGARTALA)).click()

    def select_profession(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFESSION_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.PROFESSION_ACTOR)).click()

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def click_theme_settings(self):
        self.wait.until(EC.element_to_be_clickable(self.THEME_SETTINGS)).click()

    def click_dark_mode(self):
        self.wait.until(EC.element_to_be_clickable(self.DARK_MODE)).click()

    def click_back_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BACK_BUTTON)).click()

    def click_app_and_security(self):
        self.wait.until(EC.element_to_be_clickable(self.APP_AND_SECURITY)).click()

    def click_terms_and_conditions(self):
        self.wait.until(EC.element_to_be_clickable(self.TERMS_AND_CONDITIONS)).click()

    def click_back_button_image(self):
        self.wait.until(EC.element_to_be_clickable(self.BACK_BUTTON_IMAGE)).click()

    def click_privacy_agreement(self):
        self.wait.until(EC.element_to_be_clickable(self.PRIVACY_AGREEMENT)).click()

    def click_adjust_app_font_size(self):
        self.wait.until(EC.element_to_be_clickable(self.ADJUST_APP_FONT_SIZE)).click()

    def click_font_size_back_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FONT_SIZE_BACK_BUTTON)).click()

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def enter_search_input(self, query):
        field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        field.click()
        field.send_keys(query)

    def click_people_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.PEOPLE_TAB)).click()

    def click_user_profile(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_PROFILE)).click()

    def click_repost(self):
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.REPOST_BUTTON)).click()

    def click_saved(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVED_BUTTON)).click()