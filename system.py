import platform
import sys
import subprocess
import os

def check_environment():
    print("Operating System:", platform.system())
    print("OS Version:", platform.version())
    print("Machine:", platform.machine())
    print("Platform:", platform.platform())
    print("Processor:", platform.processor())
    print("Python Version:", sys.version)
    print("Python Implementation:", platform.python_implementation())
    print("Python Compiler:", platform.python_compiler())

    # Check installed packages
    try:
        import pip
        installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
        print("Installed Packages:")
        print(installed_packages.decode('utf-8'))
    except ImportError:
        print("Pip is not installed.")

    # Check environment variables
    print("\nEnvironment Variables:")
    for key, value in sorted(dict(os.environ).items()):
        print(f"{key}: {value}")

if __name__ == "__main__":
    check_environment()
