import time
from pages.login_page import LoginPage
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def reset_login_state(driver):
    login_page = LoginPage(driver)
    login_page.logout()


def test_TC_LOGIN_001_valid_login(driver):
    """
    Test Case ID: TC_LOGIN_001
    Title: Valid Login Using Email and OTP

    Objective:
    To verify that every interactive element in the login flow
    functions correctly and the user is successfully authenticated.

    Test Steps:
    1. Click on Profile button.
    2. Click on See All Options button.
    3. Click on Continue with Email and OTP button.
    4. Enter valid email address.
    5. Click on Send OTP button.
    6. Wait for manual OTP entry.
    7. Click on Verify OTP button.
    8. Verify user is navigated to home screen.

    Expected Result:
    Each button and input responds correctly and the user is
    navigated to the home screen without errors.
    """

    test_result = TestResult(
        test_id="TC_LOGIN_001",
        title="Valid Login Using Email and OTP",
        page_name="login_page"
    )

    login_page = LoginPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Profile button",
        login_page.click_profile_button
    )

    executor.step(
        "Click on See All Options button",
        login_page.click_see_all_options
    )

    executor.step(
        "Click on Continue with Email and OTP button",
        login_page.click_continue_with_email
    )

    executor.step(
        "Enter valid email address",
        lambda: login_page.enter_email("saisivakumar0906@gmail.com")
    )

    executor.step(
        "Click on Send OTP button",
        login_page.click_send_otp
    )

    executor.step(
        "Wait for manual OTP entry",
        lambda: time.sleep(3)
    )

    executor.step(
        "Click on Verify OTP button",
        login_page.click_verify_otp
    )

    executor.step(
        "Verify user is navigated to home screen",
        login_page.is_home_screen_visible
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result