import tkinter as tk
from tkinter import ttk, messagebox
import ipaddress
import pyperclip

# Parse input for either CIDR or IP + subnet mask
def get_ip_and_mask(ip_str, mask_str):
    try:
        if "/" in ip_str:
            net = ipaddress.IPv4Network(ip_str, strict=False)
            return net.network_address, net.netmask
        else:
            ip = ipaddress.IPv4Address(ip_str)
            subnet = ipaddress.IPv4Address(mask_str)
            return ip, subnet
    except ipaddress.AddressValueError:
        return None, None

def get_valid_ip(value):
    try:
        if "/" in value:
            return ipaddress.IPv4Address(value.split("/")[0])
        return ipaddress.IPv4Address(value)
    except:
        return None

def autofill_mask(event=None):
    ip_str = ip_entry.get()
    if "/" in ip_str:
        try:
            net = ipaddress.IPv4Network(ip_str, strict=False)
            mask_entry.delete(0, tk.END)
            mask_entry.insert(0, str(net.netmask))
        except:
            pass

def copy_to_clipboard():
    result = result_output.get("1.0", tk.END).strip()
    if result:
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Result copied to clipboard!")

def run_tool():
    tool = tool_selector.get()
    ip_input = ip_entry.get()
    mask_input = mask_entry.get()
    output = ""

    if tool == "Class of Network":
        ip = get_valid_ip(ip_input)
        if ip:
            first_octet = int(str(ip).split('.')[0])
            if 0 <= first_octet <= 127:
                output = "Class A"
            elif 128 <= first_octet <= 191:
                output = "Class B"
            elif 192 <= first_octet <= 223:
                output = "Class C"
            elif 224 <= first_octet <= 239:
                output = "Class D (Multicast)"
            else:
                output = "Class E (Experimental)"

    elif tool == "Default Subnet Mask":
        ip = get_valid_ip(ip_input)
        if ip:
            first_octet = int(str(ip).split('.')[0])
            if 0 <= first_octet <= 127:
                output = "255.0.0.0"
            elif 128 <= first_octet <= 191:
                output = "255.255.0.0"
            elif 192 <= first_octet <= 223:
                output = "255.255.255.0"
            else:
                output = "N/A"

    elif tool == "Subnet Bits":
        ip, subnet = get_ip_and_mask(ip_input, mask_input)
        if ip and subnet:
            actual_bits = bin(int(subnet)).count("1")
            first_octet = int(str(ip).split('.')[0])
            if 0 <= first_octet <= 127:
                default_bits = 8
            elif 128 <= first_octet <= 191:
                default_bits = 16
            elif 192 <= first_octet <= 223:
                default_bits = 24
            else:
                default_bits = 0
            subnet_bits = actual_bits - default_bits
            output = f"{subnet_bits} subnet bits (CIDR /{actual_bits} - default /{default_bits})"

    elif tool == "Network ID (Bitwise)":
        ip, subnet = get_ip_and_mask(ip_input, mask_input)
        if ip and subnet:
            network_id = ipaddress.IPv4Address(int(ip) & int(subnet))
            output = f"Network ID: {network_id}"

    elif tool == "Broadcast Address":
        ip, subnet = get_ip_and_mask(ip_input, mask_input)
        if ip and subnet:
            network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
            output = f"Broadcast Address: {network.broadcast_address}"

    elif tool == "Range of Host Addresses":
        ip, subnet = get_ip_and_mask(ip_input, mask_input)
        if ip and subnet:
            net = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
            hosts = list(net.hosts())
            if len(hosts) >= 2:
                output = f"Host range: {hosts[0]} - {hosts[-1]}"
            elif hosts:
                output = f"Only host: {hosts[0]}"
            else:
                output = "No usable host addresses"

    elif tool == "How Many Host Addresses":
        ip, subnet = get_ip_and_mask(ip_input, mask_input)
        if ip and subnet:
            net = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
            count = net.num_addresses - 2 if net.num_addresses >= 2 else 0
            output = f"{count} usable host addresses"

    elif tool == "Default Gateway":
        ip, subnet = get_ip_and_mask(ip_input, mask_input)
        if ip and subnet:
            network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
            hosts = list(network.hosts())
            if hosts:
                output = f"Default Gateway (first usable host): {hosts[0]}"
            else:
                output = "No usable hosts in this subnet."

    if output:
        result_output.delete(1.0, tk.END)
        result_output.insert(tk.END, output)
    else:
        messagebox.showerror("Error", "Invalid IP or Subnet Mask")

# ==== GUI Setup ====
root = tk.Tk()
root.title("🧰 IP Networking Toolkit")
root.geometry("560x450")
root.configure(bg="#2e2e2e")

# Style for dark mode
style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background="#2e2e2e", foreground="#ffffff")
style.configure("TEntry", fieldbackground="#3a3a3a", foreground="#ffffff")
style.configure("TButton", background="#3a3a3a", foreground="#ffffff")
style.configure("TCombobox", fieldbackground="#3a3a3a", background="#3a3a3a", foreground="#ffffff")

# Tool list
tools = [
    "Class of Network",
    "Default Subnet Mask",
    "Subnet Bits",
    "Network ID (Bitwise)",
    "Broadcast Address",
    "Range of Host Addresses",
    "How Many Host Addresses",
    "Default Gateway"
]

# Widgets
ttk.Label(root, text="Select Tool:").pack(pady=(10, 0))
tool_selector = ttk.Combobox(root, values=tools, state="readonly", width=50)
tool_selector.pack()
tool_selector.current(0)

ttk.Label(root, text="IP Address (e.g. 192.168.1.1 or 192.168.1.1/24):").pack(pady=(10, 0))
ip_entry = ttk.Entry(root, width=50)
ip_entry.pack()
ip_entry.bind("<FocusOut>", autofill_mask)

ttk.Label(root, text="Subnet Mask (e.g. 255.255.255.0):").pack(pady=(10, 0))
mask_entry = ttk.Entry(root, width=50)
mask_entry.pack()

button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(pady=10)
ttk.Button(button_frame, text="Run Tool", command=run_tool).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Copy Result", command=copy_to_clipboard).grid(row=0, column=1, padx=5)

ttk.Label(root, text="Output:").pack()
result_output = tk.Text(root, height=6, width=65, bg="#1e1e1e", fg="#00ff99")
result_output.pack(pady=5)

root.mainloop()
