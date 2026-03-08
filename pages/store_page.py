from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class StorePage:

    PROFILE_BUTTON = (AppiumBy.XPATH,
                      "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]")
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
    # NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Next")
    ABOUT_BUSINESS_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    WEBSITE_LINK_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    STORE_HANDLE_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    STORE_HANDLE_AVAILABLE = (AppiumBy.ACCESSIBILITY_ID, "test_store1 is available")
    CREATE_STORE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Create The Store")
    FINISH_SETUP = (AppiumBy.ANDROID_UIAUTOMATOR,
                    "new UiSelector().description(\"Finish Setup & Start Sharing\nComplete your store so people with your StoreLink can see it instantly.\n50%\")")
    REVIEW_TRUST_CENTER = (AppiumBy.ACCESSIBILITY_ID, "Review Trust Center")
    PHONE_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    EMAIL_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "save")
    ONLINE_ONLY = (AppiumBy.ACCESSIBILITY_ID, "It's online only")
    AREA_OF_OPERATIONS_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    SELECT_CITY_DROPDOWN = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(15)")
    ADILABAD = (AppiumBy.ACCESSIBILITY_ID, "Adilabad")
    PINCODE_INPUT_1 = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    STATE_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(16)")
    ANDHRA_PRADESH = (AppiumBy.ACCESSIBILITY_ID, "Andhra Pradesh")
    CITY_DROPDOWN_1 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(20)")
    AMLAPURAM = (AppiumBy.ACCESSIBILITY_ID, "Amlapuram")
    LOCALITY_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(17)")
    LOCALITY_SEARCH_ICON = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    LOCALITY_SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    ADD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Add")
    PLACE_DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(18)")
    PLACE_SEARCH_ICON = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    PLACE_SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    PINCODE_INPUT_2 = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(2)")
    INDIVIDUAL_TICKBOX = (AppiumBy.ACCESSIBILITY_ID, "Individual")
    PAN_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    PAN_NAME_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    DATE_OF_BIRTH = (AppiumBy.ACCESSIBILITY_ID, "DD / MM / YYYY")
    OK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "OK")
    ADD_SIGNATURE = (AppiumBy.ACCESSIBILITY_ID, "Add signature")
    REQUEST_VERIFICATION = (AppiumBy.ACCESSIBILITY_ID, "Request verification")
    PLUS_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(25)")
    ADD_PRODUCT = (AppiumBy.ACCESSIBILITY_ID, "Add a product")
    VIDEO_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(15)")
    UPLOAD_FROM_GALLERY = (AppiumBy.ACCESSIBILITY_ID, "Upload from Gallery")
    VIDEO_INSTANCE_23 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(23)")
    VIDEO_CONFIRM_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(6)")
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Continue")
    IMAGE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(15)")
    UPLOAD_PHOTOS = (AppiumBy.ACCESSIBILITY_ID, "Upload photos from your phone")
    IMAGE_INSTANCE_18 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(18)")
    IMAGE_CONFIRM_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(6)")
    BASIC_DETAILS = (AppiumBy.ANDROID_UIAUTOMATOR,
                     "new UiSelector().description(\"Basic Details\nBrand, product name, category, and description.\")")
    BRAND_NAME_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    PRODUCT_NAME_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    PRODUCT_CATEGORY_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(2)")
    PRODUCT_DESCRIPTION_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(3)")
    BASIC_DETAILS_BACK = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(7)")
    INVENTORY_AND_PRICING = (AppiumBy.ANDROID_UIAUTOMATOR,
                             "new UiSelector().description(\"Inventory & Pricing\nAdd variants (if any), set MRP, selling price, and stock.\")")
    IN_STOCK_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")
    MRP_INPUT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")
    SELLING_PRICE_INPUT = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(2)")
    INVENTORY_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "save")
    INVENTORY_BACK = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(8)")
    ORIGIN_AND_TRANSPARENCY = (AppiumBy.ANDROID_UIAUTOMATOR,
                               "new UiSelector().description(\"Origin & Transparency\nOrigin & Transparency help consumers understand and make informed decisions.\")")
    MANUFACTURED_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "Manufactured")
    MANUFACTURED_OPTION = (AppiumBy.ACCESSIBILITY_ID, "Manufactured")
    SELECT_COUNTRY_0 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"Select country\").instance(0)")
    INDIA = (AppiumBy.ACCESSIBILITY_ID, "India")
    SELECT_COUNTRIES = (AppiumBy.ACCESSIBILITY_ID, "Select countries")
    DONE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Done")
    SELECT_COUNTRY = (AppiumBy.ACCESSIBILITY_ID, "Select country")
    ORIGIN_SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Save")
    NEXT_PRODUCT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Next")
    PUBLISH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Publish")
    ALL_ORDERS = (AppiumBy.ACCESSIBILITY_ID, "All orders")
    # ORDER_ITEM_DELIVERY = (AppiumBy.ACCESSIBILITY_ID, "test345\n₹50\n08-03-2026 6:43 PM\n1 item\nSuborders: 1 waiting")
    CONFIRM_ALL = (AppiumBy.ACCESSIBILITY_ID, "Confirm all")
    CONFIRM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Confirm")
    ALL_TAB = (AppiumBy.ACCESSIBILITY_ID, "All")
    START_SHIPPING_ALL = (AppiumBy.ACCESSIBILITY_ID, "Start shipping all")
    SHIP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Ship")
    LOGISTICS_PARTNER_DROPDOWN = (
    AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.ImageView[5]/android.view.View")
    LOGISTICS_4PX = (AppiumBy.ACCESSIBILITY_ID, "4PX")
    TRACKING_NUMBER_INPUT = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]")
    ADDITIONAL_NOTES_INPUT = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
    MARK_AS_SHIPPED = (AppiumBy.ACCESSIBILITY_ID, "Mark as Shipped")
    UPDATE_DELIVERY_STATUS = (AppiumBy.ACCESSIBILITY_ID, "Update delivery status")
    MARK_AS_DELIVERED = (AppiumBy.ACCESSIBILITY_ID, "Mark as Delivered")
    CANCEL_ALL = (AppiumBy.ACCESSIBILITY_ID, "Cancel all")
    CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Cancel")
    CANCEL_REASON_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    DONE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Done")
    ACCOUNT_BALANCE = (AppiumBy.ACCESSIBILITY_ID, "Account balance")
    SEND_NOW_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    SEND_TO_PRIMARY_ACCOUNT = (AppiumBy.ACCESSIBILITY_ID, "Send ₹10 to Primary Account")

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

    # def click_next(self):
    #     self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def enter_about_business(self, text):
        time.sleep(3)
        field = self.wait.until(EC.element_to_be_clickable(self.ABOUT_BUSINESS_INPUT))
        field.click()
        field.send_keys(text)

    def enter_website_link(self, url):
        field = self.wait.until(EC.element_to_be_clickable(self.WEBSITE_LINK_INPUT))
        field.click()
        field.send_keys(url)

    def enter_store_handle(self, handle):
        time.sleep(3)
        field = self.wait.until(EC.element_to_be_clickable(self.STORE_HANDLE_INPUT))
        field.click()
        field.send_keys(handle)

    def is_store_handle_available(self):
        self.wait.until(EC.presence_of_element_located(self.STORE_HANDLE_AVAILABLE))

    def click_create_the_store(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_STORE_BUTTON)).click()

    def click_finish_setup(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_SETUP)).click()

    def click_review_trust_center(self):
        self.wait.until(EC.element_to_be_clickable(self.REVIEW_TRUST_CENTER)).click()

    def enter_phone(self, phone):
        time.sleep(2)
        field = self.wait.until(EC.element_to_be_clickable(self.PHONE_INPUT))
        field.click()
        field.send_keys(phone)

    def enter_email(self, email):
        field = self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
        field.click()
        field.send_keys(email)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    def click_online_only(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.ONLINE_ONLY)).click()

    def enter_area_of_operations(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.AREA_OF_OPERATIONS_INPUT))
        field.click()
        field.send_keys(text)

    def select_city_adilabad(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_CITY_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADILABAD)).click()

    def enter_pincode_1(self, pincode):
        field = self.wait.until(EC.element_to_be_clickable(self.PINCODE_INPUT_1))
        field.click()
        field.send_keys(pincode)

    def select_state_andhra_pradesh(self):
        self.wait.until(EC.element_to_be_clickable(self.STATE_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.ANDHRA_PRADESH)).click()

    def select_city_amlapuram(self):
        self.wait.until(EC.element_to_be_clickable(self.CITY_DROPDOWN_1)).click()
        self.wait.until(EC.element_to_be_clickable(self.AMLAPURAM)).click()

    def select_locality(self, text):
        self.wait.until(EC.element_to_be_clickable(self.LOCALITY_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOCALITY_SEARCH_ICON)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.LOCALITY_SEARCH_INPUT))
        field.click()
        field.send_keys(text)
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def select_place(self, text):
        self.wait.until(EC.element_to_be_clickable(self.PLACE_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.PLACE_SEARCH_ICON)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.PLACE_SEARCH_INPUT))
        field.click()
        field.send_keys(text)
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def enter_pincode_2(self, pincode):
        field = self.wait.until(EC.element_to_be_clickable(self.PINCODE_INPUT_2))
        field.click()
        field.send_keys(pincode)

    def click_individual_tickbox(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.INDIVIDUAL_TICKBOX)).click()

    def enter_pan(self, pan):
        field = self.wait.until(EC.element_to_be_clickable(self.PAN_INPUT))
        field.click()
        field.send_keys(pan)

    def enter_pan_name(self, name):
        field = self.wait.until(EC.element_to_be_clickable(self.PAN_NAME_INPUT))
        field.click()
        field.send_keys(name)

    def click_date_of_birth(self):
        self.wait.until(EC.element_to_be_clickable(self.DATE_OF_BIRTH)).click()

    def click_ok(self):
        self.wait.until(EC.element_to_be_clickable(self.OK_BUTTON)).click()

    def click_add_signature(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_SIGNATURE)).click()

    def click_request_verification(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.REQUEST_VERIFICATION)).click()

    def click_plus_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PLUS_BUTTON)).click()

    def click_add_product(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT)).click()

    def upload_product_video(self):
        self.wait.until(EC.element_to_be_clickable(self.VIDEO_SECTION)).click()
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_FROM_GALLERY)).click()
        self.wait.until(EC.element_to_be_clickable(self.VIDEO_INSTANCE_23)).click()
        self.wait.until(EC.element_to_be_clickable(self.VIDEO_CONFIRM_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def upload_product_image(self):
        self.wait.until(EC.element_to_be_clickable(self.IMAGE_SECTION)).click()
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_PHOTOS)).click()
        self.wait.until(EC.element_to_be_clickable(self.IMAGE_INSTANCE_18)).click()
        self.wait.until(EC.element_to_be_clickable(self.IMAGE_CONFIRM_BUTTON)).click()

    def fill_basic_details(self, brand, product_name, category):
        self.wait.until(EC.element_to_be_clickable(self.BASIC_DETAILS)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.BRAND_NAME_INPUT))
        field.click()
        field.send_keys(brand)
        field = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_NAME_INPUT))
        field.click()
        field.send_keys(product_name)
        field = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_CATEGORY_INPUT))
        field.click()
        field.send_keys(category)
    def click_basic_details_back(self):
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.BASIC_DETAILS_BACK)).click()

    def fill_inventory_and_pricing(self, stock, mrp, selling_price):
        self.wait.until(EC.element_to_be_clickable(self.INVENTORY_AND_PRICING)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.IN_STOCK_INPUT))
        field.click()
        field.send_keys(stock)
        field = self.wait.until(EC.element_to_be_clickable(self.MRP_INPUT))
        field.click()
        field.send_keys(mrp)
        field = self.wait.until(EC.element_to_be_clickable(self.SELLING_PRICE_INPUT))
        field.click()
        field.send_keys(selling_price)
        self.wait.until(EC.element_to_be_clickable(self.INVENTORY_SAVE_BUTTON)).click()

    def click_inventory_back(self):
        self.wait.until(EC.element_to_be_clickable(self.INVENTORY_BACK)).click()

    def fill_origin_and_transparency(self):
        self.wait.until(EC.element_to_be_clickable(self.ORIGIN_AND_TRANSPARENCY)).click()
        self.wait.until(EC.element_to_be_clickable(self.MANUFACTURED_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.MANUFACTURED_OPTION)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_COUNTRY_0)).click()
        self.wait.until(EC.element_to_be_clickable(self.INDIA)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_COUNTRIES)).click()
        self.wait.until(EC.element_to_be_clickable(self.INDIA)).click()
        self.wait.until(EC.element_to_be_clickable(self.DONE_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.SELECT_COUNTRY)).click()
        self.wait.until(EC.element_to_be_clickable(self.INDIA)).click()
        self.wait.until(EC.element_to_be_clickable(self.ORIGIN_SAVE_BUTTON)).click()

    def click_next_product(self):
        self.wait.until(EC.element_to_be_clickable(self.NEXT_PRODUCT_BUTTON)).click()

    def click_publish(self):
        self.wait.until(EC.element_to_be_clickable(self.PUBLISH_BUTTON)).click()

    def click_all_orders(self):
        self.wait.until(EC.element_to_be_clickable(self.ALL_ORDERS)).click()

    # def click_order_item_delivery(self):
    #     self.wait.until(EC.element_to_be_clickable(self.ORDER_ITEM_DELIVERY)).click()

    def click_confirm_all(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_ALL)).click()

    def click_confirm(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    def click_all_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.ALL_TAB)).click()

    def click_start_shipping_all(self):
        self.wait.until(EC.element_to_be_clickable(self.START_SHIPPING_ALL)).click()

    def click_ship(self):
        self.wait.until(EC.element_to_be_clickable(self.SHIP_BUTTON)).click()

    def select_logistics_partner(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGISTICS_PARTNER_DROPDOWN)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGISTICS_4PX)).click()

    def enter_tracking_number(self, tracking):
        field = self.wait.until(EC.element_to_be_clickable(self.TRACKING_NUMBER_INPUT))
        field.click()
        field.send_keys(tracking)

    def enter_additional_notes(self, notes):
        field = self.wait.until(EC.element_to_be_clickable(self.ADDITIONAL_NOTES_INPUT))
        field.click()
        field.send_keys(notes)

    def click_mark_as_shipped(self):
        self.wait.until(EC.element_to_be_clickable(self.MARK_AS_SHIPPED)).click()

    def click_update_delivery_status(self):
        self.wait.until(EC.element_to_be_clickable(self.UPDATE_DELIVERY_STATUS)).click()

    def click_mark_as_delivered(self):
        self.wait.until(EC.element_to_be_clickable(self.MARK_AS_DELIVERED)).click()

    def click_cancel_all(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_ALL)).click()

    def click_cancel(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BUTTON)).click()

    def enter_cancel_reason(self, reason):
        field = self.wait.until(EC.element_to_be_clickable(self.CANCEL_REASON_INPUT))
        field.click()
        field.send_keys(reason)

    def click_done(self):
        self.wait.until(EC.element_to_be_clickable(self.DONE_BUTTON)).click()

    def click_account_balance(self):
        self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_BALANCE)).click()

    def enter_send_amount(self, amount):
        field = self.wait.until(EC.element_to_be_clickable(self.SEND_NOW_INPUT))
        field.click()
        field.send_keys(amount)

    def click_send_to_primary_account(self):
        self.wait.until(EC.element_to_be_clickable(self.SEND_TO_PRIMARY_ACCOUNT)).click()