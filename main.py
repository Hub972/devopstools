from tkinter import Entry, Label, Button, Tk, Text, INSERT, HORIZONTAL,messagebox
from tkinter.ttk import Progressbar, Scrollbar
import tkinter as tk
import socket
#load ssh module
import paramiko


 
#main window
window = Tk()
window.title('Main window')
window.geometry("640x480")
window.configure(background="green")
cli = paramiko.SSHClient()

#put text on window
txt1 = Label(window, text="DEVOPS Audit Routine")
txt1.pack()
Label(window, text="Insert your information and just click:", anchor='s').pack(anchor='s')



 
 
 

def autoremove():
    """make cmd for autoremove"""
    cli = test_ssh_connection()
    if cli.get_transport() is not None:
        messagebox.showinfo("Confirmation", f"Ssh connection is done")
        stdin, stdout, stderr = cli.exec_command('sudo apt --allow-remove-essential -y autoremove', get_pty=True)
        stdin.write('Fidelite\n')
        stdin.flush()
        manage_command_output(cli, stdout, stderr)
        
def display_list_user():
    """Display all divice users"""
    cli = test_ssh_connection()
    if cli.get_transport() is not None:
        messagebox.showinfo('Confirmation', 'SSH connection is done')
        stdin, stdout, stderr = cli.exec_command('cat /etc/passwd', get_pty=True)
        manage_command_output(cli, stdout, stderr)

def display_package_list():
    """Display all pkg 's server"""
    cli = test_ssh_connection()
    if cli.get_transport() is not None:
        messagebox.showinfo('Confirmation', 'SSH connection is done')
        stdin, stdout, stderr = cli.exec_command("find /etc/apt -type f -name '*.list*' -exec bash -c 'echo -e \"\n$1\n\"; [[ $1 = *\".list\" ]] && nl -ba \"$1\"' _ '{}' \;")
        manage_command_output(cli, stdout, stderr)

def manage_command_output(cli, stdout, stderr):
    """Display stdin or stderr and close the connection"""
    stdout.channel.recv_exit_status()
    if stderr is not None:
        errs = stderr.readlines()
        for err in errs:
            print(err)
        cli.close()
    lines = stdout.readlines()
    loading = True
    while loading is True:
        progress.pack(anchor='center')
        bar()
        response = ""
        for line in lines:
            response = response + line
        cli.close()
        loading = False
        progress.pack_forget()
        root = Tk()
        root.title('Response')
        scroll = Scrollbar(root)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        text = Text(root)
        text.pack(side=tk.LEFT, fill=tk.Y)
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)
        text.insert(INSERT, response)
        root.mainloop()

def test_ssh_connection():
    """Connect user with the input param and return a ssh client"""
    user = userSsh.get()
    ip = ipAdres.get()
    passwd_user = passwd.get()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cli.connect(ip, username=user, password=passwd_user)
    except paramiko.ssh_exception.AuthenticationException :
        messagebox.showinfo("Error", f"Ssh connection to {ip} is impossible password is wrong, see the log.")
        cli.close()
    except paramiko.ssh_exception.SSHException:
        messagebox.showinfo("Error", f"Ssh connection is impossible username {user} is wrong, see the log.")
        cli.close()
    except socket.gaierror:
        messagebox.showinfo("Error", f"Ssh connection is impossible ip {ip} is wrong, see the log.")     
    return cli
 
#Create widget for user and address ssh connection
userSsh = tk.StringVar()
Entry(window, bg='bisque', fg='maroon', textvariable=userSsh).place(x=200, y=120)
Label(window,text='insert username').place(x=200, y=90)
ipAdres = tk.StringVar()
Entry(window, bg ='bisque', fg='maroon', textvariable=ipAdres).place(x=200, y=180)
Label(window,text='insert Ip').place(x=200, y=150)
passwd = tk.StringVar()
Entry(window, bg ='bisque', fg='maroon', textvariable=passwd, show='*').place(x=200, y=240)
Label(window,text='insert password').place(x=200, y=210)
Button(window, text="Make autoremove", command=autoremove, activebackground="green").place(x=10, y=120)
Button(window, text="Display L users", command=display_list_user, activebackground="green").place(x=10, y=150)
Button(window, text="Display pakg list", command=display_package_list, activebackground="green").place(x=10, y=180)
progress = Progressbar(window, orient = HORIZONTAL, 
            length = 100, mode = 'indeterminate') 
  
# Function responsible for the updation 
# of the progress bar value 
def bar(): 
    import time 
    progress['value'] = 20
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 40
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 50
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 60
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 80
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 100
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 80
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 60
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 50
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 40
    window.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 20
    window.update_idletasks() 
    time.sleep(0.5) 
    progress['value'] = 0
      
window.mainloop()
