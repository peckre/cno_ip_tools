# 🧰 IP Networking Toolkit (Windows GUI)

A dark-themed, standalone Windows application for performing essential IP and subnet calculations. Designed for simplicity, accuracy, and fast workflow — all in a clean graphical interface.

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

## 📸 Screenshot

![IP Networking Toolkit Screenshot](./screenshot.png)

> *Dark mode, clean layout, and immediate results — no clutter.*

---

## 🧪 Build it Yourself (Optional)

If you want to modify or rebuild the app:

### 1. Install Requirements
```bash
pip install pyperclip
