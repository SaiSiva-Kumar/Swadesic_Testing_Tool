#report_generator.py
import os
from datetime import datetime


def generate_report(test_results):

    os.makedirs("reports", exist_ok=True)

    if not test_results:
        return

    page_name = test_results[0].page_name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{page_name}_{timestamp}.html"
    file_path = os.path.join("reports", file_name)

    total_tests = len(test_results)
    passed_tests = sum(1 for t in test_results if t.overall_status == "PASS")
    failed_tests = total_tests - passed_tests

    total_steps = sum(len(t.steps) for t in test_results)
    passed_steps = sum(
        1 for t in test_results for s in t.steps if s.status == "PASS"
    )
    failed_steps = sum(
        1 for t in test_results for s in t.steps if s.status == "FAIL"
    )
    skipped_steps = total_steps - passed_steps - failed_steps

    with open("reporting/templates/report_template.html", "r") as template_file:
        template = template_file.read()

    report_html = template.format(
        total_tests=total_tests,
        passed_tests=passed_tests,
        failed_tests=failed_tests,
        total_steps=total_steps,
        passed_steps=passed_steps,
        failed_steps=failed_steps,
        skipped_steps=skipped_steps,
        test_details=_build_test_details(test_results)
    )

    with open(file_path, "w", encoding="utf-8") as report_file:
        report_file.write(report_html)

    print(f"Report generated: {file_path}")


def _build_test_details(test_results):
    html = ""

    for test in test_results:
        html += f"""
        <h2>{test.test_id} - {test.title} - 
        <span class="{test.overall_status.lower()}">
        {test.overall_status}
        </span>
        (Time: {test.execution_time}s)</h2>

        <table>
            <tr>
                <th>Step</th>
                <th>Description</th>
                <th>Status</th>
                <th>Time (s)</th>
                <th>Error</th>
                <th>Screenshot</th>
            </tr>
        """

        for step in test.steps:
            screenshot_link = (
                f'<a href="../{step.screenshot_path}" target="_blank">View</a>'
                if step.screenshot_path else ""
            )

            html += f"""
            <tr>
                <td>{step.step_number}</td>
                <td>{step.description}</td>
                <td class="{step.status.lower()}">{step.status}</td>
                <td>{step.execution_time}</td>
                <td>{step.error_message or ""}</td>
                <td>{screenshot_link}</td>
            </tr>
            """

        html += "</table>"

    return html