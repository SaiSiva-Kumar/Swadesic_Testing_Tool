from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    SEARCH_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(7)")
    PRODUCTS_TAB = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"Products\nTab 2 of 2\")")
    PRODUCT_ITEM = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"Covers Covers\n₹ 200.00\n₹ 250.00\")")
    BUY_NOW = (AppiumBy.ACCESSIBILITY_ID, "Buy now")
    CONTINUE = (AppiumBy.ACCESSIBILITY_ID, "Continue")
    SELECT_DELIVERY_ADDRESS = (AppiumBy.ACCESSIBILITY_ID, "Select Delivery Address & Payment")
    SECURE_CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, "Secure checkout")
    PHONEPE = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"PhonePe PhonePe\")")
    GO_BACK = (AppiumBy.ID, "android:id/button2")
    PROFILE_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(10)")
    MY_ORDERS = (AppiumBy.ACCESSIBILITY_ID, "My orders")
    ORDER_ITEM = (AppiumBy.ANDROID_UIAUTOMATOR,
                  "new UiSelector().description(\" pubg\n₹205\n28-02-2026 11:02 PM\n1 item\n1 waiting confirmation\")")
    WAITING_FOR_CONFIRMATION = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"Waiting for confirmation\n# 1 suborder\")")
    CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Cancel")
    CANCEL_REASON_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    PROCEED_TO_CANCEL = (AppiumBy.ACCESSIBILITY_ID, "Proceed to cancel")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    def click_products_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCTS_TAB)).click()

    def click_product(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_ITEM)).click()

    def click_buy_now(self):
        self.wait.until(EC.element_to_be_clickable(self.BUY_NOW)).click()

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def click_select_delivery_address(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_DELIVERY_ADDRESS)).click()

    def click_secure_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.SECURE_CHECKOUT)).click()

    def click_phonepe(self):
        self.wait.until(EC.element_to_be_clickable(self.PHONEPE)).click()

    def click_go_back(self):
        self.wait.until(EC.element_to_be_clickable(self.GO_BACK)).click()

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_BUTTON)).click()

    def click_my_orders(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_ORDERS)).click()

    def click_order_item(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_ITEM)).click()

    def click_waiting_for_confirmation(self):
        self.wait.until(EC.element_to_be_clickable(self.WAITING_FOR_CONFIRMATION)).click()

    def click_cancel(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BUTTON)).click()

    def enter_cancel_reason(self, reason):
        field = self.wait.until(EC.element_to_be_clickable(self.CANCEL_REASON_INPUT))
        field.click()
        field.send_keys(reason)

    def click_proceed_to_cancel(self):
        self.wait.until(EC.element_to_be_clickable(self.PROCEED_TO_CANCEL)).click()