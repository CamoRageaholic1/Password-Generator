# Changelog

## [2.0.0] - 2025-11-26

### Added
- ✅ **Cryptographically secure randomness** - Using `secrets` module instead of `random`
- ✅ **Command-line interface** - Full argparse support with many options
- ✅ **Interactive menu** - User-friendly interactive mode
- ✅ **Password strength analyzer** - Visual strength indicator with suggestions
- ✅ **Multiple password generation** - Generate 1-20 passwords at once
- ✅ **Memorable passphrases** - Generate easy-to-remember passphrases
- ✅ **Custom character sets** - Enable/disable uppercase, lowercase, digits, symbols
- ✅ **Exclude ambiguous characters** - Option to remove confusing characters (il1Lo0O)
- ✅ **Clipboard support** - Copy passwords with pyperclip (optional)
- ✅ **Color-coded output** - Enhanced UI with colorama (optional)
- ✅ **Input validation** - Proper error handling and bounds checking
- ✅ **Help system** - Comprehensive --help documentation
- ✅ **Examples in help** - Usage examples for common scenarios

### Security
- 🔒 **Fixed insecure `random` module** - Now uses cryptographic `secrets`
- 🔒 **Guaranteed character variety** - Ensures password contains all selected types
- 🔒 **Secure shuffling** - Uses SystemRandom for shuffling

### Changed
- Complete rewrite with OOP structure
- Improved code organization
- Better user experience
- Professional CLI interface

## [1.0.0] - Initial Release

### Features
- Basic password generation
- Customizable length
- Simple interactive loop
