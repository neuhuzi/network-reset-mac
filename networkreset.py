import os
import shutil
import subprocess

def main():
    # Path to the SystemConfiguration directory
    system_config_path = "/Library/Preferences/SystemConfiguration"

    # List of files to be moved to trash
    files_to_remove = [
        "com.apple.airport.preferences.plist",
        "com.apple.network.eapolclient.configuration.plist",
        "com.apple.wifi.message-tracer.plist",
        "NetworkInterfaces.plist",
        "preferences.plist"
    ]

    # Turn off Wi-Fi
    subprocess.run(["networksetup", "-setairportpower", "airport", "off"])

    # Move files to trash
    for filename in files_to_remove:
        filepath = os.path.join(system_config_path, filename)
        if os.path.exists(filepath):
            shutil.move(filepath, os.path.expanduser("~/.Trash"))

    # Ensure com.apple.wifi.message-tracer.plist exists
    wifi_message_tracer_path = os.path.join(system_config_path, "com.apple.wifi.message-tracer.plist")
    if not os.path.exists(wifi_message_tracer_path):
        with open(wifi_message_tracer_path, 'w') as f:
            pass  # Create an empty file

    # Turn Wi-Fi back on
    subprocess.run(["networksetup", "-setairportpower", "airport", "on"])

    print("Operation completed successfully.")

if __name__ == "__main__":
    main()
