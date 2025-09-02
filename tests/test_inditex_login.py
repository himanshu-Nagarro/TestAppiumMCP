"""
Pytest-based test suite for Inditex Login Automation

This module provides pytest test cases for the Inditex mobile application
login automation.
"""

import pytest
import os
import time
from inditex_login_enhanced import InditexLoginAutomationEnhanced


class TestInditexLogin:
    """Test class for Inditex login automation"""
    
    @pytest.fixture(scope="class")
    def automation(self):
        """Fixture to setup automation instance"""
        config_path = os.path.join(os.path.dirname(__file__), "config.ini")
        automation = InditexLoginAutomationEnhanced(config_path)
        
        # Setup driver
        assert automation.setup_driver(), "Failed to setup Appium driver"
        
        yield automation
        
        # Cleanup
        automation.cleanup()
    
    @pytest.fixture(scope="class")
    def launched_app(self, automation):
        """Fixture to launch the app"""
        assert automation.launch_app(), "Failed to launch app"
        return automation
    
    def test_driver_setup(self, automation):
        """Test that the Appium driver is properly set up"""
        assert automation.driver is not None, "Driver should be initialized"
        assert automation.wait is not None, "WebDriverWait should be initialized"
    
    def test_app_launch(self, launched_app):
        """Test that the app launches successfully"""
        # Check if the app is running
        current_activity = launched_app.driver.current_activity
        assert current_activity is not None, "App should be running"
    
    def test_email_entry(self, launched_app):
        """Test email entry functionality"""
        # Test with default email from config
        result = launched_app.enter_email()
        assert result, "Email entry should succeed"
    
    def test_continue_button_click(self, launched_app):
        """Test continue button click after email entry"""
        # First enter email
        launched_app.enter_email()
        
        # Then test continue button
        result = launched_app.click_continue_button()
        assert result, "Continue button click should succeed"
    
    def test_password_entry(self, launched_app):
        """Test password entry functionality"""
        # Navigate to password screen first
        launched_app.enter_email()
        launched_app.click_continue_button()
        
        # Test password entry
        result = launched_app.enter_password()
        assert result, "Password entry should succeed"
    
    def test_login_button_click(self, launched_app):
        """Test final login button click"""
        # Navigate to login screen
        launched_app.enter_email()
        launched_app.click_continue_button()
        launched_app.enter_password()
        
        # Test login button
        result = launched_app.click_login_button()
        assert result, "Login button click should succeed"
    
    def test_complete_login_flow(self, launched_app):
        """Test the complete login workflow"""
        result = launched_app.perform_login()
        assert result, "Complete login flow should succeed"
    
    def test_login_with_custom_credentials(self, automation):
        """Test login with custom credentials"""
        # Launch app
        assert automation.launch_app(), "App should launch"
        
        # Test with specific credentials
        result = automation.perform_login(
            email="amitks", 
            password="Pl@tinum@82026"
        )
        assert result, "Login with custom credentials should succeed"
    
    @pytest.mark.parametrize("invalid_email", [
        "",  # Empty email
        "invalid",  # Invalid format
        "test@",  # Incomplete email
    ])
    def test_invalid_email_handling(self, automation, invalid_email):
        """Test handling of invalid email inputs"""
        # Launch app
        automation.launch_app()
        
        # Try with invalid email
        result = automation.enter_email(invalid_email)
        
        # The function should still succeed in entering the text
        # But continue button may not be enabled
        assert result, "Email entry function should succeed even with invalid email"
    
    def test_page_source_capture(self, launched_app):
        """Test page source capture functionality"""
        page_source = launched_app.get_page_source()
        assert page_source is not None, "Page source should be captured"
        assert len(page_source) > 0, "Page source should not be empty"


class TestInditexLoginConfiguration:
    """Test class for configuration handling"""
    
    def test_config_file_exists(self):
        """Test that configuration file exists"""
        config_path = os.path.join(os.path.dirname(__file__), "config.ini")
        assert os.path.exists(config_path), "Configuration file should exist"
    
    def test_config_loading(self):
        """Test configuration loading"""
        config_path = os.path.join(os.path.dirname(__file__), "config.ini")
        automation = InditexLoginAutomationEnhanced(config_path)
        
        # Test that config values can be retrieved
        device_name = automation.config.get('DEVICE', 'device_name')
        app_package = automation.config.get('APP', 'app_package')
        
        assert device_name is not None, "Device name should be configured"
        assert app_package is not None, "App package should be configured"


# Utility functions for manual testing
def run_single_test():
    """Run a single login test for manual verification"""
    config_path = os.path.join(os.path.dirname(__file__), "config.ini")
    automation = InditexLoginAutomationEnhanced(config_path)
    
    try:
        print("Setting up automation...")
        if automation.setup_driver():
            print("Launching app...")
            if automation.launch_app():
                print("Performing login...")
                success = automation.perform_login()
                return success
        return False
    finally:
        automation.cleanup()


if __name__ == "__main__":
    # Run a single test if executed directly
    success = run_single_test()
    print(f"Test result: {'PASSED' if success else 'FAILED'}")
