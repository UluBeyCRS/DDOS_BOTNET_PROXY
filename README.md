git clone https://github.com/UluBeyCRS/DDOS_BOTNET_PROXY.git

cd DDOS_BOTNET_PROXY

# Kali Linux

sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-pip git -y

pip3 install requests --break-system-packages

chmod +x ddos_botnet_proxy.py

python3 ddos_botnet_proxy.py


# Termux

pkg update && pkg upgrade -y

pkg install python git -y

pip install requests

chmod +x ddos_botnet_proxy.py

python ddos_botnet_proxy.py
