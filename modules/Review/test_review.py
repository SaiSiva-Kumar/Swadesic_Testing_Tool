from pages.review_page import ReviewPage, get_update_name
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def test_TC_REVIEW_001_create_review_page(driver):
    """
    Test Case ID: TC_REVIEW_001
    Title: Create a Review Page

    Objective:
    To verify that a user can successfully create a review page
    by providing all required details including page name,
    business category, and store link.

    Test Steps:
    1. Click on User Profile.
    2. Click on Create Review Page button.
    3. Click on Get Started.
    4. Click on Images tab and choose image.
    5. Enter Name of review page as test page.
    6. Click on Business Category dropdown and add test page.
    7. Enter Store link as https://example.com.
    8. Click on Create your review page button.

    Expected Result:
    Review page is created successfully.
    """

    test_result = TestResult(
        test_id="TC_REVIEW_001",
        title="Create a Review Page",
        page_name="review_page"
    )

    review_page = ReviewPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on User Profile",
        review_page.click_profile_button
    )

    executor.step(
        "Click on Create Review Page button",
        review_page.click_create_review_page
    )

    executor.step(
        "Click on Get Started",
        review_page.click_get_started
    )

    executor.step(
        "Click on Images tab and choose image",
        review_page.choose_image
    )

    executor.step(
        "Enter Name of review page as test page",
        lambda: review_page.enter_page_name("test page")
    )

    executor.step(
        "Click on Business Category dropdown and add test page",
        lambda: review_page.select_business_category("test page")
    )

    executor.step(
        "Enter Store link as https://example.com",
        lambda: review_page.enter_store_link("https://example.com")
    )

    executor.step(
        "Click on Create your review page button",
        review_page.click_create_review_page_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_REVIEW_002_update_review_page(driver):
    """
    Test Case ID: TC_REVIEW_002
    Title: Update a Review Page

    Objective:
    To verify that a user can successfully update a review page
    by changing the page name.

    Test Steps:
    1. Click on Switch Profile tab.
    2. Choose required Review Page tab.
    3. Click on Settings button.
    4. Click on Edit Page.
    5. Enter updated name in Name of your review page input field.
    6. Click on Update the review page button.

    Expected Result:
    Review page is updated successfully with the new name.
    """

    test_result = TestResult(
        test_id="TC_REVIEW_002",
        title="Update a Review Page",
        page_name="review_page"
    )

    review_page = ReviewPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Switch Profile tab",
        review_page.click_switch_profile_tab
    )

    executor.step(
        "Choose required Review Page tab",
        review_page.click_review_page_tab
    )

    executor.step(
        "Click on Settings button",
        review_page.click_settings_button
    )

    executor.step(
        "Click on Edit Page",
        review_page.click_edit_page
    )

    executor.step(
        "Enter updated name in review page input field",
        lambda: review_page.enter_update_page_name(get_update_name())
    )

    executor.step(
        "Click on Update the review page button",
        review_page.click_update_review_page_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result