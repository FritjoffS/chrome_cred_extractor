# Chrome Credentials Extractor

This Python script extracts saved usernames and passwords from Google Chrome on Windows systems. It decrypts the stored credentials and saves them to an Excel file.

## ⚠️ Disclaimer

This script is for **educational purposes only**. Accessing or extracting passwords without explicit permission is illegal and unethical. Only use this script on your own computer or with the explicit consent of the owner. The author is not responsible for any misuse or damage caused by this script.

## 🚀 Features

- Extracts usernames and passwords stored in Google Chrome
- Decrypts encrypted passwords
- Saves extracted data to an Excel file

## 📋 Requirements

- Windows operating system
- Google Chrome installed
- Python 3.9 or higher
- Conda for environment management

## 🛠️ Installation

1. Clone this repository:

```sh
git clone https://github.com/yourusername/chrome-creds-extractor.git
cd chrome-creds-extractor
```


2. Create the Conda environment:
```sh
conda env create -f environment.yml
```

3. Activate the environment:
```sh
conda activate chrome_extract
```

## 🖥️ Usage

1. Ensure Google Chrome is closed.
2. Run the script:
```sh
python chrome_creds_extractor.py
```
3. The extracted credentials will be saved in `chrome_creds.xlsx` in the same directory.

## 📁 File Structure

- `chrome_creds_extractor.py`: Main script file
- `environment.yml`: Conda environment file
- `README.md`: This file

## 🔒 Security Note

This script demonstrates how easily stored credentials can be accessed. Always use strong, unique passwords and consider using a password manager for better security.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/chrome-creds-extractor/issues) if you want to contribute.

## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [@yourlinkedin](https://linkedin.com/in/yourlinkedin)

## 🙏 Acknowledgments

- Google Chrome documentation
- Python cryptography community

This README provides:
A clear description of what the script does
An important disclaimer about ethical use
Features of the script
Requirements and installation instructions
Usage guide
File structure
Security note
Licensing information
Contribution guidelines
Author information
Acknowledgments
Remember to replace placeholders like yourusername with your actual GitHub username, and add any other specific details about your project. Also, ensure you have a LICENSE file in your repository if you mention it in the README.