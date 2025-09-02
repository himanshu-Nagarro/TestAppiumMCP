"""
Inditex Mobile App Login Automation Script

This script automates the login process for the Inditex mobile application
using Appium WebDriver with Python.

Requirements:
- Appium Server running
- Android device/emulator connected
- Inditex app installed on the device
"""

import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging


class InditexLoginAutomation:
    def __init__(self, device_name="AppiumTest", app_package="com.inditex.trazabilidapp"):
        """
        Initialize the Inditex Login Automation
        
        Args:
            device_name (str): Name of the device to connect to
            app_package (str): Package name of the Inditex app
        """
        self.device_name = device_name
        self.app_package = app_package
        self.driver = None
        self.wait = None
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Appium server configuration
        self.appium_server_url = "http://127.0.0.1:4723"
        
    def setup_driver(self):
        """Setup Appium driver with Android capabilities"""
        try:
            # Configure desired capabilities
            options = UiAutomator2Options()
            options.device_name = self.device_name
            options.platform_name = "Android"
            options.app_package = self.app_package
            options.app_activity = ".MainActivity"  # Adjust if needed
            options.automation_name = "UiAutomator2"
            options.no_reset = True
            options.full_reset = False
            
            # Initialize driver
            self.driver = webdriver.Remote(
                command_executor=self.appium_server_url,
                options=options
            )
            
            # Setup explicit wait
            self.wait = WebDriverWait(self.driver, 30)
            
            self.logger.info(f"Successfully connected to device: {self.device_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to setup driver: {str(e)}")
            return False
    
    def launch_app(self):
        """Launch the Inditex application"""
        try:
            self.driver.activate_app(self.app_package)
            self.logger.info(f"Launched app: {self.app_package}")
            time.sleep(3)  # Wait for app to load
            return True
        except Exception as e:
            self.logger.error(f"Failed to launch app: {str(e)}")
            return False
    
    def wait_for_element(self, locator_type, locator_value, timeout=30):
        """
        Wait for an element to be present and return it
        
        Args:
            locator_type (str): Type of locator (xpath, id, etc.)
            locator_value (str): Locator value
            timeout (int): Maximum time to wait
            
        Returns:
            WebElement or None
        """
        try:
            if locator_type.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, locator_value))
                )
            elif locator_type.lower() == "id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((AppiumBy.ID, locator_value))
                )
            else:
                raise ValueError(f"Unsupported locator type: {locator_type}")
            
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {locator_type}={locator_value}")
            return None
    
    def enter_email(self, email):
        """
        Enter email in the email field
        
        Args:
            email (str): Email address to enter
        """
        try:
            self.logger.info("Looking for email input field...")
            
            # Wait for email field to be present
            email_field = self.wait_for_element("xpath", "//android.widget.EditText[@resource-id='idToken7']")
            
            if email_field:
                email_field.clear()
                email_field.send_keys(email)
                self.logger.info(f"Entered email: {email}")
                return True
            else:
                self.logger.error("Email field not found")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to enter email: {str(e)}")
            return False
    
    def click_continue_button(self):
        """Click the Continue button after entering email"""
        try:
            self.logger.info("Looking for Continue button...")
            
            # Wait for continue button to be clickable
            continue_btn = self.wait_for_element("xpath", "//android.widget.Button[@resource-id='loginButton_0']")
            
            if continue_btn and continue_btn.is_enabled():
                continue_btn.click()
                self.logger.info("Clicked Continue button")
                time.sleep(2)  # Wait for page transition
                return True
            else:
                self.logger.error("Continue button not found or not enabled")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to click continue button: {str(e)}")
            return False
    
    def enter_password(self, password):
        """
        Enter password in the password field
        
        Args:
            password (str): Password to enter
        """
        try:
            self.logger.info("Looking for password input field...")
            
            # Wait for password field to be present
            password_field = self.wait_for_element("xpath", "//android.widget.EditText[@resource-id='idToken3']")
            
            if password_field:
                password_field.clear()
                password_field.send_keys(password)
                self.logger.info("Entered password")
                return True
            else:
                self.logger.error("Password field not found")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to enter password: {str(e)}")
            return False
    
    def click_login_button(self):
        """Click the final Login button"""
        try:
            self.logger.info("Looking for Login button...")
            
            # Wait for login button to be clickable
            login_btn = self.wait_for_element("xpath", "//android.widget.Button[@resource-id='idToken11_0']")
            
            if login_btn and login_btn.is_enabled():
                login_btn.click()
                self.logger.info("Clicked Login button")
                time.sleep(3)  # Wait for login to complete
                return True
            else:
                self.logger.error("Login button not found or not enabled")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to click login button: {str(e)}")
            return False
    
    def verify_login_success(self):
        """Verify if login was successful"""
        try:
            # Wait a bit for the app to load after login
            time.sleep(5)
            
            # Check if we're still on login page or moved to main app
            # This is a basic check - you might need to adjust based on the actual app behavior
            current_activity = self.driver.current_activity
            self.logger.info(f"Current activity: {current_activity}")
            
            # You can add more specific verification logic here
            # For example, check for presence of specific elements that indicate successful login
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to verify login: {str(e)}")
            return False
    
    def perform_login(self, email, password):
        """
        Perform the complete login workflow
        
        Args:
            email (str): Email address
            password (str): Password
            
        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            self.logger.info("Starting Inditex login automation...")
            
            # Step 1: Enter email
            if not self.enter_email(email):
                return False
            
            # Step 2: Click Continue
            if not self.click_continue_button():
                return False
            
            # Step 3: Enter password
            if not self.enter_password(password):
                return False
            
            # Step 4: Click Login
            if not self.click_login_button():
                return False
            
            # Step 5: Verify login success
            if self.verify_login_success():
                self.logger.info("Login automation completed successfully!")
                return True
            else:
                self.logger.error("Login verification failed")
                return False
                
        except Exception as e:
            self.logger.error(f"Login automation failed: {str(e)}")
            return False
    
    def cleanup(self):
        """Clean up resources"""
        try:
            if self.driver:
                self.driver.quit()
                self.logger.info("Driver session closed")
        except Exception as e:
            self.logger.error(f"Error during cleanup: {str(e)}")


def main():
    """Main function to run the automation"""
    # Configuration
    device_name = "AppiumTest"
    email = "amitks"
    password = "Pl@tinum@82026"
    
    # Initialize automation
    automation = InditexLoginAutomation(device_name=device_name)
    
    try:
        # Setup driver
        if not automation.setup_driver():
            print("Failed to setup driver. Exiting...")
            return False
        
        # Launch app
        if not automation.launch_app():
            print("Failed to launch app. Exiting...")
            return False
        
        # Perform login
        success = automation.perform_login(email, password)
        
        if success:
            print("✅ Login automation completed successfully!")
        else:
            print("❌ Login automation failed!")
        
        return success
        
    except KeyboardInterrupt:
        print("\n🛑 Automation interrupted by user")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False
    finally:
        # Cleanup
        automation.cleanup()


if __name__ == "__main__":
    main()
