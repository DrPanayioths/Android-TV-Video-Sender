import subprocess
import os
# Install The Dependencies Required To Run This Script :)
subprocess.run("pip install python-dotenv")
from dotenv import load_dotenv

# Load Config File So We Can Use The Settings The User Setted
dotenv_path = os.path.join(os.path.dirname(__file__), 'config.env')
adb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'platform-tools', 'adb.exe')
load_dotenv(dotenv_path)
subprocess.run("color 9", shell=True)

exit_selection="a"
connection_status="no"

while exit_selection.lower() == "a":
    print()
    
    if connection_status != "yes":
        android_tv_ip = os.getenv('atv_ip')
        connection_status="yes"
        subprocess.run(f'"{adb_path}" connect {android_tv_ip}')
        
    print("-------------------------------")

    video_url = input("Enter YouTube Video URL: ")
    video_id = video_url.split('v=')[-1].split('&')[0]
    final_url = "https://www.youtube.com/watch?v=" + video_id

    print("-------------------------------")
    subprocess.run([adb_path, "shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", final_url])
    print("-------------------------------")
    print()
    exit_selection = input("Press A to rerun OR anything else to exit: ")
    subprocess.run("cls", shell=True)
    



