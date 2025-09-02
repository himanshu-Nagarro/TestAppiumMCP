#!/usr/bin/env python3
"""
Inditex Automation Runner

Simple script to run Inditex login automation with different options.
"""

import sys
import os
import argparse
from pathlib import Path

# Add tests directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests'))

try:
    from tests.inditex_login_enhanced import InditexLoginAutomationEnhanced
except ImportError:
    print("❌ Error: Could not import automation modules")
    print("Make sure you're running from the correct directory")
    sys.exit(1)


def run_basic_automation():
    """Run basic automation"""
    print("🔄 Running Basic Automation...")
    config_path = os.path.join("tests", "config.ini")
    
    automation = InditexLoginAutomationEnhanced(config_path)
    
    try:
        if automation.setup_driver():
            if automation.launch_app():
                success = automation.perform_login()
                return success
        return False
    finally:
        automation.cleanup()


def run_with_custom_credentials(email, password):
    """Run automation with custom credentials"""
    print(f"🔄 Running Automation with custom credentials...")
    config_path = os.path.join("tests", "config.ini")
    
    automation = InditexLoginAutomationEnhanced(config_path)
    
    try:
        if automation.setup_driver():
            if automation.launch_app():
                success = automation.perform_login(email=email, password=password)
                return success
        return False
    finally:
        automation.cleanup()


def run_tests():
    """Run pytest test suite"""
    print("🧪 Running Test Suite...")
    import subprocess
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_inditex_login.py", 
            "-v", 
            "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False


def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(
        description="Inditex Login Automation Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_automation.py                           # Run with config credentials
  python run_automation.py -e user@example.com -p password123  # Custom credentials
  python run_automation.py --test                    # Run test suite
  python run_automation.py --check                   # Check prerequisites
        """
    )
    
    parser.add_argument(
        "-e", "--email",
        help="Email address for login"
    )
    
    parser.add_argument(
        "-p", "--password",
        help="Password for login"
    )
    
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the pytest test suite"
    )
    
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check prerequisites and configuration"
    )
    
    args = parser.parse_args()
    
    # Check prerequisites
    if args.check:
        check_prerequisites()
        return
    
    # Run tests
    if args.test:
        success = run_tests()
        if success:
            print("✅ All tests passed!")
        else:
            print("❌ Some tests failed!")
        return
    
    # Run automation
    try:
        if args.email and args.password:
            success = run_with_custom_credentials(args.email, args.password)
        else:
            success = run_basic_automation()
        
        if success:
            print("✅ Automation completed successfully!")
        else:
            print("❌ Automation failed!")
            
    except KeyboardInterrupt:
        print("\n🛑 Automation interrupted by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def check_prerequisites():
    """Check if all prerequisites are met"""
    print("🔍 Checking Prerequisites...")
    
    issues = []
    
    # Check Python version
    if sys.version_info < (3, 7):
        issues.append("Python 3.7+ required")
    else:
        print("✅ Python version OK")
    
    # Check if config file exists
    config_path = os.path.join("tests", "config.ini")
    if not os.path.exists(config_path):
        issues.append("Configuration file missing: tests/config.ini")
    else:
        print("✅ Configuration file found")
    
    # Check if required modules can be imported
    try:
        import appium
        print("✅ Appium Python client available")
    except ImportError:
        issues.append("Appium Python client not installed (pip install Appium-Python-Client)")
    
    try:
        import selenium
        print("✅ Selenium available")
    except ImportError:
        issues.append("Selenium not installed (pip install selenium)")
    
    # Check if tests directory exists
    if not os.path.exists("tests"):
        issues.append("Tests directory not found")
    else:
        print("✅ Tests directory found")
    
    # Check if automation scripts exist
    required_files = [
        "tests/inditex_login_enhanced.py",
        "tests/test_inditex_login.py"
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} found")
        else:
            issues.append(f"Required file missing: {file_path}")
    
    # Summary
    if issues:
        print("\n❌ Issues found:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nPlease resolve these issues before running automation.")
    else:
        print("\n✅ All prerequisites met! You can run the automation.")


if __name__ == "__main__":
    main()
