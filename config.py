APPIUM_EXECUTABLE = r"C:\Users\LENOVO\AppData\Roaming\npm\appium.cmd"

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 4725

APPIUM_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"

DEVICE_NAME = "10BE4L0A7C00078"
APP_PACKAGE = "com.sociallyx.dev"
APP_ACTIVITY = "com.swadesic.swadesic.MainActivity"

CAPABILITIES = {
    "platformName": "Android",
    "deviceName": DEVICE_NAME,
    "appPackage": APP_PACKAGE,
    "appActivity": APP_ACTIVITY,
    "udid": DEVICE_NAME,
    "platformVersion": "13",
    "automationName": "UiAutomator2",
    "noReset": True,
}
