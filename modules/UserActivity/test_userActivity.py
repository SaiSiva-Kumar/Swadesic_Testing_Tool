from pages.userActivity_page import UserActivityPage
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def test_TC_USERACTIVITY_001_update_personal_information(driver):
    """
    Test Case ID: TC_USERACTIVITY_001
    Title: Update User Personal Information

    Objective:
    To verify that a user can successfully update their personal
    information by changing city and profession.

    Test Steps:
    1. Click on User Profile button.
    2. Click on Settings button.
    3. Click on Personal Information button.
    4. Click on City you live dropdown and choose Agartala.
    5. Click on Profession dropdown and choose Actor.
    6. Click on Save button.

    Expected Result:
    Personal information is updated successfully.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_001",
        title="Update User Personal Information",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on User Profile button",
        user_activity_page.click_profile_button
    )

    executor.step(
        "Click on Settings button",
        user_activity_page.click_settings_button
    )

    executor.step(
        "Click on Personal Information button",
        user_activity_page.click_personal_information
    )

    executor.step(
        "Click on City you live dropdown and choose Agartala",
        user_activity_page.select_city
    )

    executor.step(
        "Click on Profession dropdown and choose Actor",
        user_activity_page.select_profession
    )

    executor.step(
        "Click on Save button",
        user_activity_page.click_save
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_USERACTIVITY_002_change_theme_color(driver):
    """
    Test Case ID: TC_USERACTIVITY_002
    Title: Change Theme Color

    Objective:
    To verify that a user can successfully navigate to theme
    settings and select dark mode.

    Test Steps:
    1. Click on Theme Settings.
    2. Click on Dark Mode.
    3. Click on Back button.

    Expected Result:
    Theme settings screen is navigated and dark mode is selected.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_002",
        title="Change Theme Color",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Theme Settings",
        user_activity_page.click_theme_settings
    )

    executor.step(
        "Click on Dark Mode",
        user_activity_page.click_dark_mode
    )

    executor.step(
        "Click on Back button",
        user_activity_page.click_back_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_USERACTIVITY_003_app_and_security_functionality(driver):
    """
    Test Case ID: TC_USERACTIVITY_003
    Title: Check App and Security Functionality

    Objective:
    To verify that Terms and Conditions, Privacy Agreement,
    and Adjust App Font Size screens are accessible and
    navigable from App and Security settings.

    Test Steps:
    1. Click on App and Security.
    2. Click on Terms and Conditions.
    3. Click on Back button.
    4. Click on Privacy Agreement.
    5. Click on Back button.
    6. Click on Adjust App Font Size.
    7. Click on Back button.

    Expected Result:
    All three screens are accessible and back navigation works correctly.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_003",
        title="Check App and Security Functionality",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on App and Security",
        user_activity_page.click_app_and_security
    )

    executor.step(
        "Click on Terms and Conditions",
        user_activity_page.click_terms_and_conditions
    )

    executor.step(
        "Click on Back button",
        user_activity_page.click_back_button_image
    )

    executor.step(
        "Click on Privacy Agreement",
        user_activity_page.click_privacy_agreement
    )

    executor.step(
        "Click on Back button",
        user_activity_page.click_back_button_image
    )

    executor.step(
        "Click on Adjust App Font Size",
        user_activity_page.click_adjust_app_font_size
    )

    executor.step(
        "Click on Back button",
        user_activity_page.click_font_size_back_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result