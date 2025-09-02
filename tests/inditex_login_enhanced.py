"""
Enhanced Inditex Mobile App Login Automation Script with Configuration Support

This script provides a more robust automation framework for the Inditex mobile application
using Appium WebDriver with Python and configuration file support.
"""

import os
import time
import configparser
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging


class InditexLoginConfig:
    """Configuration manager for Inditex automation"""
    
    def __init__(self, config_file_path):
        self.config = configparser.ConfigParser()
        self.config_file_path = config_file_path
        self.load_config()
    
    def load_config(self):
        """Load configuration from file"""
        if os.path.exists(self.config_file_path):
            self.config.read(self.config_file_path)
        else:
            raise FileNotFoundError(f"Configuration file not found: {self.config_file_path}")
    
    def get(self, section, key, fallback=None):
        """Get configuration value"""
        return self.config.get(section, key, fallback=fallback)
    
    def getint(self, section, key, fallback=None):
        """Get integer configuration value"""
        return self.config.getint(section, key, fallback=fallback)


class InditexLoginAutomationEnhanced:
    def __init__(self, config_file_path="config.ini"):
        """
        Initialize the Enhanced Inditex Login Automation
        
        Args:
            config_file_path (str): Path to configuration file
        """
        # Load configuration
        self.config = InditexLoginConfig(config_file_path)
        
        # Initialize variables
        self.driver = None
        self.wait = None
        
        # Setup logging
        self.setup_logging()
        
    def setup_logging(self):
        """Setup logging configuration"""
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler('inditex_automation.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_driver(self):
        """Setup Appium driver with configuration"""
        try:
            # Get configuration values
            device_name = self.config.get('DEVICE', 'device_name')
            platform_name = self.config.get('DEVICE', 'platform_name')
            app_package = self.config.get('APP', 'app_package')
            app_activity = self.config.get('APP', 'app_activity')
            server_url = self.config.get('SERVER', 'appium_server_url')
            
            # Configure desired capabilities
            options = UiAutomator2Options()
            options.device_name = device_name
            options.platform_name = platform_name
            options.app_package = app_package
            options.app_activity = app_activity
            options.automation_name = "UiAutomator2"
            options.no_reset = True
            options.full_reset = False
            
            # Initialize driver
            self.driver = webdriver.Remote(
                command_executor=server_url,
                options=options
            )
            
            # Setup waits
            implicit_wait = self.config.getint('SERVER', 'implicit_wait', 10)
            explicit_wait = self.config.getint('SERVER', 'explicit_wait', 30)
            
            self.driver.implicitly_wait(implicit_wait)
            self.wait = WebDriverWait(self.driver, explicit_wait)
            
            self.logger.info(f"Successfully connected to device: {device_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to setup driver: {str(e)}")
            return False
    
    def launch_app(self):
        """Launch the Inditex application"""
        try:
            app_package = self.config.get('APP', 'app_package')
            app_launch_wait = self.config.getint('TIMEOUTS', 'app_launch_wait', 3)
            
            self.driver.activate_app(app_package)
            self.logger.info(f"Launched app: {app_package}")
            time.sleep(app_launch_wait)
            return True
        except Exception as e:
            self.logger.error(f"Failed to launch app: {str(e)}")
            return False
    
    def wait_for_element(self, locator_type, locator_value, timeout=None):
        """
        Wait for an element to be present and return it
        
        Args:
            locator_type (str): Type of locator (xpath, id, etc.)
            locator_value (str): Locator value
            timeout (int): Maximum time to wait (uses config default if None)
            
        Returns:
            WebElement or None
        """
        if timeout is None:
            timeout = self.config.getint('SERVER', 'explicit_wait', 30)
            
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
    
    def wait_for_clickable_element(self, locator_type, locator_value, timeout=None):
        """
        Wait for an element to be clickable and return it
        
        Args:
            locator_type (str): Type of locator (xpath, id, etc.)
            locator_value (str): Locator value
            timeout (int): Maximum time to wait (uses config default if None)
            
        Returns:
            WebElement or None
        """
        if timeout is None:
            timeout = self.config.getint('SERVER', 'explicit_wait', 30)
            
        try:
            if locator_type.lower() == "xpath":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((AppiumBy.XPATH, locator_value))
                )
            elif locator_type.lower() == "id":
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((AppiumBy.ID, locator_value))
                )
            else:
                raise ValueError(f"Unsupported locator type: {locator_type}")
            
            return element
        except TimeoutException:
            self.logger.error(f"Clickable element not found: {locator_type}={locator_value}")
            return None
    
    def enter_email(self, email=None):
        """
        Enter email in the email field
        
        Args:
            email (str): Email address to enter (uses config if None)
        """
        if email is None:
            email = self.config.get('CREDENTIALS', 'email')
            
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
            continue_btn = self.wait_for_clickable_element("xpath", "//android.widget.Button[@resource-id='loginButton_0']")
            
            if continue_btn:
                continue_btn.click()
                self.logger.info("Clicked Continue button")
                
                page_transition_wait = self.config.getint('TIMEOUTS', 'page_transition_wait', 2)
                time.sleep(page_transition_wait)
                return True
            else:
                self.logger.error("Continue button not found or not clickable")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to click continue button: {str(e)}")
            return False
    
    def enter_password(self, password=None):
        """
        Enter password in the password field
        
        Args:
            password (str): Password to enter (uses config if None)
        """
        if password is None:
            password = self.config.get('CREDENTIALS', 'password')
            
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
            login_btn = self.wait_for_clickable_element("xpath", "//android.widget.Button[@resource-id='idToken11_0']")
            
            if login_btn:
                login_btn.click()
                self.logger.info("Clicked Login button")
                
                login_completion_wait = self.config.getint('TIMEOUTS', 'login_completion_wait', 5)
                time.sleep(login_completion_wait)
                return True
            else:
                self.logger.error("Login button not found or not clickable")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to click login button: {str(e)}")
            return False
    
    def verify_login_success(self):
        """Verify if login was successful"""
        try:
            # Wait a bit for the app to load after login
            time.sleep(3)
            
            # Get current activity
            current_activity = self.driver.current_activity
            self.logger.info(f"Current activity after login: {current_activity}")
            # Wait for page to load before taking screenshot
            page_load_wait = self.config.getint('TIMEOUTS', 'page_load_wait', 5)
            time.sleep(page_load_wait)
            # Take a screenshot for verification
            screenshot_path = f"login_result_{int(time.time())}.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved: {screenshot_path}")
            
            # Check if we're no longer on the login page
            # This can be enhanced based on specific success indicators
            try:
                # Try to find login elements - if they're not present, login likely succeeded
                login_elements = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='idToken7']")
                if len(login_elements) == 0:
                    self.logger.info("Login elements not found - likely successful login")
                    return True
                else:
                    self.logger.warning("Still on login page - login may have failed")
                    return False
            except:
                # If we can't find login elements, assume success
                return True
            
        except Exception as e:
            self.logger.error(f"Failed to verify login: {str(e)}")
            return False
    
    def perform_login(self, email=None, password=None):
        """
        Perform the complete login workflow
        
        Args:
            email (str): Email address (uses config if None)
            password (str): Password (uses config if None)
            
        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            self.logger.info("🚀 Starting Inditex login automation...")
            
            # Step 1: Enter email
            self.logger.info("📧 Step 1: Entering email...")
            if not self.enter_email(email):
                return False
            
            # Step 2: Click Continue
            self.logger.info("➡️ Step 2: Clicking Continue...")
            if not self.click_continue_button():
                return False
            
            # Step 3: Enter password
            self.logger.info("🔒 Step 3: Entering password...")
            if not self.enter_password(password):
                return False
            
            # Step 4: Click Login
            self.logger.info("🔑 Step 4: Clicking Login...")
            if not self.click_login_button():
                return False
            
            # Step 5: Verify login success
            self.logger.info("✅ Step 5: Verifying login...")
            if self.verify_login_success():
                self.logger.info("🎉 Login automation completed successfully!")
                return True
            else:
                self.logger.error("❌ Login verification failed")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Login automation failed: {str(e)}")
            return False
    
    def get_page_source(self):
        """Get current page source for debugging"""
        try:
            return self.driver.page_source
        except:
            return None
    
    def cleanup(self):
        """Clean up resources"""
        try:
            if self.driver:
                self.driver.quit()
                self.logger.info("Driver session closed")
        except Exception as e:
            self.logger.error(f"Error during cleanup: {str(e)}")


def main():
    """Main function to run the enhanced automation"""
    config_path = os.path.join(os.path.dirname(__file__), "config.ini")
    
    print("🔄 Initializing Inditex Login Automation...")
    automation = InditexLoginAutomationEnhanced(config_path)
    
    try:
        # Setup driver
        print("🔧 Setting up Appium driver...")
        if not automation.setup_driver():
            print("❌ Failed to setup driver. Exiting...")
            return False
        
        # Launch app
        print("📱 Launching Inditex app...")
        if not automation.launch_app():
            print("❌ Failed to launch app. Exiting...")
            return False
        
        # Perform login
        print("🔐 Starting login process...")
        success = automation.perform_login()
        
        if success:
            print("✅ Login automation completed successfully!")
            print("📸 Check the screenshot for verification")
        else:
            print("❌ Login automation failed!")
            print("📋 Check the log file 'inditex_automation.log' for details")
        
        return success
        
    except KeyboardInterrupt:
        print("\n🛑 Automation interrupted by user")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False
    finally:
        # Cleanup
        print("🧹 Cleaning up...")
        automation.cleanup()


if __name__ == "__main__":
    main()
