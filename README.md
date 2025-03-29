# 🧰 IP Networking Toolkit (Windows GUI)

A dark-themed, standalone Windows application for performing essential IP and subnet calculations because finding these tools across multiple sites or commands was far too much work. 

---

## 🚀 Features

✅ Clean GUI using Tkinter  
✅ Works with both `IP + subnet mask` and CIDR format (e.g. `192.168.1.10/24`)  
✅ Auto-fills subnet mask when CIDR is detected  
✅ Built-in copy-to-clipboard button  
✅ Dark mode interface for reduced eye strain  
✅ No Python installation needed (when using the `.exe`)

---

## 🔧 Included Tools

1. **Class of Network** – Determines if the IP is Class A, B, C, D, or E.
2. **Default Subnet Mask** – Based on IP class.
3. **Subnet Bits** – Number of subnetting bits beyond classful default.
4. **Network ID (Bitwise)** – Calculates network ID using bitwise AND.
5. **Broadcast Address** – Outputs the subnet's broadcast address.
6. **Range of Host Addresses** – First and last usable IPs.
7. **How Many Host Addresses** – Number of usable hosts in the subnet.
8. **Default Gateway** – Suggests the first usable IP as the gateway.

---

## 🖥️ How to Use

1. **Download the `.exe`** from the [Releases](./releases) section.
2. Launch the program — no install needed.
3. Select a tool from the dropdown.
4. Enter:
   - IP (e.g. `192.168.1.10`) and Subnet Mask (`255.255.255.0`) **or**
   - CIDR format (e.g. `192.168.1.10/24`) in the IP field and leave Subnet Mask blank.
5. Click **Run Tool**.
6. Click **Copy Result** to quickly grab the output.

---

## 🧪 Run in Python or Build It Yourself (Optional)

If you want to run or customize the source code, here’s how to do it.

---

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/peckre/cno_ip_tools.git
cd cno_ip_tools
```

---

### 📦 2. Install Requirements

Make sure you have Python 3.x installed. Then, install the required Python packages if not installed:

```bash
pip install pyperclip tkinter ipaddress
```


### 🧰 3. Run the App (for Testing or Development)

```bash
python3 ip_tool.py
```

You’ll see the dark mode GUI window appear.

---

### 🏗️ 4. Build a Standalone `.exe` (Windows Only)

To make a distributable `.exe`:

#### Install PyInstaller:
```bash
pip install pyinstaller
```

#### Build the app:
```bash
pyinstaller --onefile --windowed ip_tool_gui2.py
```

#### Output:
- You’ll find the `.exe` in the `dist/` folder.
- Share or run it on any Windows machine — **no Python required!**

---

### 📌 Build Tips

- Add `--icon=myicon.ico` to the command if you want a custom icon.
- Use `--clean` to remove old build artifacts:
  ```bash
  pyinstaller --onefile --windowed --clean ip_tool_gui2.py
  ```

---
