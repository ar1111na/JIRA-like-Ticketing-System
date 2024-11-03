import subprocess
import django

# List of apps to test
apps = ['users', 'tickets', 'dashboard']

# Run tests for each app
for app in apps:
    print(f"Running tests for the {app} app...")
    result = subprocess.run(['python', 'manage.py', 'test', app], capture_output=True, text=True)
    
    # Print the output
    print(result.stdout)
    print(result.stderr)
