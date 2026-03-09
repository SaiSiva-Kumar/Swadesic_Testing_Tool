from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StoreSettingsPage:

    SETTINGS_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(7)")
    STORE_PROFILE = (AppiumBy.ACCESSIBILITY_ID, "Store profile")
    STORE_NAME_CURRENT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Test 1\")")
    STORE_NAME_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    STORE_HANDLE_CURRENT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"test123_123\")")
    STORE_HANDLE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    BUSINESS_CATEGORY_CURRENT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Apparel\")")
    ART_AND_CRAFT_SUPPLIES = (AppiumBy.ACCESSIBILITY_ID, "Art and Craft Supplies")
    BUSINESS_TYPE_CURRENT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"E-commerce Platforms\")")
    DIRECT_TO_CONSUMER = (AppiumBy.ACCESSIBILITY_ID, "Direct-to-Consumer (D2C) Brands")
    BUSINESS_TYPE_SELECTED = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Direct-to-Consumer (D2C) Brands\")")
    DISTRIBUTORS = (AppiumBy.ACCESSIBILITY_ID, "Distributors")
    ABOUT_BUSINESS_CURRENT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Test 124\")")
    ABOUT_BUSINESS_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "save")
    FULFILLMENT_SETTINGS = (AppiumBy.ACCESSIBILITY_ID, "Fulfillment settings")
    PREPARE_SHIP_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"3 days\")")
    PREPARE_SHIP_2_DAYS = (AppiumBy.ACCESSIBILITY_ID, "2 days")
    DELIVERY_TIME_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"7 days\")")
    DELIVERY_TIME_10_DAYS = (AppiumBy.ACCESSIBILITY_ID, "10 days")
    LOGISTICS_PARTNER_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"ABF Freight\")")
    ABF_FREIGHT = (AppiumBy.ACCESSIBILITY_ID, "ABF Freight")
    SAVE_CHANGES = (AppiumBy.XPATH, "//android.widget.Button[@content-desc=\"Save changes\"]")
    RETURN_AND_REFUND_SETTINGS = (AppiumBy.ACCESSIBILITY_ID, "Return and refund settings")
    RETURN_PERIOD_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"7\")")
    RETURN_PERIOD_4_DAYS = (AppiumBy.ACCESSIBILITY_ID, "4 days")
    RETURN_CONDITIONS_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_settings_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.SETTINGS_ICON)).click()

    def click_store_profile(self):
        self.wait.until(EC.element_to_be_clickable(self.STORE_PROFILE)).click()

    def enter_store_name(self, name):
        self.wait.until(EC.element_to_be_clickable(self.STORE_NAME_CURRENT)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.STORE_NAME_INPUT))
        field.click()
        field.send_keys(name)

    def enter_store_handle(self, handle):
        self.wait.until(EC.element_to_be_clickable(self.STORE_HANDLE_CURRENT)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.STORE_HANDLE_INPUT))
        field.click()
        field.send_keys(handle)

    def select_business_category(self):
        self.wait.until(EC.element_to_be_clickable(self.BUSINESS_CATEGORY_CURRENT)).click()
        self.wait.until(EC.element_to_be_clickable(self.ART_AND_CRAFT_SUPPLIES)).click()

    def select_business_type(self):
        self.wait.until(EC.element_to_be_clickable(self.BUSINESS_TYPE_CURRENT)).click()
        self.wait.until(EC.element_to_be_clickable(self.DIRECT_TO_CONSUMER)).click()
        self.wait.until(EC.element_to_be_clickable(self.BUSINESS_TYPE_SELECTED)).click()
        self.wait.until(EC.element_to_be_clickable(self.DISTRIBUTORS)).click()

    def enter_about_business(self, text):
        self.wait.until(EC.element_to_be_clickable(self.ABOUT_BUSINESS_CURRENT)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.ABOUT_BUSINESS_INPUT))
        field.click()
        field.send_keys(text)
    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def click_fulfillment_settings(self):
        self.wait.until(EC.element_to_be_clickable(self.FULFILLMENT_SETTINGS)).click()

    def select_prepare_ship_time(self):
        self.wait.until(EC.element_to_be_clickable(self.PREPARE_SHIP_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.PREPARE_SHIP_2_DAYS)).click()

    def select_delivery_time(self):
        self.wait.until(EC.element_to_be_clickable(self.DELIVERY_TIME_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.DELIVERY_TIME_10_DAYS)).click()

    def select_logistics_partner(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGISTICS_PARTNER_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.ABF_FREIGHT)).click()

    def click_save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_CHANGES)).click()

    def click_return_and_refund_settings(self):
        self.wait.until(EC.element_to_be_clickable(self.RETURN_AND_REFUND_SETTINGS)).click()

    def select_return_period(self):
        self.wait.until(EC.element_to_be_clickable(self.RETURN_PERIOD_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.RETURN_PERIOD_4_DAYS)).click()

    def enter_return_conditions(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.RETURN_CONDITIONS_INPUT))
        field.click()
        field.send_keys(text)