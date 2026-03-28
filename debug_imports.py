import os
import sys

print(f"Current Directory: {os.getcwd()}")
print(f"sys.path: {sys.path}")
print(f"Directory items: {os.listdir('.')}")
if os.path.isdir('modules'):
    print("modules is a directory")
    print(f"modules contents: {os.listdir('modules')}")
else:
    print("modules is NOT a directory")

try:
    import modules
    print("Successfully imported modules")
except ImportError as e:
    print(f"ImportError: {e}")
