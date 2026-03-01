from pages.user_page import UserPage, get_next_email
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def test_TC_USER_001_onboard_user_with_email(driver):
    """
    Test Case ID: TC_USER_001
    Title: Onboard User with Email

    Objective:
    To verify that a new user can successfully complete the onboarding
    flow using email and OTP authentication, providing all required
    profile details including gender, city, role, and profile picture.

    Test Steps:
    1. Click on Profile button.
    2. Click on See All Options.
    3. Click on Continue with Email and OTP.
    4. Enter email address as test1@gmail.com.
    5. Click on Send OTP button.
    6. Wait for manual OTP entry.
    7. Click on Verify OTP.
    8. Click on Yes, I am.
    9. Select Male under Gender.
    10. Click on City dropdown and provide Nellore.
    11. Click on Continue.
    12. Click on As a Buyer tick box.
    13. Upload profile picture and choose photo.
    14. Click on Join the Future of Shopping button.

    Expected Result:
    User is successfully onboarded and navigated to the home screen.
    """

    test_result = TestResult(
        test_id="TC_USER_001",
        title="Onboard User with Email",
        page_name="userOnboarding_page"
    )

    user_page = UserPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Profile button",
        user_page.click_profile_button
    )

    executor.step(
        "Click on See All Options",
        user_page.click_see_all_options
    )

    executor.step(
        "Click on Continue with Email and OTP",
        user_page.click_continue_with_email
    )

    executor.step(
        "Enter email address",
        lambda: user_page.enter_email(get_next_email())
    )

    executor.step(
        "Click on Send OTP button",
        user_page.click_send_otp
    )

    executor.step(
        "Wait for manual OTP entry",
        user_page.wait_for_otp
    )

    executor.step(
        "Click on Verify OTP",
        user_page.click_verify_otp
    )

    executor.step(
        "Click on Yes, I am",
        user_page.click_yes_i_am
    )

    executor.step(
        "Select Male under Gender",
        user_page.select_gender_male
    )

    executor.step(
        "Click on City dropdown and provide Nellore",
        lambda: user_page.select_city("Nellore")
    )

    executor.step(
        "Click on Continue",
        user_page.click_continue
    )

    executor.step(
        "Click on As a Buyer tick box",
        user_page.click_as_a_buyer
    )

    executor.step(
        "Upload profile picture and choose photo",
        user_page.upload_profile_picture
    )

    executor.step(
        "Click on Join the Future of Shopping button",
        user_page.click_join
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_USER_002_update_profile(driver):
    """
    Test Case ID: TC_USER_002
    Title: Update User Profile

    Objective:
    To verify that a user can successfully update their profile
    by changing the profile picture and updating all profile fields.

    Test Steps:
    1. Click on Profile button.
    2. Click on Edit Profile.
    3. Click on Change Profile Picture and choose photo.
    4. Enter First Name as test.
    5. Enter Last Name as test.
    6. Enter Display Name as test.
    7. Enter Username as test.
    8. Click on Save button.

    Expected Result:
    Profile is updated successfully.
    """

    test_result = TestResult(
        test_id="TC_USER_002",
        title="Update User Profile",
        page_name="user_edit_page"
    )

    user_page = UserPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Profile button",
        user_page.click_profile_button_post_onboard
    )

    executor.step(
        "Click on Edit Profile",
        user_page.click_edit_profile
    )

    executor.step(
        "Click on Change Profile Picture and choose photo",
        user_page.change_profile_picture
    )

    executor.step(
        "Enter First Name as test",
        lambda: user_page.enter_first_name("test")
    )

    executor.step(
        "Enter Last Name as test",
        lambda: user_page.enter_last_name("test")
    )

    executor.step(
        "Enter Display Name as test",
        lambda: user_page.enter_display_name("test")
    )

    executor.step(
        "Enter Username as test",
        lambda: user_page.enter_username("test")
    )

    executor.step(
        "Click on Save button",
        user_page.click_save
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result