import customtkinter as ctk
import subprocess
import ctypes
import sys
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os
import tempfile
from tkinter import messagebox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

# Elevate the script to run with admin privileges
def elevate_script():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        sys.exit(0)

# Log messages to a file for debugging or records
def log_to_file(message):
    try:
        with open("log.txt", "a") as log_file:
            log_file.write(f"{message}\n")
    except Exception as e:
        print(f"Logging error: {e}")

import subprocess
import tkinter as tk
from tkinter import messagebox

def run_powershell_command(command, success_msg, error_msg, button, status_label):
    if not is_admin():
        messagebox.showerror("Error", "Administrator privileges are required.")
        return

    try:
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        if result.returncode == 0:
            status_label.configure(text=success_msg)  # Use 'configure' instead of 'config'
        else:
            status_label.configure(text=error_msg + " " + result.stderr)  # Use 'configure' instead of 'config'
    except Exception as e:
        status_label.configure(text="Error: " + str(e))  # Use 'configure' instead of 'config'

def bypass_windows_requirements():
    if messagebox.askyesno("Confirmation", "Are you sure you want to bypass Windows 11 requirements? This could make your system unstable."):
        command = '''
        # Ensure registry path exists
        if (-not (Test-Path "HKLM:\\SYSTEM\\Setup\\MoSetup")) {
            New-Item -Path "HKLM:\\SYSTEM\\Setup\\MoSetup" -Force
        }
        # Add property if it doesn't exist
        New-ItemProperty -Path "HKLM:\\SYSTEM\\Setup\\MoSetup" -Name "AllowUpgradesWithUnsupportedTPMOrCPU" -Value 1 -PropertyType DWORD -Force
        '''
        run_powershell_command(command, "Windows 11 requirements bypassed.", "Failed to bypass Windows 11 requirements.", bypass_button, status_label)
    else:
        messagebox.showinfo("Cancelled", "Bypass operation has been cancelled.")


def revert_windows_requirements():
    if messagebox.askyesno("Confirmation", "Are you sure you want to revert the bypass of Windows 11 requirements?"):
        command = '''
        Remove-ItemProperty -Path "HKLM:\\SYSTEM\\Setup\\MoSetup" -Name "AllowUpgradesWithUnsupportedTPMOrCPU" -Force
        '''
        run_powershell_command(command, "Windows 11 requirements reverted.", "Failed to revert Windows 11 requirements.", revert_bypass_button, status_label)
    else:
        messagebox.showinfo("Cancelled", "Revert operation has been cancelled.")

def disable_uac():
    if messagebox.askyesno("Confirmation", "Are you sure you want to disable User Account Control (UAC)? Your system will be less secure."):
        command = '''
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA" -Value 0
        '''
        run_powershell_command(command, "User Account Control disabled.", "Failed to disable User Account Control.", uac_button, status_label)

        # Check if the UAC setting is actually disabled after executing the command
        check_command = '''
        $uacStatus = Get-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA"
        if ($uacStatus.EnableLUA -eq 0) {
            Write-Host "UAC is disabled."
        } else {
            Write-Host "Failed to disable UAC."
        }
        '''
        # Run the check command to update the status label
        run_powershell_command(check_command, "UAC is disabled.", "Failed to disable UAC.", uac_button, status_label)
    else:
        messagebox.showinfo("Cancelled", "Disable UAC operation has been cancelled.")

# Re-enable UAC
def revert_uac():
    if messagebox.askyesno("Confirmation", "Are you sure you want to re-enable User Account Control (UAC)?"):
        command = '''
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA" -Value 1
        '''
        run_powershell_command(command, "User Account Control re-enabled.", "Failed to re-enable User Account Control.", revert_uac_button, status_label)

def optimize_registry():
    if messagebox.askyesno("Confirmation", "Are you sure you want to optimize the registry?"):
        command = '''
        Set-ItemProperty -Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "NoLowDiskSpaceChecks" -Value 1
        '''
        run_powershell_command(command, "Registry optimized.", "Failed to optimize registry.", optimize_button, status_label)

        # Check if the registry key is set correctly
        check_command = '''
        $regValue = Get-ItemProperty -Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "NoLowDiskSpaceChecks"
        if ($regValue.NoLowDiskSpaceChecks -eq 1) {
            Write-Host "Registry optimized successfully."
        } else {
            Write-Host "Failed to optimize registry."
        }
        '''
        # Run the check command to update the status label
        run_powershell_command(check_command, "Registry optimized successfully.", "Failed to verify registry optimization.", optimize_button, status_label)
    else:
        messagebox.showinfo("Cancelled", "Registry optimization has been cancelled.")

# Revert Registry Optimization
def revert_registry():
    if messagebox.askyesno("Confirmation", "Are you sure you want to revert the registry optimization?"):
        command = '''
        Remove-ItemProperty -Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "NoLowDiskSpaceChecks" -ErrorAction SilentlyContinue
        '''
        run_powershell_command(command, "Registry optimization reverted.", "Failed to revert registry optimization.", revert_optimize_button, status_label)

def bypass_all_requirements():
    if messagebox.askyesno("Confirmation", "Are you sure you want to bypass Windows 11 requirements, disable UAC, and optimize the registry? This could make your system unstable."):
        # Bypass Windows 11 requirements
        bypass_command = '''
        if (-not (Test-Path "HKLM:\\SYSTEM\\Setup\\MoSetup")) {
            New-Item -Path "HKLM:\\SYSTEM\\Setup\\MoSetup" -Force
        }
        New-ItemProperty -Path "HKLM:\\SYSTEM\\Setup\\MoSetup" -Name "AllowUpgradesWithUnsupportedTPMOrCPU" -Value 1 -PropertyType DWORD -Force
        '''
        run_powershell_command(bypass_command, "Windows 11 requirements bypassed.", "Failed to bypass Windows 11 requirements.", bypass_button, status_label)

        # Disable UAC
        uac_command = '''
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA" -Value 0
        '''
        run_powershell_command(uac_command, "User Account Control disabled.", "Failed to disable User Account Control.", uac_button, status_label)

        # Optimize Registry
        registry_command = '''
        Set-ItemProperty -Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "NoLowDiskSpaceChecks" -Value 1
        '''
        run_powershell_command(registry_command, "Registry optimized.", "Failed to optimize registry.", optimize_button, status_label)

    else:
        messagebox.showinfo("Cancelled", "Operation has been cancelled.")

def revert_all_changes():
    if messagebox.askyesno("Confirmation", "Are you sure you want to revert all changes? This will restore the system settings to their defaults."):
        # Revert Windows 11 Requirements Bypass
        revert_bypass_command = '''
        Remove-ItemProperty -Path "HKLM:\\SYSTEM\\Setup\\MoSetup" -Name "AllowUpgradesWithUnsupportedTPMOrCPU" -Force
        '''
        run_powershell_command(revert_bypass_command, "Windows 11 requirements reverted.", "Failed to revert Windows 11 requirements.", revert_bypass_button, status_label)

        # Revert UAC
        revert_uac_command = '''
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA" -Value 1
        '''
        run_powershell_command(revert_uac_command, "User Account Control re-enabled.", "Failed to re-enable User Account Control.", revert_uac_button, status_label)

        # Revert Registry Optimization
        revert_registry_command = '''
        Remove-ItemProperty -Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "NoLowDiskSpaceChecks" -ErrorAction SilentlyContinue
        '''
        run_powershell_command(revert_registry_command, "Registry optimization reverted.", "Failed to revert registry optimization.", revert_optimize_button, status_label)

    else:
        messagebox.showinfo("Cancelled", "Revert operation has been cancelled.")

# Create a Label with an Image from a URL
def create_label_with_image(app, text, logo_url):
    try:
        response = requests.get(logo_url, timeout=10)  # 10-second timeout for image load
        response.raise_for_status()
        img_data = response.content
        image = Image.open(BytesIO(img_data))
        image = image.resize((100, 100))
        logo = ImageTk.PhotoImage(image)

        label = ctk.CTkLabel(app, text=text, image=logo, compound="left", font=("Arial", 18))
        label.image = logo
        label.pack(pady=20)
    except requests.exceptions.RequestException as e:
        print(f"Error loading image: {e}")
        label = ctk.CTkLabel(app, text=text, font=("Arial", 18))
        label.pack(pady=20)

# GUI Setup
app = ctk.CTk()
app.geometry("400x590")
app.title("WinTweaker - Windows Optimization Tool")
app.resizable(False, False)

# Elevate script if not run as admin
elevate_script()

# Logo URL
logo_url = "https://raw.githubusercontent.com/Ghostshadowplays/Ghostyware-Logo/main/GhostywareLogo.png"
create_label_with_image(app, "Ghosty Winstall", logo_url)

# Status Label
status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)

button_params = {
    "fg_color": "#4158D0",
    "hover_color": "#993cda",
    "border_color": "#e7e7e7",
    "border_width": 2
}

# Create Frames and Buttons for Various Operations
bypass_frame = ctk.CTkFrame(app)
bypass_frame.pack(pady=10)
bypass_button = ctk.CTkButton(bypass_frame, text="Bypass Windows 11 Requirements", command=bypass_windows_requirements, **button_params)
bypass_button.pack(pady=5)
revert_bypass_button = ctk.CTkButton(bypass_frame, text="Revert Windows 11 Requirements Bypass", command=revert_windows_requirements, **button_params)
revert_bypass_button.pack(pady=5)

uac_frame = ctk.CTkFrame(app)
uac_frame.pack(pady=10)
uac_button = ctk.CTkButton(uac_frame, text="Disable User Account Control", command=disable_uac, **button_params)
uac_button.pack(pady=5)
revert_uac_button = ctk.CTkButton(uac_frame, text="Re-enable User Account Control", command=revert_uac, **button_params)
revert_uac_button.pack(pady=5)

optimize_frame = ctk.CTkFrame(app)
optimize_frame.pack(pady=10)
optimize_button = ctk.CTkButton(optimize_frame, text="Optimize Registry", command=optimize_registry, **button_params)
optimize_button.pack(pady=5)
revert_optimize_button = ctk.CTkButton(optimize_frame, text="Revert Registry Optimization", command=revert_registry, **button_params)
revert_optimize_button.pack(pady=5)

all_frame = ctk.CTkFrame(app)
all_frame.pack(pady=10)
bypass_all_button = ctk.CTkButton(all_frame, text="Bypass All Windows 11 Requirements", command=bypass_all_requirements, **button_params)
bypass_all_button.pack(pady=10)
revert_all_button = ctk.CTkButton(all_frame, text="Revert All Changes", command=revert_all_changes, **button_params)
revert_all_button.pack(pady=10)

# Run the GUI
app.mainloop()
