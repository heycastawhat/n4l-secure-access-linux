# N4L Secure Access Wi-Fi Installer for Linux

A lightweight, native Python application that helps Linux users easily install their unique N4L Secure Access certificates. It provides a simple graphical interface to select your certificate and securely installs it to the system trust store, automatically handling privilege escalation via `pkexec`.

## Features
- **Modern GUI**: Built using `tkinter`.
- **System Native**: Escalates privileges using Linux's native Polkit (`pkexec`) to prompt for your password securely.
- **Easy Sharing**: It's a single Python file, making it easy to distribute to your classmates or friends on Linux.

## Requirements

### Arch Linux
Python is pre-installed. You just need to ensure `tk` is installed:
```bash
sudo pacman -S tk
```

### Ubuntu / Debian / Linux Mint
```bash
sudo apt install python3-tk
```

## Usage
1. Make the script executable (if it isn't already):
```bash
chmod +x n4l_installer.py
```
2. Run the application:
```bash
./n4l_installer.py
```
3. Click **Browse for Certificate** and select your `.crt`, `.pem`, or `.cer` file.
4. Click **Install to System**. You will be prompted for your password to install the certificate to the system trust store.

## Post-Installation
Once the certificate is successfully installed, open your Wi-Fi settings (e.g., NetworkManager), select the N4L Secure Access Wi-Fi network, and choose your newly installed certificate from the "CA Certificate" dropdown list.