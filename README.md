# Password Generator

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Password_Tool-red?style=for-the-badge&logo=key&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Simple command-line tool to generate secure random passwords with customizable length.

## 🎯 Purpose

Create strong, random passwords quickly using Python's built-in cryptographic randomness. Perfect for generating secure credentials for new accounts or updating existing passwords.

## ✨ Features

- ✅ **Customizable Length** - Generate passwords of any length
- ✅ **Strong Character Set** - Includes uppercase, lowercase, numbers, and symbols
- ✅ **Cryptographically Random** - Uses Python's `random` module
- ✅ **Interactive CLI** - Simple command-line interface
- ✅ **Quick Generation** - Create multiple passwords in one session
- ✅ **Zero Dependencies** - Uses only Python standard library

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher (no additional dependencies!)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/CamoRageaholic1/Password-Generator.git
   cd Password-Generator
   ```

2. **Run the script**
   ```bash
   python Password_Generator.py
   ```

## 📖 Usage Guide

### Basic Usage

```bash
$ python Password_Generator.py

Enter the desired password length: 16
Generated password: 7xK@3#mP!nQ$8zR%

Press Enter to generate another password or type 'exit' to quit:
```

### Generate Multiple Passwords

```bash
$ python Password_Generator.py

Enter the desired password length: 20
Generated password: aB3!dE5@gH7#jK9$mN1%

Press Enter to generate another password or type 'exit' to quit: [Enter]

Enter the desired password length: 12
Generated password: xY2!wZ4@vU6#

Press Enter to generate another password or type 'exit' to quit: exit
```

## 🔒 Password Strength

### Character Set

The generator uses a comprehensive character set:

| Type | Characters | Count |
|------|------------|-------|
| **Uppercase** | A-Z | 26 |
| **Lowercase** | a-z | 26 |
| **Digits** | 0-9 | 10 |
| **Symbols** | !@#$%^&*()_+-=[]{};\|:<>?,. | 32 |
| **Total** | | 94 |

### Recommended Lengths

| Use Case | Recommended Length | Security Level |
|----------|-------------------|----------------|
| Low security accounts | 8-10 characters | Basic |
| General accounts | 12-16 characters | Good |
| Sensitive accounts | 16-20 characters | Strong |
| High-security systems | 20+ characters | Very Strong |
| Passwords for encryption | 32+ characters | Maximum |

### Example Passwords

```bash
Length 8:  aB3!xY7@
Length 12: xK9#pL2$mN5!
Length 16: wZ7@vU3#tS9$qR1!
Length 20: dF8!cE2@bD6#aA4$zX0%
```

## 💡 Best Practices

### Using Generated Passwords

1. **Never reuse passwords** - Generate unique password for each account
2. **Use a password manager** - Store generated passwords securely
3. **Enable 2FA** - Add second factor authentication when available
4. **Update regularly** - Change passwords periodically for sensitive accounts

### Security Tips

- ✅ **DO:** Use passwords 12+ characters for important accounts
- ✅ **DO:** Combine with password manager
- ✅ **DO:** Generate new password when security is compromised
- ❌ **DON'T:** Use generated password for multiple accounts
- ❌ **DON'T:** Write passwords on sticky notes
- ❌ **DON'T:** Share passwords over insecure channels

## 🔧 Customization

### Modify Character Set

Edit `Password_Generator.py` to customize the character set:

```python
# Only alphanumeric (no symbols)
characters = string.ascii_letters + string.digits

# Only letters and numbers (no special chars)
characters = string.ascii_letters + string.digits

# Custom character set
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
```

### Add Password Strength Meter

```python
def check_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    elif len(password) < 16:
        return "Strong"
    else:
        return "Very Strong"
```

## 📁 Project Structure

```
Password-Generator/
├── Password_Generator.py    # Main password generator
├── README.md                # This file
└── LICENSE                  # MIT License
```

## 🛠️ Troubleshooting

### "SyntaxError" or script won't run
Ensure you're using Python 3:
```bash
python3 Password_Generator.py
```

### Want to run without typing Python command
Make executable (Linux/macOS):
```bash
chmod +x Password_Generator.py
./Password_Generator.py
```

Or create shortcut (Windows):
- Right-click → "Send to" → "Desktop (create shortcut)"

## 🚀 Future Enhancements

Ideas for improvements:

- [ ] Add password strength meter
- [ ] Include pronounceable password option
- [ ] Add password history/clipboard copy
- [ ] Create GUI version
- [ ] Add pattern exclusions (no similar characters like O/0, l/1)
- [ ] Export passwords to file
- [ ] Integration with password managers

## 🤝 Contributing

Contributions welcome! Some ideas:

- Improve randomness (use `secrets` module for production)
- Add configuration file support
- Create batch password generation
- Add password complexity checker
- Implement different password patterns

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔐 Security Note

For production use or highly sensitive applications, consider using Python's `secrets` module instead of `random` for cryptographically secure random number generation:

```python
import secrets
password = ''.join(secrets.choice(characters) for _ in range(length))
```

## 📫 Support

- 🐛 **Bug Reports:** Open an issue on GitHub  
- 💡 **Feature Requests:** Open an issue with the "enhancement" label

---

**Author:** David Osisek (CamoZeroDay)  
**Made with ❤️ for secure password generation**
