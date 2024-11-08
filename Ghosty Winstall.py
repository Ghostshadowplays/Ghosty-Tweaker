import customtkinter as ctk
import subprocess
import ctypes
import sys
from PIL import Image, ImageTk
import requests
from io import BytesIO


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()  


def log_to_file(message):
    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")


def run_powershell_command(command, success_message, error_message, button):
    try:
        button.config(state="disabled", text="Running...")
        log_to_file(f"Running command: {command}")
        subprocess.run(["powershell", "-Command", command], check=True)
        status_label.config(text=success_message, fg="green")
        log_to_file(success_message)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        status_label.config(text=error_message, fg="red")
        log_to_file(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        status_label.config(text="Unexpected error occurred.", fg="red")
        log_to_file(f"Unexpected error: {e}")
    finally:
        button.config(state="normal", text="Done")


def bypass_windows_requirements():
    command = '''
    # Bypass Windows 11 requirements
    New-Item -Path "HKLM:\\SYSTEM\\Setup\\MoSetup" -Name "AllowUpgradesWithUnsupportedTPMOrCPU" -PropertyType DWORD -Value 1 -Force
    '''
    run_powershell_command(command, "Windows 11 requirements bypassed.", "Failed to bypass Windows 11 requirements.", bypass_button)

def revert_windows_requirements():
    command = '''
    Remove-ItemProperty -Path "HKLM:\\SYSTEM\\Setup\\MoSetup" -Name "AllowUpgradesWithUnsupportedTPMOrCPU" -ErrorAction SilentlyContinue
    '''
    run_powershell_command(command, "Windows 11 requirements bypass reverted.", "Failed to revert Windows 11 requirements bypass.", revert_bypass_button)

def disable_defender():
    command = '''
    Set-Service -Name WinDefend -StartupType Disabled
    Stop-Service -Name WinDefend
    '''
    run_powershell_command(command, "Windows Defender disabled.", "Failed to disable Windows Defender.", defender_button)

def revert_defender():
    command = '''
    Set-Service -Name WinDefend -StartupType Manual
    Start-Service -Name WinDefend
    '''
    run_powershell_command(command, "Windows Defender re-enabled.", "Failed to re-enable Windows Defender.", revert_defender_button)

def disable_uac():
    command = '''
    Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA" -Value 0
    '''
    run_powershell_command(command, "User Account Control disabled.", "Failed to disable User Account Control.", uac_button)

def revert_uac():
    command = '''
    Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA" -Value 1
    '''
    run_powershell_command(command, "User Account Control re-enabled.", "Failed to re-enable User Account Control.", revert_uac_button)

def optimize_registry():
    command = '''
    Set-ItemProperty -Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "NoLowDiskSpaceChecks" -Value 1
    '''
    run_powershell_command(command, "Registry optimized.", "Failed to optimize registry.", optimize_button)

def revert_registry():
    command = '''
    Remove-ItemProperty -Path "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "NoLowDiskSpaceChecks" -ErrorAction SilentlyContinue
    '''
    run_powershell_command(command, "Registry optimization reverted.", "Failed to revert registry optimization.", revert_optimize_button)


def create_label_with_image(app, text, logo_url):

    response = requests.get(logo_url)
    img_data = response.content
    image = Image.open(BytesIO(img_data))
    image = image.resize((100, 100))  
    logo = ImageTk.PhotoImage(image)

    
    label = ctk.CTkLabel(app, text=text, image=logo, compound="left", font=("Arial", 18))
    label.image = logo  
    label.pack(pady=20)


app = ctk.CTk()
app.geometry("400x580")
app.title("WinTweaker - Windows Optimization Tool")
app.resizable (False,False)


logo_url = "https://raw.githubusercontent.com/Ghostshadowplays/Ghostyware-Logo/main/GhostywareLogo.png"


create_label_with_image(app, "Ghosty Winstall", logo_url)


status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)


button_params = {
    "fg_color": "#4158D0",
    "hover_color": "#993cda",
    "border_color": "#e7e7e7",
    "border_width": 2
}


bypass_frame = ctk.CTkFrame(app)
bypass_frame.pack(pady=10)
bypass_button = ctk.CTkButton(bypass_frame, text="Bypass Windows 11 Requirements", command=bypass_windows_requirements, **button_params)
bypass_button.pack(pady=5)
revert_bypass_button = ctk.CTkButton(bypass_frame, text="Revert Windows 11 Requirements Bypass", command=revert_windows_requirements, **button_params)
revert_bypass_button.pack(pady=5)


defender_frame = ctk.CTkFrame(app)
defender_frame.pack(pady=10)
defender_button = ctk.CTkButton(defender_frame, text="Disable Windows Defender", command=disable_defender, **button_params)
defender_button.pack(pady=5)
revert_defender_button = ctk.CTkButton(defender_frame, text="Re-enable Windows Defender", command=revert_defender, **button_params)
revert_defender_button.pack(pady=5)


uac_frame = ctk.CTkFrame(app)
uac_frame.pack(pady=10)
uac_button = ctk.CTkButton(uac_frame, text="Disable User Account Control (UAC)", command=disable_uac, **button_params)
uac_button.pack(pady=5)
revert_uac_button = ctk.CTkButton(uac_frame, text="Re-enable User Account Control (UAC)", command=revert_uac, **button_params)
revert_uac_button.pack(pady=5)


registry_frame = ctk.CTkFrame(app)
registry_frame.pack(pady=10)
optimize_button = ctk.CTkButton(registry_frame, text="Optimize Registry", command=optimize_registry, **button_params)
optimize_button.pack(pady=5)
revert_optimize_button = ctk.CTkButton(registry_frame, text="Revert Registry Optimization", command=revert_registry, **button_params)
revert_optimize_button.pack(pady=5)


app.mainloop()
