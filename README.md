# JWT Generator Tool

Simple script to generate a signed JWT token, useful for CTFs, pentesting, or application testing.

## Features
- Supports custom payloads and headers (JSON format).
- Supports different signing algorithms (default: HS256).
- Useful for CTFs, hacking challenges, and pentesting scenarios involving JWTs.

## Installation
```bash
git clone https://github.com/lluriam19/jwt-generator.git
cd jwt-generator
pip install -r requirements.txt
```

## Usage

` python3 jwt_generator.py -s <SECRET_KEY> -p <PAYLOAD_FILE> [-hd <HEADERS_FILE>] [-a <ALGORITHM>]`

Arguments:
- -s, --secret: Secret key used to sign the token.
- -p, --payload: Path to a JSON file containing the payload.
- -hd, --headers: Path to a JSON file containing the headers (optional).
- -a, --algorithm: Algorithm to use (default is HS256).

# Example
`python3 jwt_generator.py -s "supersecretkey" -p examples/payload.json -hd examples/headers.json`

# Example Output
`[+] JWT generated:
eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCIsICJraWQiOiAiL3BhdGgvdG8veW91ci5rZXkifQ.eyJkYXRhIjp7InVzZXJfaWQiOjEsImVtYWlsIjoidXNlckBleGFtcGxlLmNvbSIsInJvbGUiOiJhZG1pbiJ9fQ.Nflq4kxh3J5SgSDgJk1ybbKOI3qzMZ2jbbF9TmSk09w `

