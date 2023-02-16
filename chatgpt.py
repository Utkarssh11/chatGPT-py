import requests
import time
import sys
import os

def write(text, speed=0.02):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()

    time.sleep(speed)

  print("")

def clear():
  os.system('clear')

def fg(r,g,b):
  return f'\033[38;2;{r};{g};{b}m'

def bg(r,b,g):
  return f"\033[48;2;{r};{g};{b}m"

fg_red = fg(242,78,78)
fg_orange = fg(255,168,5)
fg_yellow = fg(249,255,89)
fg_light_green = '\033[92m'
fg_green = '\033[32m'
fg_lightblue = '\033[94m'
fg_blue = '\033[34m'
fg_dark_blue = fg(161,206,255)

bg_red = bg(242,78,78)
bg_orange = bg(255,168,5)
bg_yellow = bg(249,255,89)
bg_lightgreen = '\033[102m'
bg_green = '\033[42m'
bg_lightblue = '\033[104m'
bg_blue = '\033[44m'

bold = '\033[1m'
dim = '\033[2m'
italic = '\033[3m'
underline = '\033[4m'
reverse = '\033[7m'
invisible = '\033[8m'
crossover = '\033[9m'
reset = '\033[0m'

headers = {
  "Content-Type": "application/json"
}

while True:
  prompt = input(f"{bold}Prompt:{fg_dark_blue} ")

  response = requests.post("https://plutoniumserver.onrender.com/", json={"prompt":prompt}, headers=headers).json()

  if 'status' in response:
    if  response['status'] == 429:
      write(f"{reset}{bold}Chatbot: {fg_red}Your prompt returned an error...{reset}\n")

    continue

  while response["bot"].startswith('\n'):
    response["bot"] = response["bot"][2:]

  write(f"{reset}{bold}Chatbot: {fg_light_green}{response['bot']}{reset}\n")
