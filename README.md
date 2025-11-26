# Password Generator v2.0

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Cryptographic-red?style=for-the-badge&logo=shield&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0-blue?style=for-the-badge)

**Cryptographically secure password generator with CLI, interactive mode, and strength analysis.**

**Author:** David Osisek (CamoZeroDay)

---

## 🎉 What's New in v2.0

### 🔒 Security Fixes
- ✅ **Fixed insecure `random` module** - Now uses cryptographic `secrets`
- ✅ **Guaranteed character variety** - Ensures all selected character types
- ✅ **Secure shuffling** - Uses SystemRandom for shuffling

### ✨ New Features
- ✅ **Command-line interface** - Full argparse support
- ✅ **Interactive menu** - User-friendly interactive mode
- ✅ **Password strength analyzer** - Visual feedback with suggestions
- ✅ **Multiple passwords** - Generate 1-20 at once
- ✅ **Memorable passphrases** - Easy-to-remember phrases
- ✅ **Custom character sets** - Enable/disable character types
- ✅ **Exclude ambiguous** - Remove confusing characters (il1Lo0O)
- ✅ **Clipboard support** - Copy with one click (optional)
- ✅ **Color-coded output** - Enhanced UI (optional)
- ✅ **Input validation** - Proper bounds checking
- ✅ **Comprehensive help** - Usage examples included

---

## 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/CamoRageaholic1/Password-Generator.git
cd Password-Generator
pip install -r requirements.txt

# Interactive mode (default)
python password_generator_v2.py

# Or use CLI
python password_generator_v2.py -l 20
```

---

## 📚 Features

### Generation Modes

**1. Standard Password**
```
K@9mPx#L2nQ$8vY&Tz4W
  Strength: █████ Very Strong
  Length: 20 characters
```

**2. Memorable Passphrase**
```
Alpha-Bravo-Charlie-Delta42
  Strength: ████░ Strong
  Length: 27 characters
```

**3. Multiple Passwords**
```
 1. K@9mPx#L2nQ$8vY&
 2. Tz4W!bN8xY$2pQm&
 3. L5v#Xn2@Ky8Pw$9M
```

**4. Custom Options**
- Choose character types
- Exclude ambiguous characters
- Set custom length (8-64)

**5. Strength Analysis**
```
Password: MyP@ss
  Strength: ██░░░ Fair
  Length: 6 characters

Suggestions:
  • Too short (min 8)
  • Add more length
```

---

## 🔧 Usage

### Interactive Mode

```bash
python password_generator_v2.py
# or
python password_generator_v2.py -i
```

**Menu:**
```
=== Password Generator ===

1. Generate Standard Password
2. Generate Memorable Passphrase
3. Generate Multiple Passwords
4. Custom Options
5. Analyze Password Strength
6. Quit
```

### Command-Line Mode

**Basic usage:**
```bash
# Generate 16-char password (default)
python password_generator_v2.py

# Generate 20-char password
python password_generator_v2.py -l 20

# Generate 5 passwords
python password_generator_v2.py -m 5
```

**Advanced options:**
```bash
# No symbols
python password_generator_v2.py --no-symbols

# No uppercase
python password_generator_v2.py --no-upper

# Include ambiguous characters
python password_generator_v2.py --include-ambiguous

# Memorable passphrase
python password_generator_v2.py --memorable --words 5

# Copy to clipboard
python password_generator_v2.py -c

# Analyze strength
python password_generator_v2.py --analyze "MyPassword123"
```

### Full CLI Options

```
usage: password_generator_v2.py [-h] [-l LENGTH] [-m MULTIPLE]
                                [--no-upper] [--no-lower]
                                [--no-digits] [--no-symbols]
                                [--include-ambiguous] [--memorable]
                                [--words WORDS] [--analyze ANALYZE]
                                [-c] [-i]

optional arguments:
  -h, --help            show help message
  -l, --length LENGTH   password length (8-64, default: 16)
  -m, --multiple        generate multiple (1-20)
  --no-upper            exclude uppercase
  --no-lower            exclude lowercase
  --no-digits           exclude digits
  --no-symbols          exclude symbols
  --include-ambiguous   include ambiguous (il1Lo0O)
  --memorable           generate passphrase
  --words WORDS         words for passphrase (3-8)
  --analyze ANALYZE     analyze password strength
  -c, --copy            copy to clipboard
  -i, --interactive     interactive mode
```

---

## 📦 Requirements

### Required
- Python 3.8+

### Optional
- pyperclip>=1.8.2 (clipboard)
- colorama>=0.4.6 (colors)

```bash
# Install all (recommended)
pip install -r requirements.txt

# Or minimal (no dependencies)
python password_generator_v2.py
```

---

## 📁 Files

```
Password-Generator/
├── password_generator_v2.py  # v2.0 (use this)
├── Password_Generator.py     # v1.0 (legacy)
├── requirements.txt          # Dependencies
├── CHANGELOG.md              # Version history
├── README.md                 # This file
└── LICENSE                   # MIT License
```

---

## 🔒 Security

### Cryptographic Randomness

**v1.0 (Insecure):**
```python
import random  # Predictable!
password = ''.join(random.choice(chars) for _ in range(n))
```

**v2.0 (Secure):**
```python
import secrets  # Cryptographically secure!
password = ''.join(secrets.choice(chars) for _ in range(n))
```

### Why This Matters

The `random` module uses a **pseudorandom** number generator that can be predicted if an attacker knows the seed. The `secrets` module uses OS-level cryptographically secure randomness.

**For passwords:** Always use `secrets`, never `random`!

---

## 📊 Password Strength Guide

| Length | Characters | Strength | Time to Crack* |
|--------|------------|----------|----------------|
| 8 | All types | Fair | Hours |
| 12 | All types | Good | Years |
| 16 | All types | Strong | Centuries |
| 20+ | All types | Very Strong | Beyond practical |

*Estimated time with modern hardware/techniques

### Character Set Size

- **Uppercase only:** 26 chars
- **+ Lowercase:** 52 chars
- **+ Digits:** 62 chars
- **+ Symbols:** 94 chars
- **- Ambiguous:** 87 chars (recommended)

**More characters = exponentially stronger passwords!**

---

## 🔧 Troubleshooting

**Import errors:**
```bash
pip install pyperclip colorama
```

**Clipboard not working (Linux):**
```bash
sudo apt-install xclip  # or xsel
```

**No colors:**
```bash
pip install colorama
```

---

## 📊 v1.0 vs v2.0

| Feature | v1.0 | v2.0 |
|---------|------|------|
| Random Module | ❌ `random` | ✅ `secrets` |
| CLI Support | ❌ | ✅ |
| Interactive Menu | ❌ | ✅ |
| Strength Analysis | ❌ | ✅ |
| Multiple Generation | ❌ | ✅ |
| Memorable Phrases | ❌ | ✅ |
| Custom Options | ❌ | ✅ |
| Clipboard | ❌ | ✅ |
| Colors | ❌ | ✅ |
| Input Validation | ❌ | ✅ |
| Help System | ❌ | ✅ |

---

## 💡 Examples

### Quick Generation
```bash
# Generate and copy 20-char password
python password_generator_v2.py -l 20 -c

# Generate 10 passwords
python password_generator_v2.py -m 10

# Generate without symbols
python password_generator_v2.py --no-symbols
```

### Memorable Passphrases
```bash
# 4-word passphrase
python password_generator_v2.py --memorable

# 6-word passphrase
python password_generator_v2.py --memorable --words 6
```

### Security Analysis
```bash
# Check your current password
python password_generator_v2.py --analyze "MyCurrentPassword"
```

---

## 🤝 Contributing

Contributions welcome!

**Ideas for v3.0:**
- Pronounceable password generation
- Password policy compliance checker
- Batch generation to file
- API for integration
- GUI version

---

## 📝 License

MIT License - see [LICENSE](LICENSE)

---

## ⚠️ Security Note

**For Security-Critical Applications:**

While this generator uses cryptographic randomness, for highest-security needs consider:
- Hardware random number generators
- Dice-based generation (Diceware)
- Audited password managers

---

**Author:** David Osisek (CamoZeroDay)  
**Version:** 2.0  
**License:** MIT

**🔒 Generate strong passwords. Use unique passwords. Stay secure. 🔒**
