# Final Code
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
from itertools import product
import os

# ---------------- Conversion Logic ----------------
class Converter:
    def binary_to_decimal(self, b): return int(b, 2)
    def decimal_to_binary(self, d): return bin(int(d))[2:]
    def binary_to_octal(self, b): return oct(int(b, 2))[2:]
    def binary_to_hexadecimal(self, b): return hex(int(b, 2))[2:].upper()
    def binary_to_gray(self, b):
        n = int(b, 2)
        return bin(n ^ (n >> 1))[2:]
    def gray_to_binary(self, g):
        g = int(g, 2)
        m = g
        while m:
            m >>= 1
            g ^= m
        return bin(g)[2:]
    def ones_complement(self, b): return ''.join('1' if i == '0' else '0' for i in b)
    def twos_complement(self, b): return bin(int(self.ones_complement(b), 2) + 1)[2:]
    def binary_add(self, b1, b2): return bin(int(b1, 2) + int(b2, 2))[2:]
    def binary_sub(self, b1, b2): return bin(int(b1, 2) - int(b2, 2))[2:]

conv = Converter()
USER_FILE = "user_data.txt"  # file to remember last user

# ---------------- Function Windows ----------------
class ConversionWindow:
    def __init__(self, parent, username):
        self.window = tk.Toplevel(parent)
        self.window.title("Conversions")
        self.window.geometry("900x500")
        self.window.config(bg="#E3F2FD")
        self.history_data = []
        
        # Header
        tk.Label(self.window, text=f"Conversions ({username})", font=("Century Gothic",16,"bold"), bg="#BBDEFB", fg="#0D47A1").pack(pady=8, fill=tk.X)
        
        # Main frame
        main_frame = tk.Frame(self.window, bg="#E3F2FD")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input frame
        input_frame = tk.LabelFrame(main_frame, text="Input", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        input_frame.pack(fill="x", pady=5)
        tk.Label(input_frame, text="Value:", bg="#E3F2FD").grid(row=0, column=0)
        self.entry_val = tk.Entry(input_frame, width=15)
        self.entry_val.grid(row=0,column=1)
        
        # Buttons frame
        buttons_frame = tk.LabelFrame(main_frame, text="Conversions", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        buttons_frame.pack(fill="x", pady=5)
        
        for i,t in enumerate(["Bin->Dec","Dec->Bin","Bin->Hex","Bin->Oct","Bin->Gray","Gray->Bin","1's","2's"]):
            tk.Button(buttons_frame, text=t, command=lambda x=t: self.convert(x), width=10).grid(row=i//2, column=i%2, pady=5, padx=5)
        
        # Output frame
        output_frame = tk.LabelFrame(main_frame, text="Output", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        output_frame.pack(fill="both", expand=True, pady=5)
        
        self.output_box = scrolledtext.ScrolledText(output_frame, width=55, height=15, font=("Consolas",10), bg="#E1F5FE", fg="#01579B")
        self.output_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Button frame
        btn_frame = tk.Frame(self.window, bg="#E3F2FD")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Clear", command=self.clear, bg="#81D4FA", fg="black", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="History", command=self.show_history, bg="#FFD54F", fg="black", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Back", command=self.window.destroy, bg="#FF8A65", fg="black", width=12).pack(side=tk.LEFT, padx=5)
    
    def convert(self, op):
        v = self.entry_val.get()
        try:
            if op=="Bin->Dec": r=str(conv.binary_to_decimal(v))
            elif op=="Dec->Bin": r=conv.decimal_to_binary(v)
            elif op=="Bin->Hex": r=conv.binary_to_hexadecimal(v)
            elif op=="Bin->Oct": r=conv.binary_to_octal(v)
            elif op=="Bin->Gray": r=conv.binary_to_gray(v)
            elif op=="Gray->Bin": r=conv.gray_to_binary(v)
            elif op=="1's": r=conv.ones_complement(v)
            elif op=="2's": r=conv.twos_complement(v)
        except: r="Error!"
        self.output_box.insert(tk.END, f"{op}: {r}\n")
        self.history_data.append(f"{op}: {r}")
    
    def clear(self):
        self.entry_val.delete(0, tk.END)
        self.output_box.delete(1.0, tk.END)
    
    def show_history(self):
        hist_win = tk.Toplevel(self.window)
        hist_win.title("Conversion History")
        hist_win.geometry("600x400")
        hist_box = scrolledtext.ScrolledText(hist_win, width=70, height=30, font=("Consolas",10))
        hist_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        hist_box.insert(tk.END, "\n".join(self.history_data))
        hist_box.config(state=tk.DISABLED)

class ArithmeticWindow:
    def __init__(self, parent, username):
        self.window = tk.Toplevel(parent)
        self.window.title("Binary Arithmetic")
        self.window.geometry("900x500")
        self.window.config(bg="#E3F2FD")
        self.history_data = []
        
        # Header
        tk.Label(self.window, text=f"Binary Arithmetic ({username})", font=("Century Gothic",16,"bold"), bg="#BBDEFB", fg="#0D47A1").pack(pady=8, fill=tk.X)
        
        # Main frame
        main_frame = tk.Frame(self.window, bg="#E3F2FD")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input frame
        input_frame = tk.LabelFrame(main_frame, text="Input", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        input_frame.pack(fill="x", pady=5)
        tk.Label(input_frame, text="Binary 1:", bg="#E3F2FD").grid(row=0,column=0)
        self.entry_b1=tk.Entry(input_frame,width=15)
        self.entry_b1.grid(row=0,column=1)
        tk.Label(input_frame, text="Binary 2:", bg="#E3F2FD").grid(row=1,column=0)
        self.entry_b2=tk.Entry(input_frame,width=15)
        self.entry_b2.grid(row=1,column=1)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg="#E3F2FD")
        buttons_frame.pack(fill="x", pady=10)
        tk.Button(buttons_frame, text="Add", command=lambda:self.calc("Add"), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(buttons_frame, text="Subtract", command=lambda:self.calc("Subtract"), width=10).pack(side=tk.LEFT, padx=5)
        
        # Output frame
        output_frame = tk.LabelFrame(main_frame, text="Output", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        output_frame.pack(fill="both", expand=True, pady=5)
        
        self.output_box = scrolledtext.ScrolledText(output_frame, width=55, height=15, font=("Consolas",10), bg="#E1F5FE", fg="#01579B")
        self.output_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Button frame
        btn_frame = tk.Frame(self.window, bg="#E3F2FD")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Clear", command=self.clear, bg="#81D4FA", fg="black", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="History", command=self.show_history, bg="#FFD54F", fg="black", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Back", command=self.window.destroy, bg="#FF8A65", fg="black", width=12).pack(side=tk.LEFT, padx=5)
    
    def calc(self, op):
        b1, b2 = self.entry_b1.get(), self.entry_b2.get()
        try: r = conv.binary_add(b1,b2) if op=="Add" else conv.binary_sub(b1,b2)
        except: r="Error!"
        self.output_box.insert(tk.END, f"{op}: {r}\n")
        self.history_data.append(f"{op}: {r}")
    
    def clear(self):
        self.entry_b1.delete(0, tk.END)
        self.entry_b2.delete(0, tk.END)
        self.output_box.delete(1.0, tk.END)
    
    def show_history(self):
        hist_win = tk.Toplevel(self.window)
        hist_win.title("Arithmetic History")
        hist_win.geometry("600x400")
        hist_box = scrolledtext.ScrolledText(hist_win, width=70, height=30, font=("Consolas",10))
        hist_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        hist_box.insert(tk.END, "\n".join(self.history_data))
        hist_box.config(state=tk.DISABLED)

class LogicGatesWindow:
    def __init__(self, parent, username):
        self.window = tk.Toplevel(parent)
        self.window.title("Logic Gates")
        self.window.geometry("900x500")
        self.window.config(bg="#E3F2FD")
        self.history_data = []
        
        # Header
        tk.Label(self.window, text=f"Logic Gates ({username})", font=("Century Gothic",16,"bold"), bg="#BBDEFB", fg="#0D47A1").pack(pady=8, fill=tk.X)
        
        # Main frame
        main_frame = tk.Frame(self.window, bg="#E3F2FD")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input frame
        input_frame = tk.LabelFrame(main_frame, text="Input", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        input_frame.pack(fill="x", pady=5)
        tk.Label(input_frame, text="Gate (AND, OR, NAND, NOR, XOR, XNOR):", bg="#E3F2FD").grid(row=0,column=0)
        self.entry_gate=tk.Entry(input_frame,width=15)
        self.entry_gate.grid(row=0,column=1)
        tk.Button(input_frame, text="Show Truth Table", command=self.logic_gate_table, width=15).grid(row=1,column=0,columnspan=2,pady=5)
        
        # Output frame
        output_frame = tk.LabelFrame(main_frame, text="Output", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        output_frame.pack(fill="both", expand=True, pady=5)
        
        self.output_box = scrolledtext.ScrolledText(output_frame, width=55, height=15, font=("Consolas",10), bg="#E1F5FE", fg="#01579B")
        self.output_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Button frame
        btn_frame = tk.Frame(self.window, bg="#E3F2FD")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Clear", command=self.clear, bg="#81D4FA", fg="black", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="History", command=self.show_history, bg="#FFD54F", fg="black", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Back", command=self.window.destroy, bg="#FF8A65", fg="black", width=12).pack(side=tk.LEFT, padx=5)
    
    def logic_gate_table(self):
        g = self.entry_gate.get().strip().upper()
        self.output_box.delete(1.0, tk.END)
        data = {
            "AND": [(0,0,0),(0,1,0),(1,0,0),(1,1,1)],
            "OR": [(0,0,0),(0,1,1),(1,0,1),(1,1,1)],
            "NAND": [(0,0,1),(0,1,1),(1,0,1),(1,1,0)],
            "NOR": [(0,0,1),(0,1,0),(1,0,0),(1,1,0)],
            "XOR": [(0,0,0),(0,1,1),(1,0,1),(1,1,0)],
            "XNOR": [(0,0,1),(0,1,0),(1,0,0),(1,1,1)]
        }
        if g in data:
            out = f"Truth Table for {g} Gate:\nA | B | Output\n" + "-"*15 + "\n"
            for a,b,o in data[g]:
                out += f"{a} | {b} | {o}\n"
        else:
            out = "Invalid Gate! Use AND, OR, NAND, NOR, XOR, XNOR.\n"
        self.output_box.insert(tk.END, out)
        self.history_data.append(out)
    
    def clear(self):
        self.entry_gate.delete(0, tk.END)
        self.output_box.delete(1.0, tk.END)
    
    def show_history(self):
        hist_win = tk.Toplevel(self.window)
        hist_win.title("Logic Gates History")
        hist_win.geometry("600x400")
        hist_box = scrolledtext.ScrolledText(hist_win, width=70, height=30, font=("Consolas",10))
        hist_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        hist_box.insert(tk.END, "\n".join(self.history_data))
        hist_box.config(state=tk.DISABLED)

class BooleanExpressionWindow:
    def __init__(self, parent, username):
        self.window = tk.Toplevel(parent)
        self.window.title("Boolean Expression")
        self.window.geometry("900x500")
        self.window.config(bg="#E3F2FD")
        self.history_data = []
        
        # Header
        tk.Label(self.window, text=f"Boolean Expression ({username})", font=("Century Gothic",16,"bold"), bg="#BBDEFB", fg="#0D47A1").pack(pady=8, fill=tk.X)
        
        # Main frame
        main_frame = tk.Frame(self.window, bg="#E3F2FD")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input frame
        input_frame = tk.LabelFrame(main_frame, text="Input", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        input_frame.pack(fill="x", pady=5)
        tk.Label(input_frame, text="Expression (and,or,not):", bg="#E3F2FD").grid(row=0,column=0)
        self.expr_entry = tk.Entry(input_frame,width=20)
        self.expr_entry.grid(row=0,column=1)
        tk.Label(input_frame, text="Variables (space-separated):", bg="#E3F2FD").grid(row=1,column=0)
        self.vars_entry = tk.Entry(input_frame,width=20)
        self.vars_entry.grid(row=1,column=1)
        tk.Button(input_frame, text="Generate Truth Table", command=self.generate_tt, bg="#FFB6C1", width=20).grid(row=2,column=0,columnspan=2,pady=5)
        
        # Output frame
        output_frame = tk.LabelFrame(main_frame, text="Output", bg="#E3F2FD", fg="#0D47A1", font=("Arial",10,"bold"), padx=5, pady=5)
        output_frame.pack(fill="both", expand=True, pady=5)
        
        self.output_box = scrolledtext.ScrolledText(output_frame, width=55, height=15, font=("Consolas",10), bg="#E1F5FE", fg="#01579B")
        self.output_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        # Button frame
        btn_frame = tk.Frame(self.window, bg="#E3F2FD")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Clear", command=self.clear, bg="#81D4FA", fg="black", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="History", command=self.show_history, bg="#FFD54F", fg="black", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Back", command=self.window.destroy, bg="#FF8A65", fg="black", width=12).pack(side=tk.LEFT, padx=5)
    
    def generate_tt(self):
        e = self.expr_entry.get(); v = self.vars_entry.get()
        if not e or not v:
            messagebox.showwarning("Input Missing","Enter expression & variables")
            return
        out = self.truth_table(e, v.split())
        self.output_box.delete(1.0, tk.END)
        self.output_box.insert(tk.END, out)
        self.history_data.append(out)
    
    def truth_table(self, expr, vars_):
    n = len(vars_)
    out = f"\nTruth Table for: {expr}\n"
    out += "-" * (6*(n+1)) + "\n"
    out += " | ".join(vars_) + " | Output\n"
    out += "-" * (6*(n+1)) + "\n"
    
    # Normalize the expression (allow user to type AND/OR/NOT)
    expr = expr.lower().replace("and", " and ").replace("or", " or ").replace("not", " not ")
    
    for v in product([0, 1], repeat=n):
        # Convert 0/1 → bool
        env = {var: bool(val) for var, val in zip(vars_, v)}
        try:
            res = eval(expr, {}, env)
            res = int(bool(res))  # convert True/False → 1/0
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression:\n{e}")
            return ""
        out += " | ".join(str(i) for i in v) + f" |   {res}\n"
    
    out += "-" * (6*(n+1)) + "\n"
    return out
    
    def clear(self):
        self.expr_entry.delete(0, tk.END)
        self.vars_entry.delete(0, tk.END)
        self.output_box.delete(1.0, tk.END)
    
    def show_history(self):
        hist_win = tk.Toplevel(self.window)
        hist_win.title("Boolean Expression History")
        hist_win.geometry("600x400")
        hist_box = scrolledtext.ScrolledText(hist_win, width=70, height=30, font=("Consolas",10))
        hist_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        hist_box.insert(tk.END, "\n".join(self.history_data))
        hist_box.config(state=tk.DISABLED)

# ---------------- Main Window ----------------
class MainWindow:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(f"LogiCal - {username}")
        self.root.geometry("900x500")
        self.root.config(bg="#E3F2FD")
        
        # Header
        header_frame = tk.Frame(self.root, bg="#BBDEFB", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        tk.Label(header_frame, text=f"LogiCal - {username}", font=("Century Gothic",20,"bold"), bg="#BBDEFB", fg="#0D47A1").pack(expand=True)
        
        # Main content
        content_frame = tk.Frame(self.root, bg="#E3F2FD")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create buttons for each function
        button_frame = tk.Frame(content_frame, bg="#E3F2FD")
        button_frame.pack(expand=True)
        
        # Button styling
        button_style = {"font": ("Arial", 12), "width": 20, "height": 3, "bg": "#90CAF9", "fg": "#0D47A1"}
        
        # Create buttons in a grid
        tk.Button(button_frame, text="Conversions", command=self.open_conversions, **button_style).grid(row=0, column=0, padx=20, pady=20)
        tk.Button(button_frame, text="Binary Arithmetic", command=self.open_arithmetic, **button_style).grid(row=0, column=1, padx=20, pady=20)
        tk.Button(button_frame, text="Logic Gates", command=self.open_logic_gates, **button_style).grid(row=1, column=0, padx=20, pady=20)
        tk.Button(button_frame, text="Boolean Expression", command=self.open_boolean_expression, **button_style).grid(row=1, column=1, padx=20, pady=20)
        
        # Bottom frame with sign out button
        bottom_frame = tk.Frame(self.root, bg="#E3F2FD")
        bottom_frame.pack(fill=tk.X, pady=10)
        tk.Button(bottom_frame, text="Exit", command=self.exit_app, bg="#FF8A65", fg="black", width=12).pack(side=tk.RIGHT, padx=20)
        tk.Button(bottom_frame, text="Sign Out", command=self.sign_out, bg="#FFB74D", fg="black", width=12).pack(side=tk.RIGHT, padx=5)
    
    def open_conversions(self):
        ConversionWindow(self.root, self.username)
    
    def open_arithmetic(self):
        ArithmeticWindow(self.root, self.username)
    
    def open_logic_gates(self):
        LogicGatesWindow(self.root, self.username)
    
    def open_boolean_expression(self):
        BooleanExpressionWindow(self.root, self.username)
    
    def sign_out(self):
        if os.path.exists(USER_FILE):
            os.remove(USER_FILE)
        messagebox.showinfo("Signed Out", "You have been signed out.")
        self.root.destroy()
        main()  # back to launcher
    
    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

# ---------------- User Accounts ----------------
users = {}

def login_window(parent_root):
    parent_root.destroy()
    login = tk.Tk()
    login.title("LogiCal Login")
    login.geometry("300x200")

    tk.Label(login, text="Username:").pack(pady=5)
    user_entry = tk.Entry(login)
    user_entry.pack(pady=5)
    tk.Label(login, text="Password:").pack(pady=5)
    pass_entry = tk.Entry(login, show="*")
    pass_entry.pack(pady=5)

    def try_login():
        u, p = user_entry.get(), pass_entry.get()
        if u in users and users[u] == p:
            with open(USER_FILE, "w") as f:
                f.write(u)
            messagebox.showinfo("Success", f"Welcome {u}!")
            login.destroy()
            new_root = tk.Tk()
            MainWindow(new_root, u)
            new_root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    tk.Button(login, text="Login", command=try_login, bg="#81D4FA").pack(pady=5)
    tk.Button(login, text="Sign Up", command=lambda: signup_window(login), bg="#FFB74D").pack(pady=5)

def signup_window(parent):
    u = simpledialog.askstring("Sign Up","Enter Username:", parent=parent)
    p = simpledialog.askstring("Sign Up","Enter Password:", parent=parent, show="*")
    if u and p:
        if u in users:
            messagebox.showerror("Error","Username already exists")
        else:
            users[u] = p
            messagebox.showinfo("Success","Account created! You can login now.")

# ---------------- Main ----------------
def main():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            user = f.read().strip()
        root = tk.Tk()
        MainWindow(root, user)
        root.mainloop()
    else:
        launcher = tk.Tk()
        launcher.title("LogiCal Launcher")
        launcher.geometry("300x150")
        tk.Button(launcher, text="Login / Open Account", command=lambda: login_window(launcher), bg="#FFCC80", width=20).pack(pady=30)
        launcher.mainloop()

main()
