# User Story & Test Cases for Mobile Automation

## User Story
**As an** automation engineer  
**I want to** automate the mobile shopping application workflow to verify audit production check functionality  
**So that** I can validate the total assigned units calculation and ensure the audit process works correctly across mobile devices  

---

## Test Case 1: INDITEX iTrace App - Audit Production Check Validation

**Test Case ID:** TC_MOBILE_AUDIT_001  
**Test Objective:** Verify that an automation engineer can successfully navigate through the mobile shopping application's audit workflow and retrieve total assigned units for audit number `206699`.

---

## Test Case 2: NET-1028 - Audit Production Check Unit Confirmation

**Test Case ID:** TC_MOBILE_AUDIT_002  
**Test Objective:** Verify that an auditor can validate production check functionality in the iTrace App by confirming that real units match the assigned units for audit number `206697`.

---

### Pre-conditions
- INDITEX iTrace App automation MCP framework is set up and configured  
- INDITEX iTrace App application is installed and accessible  
- Test credentials are available:  
  - Username: `amitks`  
  - Password: `Pl@tinum@82026`  
- Audit number `206699` exists in the system with production check items  

---

### Test Steps

| Step | Action | Expected Result |
|------|--------|------------------|
| 1 | Initialize mobile-automation MCP framework | Framework loads successfully |
| 2 | Launch INDITEX iTrace App application on mobile device | Application opens to login screen |
| 3 | Enter username: `amitks` and click **Continue** | Username field populated correctly |
| 4 | Enter password: `Pl@tinum@82026` and click **LOG IN** | Password field populated (masked) |
| 5 | Tap **Login** button | User successfully logged in |
| 6 | Handle user alert popup by clicking **OK** | Alert dismissed, main screen visible |
| 7 | Click on **Audit number 206699** | Audit screen loads successfully |
| 8 | Click on the **three dots** (top right corner) → Select **Start** | Audit session started |
| 9 | Click on **Production Check** option | Multiple items displayed on screen |
| 10 | Select and click on one of the displayed items | Item selected and highlighted |
| 11 | Click **Confirm Units** button | Units confirmation dialog appears |
| 12 | Fetch and capture **Total** value | Total assigned units value retrieved successfully |

---

### Test Data
- **Username:** `amitks`  
- **Password:** `Pl@tinum@82026`  
- **Audit Number:** `206699`  

---

### Expected Results
- Successful login without errors  
- Alert popup handled appropriately  
- Audit screen loads with correct audit number (`206699`)  
- Production check displays multiple selectable items  
- Units confirmation process completes successfully  
- Total assigned units value is captured and can be validated  

---

### Pass/Fail Criteria
- **Pass:** All steps execute successfully and total assigned units value is retrieved  
- **Fail:** Any step fails or total assigned units cannot be fetched  

---

### Environment
- **Platform:** Mobile (Android)  
- **Framework:** Mobile-automation MCP  
- **Application:** INDITEX iTrace App (`com.inditex.trazabilidap`) (Mobile version)  

---

### Notes for Automation Engineer
- Ensure proper **wait conditions** between steps for mobile UI elements to load  
- Implement **error handling** for network connectivity issues  
- Add **assertions** to validate each step completion  
- Implement **screenshot capture** for failed steps  
- Store the fetched **total assigned units value** for further validation or reporting  

---

## Test Steps for NET-1028 (TC_MOBILE_AUDIT_002)

| Step | Action | Expected Result |
|------|--------|------------------|
| 1 | Initialize mobile-automation MCP framework | Framework loads successfully |
| 2 | Launch INDITEX iTrace App application on mobile device | Application opens to login screen |
| 3 | Enter username: `amitks` and click **Continue** | Username field populated correctly |
| 4 | Enter password: `Pl@tinum@82026` and click **LOG IN** | Password field populated (masked) |
| 5 | Tap **Login** button | User successfully logged in |
| 6 | Navigate to Audits screen | Audits list displayed |
| 7 | Click on **Audit number 206697** | Audit details screen loads successfully |
| 8 | Click on **PRODUCTION CHECK** option | Production Check screen loads |
| 9 | Select the first item in the list | Item details displayed |
| 10 | Click on **CONFIRM UNITS** tab | Units confirmation screen appears |
| 11 | Observe the **Total Assigned** value (65,404) | Value displayed correctly |
| 12 | Enter the real units value in the first order field | Value entered successfully |
| 13 | Click the confirmation icon | Value saved and total updated |
| 14 | Verify the **Total Real** value is updated | Total Real value matches input |

---

### Test Data for NET-1028
- **Username:** `amitks`  
- **Password:** `Pl@tinum@82026`  
- **Audit Number:** `206697`  
- **Expected Total Assigned Units:** `65,404`  
- **Real Units to Enter:** Matching the assigned units for the first order (`16,351`)

---

### Expected Results for NET-1028
- Successful login without errors  
- Audit screen loads with correct audit number (`206697`)  
- Production check screen loads with item list  
- Item details display correctly with CONFIRM UNITS tab  
- Total Assigned units value is visible and correct  
- Real units value can be entered and confirmed  
- Total Real units value updates correctly after confirmation  

---

### Pass/Fail Criteria for NET-1028
- **Pass:** All steps execute successfully and total real units value is updated correctly  
- **Fail:** Any step fails or total real units value doesn't update as expected  