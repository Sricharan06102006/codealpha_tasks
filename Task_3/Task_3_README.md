# 📧 Email Extractor Automation Script

## ✅ Task 3: Task Automation with Python Scripts

### 🔍 Goal
Automate a real-life repetitive task by **extracting all email addresses** from a given `.txt` file and saving them to a new file.

---
## 🚀 Features
- Reads any text file containing mixed content.
- Extracts **all valid email addresses** using Regular Expressions.
- Eliminates duplicates and sorts emails alphabetically.
- Saves the result in a clean, separate `.txt` file.
- Error handling for missing files or unexpected issues.

---
## 🧠 Key Concepts Used
| Concept        | Module        | Purpose                          |
|----------------|---------------|----------------------------------|
| Regex          | `re`          | To detect valid email patterns   |
| File Handling  | Built-in I/O  | Reading and writing `.txt` files |
| Error Handling | `try-except`  | Graceful failure management      |

---
## 🛠️ Requirements
- Python 3.x
- No external libraries required

---
## 📁 Folder Structure
task_3_email_extractor/
├── Task_3_sample_input.txt # Input file containing emails
├── Task_3_extracted_emails.txt # Output file with unique emails
└── Task_3_email_extractor.py # Python script

---
## ▶️ How to Run
1. Make sure Python is installed.
2. Place your input file (e.g., `Task_3_sample_input.txt`) in the same folder.
3. Run the script:

```bash
python Task_3_email_extractor.py

