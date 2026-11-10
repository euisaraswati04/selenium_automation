# Test Plan – SauceDemo UI Automation

## 1. Objective
Validate the main e-commerce user journeys through browser UI automation using Selenium WebDriver and Pytest.

## 2. Scope
**In scope**
- Login with valid and invalid credentials
- Add a product to the cart
- Remove a product from the cart
- Checkout required-field validation
- Successful checkout

**Out of scope**
- Payment gateway integration
- Performance, load, security, and accessibility testing
- Real transactions or real customer data
- Mobile browser compatibility

## 3. Test environment
- Application: https://www.saucedemo.com/
- Browser: Google Chrome
- Automation: Selenium WebDriver 4
- Language: Python 3.10+
- Test runner: Pytest
- Account: public SauceDemo standard demo account

## 4. Entry criteria
- Demo application is reachable
- Python and dependencies are installed
- Chrome is installed
- Demo account is available

## 5. Exit criteria
- All planned test cases have been executed
- Actual results and evidence are recorded
- Failed tests are investigated and documented
- Known limitations are stated in the test summary

## 6. Risks
- Demo site downtime or UI changes can cause failures unrelated to the product behavior.
- Browser/driver compatibility may affect execution.
- Network latency can affect page loading; explicit waits are used to reduce timing-related flakiness.

## 7. Deliverables
- Automated test scripts
- Test case inventory
- Execution summary
- Screenshots for failures
- Defect reports for reproducible defects
