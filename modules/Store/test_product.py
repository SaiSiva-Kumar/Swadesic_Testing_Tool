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

    # executor.step(
    #     "Click on Next button",
    #     product_page.click_next
    # )

    executor.step(
        "Enter about business",
        lambda: product_page.enter_about_business("test_store1")
    )

    executor.step(
        "Enter website link",
        lambda: product_page.enter_website_link("https://teststore1.com")
    )

    # executor.step(
    #     "Click on Next button",
    #     product_page.click_next
    # )

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

def test_TC_STORE_002_store_verification(driver):
    """
    Test Case ID: TC_STORE_002
    Title: Store Verification

    Objective:
    To verify that a user can successfully complete the store
    verification process by providing all required details
    including contact information, store location, and PAN details.

    Test Steps:
    1. Click on Finish Setup and Start Sharing button.
    2. Click on Review Trust Center.
    3. Click on Phone input and provide 9999999999.
    4. Click on Email input and provide test9@gmail.com.
    5. Click on Save button.
    6. Click on Its online only tick box.
    7. Click on Area of store operations input and provide test123.
    8. Click on Select City dropdown and select Adilabad.
    9. Click on Pincode input and provide 524004.
    10. Click on State dropdown and choose Andhra Pradesh.
    11. Click on City dropdown and choose Amlapuram.
    12. Click on Locality dropdown and provide test123.
    13. Click on Place dropdown and provide test123.
    14. Click on Pincode input and provide 524004.
    15. Click on Save button.
    16. Click on Individual tick box.
    17. Enter PAN as GJLPB8255A.
    18. Enter Name as mentioned on PAN as test123.
    19. Click on Date of Birth box.
    20. Click on Ok.
    21. Click on Add Signature.
    22. Click on Request Verification.

    Expected Result:
    Store verification request is submitted successfully.
    """

    test_result = TestResult(
        test_id="TC_STORE_002",
        title="Store Verification",
        page_name="store_page"
    )

    store_page = StorePage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Finish Setup and Start Sharing button",
        store_page.click_finish_setup
    )

    executor.step(
        "Click on Review Trust Center",
        store_page.click_review_trust_center
    )

    executor.step(
        "Click on Phone input and provide 9999999999",
        lambda: store_page.enter_phone("9999999999")
    )

    executor.step(
        "Click on Email input and provide test9@gmail.com",
        lambda: store_page.enter_email("test9@gmail.com")
    )

    executor.step(
        "Click on Save button",
        store_page.click_save
    )

    executor.step(
        "Click on Its online only tick box",
        store_page.click_online_only
    )

    executor.step(
        "Click on Area of store operations input and provide test123",
        lambda: store_page.enter_area_of_operations("test123")
    )

    executor.step(
        "Click on Select City dropdown and select Adilabad",
        store_page.select_city_adilabad
    )

    executor.step(
        "Click on Pincode input and provide 524004",
        lambda: store_page.enter_pincode_1("524004")
    )

    executor.step(
        "Click on State dropdown and choose Andhra Pradesh",
        store_page.select_state_andhra_pradesh
    )

    executor.step(
        "Click on City dropdown and choose Amlapuram",
        store_page.select_city_amlapuram
    )

    executor.step(
        "Click on Locality dropdown and provide test123",
        lambda: store_page.select_locality("test123")
    )

    executor.step(
        "Click on Place dropdown and provide test123",
        lambda: store_page.select_place("test123")
    )

    executor.step(
        "Click on Pincode input and provide 524004",
        lambda: store_page.enter_pincode_2("524004")
    )

    executor.step(
        "Click on Save button",
        store_page.click_save
    )

    executor.step(
        "Click on Individual tick box",
        store_page.click_individual_tickbox
    )

    executor.step(
        "Enter PAN as GJLPB8255A",
        lambda: store_page.enter_pan("GJLPB8255A")
    )

    executor.step(
        "Enter Name as mentioned on PAN as test123",
        lambda: store_page.enter_pan_name("test123")
    )

    executor.step(
        "Click on Date of Birth box",
        store_page.click_date_of_birth
    )

    executor.step(
        "Click on Ok",
        store_page.click_ok
    )

    executor.step(
        "Click on Add Signature",
        store_page.click_add_signature
    )

    executor.step(
        "Click on Request Verification",
        store_page.click_request_verification
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result