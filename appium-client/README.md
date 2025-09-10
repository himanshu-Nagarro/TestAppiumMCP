# Inditex Mobile Automation Project

A comprehensive Python-based automation framework for testing the Inditex mobile application using Appium WebDriver.

## 🏗️ Project Overview

This project provides multiple automation scripts and testing frameworks for automating the login workflow of the Inditex mobile application. It includes basic automation, enhanced configuration-driven automation, and a complete pytest-based testing suite.

## 📁 Project Structure

```
appium-client/
├── tests/                              # Main test directory
│   ├── inditex_login_automation.py     # Basic automation script
│   ├── inditex_login_enhanced.py       # Enhanced automation with config
│   ├── test_inditex_login.py           # Pytest test suite
│   ├── test_production_check.py        # Production check validation test
│   ├── config.ini                      # Configuration file
│   └── README.md                       # Detailed test documentation
├── .vscode/
│   └── mcp.json                       # VS Code MCP configuration
├── requirements.txt                    # Python dependencies
├── run_automation.py                  # Main automation runner
├── run_automation.bat                 # Windows batch runner
└── README.md                          # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Settings
Edit `tests/config.ini` with your device and credential information.

### 3. Run Automation

**Option A: Using Python Runner**
```bash
python run_automation.py
```

**Option B: Using Windows Batch File**
```cmd
run_automation.bat
```

**Option C: Direct Script Execution**
```bash
cd tests
python inditex_login_enhanced.py
```

## 🎯 Available Automation Scripts

### 1. Basic Automation (`inditex_login_automation.py`)
- Simple, straightforward automation script
- Hardcoded configurations
- Basic error handling
- Good for learning and simple use cases

### 2. Enhanced Automation (`inditex_login_enhanced.py`)
- Configuration file support
- Advanced logging and screenshot capture
- Better error handling and recovery
- Production-ready features

### 3. Pytest Test Suite (`test_inditex_login.py`)
- Complete testing framework
- Individual component testing
- Parameterized tests
- HTML reporting support

### 4. Production Check Test (`test_production_check.py`)
- Validates the Production Check functionality
- Automates audit selection and inspection
- Confirms units assignment and verification
- Implementation of NET-1028 requirements

## ⚙️ Configuration

The `tests/config.ini` file contains all configuration parameters:

```ini
[DEVICE]
device_name = AppiumTest
platform_name = Android

[APP]
app_package = com.inditex.trazabilidapp
app_activity = .MainActivity

[SERVER]
appium_server_url = http://127.0.0.1:4723
implicit_wait = 10
explicit_wait = 30

[CREDENTIALS]
email = your_email
password = your_password

[TIMEOUTS]
app_launch_wait = 3
page_transition_wait = 2
login_completion_wait = 5
```

## 🔧 Prerequisites

1. **Python 3.7+**
2. **Appium Server** running on default port (4723)
3. **Android Device/Emulator** connected and configured
4. **Inditex Mobile App** installed on the device
5. **ADB (Android Debug Bridge)** properly configured

## 📋 Workflow Automation

The automation follows this login workflow:

1. **🚀 Initialize** - Setup Appium driver connection
2. **📱 Launch App** - Start the Inditex application  
3. **📧 Enter Email** - Input email in the login field
4. **➡️ Click Continue** - Navigate to password screen
5. **🔒 Enter Password** - Input password securely
6. **🔑 Click Login** - Complete authentication
7. **✅ Verify Success** - Confirm successful login
8. **🧹 Cleanup** - Close driver session

## 🎮 Usage Examples

### Basic Usage
```bash
# Run with configuration file settings
python run_automation.py

# Run with custom credentials
python run_automation.py -e "user@example.com" -p "password123"

# Check if everything is properly configured
python run_automation.py --check
```

### Testing
```bash
# Run all tests
python run_automation.py --test

# Run specific test with pytest directly
cd tests
pytest test_inditex_login.py::TestInditexLogin::test_complete_login_flow -v

# Generate HTML test report
pytest test_inditex_login.py --html=report.html
```

## 🔍 Element Locators

The automation uses XPath strategies for reliable element identification:

| Element | XPath Locator |
|---------|---------------|
| Email Field | `//android.widget.EditText[@resource-id='idToken7']` |
| Continue Button | `//android.widget.Button[@resource-id='loginButton_0']` |
| Password Field | `//android.widget.EditText[@resource-id='idToken3']` |
| Login Button | `//android.widget.Button[@resource-id='idToken11_0']` |

## 📊 Logging and Reporting

### Logging Features
- **Console Logging**: Real-time progress information
- **File Logging**: Detailed logs saved to `inditex_automation.log`
- **Screenshots**: Automatic capture at key verification points
- **Error Tracking**: Comprehensive error reporting and debugging

### Test Reports
```bash
# Generate detailed HTML test report
pytest tests/test_inditex_login.py --html=test_report.html --self-contained-html
```

## 🛠️ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **Appium Connection Failed** | Ensure Appium server is running: `appium` |
| **Device Not Found** | Check device connection: `adb devices` |
| **App Launch Failed** | Verify app package name and installation |
| **Element Not Found** | Check if app UI has changed; update locators |
| **Timeout Errors** | Increase timeout values in configuration |

### Debug Commands
```bash
# Check device connectivity
adb devices

# Check installed packages
adb shell pm list packages | grep inditex

# Check Appium server status
curl http://localhost:4723/wd/hub/status

# Run with verbose logging
python run_automation.py --check
```

## 🔐 Security Best Practices

- **Environment Variables**: Use for production credentials
- **Config Management**: Keep sensitive data out of version control
- **Credential Encryption**: Consider encrypted storage for passwords

Example with environment variables:
```python
import os
email = os.getenv('INDITEX_EMAIL', 'fallback@example.com')
password = os.getenv('INDITEX_PASSWORD', 'fallback_password')
```

## 🚀 Advanced Features

### Continuous Integration
```yaml
# Example GitHub Actions workflow
name: Inditex Mobile Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python run_automation.py --test
```

### Custom Extensions
```python
# Add new test methods to test_inditex_login.py
def test_custom_workflow(self, automation):
    """Test custom workflow"""
    # Your custom test logic here
    pass
```

## 📈 Performance Optimization

- **Implicit Waits**: Set appropriate default wait times
- **Explicit Waits**: Use for specific element conditions
- **Screenshot Optimization**: Capture only when necessary
- **Resource Cleanup**: Always close driver sessions properly

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Add tests** for new functionality
4. **Ensure** all tests pass
5. **Commit** changes (`git commit -m 'Add amazing feature'`)
6. **Push** to branch (`git push origin feature/amazing-feature`)
7. **Create** a Pull Request

## 📝 Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include unit tests for new features
- Update documentation for changes
- Use meaningful commit messages

## 🏆 Project Roadmap

- [x] Basic automation framework
- [x] Configuration file support
- [x] Pytest integration
- [x] Enhanced logging and reporting
- [x] Windows batch runner
- [ ] Cross-platform shell scripts
- [ ] CI/CD pipeline integration
- [ ] Docker containerization
- [ ] Parallel test execution
- [ ] Test data management
- [ ] Performance metrics collection

## 📞 Support

For issues, questions, or contributions:

1. **Check Documentation**: Review README files and inline comments
2. **Search Issues**: Look for existing solutions in project issues
3. **Run Diagnostics**: Use `python run_automation.py --check`
4. **Review Logs**: Check `inditex_automation.log` for detailed error information
5. **Contact Team**: Reach out to the development team

## 📄 License

This project is for internal testing and development purposes.

---

**Happy Automating! 🎉**

*Built with ❤️ for the Inditex QA Team*
"# TestAppiumMCP" 
