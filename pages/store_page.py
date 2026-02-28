from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StorePage:

    PROFILE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(10)")
    CREATE_STORE = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"Create store\")")
    START_NOW = (AppiumBy.ACCESSIBILITY_ID, "Start now")
    GET_STARTED = (AppiumBy.ACCESSIBILITY_ID, "Get started")
    STORE_NAME_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    BUSINESS_CATEGORY_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(17)")
    CATEGORY_SEARCH_ICON = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    CATEGORY_SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    ADD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Add")
    BUSINESS_TYPE_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(20)")
    BUSINESS_TYPE_SEARCH_ICON = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    BUSINESS_TYPE_SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    BUSINESS_TYPE_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"test_store1\ntest_store1\")")
    PROFILE_PHOTO = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(18)")
    PHOTO_INSTANCE_18 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(6)")
    CROP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Crop")
    NEXT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"Next\")")
    ABOUT_BUSINESS_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    WEBSITE_LINK_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    STORE_HANDLE_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    STORE_HANDLE_AVAILABLE = (AppiumBy.ACCESSIBILITY_ID, "test_store1 is available")
    CREATE_STORE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Create The Store")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_BUTTON)).click()

    def click_create_store(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_STORE)).click()

    def click_start_now(self):
        self.wait.until(EC.element_to_be_clickable(self.START_NOW)).click()

    def click_get_started(self):
        self.wait.until(EC.element_to_be_clickable(self.GET_STARTED)).click()

    def enter_store_name(self, name):
        field = self.wait.until(EC.element_to_be_clickable(self.STORE_NAME_INPUT))
        field.click()
        field.send_keys(name)

    def select_business_category(self, category):
        self.wait.until(EC.element_to_be_clickable(self.BUSINESS_CATEGORY_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.CATEGORY_SEARCH_ICON)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.CATEGORY_SEARCH_INPUT))
        field.click()
        field.send_keys(category)
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def select_business_type(self, business_type):
        self.wait.until(EC.element_to_be_clickable(self.BUSINESS_TYPE_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUSINESS_TYPE_SEARCH_ICON)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.BUSINESS_TYPE_SEARCH_INPUT))
        field.click()
        field.send_keys(business_type)
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUSINESS_TYPE_RESULT)).click()

    def choose_profile_photo(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_PHOTO)).click()
        self.wait.until(EC.element_to_be_clickable(self.PHOTO_INSTANCE_18)).click()
        self.wait.until(EC.element_to_be_clickable(self.CROP_BUTTON)).click()

    def click_next(self):
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def enter_about_business(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.ABOUT_BUSINESS_INPUT))
        field.click()
        field.send_keys(text)

    def enter_website_link(self, url):
        field = self.wait.until(EC.element_to_be_clickable(self.WEBSITE_LINK_INPUT))
        field.click()
        field.send_keys(url)

    def enter_store_handle(self, handle):
        field = self.wait.until(EC.element_to_be_clickable(self.STORE_HANDLE_INPUT))
        field.click()
        field.send_keys(handle)

    def is_store_handle_available(self):
        self.wait.until(EC.presence_of_element_located(self.STORE_HANDLE_AVAILABLE))

    def click_create_the_store(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_STORE_BUTTON)).click()