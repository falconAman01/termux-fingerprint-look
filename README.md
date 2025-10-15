# Termux Fingerprint Authentication Logger

A Python script that authenticates users using fingerprint scanning on Termux and logs all authentication attempts with timestamps.

## Features

- **Fingerprint Authentication**: Uses Termux's fingerprint API to authenticate users
- **Automatic Logging**: Records all authentication attempts with timestamps to `data.log`
- **Real-time Feedback**: Provides immediate success/failure messages
- **Detailed Logs**: Captures complete authentication response including errors and failed attempts

## Prerequisites

- **Termux** (Android terminal emulator)
- **Termux:API** app installed from F-Droid
- **termux-api** package installed
- **Git** (for cloning the repository)

## Installation

1. Install Termux from F-Droid (not Google Play Store)

2. Install Termux:API app from F-Droid

3. Install required packages in Termux:
```bash
pkg update
pkg install termux-api python git
```

4. Grant necessary permissions to Termux:API app in Android settings (especially fingerprint/biometric permissions)

## Download & Setup

Clone the repository:
```bash
git clone https://github.com/falconAman01/termux-fingerprint-look.git
```

Navigate to the project directory:
```bash
cd termux-fingerprint-look
```

## Usage

Run the script:
```bash
python main.py
```

When prompted, scan your fingerprint on your device's fingerprint sensor

Check authentication result:
- Success: "Wellcome! Fingerprint match"
- Failure: "Very Bad! Fingerprint Not match"

All attempts are automatically logged in `data.log` with timestamps

## Viewing Logs

To view the authentication log file:

```bash
cat data.log
```

To view logs with line numbers:
```bash
cat -n data.log
```

To view last 10 entries:
```bash
tail data.log
```

To view logs in real-time (useful when running multiple tests):
```bash
tail -f data.log
```

To view logs page by page:
```bash
less data.log
```

To search for successful authentications only:
```bash
grep "AUTH_RESULT_SUCCESS" data.log
```

To count total authentication attempts:
```bash
wc -l data.log
```

## Quick Start (One-line commands)

```bash
# Download and enter directory
git clone https://github.com/falconAman01/termux-fingerprint-look.git && cd termux-fingerprint-look

# Run the script
python main.py

# View logs after authentication
cat data.log
```

## Log Format

Each log entry contains:
- Timestamp (YYYY-MM-DD HH:MM:SS AM/PM)
- Authentication result in JSON format
- Failed attempt count
- Error messages (if any)

Example log entry:
```
2025-10-15 02:30:45 PM
{
  "errors": [],
  "failed_attempts": 0,
  "auth_result": "AUTH_RESULT_SUCCESS"
}
```

## Response Types

- `AUTH_RESULT_SUCCESS`: Fingerprint matched successfully
- `AUTH_RESULT_FAILURE`: Fingerprint did not match
- `AUTH_RESULT_ERROR`: Error occurred during authentication

## Troubleshooting

- **"termux-fingerprint command not found"**: Install `termux-api` package
- **No fingerprint prompt**: Ensure Termux:API app has necessary permissions
- **Permission denied**: Grant fingerprint access to Termux:API in Android settings
- **Git clone fails**: Check your internet connection and verify the repository URL
- **data.log not found**: Run `python main.py` at least once to generate the log file

## Security Note

This script logs all authentication attempts. Ensure `data.log` is stored securely and not accessible to unauthorized users.

## Repository

GitHub: https://github.com/falconAman01/termux-fingerprint-look.git

## License

Free to use and modify.
