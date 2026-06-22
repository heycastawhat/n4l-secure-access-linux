#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class CertInstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("N4L Wi-Fi Certificate Installer")
        self.root.geometry("450x280")
        self.root.configure(bg="#2E3440") # Nord dark theme background
        self.root.resizable(False, False)
        
        self.cert_path = None
        
        # Title
        title_label = tk.Label(
            root, 
            text="N4L Secure Access Installer", 
            font=("Inter", 16, "bold"), 
            bg="#2E3440", 
            fg="#ECEFF4"
        )
        title_label.pack(pady=(25, 5))

        subtitle_label = tk.Label(
            root, 
            text="Easily load your certificate for school Wi-Fi.", 
            font=("Inter", 10), 
            bg="#2E3440", 
            fg="#D8DEE9"
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Selected File Label
        self.file_label = tk.Label(
            root, 
            text="No certificate selected", 
            font=("Inter", 10, "italic"), 
            bg="#2E3440", 
            fg="#88C0D0"
        )
        self.file_label.pack(pady=10)
        
        # Select Button
        select_btn = tk.Button(
            root, 
            text="Browse for Certificate", 
            command=self.select_file, 
            bg="#5E81AC", 
            fg="white", 
            activebackground="#81A1C1",
            activeforeground="white",
            font=("Inter", 10, "bold"), 
            relief="flat", 
            cursor="hand2",
            padx=15, 
            pady=8
        )
        select_btn.pack(pady=5)
        
        # Install Button
        self.install_btn = tk.Button(
            root, 
            text="Install to System", 
            command=self.install_cert, 
            bg="#A3BE8C", 
            fg="#2E3440", 
            activebackground="#8FBCBB",
            activeforeground="#2E3440",
            font=("Inter", 10, "bold"), 
            relief="flat", 
            cursor="hand2",
            state=tk.DISABLED,
            padx=15, 
            pady=8
        )
        self.install_btn.pack(pady=15)

    def select_file(self):
        filetypes = (
            ('Certificate files', '*.crt *.pem *.cer'),
            ('All files', '*.*')
        )
        filepath = filedialog.askopenfilename(title='Select your N4L Certificate', filetypes=filetypes)
        if filepath:
            self.cert_path = filepath
            filename = os.path.basename(filepath)
            self.file_label.config(text=f"Selected: {filename}")
            self.install_btn.config(state=tk.NORMAL)

    def install_cert(self):
        if not self.cert_path:
            return
        
        filename = os.path.basename(self.cert_path)
        dest_path = f"/etc/ca-certificates/trust-source/anchors/{filename}"
        
        # Use pkexec to prompt for password graphically and execute the move/update securely
        command = f"pkexec sh -c 'cp \"{self.cert_path}\" \"{dest_path}\" && chmod 644 \"{dest_path}\" && update-ca-trust'"
        
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                messagebox.showinfo(
                    "Success", 
                    "Certificate installed successfully!\n\nYou and your friends can now select this certificate when connecting to the N4L Wi-Fi."
                )
            else:
                # 126 is typically returned by pkexec if the user dismissed the auth dialog
                if result.returncode == 126:
                    messagebox.showwarning("Cancelled", "Authentication was cancelled.")
                else:
                    messagebox.showerror("Error", f"Failed to install certificate.\n\nDetails: {result.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CertInstallerApp(root)
    root.mainloop()
