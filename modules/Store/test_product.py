from pages.store_page import StorePage
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def test_TC_PRODUCT_001_create_store(driver):
    """
    Test Case ID: TC_PRODUCT_001
    Title: Create a Store

    Objective:
    To verify that a user can successfully create a store by filling
    in all required details including store name, business category,
    business type, profile photo, about, website link, and store handle.

    Test Steps:
    1. Click on Profile button.
    2. Click on Create Store button.
    3. Click on Start Now.
    4. Click on Get Started.
    5. Enter store name as test_store1.
    6. Select business category and add test_store1.
    7. Select business type and add test_store1.
    8. Choose profile photo.
    9. Click on Next button.
    10. Enter about business as test_store1.
    11. Enter website link as https://teststore1.com.
    12. Click on Next button.
    13. Enter store handle as test_store1.
    14. Verify store handle is available.
    15. Click on Create The Store button.

    Expected Result:
    Store is created successfully.
    """

    test_result = TestResult(
        test_id="TC_PRODUCT_001",
        title="Create a Store",
        page_name="store_page"
    )

    product_page = StorePage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Profile button",
        product_page.click_profile_button
    )

    executor.step(
        "Click on Create Store button",
        product_page.click_create_store
    )

    executor.step(
        "Click on Start Now",
        product_page.click_start_now
    )

    executor.step(
        "Click on Get Started",
        product_page.click_get_started
    )

    executor.step(
        "Enter store name",
        lambda: product_page.enter_store_name("test_store1")
    )

    executor.step(
        "Select business category and add test_store1",
        lambda: product_page.select_business_category("test_store1")
    )

    executor.step(
        "Select business type and add test_store1",
        lambda: product_page.select_business_type("test_store1")
    )

    executor.step(
        "Choose profile photo",
        product_page.choose_profile_photo
    )

    executor.step(
        "Click on Next button",
        product_page.click_next
    )

    executor.step(
        "Enter about business",
        lambda: product_page.enter_about_business("test_store1")
    )

    executor.step(
        "Enter website link",
        lambda: product_page.enter_website_link("https://teststore1.com")
    )

    executor.step(
        "Click on Next button",
        product_page.click_next
    )

    executor.step(
        "Enter store handle",
        lambda: product_page.enter_store_handle("test_store1")
    )

    executor.step(
        "Verify store handle is available",
        product_page.is_store_handle_available
    )

    executor.step(
        "Click on Create The Store button",
        product_page.click_create_the_store
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result