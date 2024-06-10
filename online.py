import requests
import subprocess
import time
import schedule
import threading

# Define the URL of your Codespace environment
codespace_url = "https://super-duper-succotash-q7vj964x475q29qxv.github.dev/"

# Define the interval in seconds for sending requests (e.g., 10 minutes)
request_interval = 600# 10 minutes

def keep_codespace_active():
    while True:
     try:
           # Send a GET request to your Codespace URL
        
        response = requests.get(codespace_url)
        if response.status_code == 200:
           print("Codespace is active.")
        else:
           print(f"Failed to keep Codespace active. Status code: {response.status_code}")
     except Exception as e:
          print(f"An error occurred: {str(e)}")

if __name__ =="__main__":
       
      print("starting keep codespace active")  
while True:
      keep_codespace_active()          
      print(f"Waiting for {request_interval} seconds before the next request...")
      time.sleep(request_interval) 