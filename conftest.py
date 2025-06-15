import pytest  # Import the pytest testing framework


# This hook is triggered when pytest is generating the test report for an individual test
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 'outcome' will store the test result (pass, fail, skip, etc.)
    outcome = yield  # Pause here and let pytest run the test

    # Fetch the result of the test execution (the outcome)
    rep = outcome.get_result()

    # Attach the test result as an attribute to the test item, dynamically naming it based on the phase (e.g., setup, call, teardown)
    # rep.when could be 'setup', 'call', or 'teardown' depending on the stage of the test
    setattr(item, "rep_" + rep.when, rep)

    # Return the test result so pytest can continue with its default behavior (e.g., logging, printing the result)
    return rep
