#result_models.py
class StepResult:
    def __init__(self, step_number, description):
        self.step_number = step_number
        self.description = description
        self.status = None
        self.execution_time = 0
        self.error_message = None
        self.screenshot_path = None


class TestResult:
    def __init__(self, test_id, title, page_name):
        self.test_id = test_id
        self.title = title
        self.page_name = page_name
        self.overall_status = None
        self.execution_time = 0
        self.steps = []
