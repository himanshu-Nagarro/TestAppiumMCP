# Inditex Mobile App Login Automation

This repository contains Python scripts for automating the login process of the Inditex mobile application using Appium WebDriver.

## 📁 Project Structure

```
tests/
├── inditex_login_automation.py      # Basic automation script
├── inditex_login_enhanced.py        # Enhanced version with configuration support
├── test_inditex_login.py           # Pytest-based test suite
├── config.ini                      # Configuration file
└── README.md                       # This file

requirements.txt                     # Python dependencies
```

## 🛠️ Prerequisites

1. **Python 3.7+** installed on your system
2. **Appium Server** running (usually on http://127.0.0.1:4723)
3. **Android device/emulator** connected and configured
4. **Inditex app** installed on the device
5. **ADB (Android Debug Bridge)** configured

## 📦 Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Appium setup:**
   ```bash
   # Check if device is connected
   adb devices
   
   # Start Appium server (if not already running)
   appium
   ```

## ⚙️ Configuration

Edit the `tests/config.ini` file to match your setup:

```ini
[DEVICE]
device_name = AppiumTest          # Your device name
platform_name = Android

[APP]
app_package = com.inditex.trazabilidapp
app_activity = .MainActivity

[SERVER]
appium_server_url = http://127.0.0.1:4723
implicit_wait = 10
explicit_wait = 30

[CREDENTIALS]
email = your_email               # Replace with your email
password = your_password         # Replace with your password

[TIMEOUTS]
app_launch_wait = 3
page_transition_wait = 2
login_completion_wait = 5
```

## 🚀 Usage

### Option 1: Basic Automation Script

```bash
cd tests
python inditex_login_automation.py
```

### Option 2: Enhanced Automation Script (Recommended)

```bash
cd tests
python inditex_login_enhanced.py
```

### Option 3: Pytest Test Suite

```bash
# Run all tests
cd tests
pytest test_inditex_login.py -v

# Run specific test
pytest test_inditex_login.py::TestInditexLogin::test_complete_login_flow -v

# Generate HTML report
pytest test_inditex_login.py --html=report.html --self-contained-html
```

## 📋 Features

### Basic Script (`inditex_login_automation.py`)
- ✅ Appium WebDriver setup
- ✅ App launch automation
- ✅ Email entry with XPath locators
- ✅ Continue button click
- ✅ Password entry
- ✅ Login button click
- ✅ Basic error handling and logging

### Enhanced Script (`inditex_login_enhanced.py`)
- ✅ All basic features
- ✅ Configuration file support
- ✅ Enhanced logging with file output
- ✅ Screenshot capture for verification
- ✅ Improved wait strategies
- ✅ Better error handling
- ✅ Clickable element waiting

### Test Suite (`test_inditex_login.py`)
- ✅ Pytest framework integration
- ✅ Fixtures for setup/teardown
- ✅ Parameterized tests
- ✅ Individual component testing
- ✅ Complete workflow testing
- ✅ Configuration validation tests

## 🎯 Test Workflow

The automation follows this workflow:

1. **Initialize** - Setup Appium driver and connect to device
2. **Launch App** - Start the Inditex application
3. **Enter Email** - Input email in the login field
4. **Click Continue** - Navigate to password screen
5. **Enter Password** - Input password
6. **Click Login** - Complete the authentication
7. **Verify Success** - Check if login was successful
8. **Cleanup** - Close driver session

## 🔧 Locator Strategy

The scripts use XPath locators for element identification:

- **Email Field**: `//android.widget.EditText[@resource-id='idToken7']`
- **Continue Button**: `//android.widget.Button[@resource-id='loginButton_0']`
- **Password Field**: `//android.widget.EditText[@resource-id='idToken3']`
- **Login Button**: `//android.widget.Button[@resource-id='idToken11_0']`

## 📊 Logging and Reports

### Log Files
- **Console Output**: Real-time progress information
- **Log File**: `inditex_automation.log` (enhanced script only)
- **Screenshots**: Captured at key points for verification

### Test Reports
```bash
# Generate detailed HTML report
pytest test_inditex_login.py --html=test_report.html --self-contained-html
```

## 🐛 Troubleshooting

### Common Issues

1. **Driver Connection Failed**
   ```
   Solution: Ensure Appium server is running and device is connected
   Check: adb devices
   ```

2. **Element Not Found**
   ```
   Solution: App UI might have changed, verify locators
   Check: Use Appium Inspector to find current element locators
   ```

3. **App Launch Failed**
   ```
   Solution: Verify app package name and activity
   Check: adb shell pm list packages | grep inditex
   ```

4. **Timeout Errors**
   ```
   Solution: Increase timeout values in config.ini
   Check: Network connectivity and app performance
   ```

### Debug Mode

Run with verbose logging:
```bash
python inditex_login_enhanced.py --log-level DEBUG
```

## 🔐 Security Notes

- **Never commit real credentials** to version control
- **Use environment variables** for sensitive data in production
- **Consider using encrypted credential storage**

Example with environment variables:
```python
import os
email = os.getenv('INDITEX_EMAIL', 'default_email')
password = os.getenv('INDITEX_PASSWORD', 'default_password')
```

## 📈 Extending the Framework

### Adding New Test Cases

1. Create new test methods in `test_inditex_login.py`
2. Use existing fixtures for setup
3. Follow naming convention: `test_feature_name`

### Adding New Locators

1. Use Appium Inspector to find element properties
2. Add to the appropriate automation class
3. Update documentation

### Custom Configuration

1. Add new sections to `config.ini`
2. Update the configuration loading logic
3. Use in automation scripts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📝 License

This project is for internal use and testing purposes.

---

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review log files for error details
3. Verify Appium and device setup
4. Contact the development team

---

**Happy Testing! 🎉**
