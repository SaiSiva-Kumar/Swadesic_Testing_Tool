import os
import subprocess
import socket
import time
import traceback
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config import APPIUM_EXECUTABLE, SERVER_HOST, SERVER_PORT, CAPABILITIES, APP_PACKAGE
from reporting.report_generator import generate_report


# ─────────────────────────────────────────────
# MODULE REGISTRY
# When a new module is created, import its
# test functions and register it here.
# ─────────────────────────────────────────────
from modules.login.test_login import (
    test_TC_LOGIN_001_valid_login,
    test_TC_LOGIN_002_send_otp_without_email,
    reset_login_state
)

from modules.POST.test_post import (
    test_TC_POST_001_create_post_with_media_and_tag,
    test_TC_POST_002_delete_post
)

from modules.Store.test_store import (
    test_TC_PRODUCT_001_create_store,
    test_TC_STORE_002_store_verification,
    test_TC_STORE_003_create_product,
    test_TC_STORE_004_order_delivery_lifecycle,
    test_TC_STORE_005_cancel_order,
    test_TC_STORE_006_send_balance_to_bank
)

from modules.Store.Settings.test_store_settings import (
    test_TC_STORE_SETTINGS_001_update_store_profile,
    test_TC_STORE_SETTINGS_002_update_fulfillment_settings,
    test_TC_STORE_SETTINGS_003_update_return_and_refund_settings
)

from modules.Product.test_product import (
    test_TC_PURCHASE_001_purchase_product_via_phonepe,
    test_TC_PURCHASE_002_cancel_product
)
from modules.User.test_user import (
    test_TC_USER_001_onboard_user_with_email,
    test_TC_USER_002_update_profile
)

from modules.Search.test_search import (
    test_TC_SEARCH_001_search_user_and_follow,
    test_TC_SEARCH_002_ask_question_on_product,
    test_TC_SEARCH_003_support_store,
    test_TC_SEARCH_004_comment_on_post
)

from modules.Review.test_review import (
    test_TC_REVIEW_001_create_review_page,
    test_TC_REVIEW_002_update_review_page
)

from modules.UserActivity.test_userActivity import (
    test_TC_USERACTIVITY_001_update_personal_information,
    test_TC_USERACTIVITY_002_change_theme_color,
    test_TC_USERACTIVITY_003_app_and_security_functionality,
    test_TC_USERACTIVITY_004_save_and_repost_user_post,
    test_TC_USERACTIVITY_005_switch_accounts,
    test_TC_USERACTIVITY_006_suggest_a_feature,
    test_TC_USERACTIVITY_007_customer_support,
    test_TC_USERACTIVITY_008_request_a_feature,
    test_TC_USERACTIVITY_009_find_friends
)


MODULE_REGISTRY = {
    "1": {
        "name": "Login",
        "tests": [
            {"fn": test_TC_LOGIN_001_valid_login, "setup": None},
            {"fn": test_TC_LOGIN_002_send_otp_without_email, "setup": reset_login_state},
        ]
    },
    "2": {
        "name": "Post",
        "tests": [
            {"fn": test_TC_POST_001_create_post_with_media_and_tag, "setup": None},
            {"fn": test_TC_POST_002_delete_post, "setup": None},
        ]
    },
    "3": {
        "name": "Store",
        "tests": [
            {"fn": test_TC_PRODUCT_001_create_store, "setup": None},
            {"fn": test_TC_STORE_002_store_verification, "setup": None},
            {"fn": test_TC_STORE_003_create_product, "setup": None},
            {"fn": test_TC_STORE_004_order_delivery_lifecycle, "setup": None},
            {"fn": test_TC_STORE_005_cancel_order, "setup": None},
            {"fn": test_TC_STORE_006_send_balance_to_bank, "setup": None},
        ]
    },
    "4": {
        "name": "Product",
        "tests": [
            {"fn": test_TC_PURCHASE_001_purchase_product_via_phonepe, "setup": None},
            {"fn": test_TC_PURCHASE_002_cancel_product, "setup": None}
        ]
    },
    "5": {
        "name": "User",
        "tests": [
            {"fn": test_TC_USER_001_onboard_user_with_email, "setup": None},
            {"fn": test_TC_USER_002_update_profile, "setup": reset_login_state},
        ]
    },
    "6": {
         "name": "Search",
         "tests": [
              {"fn": test_TC_SEARCH_001_search_user_and_follow, "setup": None},
              {"fn": test_TC_SEARCH_002_ask_question_on_product, "setup": None},
              {"fn": test_TC_SEARCH_003_support_store, "setup": None},
              {"fn": test_TC_SEARCH_004_comment_on_post, "setup": None}
         ]
    },
    "7": {
        "name": "Review",
        "tests": [
            {"fn": test_TC_REVIEW_001_create_review_page, "setup": None},
            {"fn": test_TC_REVIEW_002_update_review_page, "setup": None}
        ]
    },
    "8": {
        "name": "User Activity",
        "tests": [
            {"fn": test_TC_USERACTIVITY_001_update_personal_information, "setup": None},
            {"fn": test_TC_USERACTIVITY_002_change_theme_color, "setup": None},
            {"fn": test_TC_USERACTIVITY_003_app_and_security_functionality, "setup": None},
            {"fn": test_TC_USERACTIVITY_004_save_and_repost_user_post, "setup": None},
            {"fn": test_TC_USERACTIVITY_005_switch_accounts, "setup": None},
            {"fn": test_TC_USERACTIVITY_006_suggest_a_feature, "setup": None},
            {"fn": test_TC_USERACTIVITY_007_customer_support, "setup": None},
            {"fn": test_TC_USERACTIVITY_008_request_a_feature, "setup": None},
            {"fn": test_TC_USERACTIVITY_009_find_friends, "setup": None},
        ]
    },
    "9": {
        "name": "Store Settings",
        "tests": [
            {"fn": test_TC_STORE_SETTINGS_001_update_store_profile, "setup": None},
            {"fn": test_TC_STORE_SETTINGS_002_update_fulfillment_settings, "setup": None},
            {"fn": test_TC_STORE_SETTINGS_003_update_return_and_refund_settings, "setup": None}
        ]
    }
}
# ─────────────────────────────────────────────


def validate_environment():
    try:
        subprocess.check_output(["adb", "version"])
    except Exception:
        raise Exception("ADB is not available")

    output = subprocess.check_output(["adb", "devices"]).decode()
    lines = output.strip().split("\n")
    connected = [line for line in lines[1:] if "device" in line]

    if not connected:
        raise Exception("No device connected")


def wait_for_server(host, port, timeout=30):
    start_time = time.time()
    while True:
        try:
            with socket.create_connection((host, port), timeout=2):
                return
        except Exception:
            if time.time() - start_time > timeout:
                raise Exception("Appium server did not start in time")
            time.sleep(1)


def start_appium_server():
    command = f'"{APPIUM_EXECUTABLE}" -a {SERVER_HOST} -p {SERVER_PORT} --session-override'

    process = subprocess.Popen(
        command,
        shell=True
    )

    wait_for_server(SERVER_HOST, SERVER_PORT)
    return process


def create_driver():
    options = UiAutomator2Options().load_capabilities(CAPABILITIES)
    driver = webdriver.Remote(
        f"http://{SERVER_HOST}:{SERVER_PORT}",
        options=options
    )
    driver.implicitly_wait(5)
    driver.activate_app(APP_PACKAGE)
    return driver


def initiate():
    validate_environment()
    server_process = start_appium_server()
    driver = create_driver()
    return driver, server_process


def show_modules():
    print("\nAvailable Modules:")
    for key, module in MODULE_REGISTRY.items():
        print(f"  {key}. {module['name']}")
    print()


def select_module():
    while True:
        choice = input("Enter module number to execute (or 'exit' to quit): ").strip()
        if choice.lower() == "exit":
            return None
        if choice in MODULE_REGISTRY:
            return MODULE_REGISTRY[choice]
        print("Invalid choice. Please enter a number from the list.")


def show_tests(module):
    print(f"\nAvailable Test Cases in {module['name']}:")
    for index, test_entry in enumerate(module["tests"], start=1):
        print(f"  {index}. {test_entry['fn'].__name__}")
    print()


def select_tests(module):
    while True:
        choice = input("Enter test numbers to run (comma separated), or 'all' to run all: ").strip()
        if choice.lower() == "all":
            return module["tests"]
        try:
            indices = [int(i.strip()) for i in choice.split(",")]
            selected = [module["tests"][i - 1] for i in indices if 1 <= i <= len(module["tests"])]
            if selected:
                return selected
            print("No valid selections. Please try again.")
        except Exception:
            print("Invalid input. Please try again.")


def execute_tests(driver, module, selected_tests):
    test_results = []

    print(f"\nRunning module: {module['name']}\n")

    for test_entry in selected_tests:
        test_fn = test_entry["fn"]
        setup_fn = test_entry.get("setup")

        if setup_fn:
            setup_fn(driver)

        print(f"Running: {test_fn.__name__}")
        try:
            result = test_fn(driver)
            test_results.append(result)
            print(f"Completed: {test_fn.__name__} — {result.overall_status}")
        except Exception as e:
            traceback.print_exc()

    return test_results


def open_reports_folder():
    reports_path = os.path.abspath("reports")
    os.startfile(reports_path)


def print_report_link():
    reports_path = os.path.abspath("reports")
    folder_url = reports_path.replace("\\", "/")
    print(f"\nTest Report → file:///{folder_url}")


def run():
    driver = None
    server = None

    try:
        print("Validating environment...")
        driver, server = initiate()
        print("Device ready. App launched.")

        while True:
            show_modules()
            selected_module = select_module()

            if not selected_module:
                break

            while True:
                show_tests(selected_module)
                choice = input("Enter test numbers to run (comma separated), 'all' to run all, or 'back' to go back to modules: ").strip()

                if choice.lower() == "back":
                    break

                if choice.lower() == "all":
                    selected_tests = selected_module["tests"]
                else:
                    try:
                        indices = [int(i.strip()) for i in choice.split(",")]
                        selected_tests = [selected_module["tests"][i - 1] for i in indices if 1 <= i <= len(selected_module["tests"])]
                        if not selected_tests:
                            print("No valid selections. Please try again.")
                            continue
                    except Exception:
                        print("Invalid input. Please try again.")
                        continue

                test_results = execute_tests(driver, selected_module, selected_tests)
                generate_report(test_results)
                print_report_link()

    finally:
        if driver:
            driver.quit()
        if server:
            server.terminate()


if __name__ == "__main__":
    run()