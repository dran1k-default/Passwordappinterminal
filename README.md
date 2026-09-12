# PasswordAppTerminal 🔐

A simple command-line password manager written in Python. Generate strong random passwords or store your own, save them to a local file, and browse, review, or delete them — all from an interactive terminal menu.

## Features

- **Random password generator** — creates a 12-character password mixing letters, digits, and punctuation for any service name you provide
- **Manual password entry** — save a password you've already chosen for a given service
- **Session viewer** — see every password you've added during the current run, without re-reading the file
- **Saved password viewer** — list every service/password pair ever saved, read straight from `passwords.txt`
- **Password deletion** — remove a saved entry by service name
- **Persistent local storage** — all passwords are appended to a plain-text file (`passwords.txt`) so they survive between runs

## Tech Stack

- Python 3
- Built-in `random` and `string` modules for password generation
- Plain-text file storage (no external dependencies)

## Requirements

- Python 3.9+

## Getting Started

1. Clone the repo:

   ```
   git clone https://github.com/dran1k-default/Passwordappinterminal.git
   cd Passwordappinterminal
   ```

2. Run the app:

   ```
   python main.py
   ```

3. Choose an option from the menu that appears.

> ⚠️ Passwords are stored in plain text in `passwords.txt`.

## Project Structure

```
Passwordappinterminal/
├── main.py          # Entry point — main menu loop, dispatches to each feature
├── main_func.py      # Core functions — password generation, saving, viewing, deleting
└── passwords.txt      # Local storage file (service:password, one per line)
```

## How It Works

1. `start_screen` prints the main menu and reads which option the user picked.
2. Option `1` (`random_password_generation`) generates a random 12-character password for a named service, stores it in memory, and appends it to `passwords.txt`.
3. Option `2` (`create_password_manualy`) lets the user type their own password for a named service and saves it the same way.
4. Option `3` (`all_passwords_viewer`) reads `passwords.txt` and prints every saved entry.
5. Option `4` (`session_password_viewer`) prints only the passwords added during the current session, from the in-memory dictionary.
6. Option `5` (`password_delete`) shows the saved entries, asks for a service name, and rewrites `passwords.txt` without that entry.
7. Option `6` exits the program.