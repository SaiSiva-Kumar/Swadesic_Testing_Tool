from pages.product_page import ProductPage
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def test_TC_PURCHASE_001_purchase_product_via_phonepe(driver):
    """
    Test Case ID: TC_PURCHASE_001
    Title: Purchase Product via PhonePe UPI

    Objective:
    To verify that a user can successfully navigate to a product
    and initiate a purchase using PhonePe UPI as the payment method.

    Test Steps:
    1. Click on Search button.
    2. Click on Products tab.
    3. Click on Product.
    4. Click on Buy Now.
    5. Click on Continue.
    6. Click on Select Delivery Address and Payment.
    7. Click on Secure Checkout.
    8. Click on PhonePe.
    9. Click on Go Back.

    Expected Result:
    User is able to navigate through the purchase flow and
    initiate payment via PhonePe UPI successfully.
    """

    test_result = TestResult(
        test_id="TC_PURCHASE_001",
        title="Purchase Product via PhonePe UPI",
        page_name="product_purchase_page"
    )

    purchase_page = ProductPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Search button",
        purchase_page.click_search_button
    )

    executor.step(
        "Click on Products tab",
        purchase_page.click_products_tab
    )

    executor.step(
        "Click on Product",
        purchase_page.click_product
    )

    executor.step(
        "Click on Buy Now",
        purchase_page.click_buy_now
    )

    executor.step(
        "Click on Continue",
        purchase_page.click_continue
    )

    executor.step(
        "Click on Select Delivery Address and Payment",
        purchase_page.click_select_delivery_address
    )

    executor.step(
        "Click on Secure Checkout",
        purchase_page.click_secure_checkout
    )

    executor.step(
        "Click on PhonePe",
        purchase_page.click_phonepe
    )

    executor.step(
        "Click on Go Back",
        purchase_page.click_go_back
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_PURCHASE_002_cancel_product(driver):
    """
    Test Case ID: TC_PURCHASE_002
    Title: Cancel a Product Order

    Objective:
    To verify that a user can successfully cancel a placed order
    by providing a cancellation reason and proceeding to cancel.

    Test Steps:
    1. Click on Profile button.
    2. Click on My Orders.
    3. Click on Product Information.
    4. Click on Waiting for Confirmation dropdown.
    5. Click on Cancel button.
    6. Click on Cancel button again.
    7. Enter reason to cancel as test.
    8. Click on Proceed to Cancel button.

    Expected Result:
    Order is cancelled successfully.
    """

    test_result = TestResult(
        test_id="TC_PURCHASE_002",
        title="Cancel a Product Order",
        page_name="cancel_product_page"
    )

    product_page = ProductPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Profile button",
        product_page.click_profile_button
    )

    executor.step(
        "Click on My Orders",
        product_page.click_my_orders
    )

    executor.step(
        "Click on Product Information",
        product_page.click_order_item
    )

    executor.step(
        "Click on Waiting for Confirmation dropdown",
        product_page.click_waiting_for_confirmation
    )

    executor.step(
        "Click on Cancel button",
        product_page.click_cancel
    )

    executor.step(
        "Click on Cancel button again",
        product_page.click_cancel
    )

    executor.step(
        "Enter reason to cancel",
        lambda: product_page.enter_cancel_reason("test")
    )

    executor.step(
        "Click on Proceed to Cancel button",
        product_page.click_proceed_to_cancel
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result