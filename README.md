# **Ghosty Winstall: A Windows Optimization and Tweaker Tool**

**Ghosty Winstall** is a powerful tool designed to optimize and tweak your Windows system. Below are the key features and instructions on how to use the tool.

## **Features:**

### **Bypass Windows 11 Requirements:**
- **What it does:**  
  Allows users to bypass the strict hardware requirements for Windows 11, enabling them to upgrade even on unsupported devices.
  
- **How it works:**  
  The tool adds a registry key that disables the checks for TPM 2.0 and Secure Boot during Windows 11 installation.
  
- **Revert Option:**  
  If needed, users can easily revert this change by removing the registry entry.

### **Disable Windows Defender:**
- **What it does:**  
  Disables Windows Defender Antivirus, Windows' built-in security software.
  
- **How it works:**  
  The tool stops the Defender service and changes its startup type to "Disabled."
  
- **Revert Option:**  
  Users can restore Windows Defender by re-enabling the service with the click of a button.

### **Disable User Account Control (UAC):**
- **What it does:**  
  Disables the User Account Control feature, which typically prompts users for confirmation before making system changes.
  
- **How it works:**  
  The tool modifies the UAC registry key to disable the prompts.
  
- **Revert Option:**  
  Users can restore UAC by re-enabling the registry key, which will reactivate the confirmation prompts.

### **Optimize Registry:**
- **What it does:**  
  Disables certain registry checks like low disk space warnings, which can sometimes be intrusive.
  
- **How it works:**  
  The tool tweaks the Windows registry to disable unnecessary checks and improve system performance.
  
- **Revert Option:**  
  Users can undo the registry optimization to restore the default settings.

## **User Interface (GUI):**
- **Main Window:**  
  Ghosty Winstall provides a sleek, modern interface using **CustomTkinter (CTk)**. The buttons are visually appealing, and the layout is clean, making it easy for users to perform system tweaks with minimal effort.

- **Buttons for Each Feature:**  
  Each major function (e.g., "Bypass Windows 11 Requirements" or "Disable Windows Defender") is mapped to a button, and clicking that button triggers the respective PowerShell script to execute the tweak.

- **Status Label:**  
  A status label provides feedback after each operation, showing either success or error messages to inform the user of the action’s outcome.

## **How Ghosty Winstall Works:**
- **Admin Privileges:**  
  The tool first checks if it’s being run with administrator rights (required for system-level tweaks). If it’s not, it will automatically relaunch itself with elevated permissions.

- **Executing Commands:**  
  When a user clicks on a button for a specific tweak, Ghosty Winstall runs a PowerShell script that makes the necessary system changes.

- **Reverting Changes:**  
  For every action taken, Ghosty Winstall provides an option to revert the change. Users can easily undo any tweaks if they want to restore their system to its original state.

## **How to Use Ghosty Winstall:**
1. **Open the Tool:**  
   Launch Ghosty Winstall from your desktop or start menu.

2. **Select a Function:**  
   Click on one of the available options (e.g., "Disable Windows Defender," "Optimize Registry").

3. **Admin Prompt:**  
   If Ghosty Winstall is not running as administrator, it will ask you for elevated privileges.

4. **Wait for the Process:**  
   After clicking a button, wait for the operation to complete. The status label will show a message indicating whether the action succeeded or failed.

5. **Revert the Action (Optional):**  
   If you want to undo any tweaks, simply click the revert button for that feature.

## **Example of the Tool's Interface:**

### **Buttons:**
- Bypass Windows 11 Requirements
- Revert Windows 11 Requirements Bypass
- Disable Windows Defender
- Re-enable Windows Defender
- Disable User Account Control (UAC)
- Re-enable User Account Control (UAC)
- Optimize Registry
- Revert Registry Optimization

### **Status Label:**
- **Success Message:**  
  "Windows 11 requirements bypassed."
  
- **Error Message:**  
  "Failed to disable Windows Defender."
