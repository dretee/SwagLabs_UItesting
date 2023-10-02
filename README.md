---

# Swag Labs Automation Test Project

**Introduction**

This repository contains the automation testing plan and bug reports for Swag Labs, a web application for shopping.

## Automation Testing Plan

### Objectives
The objectives of automation testing for the Swag Labs are as follows:

| Objective                        | Description                                                                                            |
|----------------------------------|------------------------------------------------------------------------------------------------------- |
| Ensure Application Stability     | Guarantee the Swag Labs application's stability and reliability.                                       |
| Improve Testing Speed            | Increase testing speed and reduce manual effort through automation.                                    |
| Reduce Testing Costs             | Lower overall testing costs by optimizing resources and minimizing human involvement.                  |
| Validate Cart to Checkout Process| Ensure items added to the cart proceed smoothly to the checkout stage without errors.                  |
| Verify Price Accuracy            | Validate that displayed prices are correct, eliminating discrepancies from manual checks.              |
| Validate Element Functionality   | Confirm proper functionality of all user interface elements, preventing duplicates.                    |
| Check Link Functionality         | Verify that all application links function correctly, ensuring seamless navigation.                    |
| Validate Login Sequence via DDT  | Ensure the login sequence functions properly, utilizing Data-Driven Testing (DDT) techniques for reliability. |

### Scope

The scope of automation testing includes:
- Functional testing of all modules.
- Regression testing of all modules.

### Automation Tool

The automation tool selected for this project is Selenium with the Python programming language.

### Test Environment

The test environment for automation testing is as follows:
- **Browser:** Google Chrome Version 117.0.5938.92
- **Programming Language:** Python
- **Integrated Development Environment:** PyCharm

### Test Cases

The following test cases will be automated:

1. **Login to the application (DDT)**
2. **Cost checks (total vs displayed) / Checkout process / Zip code test**
3. **Add and remove products from the cart**
4. **Link checks**

### Test Data

The following test data will be used for automation testing:
- Usernames and passwords
- User information (First name, Last name, Zip/Postal Code)

### Test Execution

The automation testing process will follow these steps:

1. Determine the test scenarios suitable for automation.
2. Create automation scripts corresponding to the selected test scenarios.
3. Run the automation scripts to perform the tests.
4. Evaluate the outcomes of the automated tests.
5. Document and monitor any identified defects, if they occur.

## Bug Reports

### Bug Report 1:

**Summary:** The Checkout system can proceed without any order being made by the user.

**Steps to Reproduce:**
1. Login as standard user (username: standard_user, password: secret_sauce).
2. Click on the cart icon.
3. Click on continue.
4. Fill in the first name, last name, and zip code.
5. Click on the continue button.
6. Click on the finish button.

**Expected Result:** The process of checking out should not proceed without an item in the cart.

**Actual Result:** The checkout process is completed without any payment being made.

**Severity:** Low
**Priority:** Medium
**Reported By:** Anthony
**Environment:** Chrome Version 117.0.5938.92

[Evidence/Attachment](https://docs.google.com/presentation/d/1kFfrL-p3gYj_ef8qfKLBuMmP8NW5bDJx_ZprUgw4Ne4/edit?usp=sharing)

### Bug Report 2:

**Summary:** Inability for the user to specify the quantity of items needed.

**Steps to Reproduce:**
1. Login as a standard user (username: standard_user, password: secret_sauce).
2. Click on the Sauce Labs Backpack add to cart button.
3. No option for quantity increment is displayed on the present frame.
4. Click on the cart looking for the prompt or provision for increment, but still nothing.

**Expected Result:** Provision for the quantity increment. A plus(+) and minus(-) sign for this purpose.

**Actual Result:** No such display on any frame.

**Severity:** High
**Priority:** High
**Reported By:** Anthony
**Environment:** Chrome Version 117.0.5938.92

[Evidence/Attachment](https://docs.google.com/presentation/d/1SYRqoJTtWXX3Z0adKcrBgkRU9DJiNu00MuffFHK4YD4/edit?usp=sharing)

### Bug Report 3:

**Summary:** The Zip code input box allows letters instead of only numbers.

**Steps to Reproduce:**
1. Login as a standard user (username: standard_user, password: secret_sauce).
2. Click on the cart icon.
3. Click on continue.
4. Fill in the first name (Uyah), last name (Anthony), and zip code (qwerfgh).
5. Click on the continue button.

**Expected Result:** Error message when letters are inputted by the user.

**Actual Result:** Proceeds to the next stage of checking out.

**Severity:** Medium
**Priority:** High
**Reported By:** Anthony
**Environment:** Chrome Version 117.0.5938.92

[Evidence/Attachment](https://docs.google.com/presentation/d/1d_ty_IjdalEUuvjq5MTP_lGobPTtGuiLeV4aR7LQe9w/edit?usp=sharing)


