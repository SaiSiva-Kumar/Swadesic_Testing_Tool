from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostPage:

    CREATE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(8)")
    ADD_PHOTOS = (AppiumBy.ACCESSIBILITY_ID, "Add photos (up to 5)")
    UPLOAD_PHOTOS = (AppiumBy.ACCESSIBILITY_ID, "Upload photos from your phone")
    PHOTO_INSTANCE_18 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(18)")
    PHOTO_INSTANCE_25 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(25)")
    PHOTO_INSTANCE_32 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(32)")
    PHOTO_INSTANCE_39 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(39)")
    PHOTO_CONFIRM = (AppiumBy.ACCESSIBILITY_ID, "Photo taken on Feb 22, 2026 4:11 PM")
    CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.Button\").instance(6)")
    ADD_VIDEO = (AppiumBy.ACCESSIBILITY_ID, "Add a video")
    UPLOAD_FROM_GALLERY = (AppiumBy.ACCESSIBILITY_ID, "Upload from Gallery")
    VIDEO_INSTANCE_18 = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.view.View\").instance(18)")
    CONTINUE = (AppiumBy.ACCESSIBILITY_ID, "Continue")
    TAG_STORES = (AppiumBy.ACCESSIBILITY_ID, "Tag Stores, Products & Members")
    TAG_SEARCH_ICON = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    TAG_SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    TAG_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description(\"krishna_k\nKrishna Kanth Krishna Kanth\nUser\")")
    CAPTION_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    POST_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Post")
    PROFILE_BUTTON = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(10)")
    USER_POSTS = (AppiumBy.ACCESSIBILITY_ID, "User Posts")
    THREE_DOTS_MENU = (
    AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(5)")
    DELETE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Delete")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_create_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()

    def click_add_photos(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_PHOTOS)).click()
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_PHOTOS)).click()
        self.wait.until(EC.element_to_be_clickable(self.PHOTO_INSTANCE_18)).click()
        self.wait.until(EC.element_to_be_clickable(self.PHOTO_INSTANCE_25)).click()
        self.wait.until(EC.element_to_be_clickable(self.PHOTO_INSTANCE_32)).click()
        self.wait.until(EC.element_to_be_clickable(self.PHOTO_INSTANCE_39)).click()
        self.wait.until(EC.element_to_be_clickable(self.PHOTO_CONFIRM)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()

    def click_add_video(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_VIDEO)).click()
        self.wait.until(EC.element_to_be_clickable(self.UPLOAD_FROM_GALLERY)).click()
        self.wait.until(EC.element_to_be_clickable(self.VIDEO_INSTANCE_18)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def click_tag_stores(self):
        self.wait.until(EC.element_to_be_clickable(self.TAG_STORES)).click()

    def search_and_select_tag(self, query):
        self.wait.until(EC.element_to_be_clickable(self.TAG_SEARCH_ICON)).click()
        field = self.wait.until(EC.element_to_be_clickable(self.TAG_SEARCH_INPUT))
        field.click()
        field.send_keys(query)
        self.wait.until(EC.element_to_be_clickable(self.TAG_RESULT)).click()

    def enter_post_caption(self, text):
        field = self.wait.until(EC.element_to_be_clickable(self.CAPTION_INPUT))
        field.click()
        field.send_keys(text)

    def click_post_button(self):
        self.wait.until(EC.element_to_be_clickable(self.POST_BUTTON)).click()

    def click_profile_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_BUTTON)).click()

    def click_user_posts(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_POSTS)).click()

    def click_three_dots_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.THREE_DOTS_MENU)).click()

    def click_delete_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON)).click()

    def confirm_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTON)).click()