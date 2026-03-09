from pages.store_settings_page import StoreSettingsPage
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def test_TC_STORE_SETTINGS_001_update_store_profile(driver):
    """
    Test Case ID: TC_STORE_SETTINGS_001
    Title: Update Store Profile

    Objective:
    To verify that a store owner can successfully update their
    store profile including store name, handle, business category,
    business type, and about business.

    Test Steps:
    1. Click on Settings icon.
    2. Click on Store Profile.
    3. Enter Store Name as test update 1.
    4. Enter Store Handle as test_update_2.
    5. Select Business Category as Art and Craft Supplies.
    6. Select Business Type as Distributors.
    7. Enter About Business as test update 3.
    8. Click on Save button.

    Expected Result:
    Store profile is updated successfully.
    """

    test_result = TestResult(
        test_id="TC_STORE_SETTINGS_001",
        title="Update Store Profile",
        page_name="store_settings_page"
    )

    store_settings_page = StoreSettingsPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Settings icon",
        store_settings_page.click_settings_icon
    )

    executor.step(
        "Click on Store Profile",
        store_settings_page.click_store_profile
    )

    executor.step(
        "Enter Store Name as test update 1",
        lambda: store_settings_page.enter_store_name("test update 1")
    )

    executor.step(
        "Enter Store Handle as test_update_2",
        lambda: store_settings_page.enter_store_handle("test_update_2")
    )

    executor.step(
        "Select Business Category as Art and Craft Supplies",
        store_settings_page.select_business_category
    )

    executor.step(
        "Select Business Type as Distributors",
        store_settings_page.select_business_type
    )

    executor.step(
        "Enter About Business as test update 3",
        lambda: store_settings_page.enter_about_business("test update 3")
    )

    executor.step(
        "Click on Save button",
        store_settings_page.click_save
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_STORE_SETTINGS_002_update_fulfillment_settings(driver):
    """
    Test Case ID: TC_STORE_SETTINGS_002
    Title: Update Fulfillment Settings

    Objective:
    To verify that a store owner can successfully update the
    fulfillment settings including preparation time, delivery
    time and default logistics partner.

    Test Steps:
    1. Click on Settings icon.
    2. Click on Fulfillment Settings.
    3. Click on Time to prepare and ship package dropdown and choose 2 days.
    4. Click on Time to deliver the order dropdown and choose 10 days.
    5. Click on Default Logistics Partner and choose ABF Freight.
    6. Click on Save Changes.

    Expected Result:
    Fulfillment settings are updated successfully.
    """

    test_result = TestResult(
        test_id="TC_STORE_SETTINGS_002",
        title="Update Fulfillment Settings",
        page_name="store_settings_page"
    )

    store_settings_page = StoreSettingsPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Settings icon",
        store_settings_page.click_settings_icon
    )

    executor.step(
        "Click on Fulfillment Settings",
        store_settings_page.click_fulfillment_settings
    )

    executor.step(
        "Click on Time to prepare and ship package dropdown and choose 2 days",
        store_settings_page.select_prepare_ship_time
    )

    executor.step(
        "Click on Time to deliver the order dropdown and choose 10 days",
        store_settings_page.select_delivery_time
    )

    executor.step(
        "Click on Default Logistics Partner and choose ABF Freight",
        store_settings_page.select_logistics_partner
    )

    executor.step(
        "Click on Save Changes",
        store_settings_page.click_save_changes
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result


def test_TC_STORE_SETTINGS_003_update_return_and_refund_settings(driver):
    """
    Test Case ID: TC_STORE_SETTINGS_003
    Title: Update Return and Refund Settings

    Objective:
    To verify that a store owner can successfully update the
    return and refund settings including return period and
    return conditions.

    Test Steps:
    1. Click on Settings icon.
    2. Click on Return and Refund Settings.
    3. Click on Return Period dropdown and choose 4 days.
    4. Enter Return Conditions as test.
    5. Click on Save Changes.

    Expected Result:
    Return and refund settings are updated successfully.
    """

    test_result = TestResult(
        test_id="TC_STORE_SETTINGS_003",
        title="Update Return and Refund Settings",
        page_name="store_settings_page"
    )

    store_settings_page = StoreSettingsPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Settings icon",
        store_settings_page.click_settings_icon
    )

    executor.step(
        "Click on Return and Refund Settings",
        store_settings_page.click_return_and_refund_settings
    )

    executor.step(
        "Click on Return Period dropdown and choose 4 days",
        store_settings_page.select_return_period
    )

    executor.step(
        "Enter Return Conditions as test",
        lambda: store_settings_page.enter_return_conditions("test")
    )

    executor.step(
        "Click on Save Changes",
        store_settings_page.click_save_changes
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result