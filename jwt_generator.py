#!/usr/bin/env python3
"""
JWT Generator Tool
Author: [Tu Nombre o Alias]
Description:
  Simple script to generate a signed JWT token, useful for CTFs, pentesting, or testing applications.
"""

import argparse
import json
import jwt
import sys
from pathlib import Path

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error loading {file_path}: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generate a signed JWT token.")
    parser.add_argument("-s", "--secret", required=True, help="Secret key for signing the token.")
    parser.add_argument("-p", "--payload", required=True, help="Path to JSON file containing the payload.")
    parser.add_argument("-hd", "--headers", required=False, help="Path to JSON file containing the headers (optional).")
    parser.add_argument("-a", "--algorithm", default="HS256", help="Signing algorithm (default: HS256).")
    
    args = parser.parse_args()

    secret_key = args.secret
    payload = load_json(args.payload)
    headers = load_json(args.headers) if args.headers else None

    try:
        token = jwt.encode(payload, secret_key, algorithm=args.algorithm, headers=headers)
        print(f"\n[+] JWT generated:\n{token}\n")
    except Exception as e:
        print(f"[!] Error generating token: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
