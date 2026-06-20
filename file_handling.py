import os
import shutil

try:
    # Create and write file
    with open("sample.txt", "w") as file:
        file.write("Hello Alfido Internship")

    print("✓ File Created")

    # Read file
    with open("sample.txt", "r") as file:
        content = file.read()
        print("Content:", content)

    # Rename file
    os.rename("sample.txt", "new_sample.txt")
    print("✓ File Renamed")

    # Create folder
    os.makedirs("backup", exist_ok=True)

    # Move file
    shutil.move("new_sample.txt", "backup/new_sample.txt")
    print("✓ File Moved")

    # Delete file
    os.remove("backup/new_sample.txt")
    print("✓ File Deleted")

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)