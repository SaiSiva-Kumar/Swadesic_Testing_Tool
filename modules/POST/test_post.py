from pages.post_page import PostPage
from reporting.result_models import TestResult
from reporting.step_executor import StepExecutor


def test_TC_POST_001_create_post_with_media_and_tag(driver):
    """
    Test Case ID: TC_POST_001
    Title: Create a Post with Photos, Video, Tag and Caption

    Objective:
    To verify that a user can successfully create a post by adding
    photos, a video, tagging a member, writing a caption, and
    submitting the post.

    Test Steps:
    1. Click on Create button.
    2. Click on Add Photos and select photos.
    3. Click on Add Video and select video.
    4. Click on Tag Stores, Products and Members.
    5. Search and select tag with input krishna.
    6. Enter post caption.
    7. Click on Post button.
    8. Verify post is submitted successfully.

    Expected Result:
    Post is created and user is navigated away from the post creation screen.
    """

    test_result = TestResult(
        test_id="TC_POST_001",
        title="Create a Post with Photos, Video, Tag and Caption",
        page_name="post_page"
    )

    post_page = PostPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Create button",
        post_page.click_create_button
    )

    executor.step(
        "Click on Add Photos and select photos",
        post_page.click_add_photos
    )

    executor.step(
        "Click on Add Video and select video",
        post_page.click_add_video
    )

    executor.step(
        "Click on Tag Stores, Products and Members",
        post_page.click_tag_stores
    )

    executor.step(
        "Search and select tag with input krishna",
        lambda: post_page.search_and_select_tag("krishna")
    )

    executor.step(
        "Enter post caption",
        lambda: post_page.enter_post_caption("test post")
    )

    executor.step(
        "Click on Post button",
        post_page.click_post_button
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result


def test_TC_POST_002_delete_post(driver):
    """
    Test Case ID: TC_POST_002
    Title: Delete a Post

    Objective:
    To verify that a user can successfully delete a post from
    their profile.

    Test Steps:
    1. Click on Profile button.
    2. Click on User Posts.
    3. Click on Three Dots Menu.
    4. Click on Delete button.
    5. Confirm Delete.

    Expected Result:
    Post is deleted successfully.
    """

    test_result = TestResult(
        test_id="TC_POST_002",
        title="Delete a Post",
        page_name="post_page"
    )

    post_page = PostPage(driver)
    executor = StepExecutor(driver, test_result)

    executor.step(
        "Click on Profile button",
        post_page.click_profile_button
    )

    executor.step(
        "Click on User Posts",
        post_page.click_user_posts
    )

    executor.step(
        "Click on Three Dots Menu",
        post_page.click_three_dots_menu
    )

    executor.step(
        "Click on Delete button",
        post_page.click_delete_button
    )

    executor.step(
        "Confirm Delete",
        post_page.confirm_delete
    )

    if executor.failed:
        test_result.overall_status = "FAIL"
    else:
        test_result.overall_status = "PASS"

    test_result.execution_time = round(
        sum(step.execution_time for step in test_result.steps), 2
    )

    return test_result