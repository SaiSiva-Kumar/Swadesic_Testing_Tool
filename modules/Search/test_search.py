from pages.search_page import SearchPage
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def test_TC_SEARCH_001_search_user_and_follow(driver):
    """
    Test Case ID: TC_SEARCH_001
    Title: Search User and Follow

    Objective:
    To verify that a user can search for another user
    and successfully follow them from the search results.

    Test Steps:
    1. Click on Search button.
    2. Click on Search input field and provide name as krishna.
    3. Click on People tab.
    4. Click on User result.
    5. Click on Follow button.

    Expected Result:
    User is successfully followed.
    """

    test_result = TestResult(
        test_id="TC_SEARCH_001",
        title="Search User and Follow",
        page_name="search_page"
    )

    search_page = SearchPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Search button",
        search_page.click_search_button
    )

    executor.step(
        "Click on Search input field and provide name as krishna",
        lambda: search_page.enter_search_text("krishna")
    )

    executor.step(
        "Click on People tab",
        search_page.click_people_tab
    )

    executor.step(
        "Click on User result",
        search_page.click_user_result
    )

    executor.step(
        "Click on Follow button",
        search_page.click_follow_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_SEARCH_002_ask_question_on_product(driver):
    """
    Test Case ID: TC_SEARCH_002
    Title: Ask Question on Product

    Objective:
    To verify that a user can navigate to a product from the Products tab
    and successfully ask a question to the store.

    Test Steps:
    1. Click on Products tab.
    2. Click on required Product.
    3. Click on Product info.
    4. Click on Got a Question? Ask the Store button.
    5. Click on message input field and provide test2 input.
    6. Click on Send button.

    Expected Result:
    Question is successfully sent to the store.
    """

    test_result = TestResult(
        test_id="TC_SEARCH_002",
        title="Ask Question on Product",
        page_name="search_product_page"
    )

    search_page = SearchPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Products tab",
        search_page.click_products_tab
    )

    executor.step(
        "Click on required Product",
        search_page.click_product_item
    )

    executor.step(
        "Click on Product info",
        search_page.click_product_info
    )

    executor.step(
        "Click on Got a Question? Ask the Store button",
        search_page.click_ask_store_button
    )

    executor.step(
        "Click on message input field and provide test2 input",
        lambda: search_page.enter_message("test2")
    )

    executor.step(
        "Click on Send button",
        search_page.click_send_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_SEARCH_003_support_store(driver):
    """
    Test Case ID: TC_SEARCH_003
    Title: Support Store

    Objective:
    To verify that a user can navigate to a store from the Stores tab
    and successfully support the store.

    Test Steps:
    1. Click on Stores tab.
    2. Click on required Store.
    3. Click on Support button.

    Expected Result:
    Store is successfully supported.
    """

    test_result = TestResult(
        test_id="TC_SEARCH_003",
        title="Support Store",
        page_name="search_store_page"
    )

    search_page = SearchPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Stores tab",
        search_page.click_stores_tab
    )

    executor.step(
        "Click on required Store",
        search_page.click_store_item
    )

    executor.step(
        "Click on Support button",
        search_page.click_support_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result

def test_TC_SEARCH_004_comment_on_post(driver):
    """
    Test Case ID: TC_SEARCH_004
    Title: Comment on Post

    Objective:
    To verify that a user can navigate to Posts tab
    and successfully comment on a post.

    Test Steps:
    1. Click on Posts tab.
    2. Click on Comment button.
    3. Click on write your thoughts input field and provide test input.
    4. Click on Send button.

    Expected Result:
    Comment is successfully posted.
    """

    test_result = TestResult(
        test_id="TC_SEARCH_004",
        title="Comment on Post",
        page_name="search_post_page"
    )

    search_page = SearchPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Posts tab",
        search_page.click_posts_tab
    )

    executor.step(
        "Click on Comment button",
        search_page.click_comment_button
    )

    executor.step(
        "Click on write your thoughts input field and provide test input",
        lambda: search_page.enter_comment("test")
    )

    executor.step(
        "Click on Send button",
        search_page.click_comment_send_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result