## Network Reset Mac

This repository contains a Python script that resets network settings and refreshes network interfaces on macOS systems. It can be useful in situations where network interfaces are not properly detected.

### Usage

1. **Prerequisites**:
   - macOS operating system
   - Python installed (the script is compatible with Python 3)
   - Administrative privileges (required for modifying system files)

2. **Running the Script**:
   - Download or clone the repository to your local machine.
   - Open a terminal and navigate to the repository directory.
   - Run the script with the following command:

     ```
     python3 networkreset.py
     ```

3. **Expected Behavior**:
   - The script will perform the following actions:
     - Turn off Wi-Fi using the `networksetup` command.
     - Move specific network configuration files to the Trash:
       - `com.apple.airport.preferences.plist`
       - `com.apple.network.eapolclient.configuration.plist`
       - `com.apple.wifi.message-tracer.plist`
       - `NetworkInterfaces.plist`
       - `preferences.plist`
     - Ensure the `com.apple.wifi.message-tracer.plist` file exists (create an empty file if it doesn't).
     - Turn Wi-Fi back on using the `networksetup` command.
   - Upon successful execution, the script will print "Operation completed successfully."

### Repository Contents

- `networkreset.py`: The Python script responsible for resetting network settings and refreshing network interfaces.

### Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request in this repository.

### License

The code in this repository is distributed under the [MIT License](LICENSE). See the `LICENSE` file for more details.
