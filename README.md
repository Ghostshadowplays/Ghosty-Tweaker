Key Features of Ghosty Tweaker:
Bypass Windows 11 Requirements:

What it does: This feature bypasses the stringent hardware requirements for upgrading to Windows 11 (like TPM 2.0 and Secure Boot), enabling users to install or upgrade to Windows 11 even on unsupported hardware.
How it works: The tool adds a registry entry that bypasses Windows 11's system checks during the upgrade process.
Revert Option: If desired, users can revert this tweak by removing the registry entry.
Disable Windows Defender:

What it does: It disables Windows Defender, the built-in antivirus software in Windows.
How it works: The tool stops the Defender service and prevents it from launching automatically on system boot.
Revert Option: Users can easily re-enable Windows Defender by restarting the service and setting it to start automatically.
Disable User Account Control (UAC):

What it does: UAC is a security feature that prompts users for permission before making system changes. Disabling UAC prevents these prompts.
How it works: The tool modifies a registry key to disable UAC.
Revert Option: Users can re-enable UAC by restoring the original registry key, which will trigger prompts again when needed.
Optimize Registry:

What it does: This tweak optimizes certain registry settings to improve performance and avoid unnecessary system warnings, such as low disk space checks.
How it works: The tool modifies registry values to disable low disk space alerts, which can sometimes be an annoyance.
Revert Option: Users can revert this change if they wish to restore the original settings.
User Interface (GUI):
Main Window: Ghosty Tweaker uses CustomTkinter (CTk) to provide a sleek and modern interface. This makes the tool visually appealing and easy to use, even for those with no technical background.
Buttons for Each Function: Each tweak (e.g., "Bypass Windows 11 Requirements," "Disable Windows Defender") is represented by a button in the GUI. Clicking a button runs the corresponding PowerShell command to execute the tweak.
Status Display: The tool shows the status of each operation (whether it succeeded or failed) with an updated message on the screen.
How Ghosty Tweaker Works:
Admin Privileges Check: The tool ensures it's running with administrator privileges because these tweaks require elevated permissions. If the tool is not running as an admin, it will prompt the user to relaunch it with admin rights.
Execution of Commands: When a user clicks a button, the tool executes the corresponding PowerShell script to modify system settings. Errors are handled, and the user is notified if something goes wrong.
Revert Changes: For every tweak applied, users can revert the changes with a single click. This ensures flexibility in case a user wants to undo a tweak.
How to Use Ghosty Tweaker:
Launch the Tool: Open Ghosty Tweaker to access its main window.
Click a Button: Choose one of the available tweaks, such as "Disable Windows Defender" or "Bypass Windows 11 Requirements," and click the corresponding button.
Admin Rights Check: If the tool is not already running as an administrator, it will automatically relaunch itself with elevated permissions.
Wait for Results: The tool will execute the PowerShell command and display a success or failure message in the status area.
Revert Changes: If you decide to undo any change, simply click the revert button for that tweak.

Example of the Tool's UI:
Buttons:

Bypass Windows 11 Requirements
Revert Windows 11 Requirements Bypass
Disable Windows Defender
Re-enable Windows Defender
Disable User Account Control (UAC)
Re-enable User Account Control (UAC)
Optimize Registry
Revert Registry Optimization
Status Updates:

After performing each action, the status label will update to show either a success message (e.g., "Windows 11 requirements bypassed") or an error message (e.g., "Failed to bypass Windows 11 requirements").
