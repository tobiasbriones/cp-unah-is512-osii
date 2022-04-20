# Copyright (c) 2022 Tobias Briones. All rights reserved.
# SPDX-License-Identifier: MIT
#
# This source code is part of
# https://github.com/tobiasbriones/cp-unah-is512-osii and is
# licensed under the MIT License found in the LICENSE file in the root
# directory of this source tree or at https://opensource.org/licenses/MIT

from Tkinter import *
import os
import subprocess
import tkFont
import tkMessageBox
import ScrolledText
import time

def portlist():
    os.system("sudo ufw status > portlist.txt")
    return subprocess.check_output("cat /home/ubuntu1/portlist.txt", shell=True)

class MainWindow:
    def __init__(self):
        self.mw = Tk()
        self.update_btn = Button(self.mw)
        self.allow_btn = Button(self.mw)
        self.deny_btn = Button(self.mw)
        self.textarea = ScrolledText.ScrolledText(self.mw)
        self.allow_tf = Entry(self.mw)
        self.deny_tf = Entry(self.mw)

    def init(self):
        self.mw.title("Firewall Linux")
        self.mw.geometry("500x420")

        self.update_btn.place(x=300, y=10)
        self.update_btn.config(
            text="Actualizar lista de puertos",
            command=self.__on_update
        )
        self.textarea.config(
            width=60,
            height=20,
            state=DISABLED
        )
        self.textarea.place(x=10, y=60)
        
        self.allow_tf.width=10
        self.allow_tf.place(x=10, y=10)
        self.allow_btn.config(
            text="Allow",
            command=self.__on_allow
        )
        self.allow_btn.place(
            x=200,
            y=10
        )
        
        self.deny_tf.width=5
        self.deny_tf.place(x=10, y=360)
        self.deny_btn.config(
            text="Deny",
            command=self.__on_deny
        )
        self.deny_btn.place(
            x=200,
            y=360
        )

        self.mw.mainloop()

    def __on_update(self):
        value = portlist()

        self.textarea.config(state=NORMAL)
        self.textarea.delete("1.0", "end")
        self.textarea.insert(INSERT, value)
        self.textarea.config(state=DISABLED)
        
    def __on_allow(self):
        port_value = self.allow_tf.get()
        cmd1 = "sudo ufw allow "
        cmd = (str(cmd1) + str(port_value))
        os.system(cmd)
        
    def __on_deny(self):
        port_value = self.deny_tf.get()
        cmd1 = "sudo ufw deny "
        cmd = (str(cmd1) + str(port_value))
        os.system(cmd)

mw = MainWindow()

mw.init()
