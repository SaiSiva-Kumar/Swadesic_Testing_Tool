import time

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

def test_TC_USERACTIVITY_004_save_and_repost_user_post(driver):
    """
    Test Case ID: TC_USERACTIVITY_004
    Title: Save and Repost Another User Post

    Objective:
    To verify that a user can successfully search for another user,
    navigate to their profile, repost and save their post.

    Test Steps:
    1. Click on Search button.
    2. Click on Search input field and provide krishna as input.
    3. Click on People tab.
    4. Click on Profile.
    5. Click on Repost.
    6. Click on Saved.

    Expected Result:
    Post is reposted and saved successfully.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_004",
        title="Save and Repost Another User Post",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Search button",
        user_activity_page.click_search_button
    )

    executor.step(
        "Click on Search input field and provide krishna as input",
        lambda: user_activity_page.enter_search_input("krishna")
    )

    executor.step(
        "Click on People tab",
        user_activity_page.click_people_tab
    )

    executor.step(
        "Click on Profile",
        user_activity_page.click_user_profile
    )

    executor.step(
        "Click on Repost",
        user_activity_page.click_repost
    )

    executor.step(
        "Click on Saved",
        user_activity_page.click_saved
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_USERACTIVITY_005_switch_accounts(driver):
    """
    Test Case ID: TC_USERACTIVITY_005
    Title: Switch Accounts

    Objective:
    To verify that a user can successfully switch between accounts.

    Test Steps:
    1. Click on Switch Accounts.
    2. Click on required account to switch to.

    Expected Result:
    Account is switched successfully.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_005",
        title="Switch Accounts",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Switch Accounts",
        user_activity_page.click_switch_accounts
    )

    executor.step(
        "Click on required account to switch to",
        user_activity_page.click_account
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_USERACTIVITY_006_suggest_a_feature(driver):
    """
    Test Case ID: TC_USERACTIVITY_006
    Title: Suggest a Feature

    Objective:
    To verify that a user can successfully submit a feature
    suggestion by providing category, title and description.

    Test Steps:
    1. Click on Suggest a Feature.
    2. Click on Category dropdown and provide test as input and click Add.
    3. Enter Title as test.
    4. Enter Description as test.
    5. Click on Submit button.
    6. Click on Back button.

    Expected Result:
    Feature suggestion is submitted successfully.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_006",
        title="Suggest a Feature",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Suggest a Feature",
        user_activity_page.click_suggest_a_feature
    )

    executor.step(
        "Click on Category dropdown and provide test as input and click Add",
        lambda: user_activity_page.select_category("test")
    )

    executor.step(
        "Enter Title as test",
        lambda: user_activity_page.enter_title("test")
    )

    executor.step(
        "Enter Description as test",
        lambda: user_activity_page.enter_description("test")
    )

    executor.step(
        "Click on Submit button",
        user_activity_page.click_submit
    )

    executor.step(
        "Click on Back button",
        user_activity_page.click_suggest_back_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_USERACTIVITY_007_customer_support(driver):
    """
    Test Case ID: TC_USERACTIVITY_007
    Title: Customer Support Functionality

    Objective:
    To verify that a user can successfully submit a customer
    support request by providing category, target, title
    and description.

    Test Steps:
    1. Click on Customer Support.
    2. Click on Category dropdown and select Accounts.
    3. Enter Target as test.
    4. Enter Title as test.
    5. Enter Description as test.
    6. Click on Submit button.
    7. Click on Back button.

    Expected Result:
    Customer support request is submitted successfully.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_007",
        title="Customer Support Functionality",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Customer Support",
        user_activity_page.click_customer_support
    )

    executor.step(
        "Enter Target as test",
        lambda: user_activity_page.enter_support_target("test")
    )

    executor.step(
        "Click on Category dropdown and select Accounts",
        user_activity_page.select_support_category
    )

    executor.step(
        "Enter Title as test",
        lambda: user_activity_page.enter_support_title("test")
    )

    executor.step(
        "Enter Description as test",
        lambda: user_activity_page.enter_support_description("test")
    )

    executor.step(
        "Click on Submit button",
        user_activity_page.click_support_submit
    )

    executor.step(
        "Click on Back button",
        user_activity_page.click_support_back_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_USERACTIVITY_008_request_a_feature(driver):
    """
    Test Case ID: TC_USERACTIVITY_008
    Title: Request a Feature Functionality

    Objective:
    To verify that a user can successfully submit a feature
    request by providing category, title and description.

    Test Steps:
    1. Click on Request a Feature.
    2. Click on Category dropdown and choose Accounts.
    3. Enter Title as test.
    4. Enter Description as test.
    5. Click on Submit button.
    6. Click on Back button.

    Expected Result:
    Feature request is submitted successfully.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_008",
        title="Request a Feature Functionality",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Request a Feature",
        user_activity_page.click_request_a_feature
    )

    executor.step(
        "Click on Category dropdown and choose Accounts",
        user_activity_page.select_request_category
    )

    executor.step(
        "Enter Title as test",
        lambda: user_activity_page.enter_request_title("test")
    )

    executor.step(
        "Enter Description as test",
        lambda: user_activity_page.enter_request_description("test")
    )

    executor.step(
        "Click on Submit button",
        user_activity_page.click_request_submit
    )

    executor.step(
        "Click on Back button",
        user_activity_page.click_request_back_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result


def test_TC_USERACTIVITY_009_find_friends(driver):
    """
    Test Case ID: TC_USERACTIVITY_009
    Title: Find Friends Functionality

    Objective:
    To verify that a user can successfully find friends by
    syncing contacts, following and supporting all, and undoing.

    Test Steps:
    1. Click on Find Friends.
    2. Click on Sync button.
    3. Click on Follow and Support All.
    4. Click on Undo.

    Expected Result:
    Find friends functionality works as expected.
    """

    test_result = TestResult(
        test_id="TC_USERACTIVITY_009",
        title="Find Friends Functionality",
        page_name="userActivity_page"
    )

    user_activity_page = UserActivityPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Find Friends",
        user_activity_page.click_find_friends
    )

    executor.step(
        "Click on Sync button",
        user_activity_page.click_sync
    )

    executor.step(
        "Click on Follow and Support All",
        user_activity_page.click_follow_and_support_all
    )

    executor.step(
        "Click on Undo",
        user_activity_page.click_undo
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result