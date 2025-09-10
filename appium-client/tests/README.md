# Production Check Validation Test

This automation script validates the production check functionality in the INDITEX iTrace App (NET-1028).

## Test Description

The test automates the following workflow:

1. Log in to the iTrace App
2. Navigate to the Audits screen
3. Select audit #206697
4. Navigate to the Production Check screen
5. Select the first item in the list
6. Navigate to the CONFIRM UNITS tab
7. Input the real units value (matching the assigned units)
8. Verify the total units are updated correctly

## Prerequisites

- Android device or emulator with the INDITEX iTrace App installed
- Appium server running
- Python 3.8+ with required dependencies

## Configuration

Update the `config.ini` file with your test environment settings:

```ini
[App]
package=com.inditex.trazabilidapp
activity=.MainActivity

[Device]
name=Pixel Tablet
platform_version=13

[Credentials]
username=your_username
password=your_password

[Settings]
timeout=30

[Test]
audit_id=206697
```

## Running the Test

1. Start the Appium server
2. Connect your Android device or start an emulator
3. Navigate to the `appium-client` directory
4. Run the test script:

```bash
python tests/test_production_check.py
```

## Output

The test will log progress and results to both the console and `inditex_automation.log` file.