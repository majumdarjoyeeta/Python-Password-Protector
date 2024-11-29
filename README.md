# Python-Password-Protector
# 📄 **PDF Encryption Tool** 🛡️🔒

This Python script allows you to **encrypt a PDF** with a password. It reads the contents of a PDF file, adds encryption, and writes the encrypted version to a new file. This is a simple, secure way to protect sensitive documents.  

---

## 🛠 **Features**  
- **Encrypt PDFs**: Easily add password protection to your PDF files.  
- **User-Friendly**: Uses `getpass` to securely type passwords without displaying them.  
- **PDF Handling**: Utilizes `PyPDF2` for reading and writing PDFs, making it compatible with most PDF formats.  
- **Secure Document Management**: Helps you secure important documents (like resumes, contracts, etc.).

---

## 📜 **How It Works**  
1. **Install the required package**:  
   Before running the script, make sure to install the required library by running the following command in your terminal:
   ```bash
   pip install PyPDF2
   ```

2. **Input the file**:  
   In the script, the PDF file (`cv_JM.pdf`) is read using the `PdfReader` object.

3. **Password Protection**:  
   The script prompts the user to enter a password using the `getpass` library to keep it hidden.

4. **Create Encrypted PDF**:  
   After encryption, a new PDF file (`new.pdf`) is generated with the specified password, ensuring that only authorized users can access it.

5. **Save the File**:  
   The encrypted file is written to a new location on your device.

---

## 💻 **How to Run**  
1. Clone or download this repository.
2. Make sure you have **Python 3** installed and the `PyPDF2` library:
   ```bash
   pip install PyPDF2
   ```
3. Run the **`app.py`** script:
   ```bash
   python app.py
   ```

4. Enter the password when prompted to protect your file.

---

## 📂 **File Structure**  
- **`app.py`**: The main Python script that encrypts the PDF.
- **`cv_JM.pdf`**: The original PDF file that you want to encrypt.
- **`new.pdf`**: The newly created encrypted PDF file.

---

## 🎉 **Acknowledgments**  
A special thanks to **Aimerz** for providing valuable learning opportunities and helping me enhance my skills in Python programming! 👨‍🏫💡

---

## 🔒 **Security Reminder**  
Always keep your encryption passwords safe! Don't forget them, as the encrypted PDF cannot be accessed without the correct password.

---

## 🚀 **Keep Coding**  
Feel free to modify and extend this script to include additional features like decryption or batch processing multiple PDFs!

**#️⃣PDFSecurity #️⃣Encryption #️⃣PythonProject #️⃣PyPDF2 #️⃣SecureDocuments**
