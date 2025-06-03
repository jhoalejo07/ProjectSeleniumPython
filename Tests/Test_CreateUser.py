import pytest
import random  # Used to select random characters
import string  # Contains pre-defined character sets (like ascii_letters)
import allure
from ProjectSeleniumPython.utils.Functions import Functions
from ProjectSeleniumPython.utils.ExcelFunctions import Funexcel
from ProjectSeleniumPython.Pages.CreateCustomer import CreateUsr
from allure_commons.types import AttachmentType



# Time delay used throughout the test for waits
t = .02


@pytest.fixture(scope='function')
def setup_new_customer_screen():
    """
    Fixture to set up the browser session and required page objects before each test.
    - Opens the Chrome browser and navigates to the Magento new customer creation page.
    - Initializes helper classes for browser interaction, Excel file access, and page object model.
    - Provides all relevant objects and paths to the test via a context dictionary.
    """
    f = Functions(r"C:\SeleniumDrivers\chromedriver.exe")
    f.openBrowser("https://magento.softwaretestingboard.com/customer/account/create/", t)
    fe = Funexcel()
    path_excel = "D://Projects//Projects//ProjectSeleniumPython//User_Data.xlsx"
    newCustomer = CreateUsr(f, t)

    print("Enter into /customer/account/create/")
    yield {
        "functions": f,
        "newCustomer": newCustomer,
        "fe": fe,
        "path_excel": path_excel,
        "t": t
    }
    print("log off from /customer/account/create/")
    f.teardown_function()


@pytest.fixture(scope='function')
def log_on_failure(setup_new_customer_screen, request):
    """
    Fixture that captures a screenshot with Allure reporting in case the test fails.
    This runs after each test using this fixture.
    """
    yield
    item = request.node
    if item.rep_call.failed:
        f = setup_new_customer_screen["functions"]
        # Attach screenshot to Allure report upon failure
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="Error",
            attachment_type=AttachmentType.PNG
        )


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
def test_negative_user_exist(setup_new_customer_screen):
    """
    Test to validate the negative scenario where the user already exists in the Magento system.
    Steps:
    - Fills the registration form with user data already present in the system (fetched from Excel).
    - Submits the form.
    - Asserts that the appropriate error message is displayed.
    - Logs the result back to Excel.
    """
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]
    fe = ctx["fe"]
    path_excel = ctx["path_excel"]
    f = ctx["functions"]

    try:
        # Fill out the form with existing user data from Excel
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 2, 2))
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 2, 3))
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 2, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 2, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 2, 6))

        # Submit the form
        newCustomer.PressButtonCreate()

        # Capture the error message displayed for existing user
        text = f.return_element(
            "xpath",
            "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']"
            "[contains(.,'There is already an account with this email address. If you are sure that it is "
            "your email address, click here to get your password and access your account.')]",
            t
        ).text

        # Attach screenshot to Allure on successful detection of error message
        allure.attach(f.driver.get_screenshot_as_png(), name="UserExist", attachment_type=AttachmentType.PNG)

    except AttributeError as ex:
        # Handle error if the element wasn't found or user wasn't created
        fe.writeData(path_excel, "magento_new_users", 2, 7, "Failed - That user hasn't been created")
        assert False, "That user hasn't been created"

    # Assert that the correct error message appears
    assert text == (
        "There is already an account with this email address. If you are sure that it is your email "
        "address, click here to get your password and access your account."
    )

    # Log result to Excel
    fe.writeData(path_excel, "magento_new_users", 2, 7, "Pass - That user exists")


@pytest.mark.positive
@pytest.mark.usefixtures("log_on_failure")
def test_positive_create_user(setup_new_customer_screen):
    """
    Positive test case that verifies the successful creation of a new user in the Magento site.

    This test reads valid user data from an Excel file, fills out the registration form,
    submits it, then checks if the "My Account" confirmation text appears on the page,
    indicating a successful registration. Results are logged back into the Excel file.

    Args:
        setup_new_customer_screen (fixture): Provides the initialized objects for testing.
    """

    # Unpack the context objects returned by the fixture
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]  # Interface to fill form fields
    fe = ctx["fe"]  # Excel utility to read/write test data
    path_excel = ctx["path_excel"]  # Excel file path
    f = ctx["functions"]  # Helper functions for Selenium and element interaction

    try:
        # Fill in the registration form fields using data from Excel (row 3)
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 3, 2))  # First Name
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 3, 3))  # Last Name
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 3, 4))  # Email
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 3, 5))  # Password
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 3, 6))  # Confirm Password

        # Submit the form by pressing the Create button
        newCustomer.PressButtonCreate()

        # After submission, retrieve the text element that confirms account creation
        text = f.return_element("xpath", "//span[@class='base'][contains(.,'My Account')]", t).text

        # Attach a screenshot to the Allure report for visual verification
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="CreatingUser",
            attachment_type=AttachmentType.PNG
        )

    except AttributeError as ex:
        # If elements are missing or cannot be accessed, write failure to Excel
        fe.writeData(path_excel, "magento_new_users", 3, 7, "Failed - It isn't possible to create a user")

        # Explicitly fail the test with a descriptive message
        assert False, "It isn't possible to create a user"

    # Assert that the confirmation text is exactly "My Account" indicating success
    assert text == "My Account", "User creation confirmation text not found."

    # Log success result back into the Excel sheet
    fe.writeData(path_excel, "magento_new_users", 3, 7, "Pass - User Created")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
def test_negative_First_and_last_name_long(setup_new_customer_screen):
    """
    Negative test case that verifies the system properly rejects user registration
    when the first and last names exceed the allowed length (too long input).

    This test generates overly long first and last names (302 characters),
    attempts to submit the form with these invalid inputs, and then verifies
    that the correct error message is displayed on the page.

    Args:
        setup_new_customer_screen (fixture): Provides necessary page objects and utilities.
    """

    # Retrieve objects and utilities from fixture context
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]  # Interface to interact with form fields
    fe = ctx["fe"]  # Excel utility for test data
    path_excel = ctx["path_excel"]  # Path to Excel data file
    f = ctx["functions"]  # Helper functions for Selenium

    try:
        # Generate invalid overly long first name (302 chars) and enter it
        firstname = random_char(302)
        newCustomer.EnterFirstName(firstname)

        # Generate invalid overly long last name (302 chars) and enter it
        lastname = random_char(302)
        newCustomer.EnterLastName(lastname)

        # Enter valid email, password, and confirm password from Excel data (row 4)
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 4, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 4, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 4, 6))

        # Submit the registration form
        newCustomer.PressButtonCreate()

        # Capture the error message shown on the page for invalid names
        errorText = f.return_element(
            "xpath",
            "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']"
            "[contains(.,'First Name is not valid!\nLast Name is not valid!')]",
            t
        ).text

        # Attach a screenshot to the Allure report for visual verification
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="fnameLnameLong",
            attachment_type=AttachmentType.PNG
        )

    except AttributeError as ex:
        # If page elements are missing or inaccessible, log failure in Excel and fail the test
        fe.writeData(path_excel, "magento_new_users", 4, 7, "Failed - First and lastname aren't too long")
        assert False, "First or lastname aren't too long"

    # Assert the error message matches the expected text exactly
    assert errorText == "First Name is not valid! Last Name is not valid!", "The First and last name are valid"

    # Write pass result back to Excel file
    fe.writeData(path_excel, "magento_new_users", 4, 7, "Pass - First and last Name are not valid")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
def test_negative_First_name_long(setup_new_customer_screen):
    """
    Negative test case to verify that the Magento site correctly rejects user
    registration when the first name exceeds the allowed length.

    This test uses a 301-character long string as a first name, which is assumed
    to violate the maximum length restriction. It expects the form to raise a
    validation error, and checks that the correct error message is displayed.

    Args:
        setup_new_customer_screen (fixture): Provides the page objects and test data handlers.
    """

    # Extract context objects provided by the fixture
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]  # Interface to interact with registration form fields
    fe = ctx["fe"]  # Excel data reader/writer
    path_excel = ctx["path_excel"]  # File path to test data Excel file
    f = ctx["functions"]  # Helper methods for Selenium-based interactions

    try:
        # Generate a 301-character long string to simulate an invalid first name input
        firstname = random_char(301)
        newCustomer.EnterFirstName(firstname)

        # Provide valid values for the remaining fields from Excel (row 5)
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 5, 3))
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 5, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 5, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 5, 6))

        # Click on the Create Account button
        newCustomer.PressButtonCreate()

        # Attempt to locate and capture the validation error for "First Name"
        errorText = f.return_element(
            "xpath",
            "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'First Name is not valid!')]",
            t
        ).text

        # Capture a screenshot and attach to the Allure report for traceability
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="fnameLong",
            attachment_type=AttachmentType.PNG
        )

    except AttributeError as ex:
        # Log failure in Excel if the test fails due to unexpected reasons (e.g., missing elements)
        fe.writeData(path_excel, "magento_new_users", 5, 7, "Failed - First isn't too long")
        assert False, "First isn't too long"

    # Validate the actual error message on the page
    assert errorText == "First Name is not valid!", "The First name is valid"

    # Log success in the Excel spreadsheet if validation error is correctly displayed
    fe.writeData(path_excel, "magento_new_users", 5, 7, "Pass - First Name is not valid!")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
def test_negative_Last_name_long(setup_new_customer_screen):
    """
    Negative test case to verify Magento's validation logic when the user tries to register
    with a last name longer than the accepted character limit (e.g., 301 characters).

    Steps:
    1. Load valid values from Excel for first name, email, and passwords.
    2. Generate an excessively long last name (301 characters).
    3. Attempt to register.
    4. Capture and verify the expected validation error.
    5. Log result in Excel and attach screenshot to Allure report.
    """

    # Unpack test dependencies from the fixture context
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]
    fe = ctx["fe"]
    path_excel = ctx["path_excel"]
    f = ctx["functions"]

    try:
        # Generate a last name longer than allowed (301 characters)
        lastname = random_char(301)

        # Read valid input values for other required fields from the Excel sheet (row 6)
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 6, 2))
        newCustomer.EnterLastName(lastname)
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 6, 4))
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 6, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 6, 6))

        # Submit the registration form
        newCustomer.PressButtonCreate()

        # Search for the expected validation error regarding the last name
        errorText = f.return_element(
            "xpath",
            "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)'][contains(.,'Last Name is not valid!')]",
            t
        ).text

        # Attach screenshot to Allure report for documentation
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="LnameLong",
            attachment_type=AttachmentType.PNG
        )

    except AttributeError as ex:
        # Log and fail the test if the expected validation fails to trigger
        fe.writeData(path_excel, "magento_new_users", 6, 7, "Failed - Lastname isn't too long")
        assert False, "Lastname isn't too long"

    # Verify that the error text matches the expected output
    assert errorText == "Last Name is not valid!", "The last name is valid"

    # Log the test result as successful in Excel
    fe.writeData(path_excel, "magento_new_users", 6, 7, "Pass - Last Name is not valid!!")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
def test_negative_incorrect_format_email(setup_new_customer_screen):
    """
    Negative test case to verify that the registration form displays a proper validation
    error when the user inputs an email address with an incorrect format.

    Steps:
    1. Read user details from Excel, including an invalid email format.
    2. Submit the form.
    3. Confirm that the correct email validation message appears.
    4. Attach screenshot and log results accordingly.
    """

    # Retrieve the test context
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]
    fe = ctx["fe"]
    path_excel = ctx["path_excel"]
    f = ctx["functions"]

    try:
        # Read all valid input fields from Excel except for an intentionally incorrect email
        newCustomer.EnterFirstName(fe.readData(path_excel, "magento_new_users", 7, 2))
        newCustomer.EnterLastName(fe.readData(path_excel, "magento_new_users", 7, 3))
        newCustomer.EnterEmail(fe.readData(path_excel, "magento_new_users", 7, 4))  # Invalid email format
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 7, 5))
        newCustomer.ConfirmPassw(fe.readData(path_excel, "magento_new_users", 7, 6))

        # Submit the registration form
        newCustomer.PressButtonCreate()

        # Capture the email validation error message
        errorText = f.return_element(
            "xpath",
            "//div[@for='email_address'][contains(@id,'address-error')][contains(.,"
            "'Please enter a valid email address (Ex: johndoe@domain.com).')]",
            t
        ).text

        # Save screenshot to Allure report for traceability
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="incorrect_format_email",
            attachment_type=AttachmentType.PNG
        )

    except AttributeError as ex:
        # Log failure if the email format was wrongly accepted
        fe.writeData(path_excel, "magento_new_users", 7, 7, "Failed - It doesn't look like an invalid email")
        assert False, "It doesn't look like an invalid email"

    # Validate that the correct error message was shown
    assert errorText == "Please enter a valid email address (Ex: johndoe@domain.com).", "IT IS A VALID EMAIL"

    # Mark test as passed in Excel if validation worked
    fe.writeData(path_excel, "magento_new_users", 7, 7, "Pass - email is not valid!!")


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
def test_negative_password_Strength(setup_new_customer_screen):
    """
    Negative test case to validate that the Magento registration form correctly identifies
    a weak password and displays the appropriate password strength label ("No Password" or "Weak").

    Steps:
    1. Read a weak password from the Excel sheet (row 8).
    2. Enter only the password in the password field.
    3. Capture the strength meter label.
    4. Confirm that it reads either "No Password" or "Weak".
    5. Log result in Excel and attach a screenshot to the Allure report.
    """

    # Extract all required objects from the test context
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]
    fe = ctx["fe"]
    path_excel = ctx["path_excel"]
    f = ctx["functions"]

    try:
        # Step 1: Enter the weak password (from Excel row 8, column 5)
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 8, 5))

        # Step 2: Retrieve the displayed strength text ("Weak", "Strong", etc.)
        errorText = f.return_element("xpath", "//*[@id='password-strength-meter-label']", t).text

        # Step 3: Attach screenshot of the password strength label to Allure
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="weak_pass_Strength",
            attachment_type=AttachmentType.PNG
        )

        # Step 4: Check whether the strength meter correctly flags weak passwords
        if errorText == "No Password" or errorText == "Weak":
            fe.writeData(path_excel, "magento_new_users", 8, 7, "Pass - Not accurate Password!")
            assert True, "Not accurate Password"
        else:
            fe.writeData(path_excel, "magento_new_users", 8, 7, "Failed - Accurate Password!")
            assert False, "Accurate Password was not expected"

    except AttributeError as ex:
        # Handle case where the password field or strength label is missing
        assert False, "textbox is not found"


@pytest.mark.positive
@pytest.mark.usefixtures("log_on_failure")
def test_positive_password_Strength(setup_new_customer_screen):
    """
    Positive test case to ensure Magento correctly evaluates and displays the strength of a secure password.

    Steps:
    1. Read a strong password from the Excel sheet (row 9).
    2. Enter it in the password field.
    3. Capture the password strength label.
    4. Validate it reads "Strong" or "Very Strong".
    5. Log results and attach screenshots for traceability.
    """

    # Unpack page objects and helpers from fixture context
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]
    fe = ctx["fe"]
    path_excel = ctx["path_excel"]
    f = ctx["functions"]

    try:
        # Step 1: Enter a strong password from Excel row 9, column 5
        newCustomer.EnterPassw(fe.readData(path_excel, "magento_new_users", 9, 5))

        # Step 2: Retrieve the strength label value
        errorText = f.return_element("xpath", "//*[@id='password-strength-meter-label']", t).text

        # Step 3: Attach screenshot for Allure report
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="strong_pass_Strength",
            attachment_type=AttachmentType.PNG
        )

        # Step 4: Assert that the strength label reflects a secure password
        if errorText == "Strong" or errorText == "Very Strong":
            fe.writeData(path_excel, "magento_new_users", 9, 7, "Pass - Accurate Password!")
            assert True, "Not accurate Password"
        else:
            fe.writeData(path_excel, "magento_new_users", 9, 7, "Failed - Not accurate Password!")
            assert False, "Expected a strong password evaluation"

    except AttributeError as ex:
        # Error handling in case DOM elements are not located
        assert False, "textbox is not found"


@pytest.mark.negative
@pytest.mark.usefixtures("log_on_failure")
def test_negative_password_confirm_diff(setup_new_customer_screen):
    """
    Negative test case to verify that the Magento registration form shows a validation error
    when the 'Password' and 'Confirm Password' fields have different values.

    Steps:
    1. Load test data (row 10) from Excel: First name, Last name, Email, Password, Confirm Password.
    2. Fill the registration form fields using the loaded data.
    3. Submit the form.
    4. Capture and validate the error message about password mismatch.
    5. Write the test result to the Excel sheet.
    6. Attach a screenshot to the Allure report for evidence.

    Expected Outcome:
    - Magento should display the message: "Please enter the same value again."
      if the confirmation password does not match the main password.
    """

    # Extract shared context objects from the fixture
    ctx = setup_new_customer_screen
    newCustomer = ctx["newCustomer"]  # Page object to interact with form
    fe = ctx["fe"]  # Excel file utility
    path_excel = ctx["path_excel"]  # Path to Excel sheet
    f = ctx["functions"]  # Utility functions (e.g., finding elements)

    try:
        # Step 1: Read test data from row 10 of the Excel sheet
        first_name = fe.readData(path_excel, "magento_new_users", 10, 2)
        last_name = fe.readData(path_excel, "magento_new_users", 10, 3)
        email = fe.readData(path_excel, "magento_new_users", 10, 4)
        password = fe.readData(path_excel, "magento_new_users", 10, 5)
        confirm_password = fe.readData(path_excel, "magento_new_users", 10, 6)

        # Step 2: Fill in the registration form fields
        newCustomer.EnterFirstName(first_name)
        newCustomer.EnterLastName(last_name)
        newCustomer.EnterEmail(email)
        newCustomer.EnterPassw(password)
        newCustomer.ConfirmPassw(confirm_password)

        # Step 3: Submit the registration form
        newCustomer.PressButtonCreate()

        # Step 4: Attempt to locate the error message shown when passwords don't match
        errorText = f.return_element(
            "xpath",
            "//div[@for='password-confirmation'][contains(.,'Please enter the same value again.')]",
            t
        ).text

        # Step 5: Attach a screenshot to the Allure report
        allure.attach(
            f.driver.get_screenshot_as_png(),
            name="confirm_pass_diff",
            attachment_type=AttachmentType.PNG
        )

    except AttributeError as ex:
        # If the confirmation error is not shown, assume the system accepted both passwords
        fe.writeData(path_excel, "magento_new_users", 10, 7, "Failed - Password and confirm are the same")
        assert False, "Password and confirm are the same (mismatch error not triggered)"

    # Step 6: Final validation and logging result in Excel
    assert errorText == "Please enter the same value again.", "Password and confirm are the same (no error shown)"
    fe.writeData(path_excel, "magento_new_users", 10, 7, "Pass - Password and confirm are different")





def random_char(char_num):
    """
    Generate a random string containing alphabetic characters (both uppercase and lowercase).

    Parameters:
    ----------
    char_num : int
        The number of random characters to generate.

    Returns:
    -------
    str
        A string consisting of randomly selected alphabetic characters.

    """
    # Use list comprehension to select 'char_num' random characters
    # string.ascii_letters includes both lowercase (a-z) and uppercase (A-Z) letters
    # random.choice(string.ascii_letters) selects one random letter
    # ''.join(...) combines the list of characters into a single string
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

