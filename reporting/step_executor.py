#step_executor.py
import time
import os
from reporting.result_models import StepResult


class StepExecutor:

    def __init__(self, driver, test_result):
        self.driver = driver
        self.test_result = test_result
        self.step_counter = 0
        self.failed = False

    def step(self, description, action):

        if self.failed:
            return

        self.step_counter += 1
        step_result = StepResult(self.step_counter, description)

        start_time = time.time()

        try:
            # Execute the Appium action
            action()
            step_result.status = "PASS"

        except Exception as e:
            step_result.status = "FAIL"
            error_str = str(e).strip()
            lines = [line.strip() for line in error_str.split("\n") if line.strip()]
            meaningful = next(
                (line for line in lines if "Error" in line or "Exception" in line),
                lines[0] if lines else "Unknown error"
            )
            step_result.error_message = meaningful
            self.failed = True
            try:
                os.makedirs("screenshots", exist_ok=True)
                screenshot_name = f"{self.test_result.test_id}_step{self.step_counter}.png"
                screenshot_path = os.path.join("screenshots", screenshot_name)

                self.driver.save_screenshot(screenshot_path)
                step_result.screenshot_path = screenshot_path

            except Exception:
                step_result.screenshot_path = None

        end_time = time.time()
        step_result.execution_time = round(end_time - start_time, 2)

        self.test_result.steps.append(step_result)
