#!/usr/bin/env python3
"""
Password Generator v2.0
Author: David Osisek (CamoZeroDay)
Description: Secure password generator with multiple options and strength analysis
"""

import secrets
import string
import argparse
import sys

try:
    import pyperclip
    CLIPBOARD = True
except ImportError:
    CLIPBOARD = False

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False
    class Fore:
        RED = GREEN = YELLOW = CYAN = MAGENTA = ""
    class Style:
        RESET_ALL = ""

class PasswordGenerator:
    """Secure password generator with cryptographic randomness"""
    
    def __init__(self):
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.symbols = string.punctuation
        self.ambiguous = 'il1Lo0O'
    
    def generate(self, length=16, use_upper=True, use_lower=True, 
                use_digits=True, use_symbols=True, exclude_ambiguous=True):
        """
        Generate a secure password using cryptographic randomness
        
        Args:
            length: Password length (default 16)
            use_upper: Include uppercase letters
            use_lower: Include lowercase letters
            use_digits: Include digits
            use_symbols: Include symbols
            exclude_ambiguous: Exclude ambiguous characters (il1Lo0O)
        
        Returns:
            Generated password string
        """
        # Build character set
        chars = ''
        required = []
        
        if use_upper:
            chars += self.uppercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous)
            required.append(secrets.choice([c for c in self.uppercase if c not in self.ambiguous] 
                                         if exclude_ambiguous else self.uppercase))
        
        if use_lower:
            lower_chars = self.lowercase
            if exclude_ambiguous:
                lower_chars = ''.join(c for c in lower_chars if c not in self.ambiguous)
            chars += lower_chars
            required.append(secrets.choice(lower_chars))
        
        if use_digits:
            digit_chars = self.digits
            if exclude_ambiguous:
                digit_chars = ''.join(c for c in digit_chars if c not in self.ambiguous)
            chars += digit_chars
            required.append(secrets.choice(digit_chars))
        
        if use_symbols:
            chars += self.symbols
            required.append(secrets.choice(self.symbols))
        
        if not chars:
            raise ValueError("At least one character type must be selected")
        
        # Ensure minimum length for required characters
        if length < len(required):
            length = len(required)
        
        # Generate password
        password = required.copy()
        password += [secrets.choice(chars) for _ in range(length - len(required))]
        
        # Shuffle using cryptographic randomness
        secrets.SystemRandom().shuffle(password)
        
        return ''.join(password)
    
    def generate_multiple(self, count, **kwargs):
        """Generate multiple passwords"""
        return [self.generate(**kwargs) for _ in range(count)]
    
    def generate_memorable(self, words=4, separator='-', capitalize=True, add_number=True):
        """
        Generate a memorable passphrase
        
        Args:
            words: Number of words
            separator: Character between words
            capitalize: Capitalize first letter of each word
            add_number: Add a number at the end
        
        Returns:
            Memorable passphrase
        """
        # Simple word list for demonstration
        word_list = [
            'alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot',
            'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima',
            'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo',
            'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray',
            'yankee', 'zulu', 'coffee', 'python', 'tiger', 'ocean',
            'mountain', 'river', 'forest', 'desert', 'cloud', 'thunder',
            'lightning', 'rainbow', 'sunset', 'sunrise', 'winter', 'summer'
        ]
        
        selected = [secrets.choice(word_list) for _ in range(words)]
        
        if capitalize:
            selected = [w.capitalize() for w in selected]
        
        passphrase = separator.join(selected)
        
        if add_number:
            passphrase += str(secrets.randbelow(100))
        
        return passphrase
    
    def check_strength(self, password):
        """
        Analyze password strength
        
        Returns:
            Tuple of (score, feedback)
        """
        score = 0
        feedback = []
        
        # Length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Too short (min 8)")
        
        if len(password) >= 12:
            score += 1
        
        if len(password) >= 16:
            score += 1
        
        # Character variety
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if any(c in string.punctuation for c in password):
            score += 1
        else:
            feedback.append("Add symbols")
        
        return min(score, 5), feedback
    
    def display_strength(self, password):
        """Display password strength with visual indicator"""
        score, feedback = self.check_strength(password)
        
        labels = [
            ("Very Weak", Fore.RED),
            ("Weak", Fore.RED),
            ("Fair", Fore.YELLOW),
            ("Good", Fore.YELLOW),
            ("Strong", Fore.GREEN),
            ("Very Strong", Fore.GREEN)
        ]
        
        label, color = labels[score]
        bars = "█" * score + "░" * (5 - score)
        
        print(f"\n{Fore.CYAN}Strength Analysis:{Style.RESET_ALL}")
        print(f"  {color}{bars} {label}{Style.RESET_ALL}")
        print(f"  Length: {len(password)} characters")
        
        if feedback:
            print(f"\n{Fore.YELLOW}Suggestions:{Style.RESET_ALL}")
            for tip in feedback:
                print(f"  • {tip}")

def interactive_mode():
    """Interactive password generation mode"""
    gen = PasswordGenerator()
    
    print(f"{Fore.CYAN}")
    print("  ╔═══════════════════════════════════╗")
    print("  ║  Password Generator v2.0          ║")
    print("  ║  By David Osisek (CamoZeroDay)    ║")
    print("  ╚═══════════════════════════════════╝")
    print(f"{Style.RESET_ALL}\n")
    
    if not CLIPBOARD:
        print(f"{Fore.YELLOW}Note: Install pyperclip for clipboard support{Style.RESET_ALL}\n")
    
    while True:
        print(f"{Fore.MAGENTA}=== Password Generator ==={Style.RESET_ALL}\n")
        print("1. Generate Standard Password")
        print("2. Generate Memorable Passphrase")
        print("3. Generate Multiple Passwords")
        print("4. Custom Options")
        print("5. Analyze Password Strength")
        print("6. Quit\n")
        
        choice = input(f"{Fore.CYAN}Choose option: {Style.RESET_ALL}").strip()
        
        try:
            if choice == '1':
                # Standard password
                length = input(f"{Fore.CYAN}Length (8-64, default 16): {Style.RESET_ALL}").strip()
                length = int(length) if length else 16
                length = max(8, min(64, length))
                
                password = gen.generate(length)
                print(f"\n{Fore.GREEN}Generated Password:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}{password}{Style.RESET_ALL}")
                gen.display_strength(password)
                
                if CLIPBOARD:
                    if input(f"\n{Fore.CYAN}Copy to clipboard? (y/n): {Style.RESET_ALL}").lower() == 'y':
                        try:
                            pyperclip.copy(password)
                            print(f"{Fore.GREEN}✓ Copied!{Style.RESET_ALL}")
                        except:
                            print(f"{Fore.RED}✗ Copy failed{Style.RESET_ALL}")
            
            elif choice == '2':
                # Memorable passphrase
                words = input(f"{Fore.CYAN}Number of words (3-8, default 4): {Style.RESET_ALL}").strip()
                words = int(words) if words else 4
                words = max(3, min(8, words))
                
                passphrase = gen.generate_memorable(words=words)
                print(f"\n{Fore.GREEN}Generated Passphrase:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}{passphrase}{Style.RESET_ALL}")
                gen.display_strength(passphrase)
                
                if CLIPBOARD:
                    if input(f"\n{Fore.CYAN}Copy to clipboard? (y/n): {Style.RESET_ALL}").lower() == 'y':
                        try:
                            pyperclip.copy(passphrase)
                            print(f"{Fore.GREEN}✓ Copied!{Style.RESET_ALL}")
                        except:
                            pass
            
            elif choice == '3':
                # Multiple passwords
                count = input(f"{Fore.CYAN}How many? (1-20): {Style.RESET_ALL}").strip()
                count = int(count) if count else 5
                count = max(1, min(20, count))
                
                length = input(f"{Fore.CYAN}Length (default 16): {Style.RESET_ALL}").strip()
                length = int(length) if length else 16
                length = max(8, min(64, length))
                
                passwords = gen.generate_multiple(count, length=length)
                
                print(f"\n{Fore.GREEN}Generated {count} Passwords:{Style.RESET_ALL}")
                for i, pw in enumerate(passwords, 1):
                    print(f"{i:2}. {pw}")
            
            elif choice == '4':
                # Custom options
                print(f"\n{Fore.CYAN}Customize your password:{Style.RESET_ALL}")
                
                length = int(input("Length (8-64): ") or "16")
                length = max(8, min(64, length))
                
                use_upper = input("Uppercase letters? (Y/n): ").lower() != 'n'
                use_lower = input("Lowercase letters? (Y/n): ").lower() != 'n'
                use_digits = input("Numbers? (Y/n): ").lower() != 'n'
                use_symbols = input("Symbols? (Y/n): ").lower() != 'n'
                exclude_ambiguous = input("Exclude ambiguous (il1Lo0O)? (Y/n): ").lower() != 'n'
                
                password = gen.generate(
                    length=length,
                    use_upper=use_upper,
                    use_lower=use_lower,
                    use_digits=use_digits,
                    use_symbols=use_symbols,
                    exclude_ambiguous=exclude_ambiguous
                )
                
                print(f"\n{Fore.GREEN}Generated Password:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}{password}{Style.RESET_ALL}")
                gen.display_strength(password)
                
                if CLIPBOARD:
                    if input(f"\n{Fore.CYAN}Copy to clipboard? (y/n): {Style.RESET_ALL}").lower() == 'y':
                        try:
                            pyperclip.copy(password)
                            print(f"{Fore.GREEN}✓ Copied!{Style.RESET_ALL}")
                        except:
                            pass
            
            elif choice == '5':
                # Analyze strength
                password = input(f"\n{Fore.CYAN}Enter password to analyze: {Style.RESET_ALL}")
                gen.display_strength(password)
            
            elif choice == '6':
                print(f"\n{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
                break
            
            else:
                print(f"{Fore.RED}✗ Invalid choice{Style.RESET_ALL}")
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
            print("\n" * 2)
            
        except ValueError as e:
            print(f"{Fore.RED}✗ Error: {e}{Style.RESET_ALL}")
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}Interrupted{Style.RESET_ALL}")
            break

def main():
    """Main entry point with CLI support"""
    parser = argparse.ArgumentParser(
        description='Secure Password Generator v2.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s -l 20                    # Generate 20-char password
  %(prog)s -m 5 -l 16               # Generate 5 passwords of 16 chars
  %(prog)s --no-symbols             # Generate without symbols
  %(prog)s --memorable              # Generate memorable passphrase
  %(prog)s --analyze "MyPass123"    # Analyze password strength
        """
    )
    
    parser.add_argument('-l', '--length', type=int, default=16,
                       help='Password length (8-64, default: 16)')
    parser.add_argument('-m', '--multiple', type=int, default=1,
                       help='Generate multiple passwords (1-20)')
    parser.add_argument('--no-upper', action='store_true',
                       help='Exclude uppercase letters')
    parser.add_argument('--no-lower', action='store_true',
                       help='Exclude lowercase letters')
    parser.add_argument('--no-digits', action='store_true',
                       help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_true',
                       help='Exclude symbols')
    parser.add_argument('--include-ambiguous', action='store_true',
                       help='Include ambiguous characters (il1Lo0O)')
    parser.add_argument('--memorable', action='store_true',
                       help='Generate memorable passphrase')
    parser.add_argument('--words', type=int, default=4,
                       help='Number of words for passphrase (3-8)')
    parser.add_argument('--analyze', type=str,
                       help='Analyze strength of given password')
    parser.add_argument('-c', '--copy', action='store_true',
                       help='Copy to clipboard')
    parser.add_argument('-i', '--interactive', action='store_true',
                       help='Interactive mode')
    
    args = parser.parse_args()
    
    # Interactive mode
    if args.interactive or len(sys.argv) == 1:
        interactive_mode()
        return
    
    gen = PasswordGenerator()
    
    # Analyze mode
    if args.analyze:
        print(f"{Fore.CYAN}Analyzing password...{Style.RESET_ALL}")
        gen.display_strength(args.analyze)
        return
    
    # Generate memorable passphrase
    if args.memorable:
        words = max(3, min(8, args.words))
        password = gen.generate_memorable(words=words)
        print(f"{Fore.GREEN}Passphrase: {Fore.YELLOW}{password}{Style.RESET_ALL}")
        gen.display_strength(password)
        
        if args.copy and CLIPBOARD:
            try:
                pyperclip.copy(password)
                print(f"\n{Fore.GREEN}✓ Copied to clipboard{Style.RESET_ALL}")
            except:
                pass
        return
    
    # Generate standard password(s)
    length = max(8, min(64, args.length))
    count = max(1, min(20, args.multiple))
    
    if count == 1:
        password = gen.generate(
            length=length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            exclude_ambiguous=not args.include_ambiguous
        )
        
        print(f"{Fore.GREEN}Password: {Fore.YELLOW}{password}{Style.RESET_ALL}")
        gen.display_strength(password)
        
        if args.copy and CLIPBOARD:
            try:
                pyperclip.copy(password)
                print(f"\n{Fore.GREEN}✓ Copied to clipboard{Style.RESET_ALL}")
            except:
                pass
    else:
        passwords = gen.generate_multiple(
            count,
            length=length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            exclude_ambiguous=not args.include_ambiguous
        )
        
        print(f"{Fore.GREEN}Generated {count} passwords:{Style.RESET_ALL}\n")
        for i, pw in enumerate(passwords, 1):
            print(f"{i:2}. {pw}")

if __name__ == "__main__":
    main()
