from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    SEARCH_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().className(\"android.widget.ImageView\").instance(7)"
    )

    SEARCH_INPUT = (
        AppiumBy.XPATH,
        "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.ImageView"
    )

    PEOPLE_TAB = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().description(\"People\n2\")"
    )

    USER_RESULT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().description(\"krishna_k\nKrishna Kanth\")"
    )

    FOLLOW_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Follow"
    )

    PRODUCTS_TAB = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().description(\"Products\n5\")"
    )

    PRODUCT_ITEM = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().description(\"Krishna stores Sadhguru\n₹ 200.00\n₹ 250.00\")"
    )

    PRODUCT_INFO = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().description(\"Krishna stores\nSadhguru\")"
    )

    ASK_STORE_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Got a Question? Ask the Store"
    )

    MESSAGE_INPUT = (
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    SEND_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().className(\"android.widget.Button\").instance(3)"
    )

    STORES_TAB = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().description(\"Stores\n1\")"
    )

    STORE_ITEM = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().description(\"krishna_stores\nKrishna Stores\nArts, Crafts, and Sewing • Nellore\")"
    )

    SUPPORT_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Support"
    )

    POSTS_TAB = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().description(\"Posts\n2\")"
    )

    COMMENT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().className(\"android.widget.ImageView\").instance(4)"
    )

    COMMENT_INPUT = (
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    COMMENT_SEND_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Send"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def enter_search_text(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        field.click()
        field.send_keys(text)

    def click_people_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.PEOPLE_TAB)).click()

    def click_user_result(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_RESULT)).click()

    def click_follow_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FOLLOW_BUTTON)).click()

    def click_products_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCTS_TAB)).click()

    def click_product_item(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_ITEM)).click()

    def click_product_info(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_INFO)).click()

    def click_ask_store_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ASK_STORE_BUTTON)).click()

    def enter_message(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.MESSAGE_INPUT))
        field.click()
        field.send_keys(text)

    def click_send_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEND_BUTTON)).click()

    def click_stores_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.STORES_TAB)).click()

    def click_store_item(self):
        self.wait.until(EC.element_to_be_clickable(self.STORE_ITEM)).click()

    def click_support_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUPPORT_BUTTON)).click()

    def click_posts_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.POSTS_TAB)).click()

    def click_comment_button(self):
        self.wait.until(EC.element_to_be_clickable(self.COMMENT_BUTTON)).click()

    def enter_comment(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.COMMENT_INPUT))
        field.click()
        field.send_keys(text)

    def click_comment_send_button(self):
        self.wait.until(EC.element_to_be_clickable(self.COMMENT_SEND_BUTTON)).click()