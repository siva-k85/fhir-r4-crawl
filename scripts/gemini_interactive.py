#!/usr/bin/env python3
"""Interactive Gemini CLI - Chat interface with conversation history and file context."""

import argparse
import json
import os
import pathlib
import sys
import textwrap
from datetime import datetime
from typing import List, Optional, Dict, Any

try:
    import google.generativeai as genai
except ModuleNotFoundError:
    print("Please install google-generativeai: pip install google-generativeai")
    sys.exit(1)


# ANSI color codes for better terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def load_dotenv() -> None:
    """Load environment variables from the repo-level .env file."""
    dotenv_path = pathlib.Path(__file__).resolve().parent.parent / ".env"
    if not dotenv_path.exists():
        return
    try:
        lines = dotenv_path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return
    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if not key or key in os.environ:
            continue
        value = value.strip().strip('"').strip("'")
        os.environ[key] = value


class InteractiveGeminiCLI:
    """Interactive CLI for chatting with Gemini models."""

    def __init__(self, model_name: str = "gemini-2.5-pro", temperature: float = 0.7):
        """Initialize the interactive CLI."""
        self.model_name = model_name
        self.temperature = temperature
        self.conversation_history = []
        self.model = None
        self.chat = None
        self.context_files = {}
        self._setup_model()

    def _setup_model(self) -> None:
        """Configure and initialize the Gemini model."""
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print(f"{Colors.RED}Error: Set GEMINI_API_KEY in your .env file{Colors.ENDC}")
            sys.exit(1)

        genai.configure(api_key=api_key)

        system_instruction = """You are a helpful AI assistant in an interactive chat session.
        You can help with coding, analysis, explanations, and general questions.
        When the user references files they've loaded, use that context in your responses.
        Be conversational but concise unless asked for detailed explanations."""

        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=system_instruction,
            generation_config=genai.types.GenerationConfig(
                temperature=self.temperature,
                max_output_tokens=2048,
            )
        )
        self.chat = self.model.start_chat(history=[])

    def print_welcome(self) -> None:
        """Print welcome message and help information."""
        print(f"\n{Colors.BOLD}{Colors.CYAN}🤖 Gemini Interactive CLI{Colors.ENDC}")
        print(f"{Colors.GREEN}Model: {self.model_name} | Temperature: {self.temperature}{Colors.ENDC}")
        print("-" * 60)
        print("Commands:")
        print("  /help         - Show this help message")
        print("  /load <file>  - Load a file into context")
        print("  /files        - List loaded files")
        print("  /clear        - Clear conversation history")
        print("  /save [file]  - Save conversation to JSON")
        print("  /model <name> - Change model")
        print("  /temp <value> - Set temperature (0.0-1.0)")
        print("  /exit or /quit - Exit the CLI")
        print("-" * 60)
        print(f"{Colors.CYAN}Type your message or a command. Press Ctrl+D to send multi-line input.{Colors.ENDC}\n")

    def load_file(self, filepath: str) -> bool:
        """Load a file into context."""
        path = pathlib.Path(filepath)
        if not path.exists():
            print(f"{Colors.RED}File not found: {filepath}{Colors.ENDC}")
            return False

        try:
            content = path.read_text(encoding='utf-8')
            self.context_files[str(path)] = content[:8000]  # Limit file size
            print(f"{Colors.GREEN}✓ Loaded: {path.name} ({len(content)} chars){Colors.ENDC}")
            return True
        except Exception as e:
            print(f"{Colors.RED}Error loading file: {e}{Colors.ENDC}")
            return False

    def list_files(self) -> None:
        """List all loaded files."""
        if not self.context_files:
            print(f"{Colors.WARNING}No files loaded{Colors.ENDC}")
        else:
            print(f"\n{Colors.BOLD}Loaded files:{Colors.ENDC}")
            for filepath in self.context_files:
                size = len(self.context_files[filepath])
                print(f"  • {filepath} ({size} chars)")

    def save_conversation(self, filepath: Optional[str] = None) -> None:
        """Save conversation history to a JSON file."""
        if not filepath:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"gemini_chat_{timestamp}.json"

        try:
            conversation_data = {
                "timestamp": datetime.now().isoformat(),
                "model": self.model_name,
                "temperature": self.temperature,
                "messages": self.conversation_history,
                "context_files": list(self.context_files.keys())
            }

            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(conversation_data, f, indent=2, ensure_ascii=False)

            print(f"{Colors.GREEN}✓ Conversation saved to: {filepath}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.RED}Error saving conversation: {e}{Colors.ENDC}")

    def clear_conversation(self) -> None:
        """Clear the conversation history."""
        self.conversation_history = []
        self.chat = self.model.start_chat(history=[])
        print(f"{Colors.GREEN}✓ Conversation cleared{Colors.ENDC}")

    def change_model(self, model_name: str) -> None:
        """Change the active model."""
        try:
            self.model_name = model_name
            self._setup_model()
            print(f"{Colors.GREEN}✓ Switched to model: {model_name}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.RED}Error changing model: {e}{Colors.ENDC}")

    def set_temperature(self, temp_str: str) -> None:
        """Set the temperature parameter."""
        try:
            temp = float(temp_str)
            if 0.0 <= temp <= 1.0:
                self.temperature = temp
                self.model._generation_config.temperature = temp
                print(f"{Colors.GREEN}✓ Temperature set to: {temp}{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}Temperature must be between 0.0 and 1.0{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.RED}Invalid temperature value{Colors.ENDC}")

    def process_command(self, command: str) -> bool:
        """Process a command. Returns True if should continue, False to exit."""
        parts = command.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd in ['/exit', '/quit']:
            return False
        elif cmd == '/help':
            self.print_welcome()
        elif cmd == '/load':
            if arg:
                self.load_file(arg)
            else:
                print(f"{Colors.WARNING}Usage: /load <filepath>{Colors.ENDC}")
        elif cmd == '/files':
            self.list_files()
        elif cmd == '/clear':
            self.clear_conversation()
        elif cmd == '/save':
            self.save_conversation(arg if arg else None)
        elif cmd == '/model':
            if arg:
                self.change_model(arg)
            else:
                print(f"{Colors.WARNING}Usage: /model <model_name>{Colors.ENDC}")
        elif cmd == '/temp':
            if arg:
                self.set_temperature(arg)
            else:
                print(f"{Colors.WARNING}Usage: /temp <0.0-1.0>{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}Unknown command: {command}{Colors.ENDC}")

        return True

    def get_multiline_input(self, prompt: str) -> str:
        """Get potentially multi-line input from user."""
        lines = []
        print(prompt, end='')

        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:  # Ctrl+D pressed
            pass
        except KeyboardInterrupt:  # Ctrl+C pressed
            return ""

        return '\n'.join(lines).strip()

    def format_message_with_context(self, message: str) -> str:
        """Add file context to message if files are loaded."""
        if not self.context_files:
            return message

        context_parts = [message, "\n\n--- Loaded File Context ---"]
        for filepath, content in self.context_files.items():
            filename = pathlib.Path(filepath).name
            context_parts.append(f"\n### {filename}\n```\n{content[:2000]}...\n```")

        return '\n'.join(context_parts)

    def send_message(self, message: str) -> None:
        """Send a message to Gemini and print the response."""
        try:
            # Add file context if available
            full_message = self.format_message_with_context(message)

            # Send to model
            response = self.chat.send_message(full_message)

            # Store in history
            self.conversation_history.append({
                "role": "user",
                "content": message,
                "timestamp": datetime.now().isoformat()
            })

            self.conversation_history.append({
                "role": "assistant",
                "content": response.text,
                "timestamp": datetime.now().isoformat()
            })

            # Print response
            print(f"\n{Colors.BOLD}{Colors.BLUE}Gemini:{Colors.ENDC}")
            print(response.text)
            print()

        except Exception as e:
            print(f"\n{Colors.RED}Error: {e}{Colors.ENDC}\n")

    def run(self) -> None:
        """Run the interactive CLI loop."""
        self.print_welcome()

        while True:
            try:
                # Get user input
                user_input = self.get_multiline_input(f"{Colors.GREEN}You: {Colors.ENDC}")

                if not user_input:
                    continue

                # Check if it's a command
                if user_input.startswith('/'):
                    if not self.process_command(user_input):
                        print(f"\n{Colors.CYAN}Goodbye! 👋{Colors.ENDC}")
                        break
                else:
                    # Send as message to Gemini
                    self.send_message(user_input)

            except KeyboardInterrupt:
                print(f"\n\n{Colors.CYAN}Use /exit to quit or Ctrl+D to send multi-line input{Colors.ENDC}\n")
            except Exception as e:
                print(f"\n{Colors.RED}Unexpected error: {e}{Colors.ENDC}\n")


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Interactive Gemini CLI - Chat with Google's Gemini AI"
    )
    parser.add_argument(
        "--model",
        default="gemini-2.5-pro",
        help="Gemini model to use (default: gemini-2.5-pro)"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Temperature for response generation (0.0-1.0, default: 0.7)"
    )
    parser.add_argument(
        "--load",
        nargs="*",
        help="Files to load at startup"
    )
    return parser.parse_args()


def main() -> None:
    """Main entry point."""
    args = parse_args()

    # Create and configure CLI
    cli = InteractiveGeminiCLI(
        model_name=args.model,
        temperature=args.temperature
    )

    # Load any initial files
    if args.load:
        for filepath in args.load:
            cli.load_file(filepath)

    # Run the interactive loop
    cli.run()


if __name__ == "__main__":
    main()