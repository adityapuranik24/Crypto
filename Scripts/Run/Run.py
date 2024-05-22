import os
import subprocess



def run_consumer():
    # The directory you want to change to
    new_directory = "D:/Projects/Crypto/Scripts/Kafka"

    # Change the current working directory
    os.chdir(new_directory)

    # Verify the change
    print(f"Changed directory to {os.getcwd()}")

    # Define the command you want to run
    command = ["python Consumer.py worker"]

    # Run the command in the new directory
    process = subprocess.run(command, text=True, capture_output=True)

    # Print the command's output
    print(process.stdout)

    # Check if the command was successful
    if process.returncode == 0:
        return print("Command executed successfully")
    else:
        return print(f"Command failed with status {process.returncode}")
    

run_consumer()
