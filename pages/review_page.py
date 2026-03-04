from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_update_name():
    return f"update test {int(time.time())}"

class ReviewPage:

    PROFILE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(29)")
    CREATE_REVIEW_PAGE = (AppiumBy.ACCESSIBILITY_ID, "Create review page")
    GET_STARTED = (AppiumBy.ACCESSIBILITY_ID, "Get Started")
    IMAGES_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(0)")
    PHOTO_INSTANCE_38 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(38)")
    CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(6)")
    PAGE_NAME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    BUSINESS_CATEGORY_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(12)")
    CATEGORY_SEARCH_ICON = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    CATEGORY_SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    ADD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Add")
    STORE_LINK_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    CREATE_REVIEW_PAGE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Create your review page")
    SWITCH_PROFILE_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(8)")
    REVIEW_PAGE_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"update test\n0.0 (0 reviews)\")")
    SETTINGS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(8)")
    EDIT_PAGE = (AppiumBy.ACCESSIBILITY_ID, "Edit Page")
    UPDATE_PAGE_NAME_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    UPDATE_REVIEW_PAGE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Update the review page")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_BUTTON)).click()

    def click_create_review_page(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_REVIEW_PAGE)).click()

    def click_get_started(self):
        self.wait.until(EC.element_to_be_clickable(self.GET_STARTED)).click()

    def choose_image(self):
        self.wait.until(EC.element_to_be_clickable(self.IMAGES_TAB)).click()
        self.wait.until(EC.element_to_be_clickable(self.PHOTO_INSTANCE_38)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    def enter_page_name(self, name):
        field = self.wait.until(EC.element_to_be_clickable(self.PAGE_NAME_INPUT))
        field.click()
        field.send_keys(name)

    def select_business_category(self, category):
        self.wait.until(EC.element_to_be_clickable(self.BUSINESS_CATEGORY_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.CATEGORY_SEARCH_ICON)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.CATEGORY_SEARCH_INPUT))
        field.click()
        field.send_keys(category)
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def enter_store_link(self, url):
        field = self.wait.until(EC.element_to_be_clickable(self.STORE_LINK_INPUT))
        field.click()
        field.send_keys(url)

    def click_create_review_page_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_REVIEW_PAGE_BUTTON)).click()

    def click_switch_profile_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.SWITCH_PROFILE_TAB)).click()

    def click_review_page_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.REVIEW_PAGE_TAB)).click()

    def click_settings_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS_BUTTON)).click()

    def click_edit_page(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_PAGE)).click()

    def enter_update_page_name(self, name):
        field = self.wait.until(EC.element_to_be_clickable(self.UPDATE_PAGE_NAME_INPUT))
        field.click()
        field.clear()
        field.send_keys(name)

    def click_update_review_page_button(self):
        self.wait.until(EC.element_to_be_clickable(self.UPDATE_REVIEW_PAGE_BUTTON)).click()