#!/usr/bin/env python3
"""
Production Check Validation Test Script
This script automates the workflow for validating production check functionality in the INDITEX iTrace App.
"""

import os
import sys
import time
import logging
import configparser
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("inditex_automation.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class ProductionCheckTest:
    """Class for automating the Production Check validation flow in INDITEX iTrace app."""
    
    def __init__(self):
        """Initialize the test automation with configuration parameters."""
        # Read configuration
        config = configparser.ConfigParser()
        config.read('tests/config.ini')
        
        self.app_package = config.get('App', 'package', fallback='com.inditex.trazabilidapp')
        self.app_activity = config.get('App', 'activity', fallback='.MainActivity')
        self.device_name = config.get('Device', 'name', fallback='Pixel Tablet')
        self.platform_version = config.get('Device', 'platform_version', fallback='13')
        self.timeout = int(config.get('Settings', 'timeout', fallback='30'))
        self.audit_id = config.get('Test', 'audit_id', fallback='206697')
        
        # Set up the driver
        self.setup_driver()
        self.wait = WebDriverWait(self.driver, self.timeout)
        
    def setup_driver(self):
        """Configure and initialize the Appium WebDriver."""
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': self.platform_version,
            'deviceName': self.device_name,
            'appPackage': self.app_package,
            'appActivity': self.app_activity,
            'automationName': 'UiAutomator2',
            'newCommandTimeout': 600,
            'noReset': True
        }
        
        logger.info(f"Initializing driver with capabilities: {desired_caps}")
        self.driver = webdriver.Remote('http://localhost:4723', desired_caps)
        
    def login(self, username, password):
        """Log into the iTrace application."""
        logger.info("Logging in to the application...")
        
        try:
            # Wait for login screen to load
            self.wait.until(EC.presence_of_element_located((AppiumBy.ID, f"{self.app_package}:id/username")))
            
            # Enter username
            username_field = self.driver.find_element(AppiumBy.ID, f"{self.app_package}:id/username")
            username_field.clear()
            username_field.send_keys(username)
            
            # Enter password
            password_field = self.driver.find_element(AppiumBy.ID, f"{self.app_package}:id/password")
            password_field.clear()
            password_field.send_keys(password)
            
            # Click login button
            login_button = self.driver.find_element(AppiumBy.ID, f"{self.app_package}:id/loginButton")
            login_button.click()
            
            # Wait for the main screen to load
            self.wait_for_element_present("//android.widget.TextView[contains(@text, 'Audits')]", by=AppiumBy.XPATH)
            logger.info("Login successful")
            
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Login failed: {e}")
            raise
            
    def navigate_to_audits(self):
        """Navigate to the Audits screen."""
        logger.info("Navigating to Audits screen...")
        
        try:
            # Wait for and click on Audits menu option if needed
            audits_element = self.wait_for_element_present("//android.widget.TextView[contains(@text, 'Audits')]", by=AppiumBy.XPATH)
            audits_element.click()
            
            logger.info("Successfully navigated to Audits screen")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to navigate to Audits: {e}")
            raise
            
    def select_audit(self, audit_id):
        """Select an audit by its ID."""
        logger.info(f"Selecting audit #{audit_id}...")
        
        try:
            # Find and click on the specified audit
            audit_xpath = f"//android.widget.TextView[@text='{audit_id}']"
            audit_element = self.wait_for_element_present(audit_xpath, by=AppiumBy.XPATH)
            audit_element.click()
            
            # Wait for audit details to load
            time.sleep(2)
            logger.info(f"Successfully selected audit #{audit_id}")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to select audit #{audit_id}: {e}")
            raise
            
    def navigate_to_production_check(self):
        """Navigate to the Production Check screen."""
        logger.info("Navigating to Production Check...")
        
        try:
            # Find and click on the Production Check option
            production_check_xpath = "//android.widget.TextView[@text='PRODUCTION CHECK']"
            production_check = self.wait_for_element_present(production_check_xpath, by=AppiumBy.XPATH)
            production_check.click()
            
            # Wait for Production Check screen to load
            self.wait_for_element_present("//android.widget.TextView[@text='Production check']", by=AppiumBy.XPATH)
            logger.info("Successfully navigated to Production Check screen")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to navigate to Production Check: {e}")
            raise
            
    def select_first_item(self):
        """Select the first item in the Production Check list."""
        logger.info("Selecting the first item in the list...")
        
        try:
            # Find and click on the first item in the list
            item_xpath = "//android.view.ViewGroup[.//android.widget.TextView[contains(@resource-id, 'tvModel')]]"
            item = self.wait_for_element_present(item_xpath, by=AppiumBy.XPATH)
            item.click()
            
            # Wait for item details to load
            time.sleep(2)
            logger.info("Successfully selected first item")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to select first item: {e}")
            raise
            
    def navigate_to_confirm_units_tab(self):
        """Navigate to the CONFIRM UNITS tab."""
        logger.info("Navigating to CONFIRM UNITS tab...")
        
        try:
            # Find and click on the CONFIRM UNITS tab
            confirm_units_tab_xpath = "//android.view.View[.//android.widget.TextView[@text='CONFIRM UNITS']]"
            confirm_units_tab = self.wait_for_element_present(confirm_units_tab_xpath, by=AppiumBy.XPATH)
            confirm_units_tab.click()
            
            # Wait for the tab content to load
            time.sleep(2)
            logger.info("Successfully navigated to CONFIRM UNITS tab")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to navigate to CONFIRM UNITS tab: {e}")
            raise
    
    def enter_real_units(self, units_value):
        """Enter the real units value and confirm."""
        logger.info(f"Entering real units value: {units_value}...")
        
        try:
            # Find the edit text field
            edit_field_xpath = "//android.widget.EditText[@resource-id='com.inditex.trazabilidapp:id/edRealUnits']"
            edit_field = self.wait_for_element_present(edit_field_xpath, by=AppiumBy.XPATH)
            
            # Clear and enter the value
            edit_field.clear()
            edit_field.send_keys(str(units_value))
            
            # Click on the conclusion/check icon
            conclusion_icon_xpath = "//android.widget.ImageView[@resource-id='com.inditex.trazabilidapp:id/ivConclusion']"
            conclusion_icon = self.wait_for_element_present(conclusion_icon_xpath, by=AppiumBy.XPATH)
            conclusion_icon.click()
            
            # Wait for value to be processed
            time.sleep(2)
            logger.info(f"Successfully entered and confirmed real units: {units_value}")
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to enter real units: {e}")
            raise
    
    def verify_total_units(self):
        """Verify the total units value is displayed correctly."""
        logger.info("Verifying total units...")
        
        try:
            # Find the total assigned units element
            total_assigned_xpath = "//android.widget.TextView[@resource-id='com.inditex.trazabilidapp:id/tvBottomAssignedTotal']"
            total_assigned_element = self.wait_for_element_present(total_assigned_xpath, by=AppiumBy.XPATH)
            total_assigned = total_assigned_element.text
            
            # Find the total real units element
            total_real_xpath = "//android.widget.TextView[@resource-id='com.inditex.trazabilidapp:id/tvBottomRealTotal']"
            total_real_element = self.wait_for_element_present(total_real_xpath, by=AppiumBy.XPATH)
            total_real = total_real_element.text
            
            logger.info(f"Total assigned units: {total_assigned}")
            logger.info(f"Total real units: {total_real}")
            
            return {
                "total_assigned": total_assigned,
                "total_real": total_real
            }
        except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Failed to verify total units: {e}")
            raise
            
    def wait_for_element_present(self, locator, by=AppiumBy.ID, timeout=None):
        """
        Wait for an element to be present and return it.
        
        Args:
            locator: The locator to find the element
            by: The method to use (default: AppiumBy.ID)
            timeout: Custom timeout in seconds (default: None, uses self.timeout)
            
        Returns:
            The found WebElement
        """
        if timeout is None:
            timeout = self.timeout
            
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, locator)))
        
    def teardown(self):
        """Tear down the test and close the driver."""
        if hasattr(self, 'driver') and self.driver:
            logger.info("Closing driver...")
            self.driver.quit()

def run_test():
    """Run the production check validation test."""
    test = None
    try:
        # Initialize test
        test = ProductionCheckTest()
        
        # Read config for credentials
        config = configparser.ConfigParser()
        config.read('tests/config.ini')
        username = config.get('Credentials', 'username')
        password = config.get('Credentials', 'password')
        audit_id = test.audit_id
        
        # Execute test flow
        test.login(username, password)
        test.navigate_to_audits()
        test.select_audit(audit_id)
        test.navigate_to_production_check()
        test.select_first_item()
        test.navigate_to_confirm_units_tab()
        
        # Get initial total values for verification
        initial_totals = test.verify_total_units()
        logger.info(f"Initial totals: {initial_totals}")
        
        # Extract assigned units and use that value
        assigned_units = initial_totals["total_assigned"].replace(".", "")  # Remove thousand separator
        test.enter_real_units(assigned_units)
        
        # Verify updated total
        final_totals = test.verify_total_units()
        logger.info(f"Final totals: {final_totals}")
        
        # Simple validation
        if final_totals["total_real"] != "0":
            logger.info("Test PASSED: Real units updated successfully")
        else:
            logger.warning("Test FAILED: Real units not updated")
            
    except Exception as e:
        logger.error(f"Test failed with exception: {e}")
    finally:
        # Clean up resources
        if test:
            test.teardown()

if __name__ == "__main__":
    run_test()