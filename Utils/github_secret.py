import json
import os
import sys

def create_tokens_file(dictionary, filename='tokens.json'):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)

def main():
    try:
        secret_data = os.environ.get('SECRET')
        if not secret_data:
            print("ERROR: Environment variable 'SECRET' is not set.")
            sys.exit(1)

        env_cookies = json.loads(secret_data)
        cur_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        config = os.path.join(cur_dir, "config/secrets.json")
        create_tokens_file(env_cookies, config)
        print("Tokens file created successfully.")
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON format in 'SECRET': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
