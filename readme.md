# 📺 Android TV Video Sender — Quick Start

This repository's sender.py will automatically connect to your Android TV. You only need to set the TV IP in sender.py and run it.

---

## Prerequisites

- Python 3 installed.
- Android TV and PC on the same Wi‑Fi network.
- Android TV: Developer options → enable **ADB debugging** (or Wireless debugging on newer Android versions).

---

## Enable Developer Settings

- Click the **Gear Icon** on the top left → **Device Preferences** → **About** → scroll down → click 7-8 times the **Android TV OS Build**
- Go to your homepage → Click the **Gear Icon** on the top left → **Devices Preferences** → scroll down > **Developer options** > scroll a bit down > enable **USB Debugging** > press OK

## Set the TV IP

Open sender.py and set the atv_ip variable to your TV's IP, e.g.:

```python
atv_ip = "192.168.1.42"
```

Find the TV IP: Settings → Network & internet → Wi‑Fi → connected network → view **IP address**, or Settings → Device Preferences → About → Status → **IP address**.

---

## Run

From the project folder:

```bash
python sender.py
```

‼️ On the first connection ‼️, tick the Always allow from this computer box on the TV and press **OK** ✅

sender.py will handle connecting to the TV and performing its tasks.

---

## Troubleshooting

- Ensure TV and PC are on the same subnet.
- Confirm ADB debugging / Wireless debugging is enabled on the TV.
- Disable firewalls blocking port 5555 if needed.
- Reboot TV and PC if connection fails.

Enjoy remote sending! 🔋📡📦
