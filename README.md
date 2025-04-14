# HACKER_SECURE-PROJET
This repository contains three Python tools related to computer security: a password strength checker, a basic port scanner, and a file encryption/decryption tool.
## Projects

### Cloning

To clone this project to your local machine, use the following command:

```bash
git clone https://github.com/LadanbeFlorand/HACKER_SECURE-PROJET.git
```
### 1. Password Strength Checker

**Description:**
A Python program that evaluates password strength based on length, uppercase/lowercase letters, numbers, and special characters.

**Features:**
* Password strength evaluation.
* Clear feedback (Weak, Moderate, Strong).

**Usage:**
1.  **Make the script executable (Linux/macOS):**
    ```bash
    chmod +x Password_Strength_Checker.py
    ```
2.  Run the script and enter a password when prompted:
    ```bash
    python Password_Strength_Checker.py
    ```

**Dependencies:**
* No external dependencies.

**Example:**
```python
# Example script execution
# Enter password: MyPa234word@123!
# Password strength: Strong
 ```

### 2. Basic Port Scanner

**Description:**
A Python script that scans open ports on a given IP address within a specified port range.

**Features:**
* Scans open ports.
* Handles invalid inputs (IP addresses, port ranges).
* Displays open ports.

**Usage:**

1.  **Make the script executable (Linux/macOS):**
    ```bash
    chmod +x Basic_Port_Scanner_Script.py
    ```
2.  Run the script and provide the IP address and port range to scan:
    ```bash
    python Basic_Port_Scanner_Script.py
    ```
3.  Follow the prompts to enter the target IP address and the port range to scan.

    * Enter the target IP address (e.g., 192.168.1.1).
    * Enter the starting port number.
    * Enter the ending port number.
      
4.  The script will display the open ports found during the scan.
   
**Dependencies:**
* `socket` (Python standard library).

**Example:**
  ```bash
  python Basic_Port_Scanner_Script.py
  
  Enter target IP address: 127.0.0.1
  Enter start port (e.g., 1): 80
  Enter end port (e.g., 1024): 85
 ```

### 3. File Encryption/Decryption Tool

**Description:**
A Python program that encrypts and decrypts text files using a secret key with the `cryptography` library. Includes options to save the output as a new file.

**Features:**

* Encrypts text files.
* Decrypts text files.
* Secure encryption key generation.
* Uses a secret key for encryption/decryption.
* Option to specify the output file path.
*Error handling for incorrect keys and corrupted files.

**Installation:**

1.  Ensure Python is installed.
2.  Install the `cryptography` library:
    ```bash
    pip install cryptography
    ```

**Usage:**

1.  **Make the script executable (Linux/macOS):**
    ```bash
    chmod +x File_Ecryption_Decryption.py
    ```
2.  Run the script and follow the prompts:
    ```bash
    python File_Ecryption_Decryption.py
    ```
3.  Follow the on-screen instructions:

    * Choose to generate a new key (option 1), encrypt a file (option 2), or decrypt a file (option 3).
    * If you choose to encrypt or decrypt, you will be prompted to enter the input file path, the output file name.

**Dependencies:**
* `cryptography`

**Example:**

1.  Generate a key:

    ```bash
    python File_Ecryption_Decryption.py
    ```

    Choose option 1. The key will be saved in the `secret.key` file.

2.  Encrypt a file:

    ```bash
    python File_Ecryption_Decryption.py
    ```

    Choose option 2. Enter the path of the file to encrypt and the name of the encrypted file.

3.  Decrypt a file:

    ```bash
    python File_Ecryption_Decryption.py
    ```

    Choose option 3. Enter the path of the encrypted file and the name of the decrypted file.
