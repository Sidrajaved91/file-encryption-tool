# 🔐 File Encryption & Decryption Tool

A simple Python tool to **encrypt and decrypt files** using the Fernet symmetric encryption (AES).  
This project demonstrates skills in **cybersecurity, file handling, and Python programming**.  

## 🚀 Features
- Generate and store a secret encryption key  
- Encrypt any file (text, image, pdf, etc.)  
- Decrypt encrypted files back to original form  

## 🛠️ Tech Stack
- Python 3
- [cryptography library](https://pypi.org/project/cryptography/)

## 📦 Installation
```bash
git clone https://github.com/yourusername/file-encryption-tool.git
cd file-encryption-tool
pip install -r requirements.txt
```

## 📌 Usage
1. Place a file (e.g., `test.txt`) in the project folder.  
2. Run the script:  
   ```bash
   python encryption_tool.py
   ```
3. The tool will generate:  
   - `secret.key` (encryption key)  
   - `test.txt.enc` (encrypted file)  
   - Decrypted file restored as `test.txt`  

## 🔮 Future Improvements
- Add GUI for user interaction  
- Support for large file streaming encryption  
- Key management system for multiple users  

---
👩‍💻 Author: Sidra Javed  
📌 Bachelor’s in Computer Science  
📂 Example Portfolio Project for Cybersecurity & Systems Programming
