# GUI Client program.

import socket
from threading import Thread
from tkinter import *
import fontstyle
serverIp = 'localhost'
port = 9999
client = socket.socket()
client.connect((serverIp, port))
FORMAT = "utf=8"
class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        self.login = Tk()
        self.login.title("Login")
        self.login.configure(width = 400, height = 300)
        self.pls = Label(self.login, text = "Please login to continue", justify = CENTER, font = "Helvetica 14 bold")
        self.pls.place(relheight = 0.15, relx = 0.2, rely = 0.07)
        self.labelName = Label(self.login, text = "Name: ", font = "Helvetica 12")
        self.labelName.place(relheight = 0.2, relx = 0.1, rely = 0.2)
        self.entryName = Entry(self.login, font = "Helvetica 14")
        self.entryName.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.2)
        self.entryName.focus()
        self.go = Button(self.login, text = "CONTINUE", font = "Helvetica 14 bold", command = lambda: self.goAhead(self.entryName.get())) #userNames = []
        self.login.bind('<Return>', self.continueKey)
        self.go.place(relx = 0.4, rely = 0.55)
        self.Window.mainloop()
    def continueKey(self, e):
        self.goAhead(self.entryName.get())
    def goAhead(self, name):
        client.send(str.encode(name))
        self.login.destroy()
        self.layout(name)
        Thread(target = self.receive).start()
    def layout(self,name):
        self.name = name
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.configure(width = 470, height = 550, bg = "#17202A")
        self.labelHead = Label(self.Window, bg = "#17202A", fg = "#EAECEE", text = self.name, font = "Helvetica 13 bold", pady = 5)
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window, width = 450, bg = "#ABB2B9")
        self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
        self.textCons = Text(self.Window, width = 20, height = 2, bg = "#17202A", fg = "#EAECEE", font = "Times 14", padx = 5, pady = 5)
        self.textCons.place(relheight = 0.745, relwidth = 1, rely = 0.08)
        self.labelBottom = Label(self.Window, bg = "#ABB2B9", height = 80)
        self.labelBottom.place(relwidth = 1, rely = 0.825)
        self.entryMsg = Entry(self.labelBottom, bg = "#2C3E50", fg = "#EAECEE", font = "Helvetica 13")
        self.entryMsg.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.entryMsg.focus()
        self.buttonMsg = Button(self.labelBottom, text = "Send", font = "Helvetica 10 bold", width = 20, bg = "#ABB2B9", command = lambda : self.sendButton(self.entryMsg.get()))
        self.buttonMsg.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)
        self.Window.bind('<Return>', self.handler)
        self.textCons.config(cursor = "arrow")
        scrollbar = Scrollbar(self.textCons)
        scrollbar.place(relheight = 1, relx = 0.974)
        scrollbar.config(command = self.textCons.yview)
        self.textCons.config(state = DISABLED)
    def handler(self, e):
        self.sendButton(self.entryMsg.get()) 
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        self.msg=msg
        self.entryMsg.delete(0, END)
        Thread(target = self.sendMessage).start()
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)  
                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    self.textCons.config(state = NORMAL)
                    self.textCons.insert(END, message+"\n\n")
                    self.textCons.config(state = DISABLED)
                    self.textCons.see(END)
            except:
                print("An error occured!")
                client.close()
                break
    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        message = (f"{self.name}: {self.msg}")
        client.send(message.encode(FORMAT))  
g = GUI()


# # GUI Client program.

# import socket
# from threading import Thread
# from tkinter import *
# from tkinter import font
# from tkinter import ttk
# # from chat import *
# # serverIp = "165.22.14.77"
# serverIp = "192.168.0.104"
# port = 9927
# client = socket.socket()
# client.connect((serverIp, port))
# FORMAT = "utf=8"
# # userNames = []
# # userNames = client.recv(1024).decode()
# # print(userNames)

# class GUI:
#     # constructor method
#     def __init__(self):
       
#         # chat window which is currently hidden
#         self.Window = Tk()
#         self.Window.withdraw()
         
#         # login window
#         self.login = Toplevel()
#         # set the title
#         self.login.title("Login")
#         self.login.resizable(width = False,
#                              height = False)
#         self.login.configure(width = 400,
#                              height = 300)
#                               # create a Label
#         self.pls = Label(self.login,
#                        text = "Please login to continue",
#                        justify = CENTER,
#                        font = "Helvetica 14 bold")
         
#         self.pls.place(relheight = 0.15,
#                        relx = 0.2,
#                        rely = 0.07)
#         # create a Label
#         self.labelName = Label(self.login,
#                                text = "Name: ",
#                                font = "Helvetica 12")
         
#         self.labelName.place(relheight = 0.2,
#                              relx = 0.1,
#                              rely = 0.2)
#         self.entryName = Entry(self.login,
#                              font = "Helvetica 14")
         
#         self.entryName.place(relwidth = 0.4,
#                              relheight = 0.12,
#                              relx = 0.35,
#                              rely = 0.2)
         
#         # set the focus of the cursor
#         self.entryName.focus()
#          # create a Continue Button
#         # along with action
#         self.go = Button(self.login,
#                          text = "CONTINUE",
#                          font = "Helvetica 14 bold",
#                          command = lambda: self.goAhead(self.entryName.get())) #userNames = []
         
#         self.go.place(relx = 0.4,
#                       rely = 0.55)
#         self.Window.mainloop()
#     def goAhead(self, name):
#         self.login.destroy()
#         self.layout(name)
         
#         # the thread to receive messages
#         Thread(target = self.receive).start()
#         # The main layout of the chat
#     def layout(self,name):
       
#         self.name = name
#         # to show chat window
#         self.Window.deiconify()
#         self.Window.title("CHATROOM")
#         self.Window.resizable(width = False,
#                               height = False)
#         self.Window.configure(width = 470,
#                               height = 550,
#                               bg = "#17202A")
#         self.labelHead = Label(self.Window,
#                              bg = "#17202A",
#                               fg = "#EAECEE",
#                               text = self.name ,
#                                font = "Helvetica 13 bold",
#                                pady = 5)
#         self.labelHead.place(relwidth = 1)
#         self.line = Label(self.Window,
#                           width = 450,
#                           bg = "#ABB2B9")
         
#         self.line.place(relwidth = 1,
#                         rely = 0.07,
#                         relheight = 0.012)
         
#         self.textCons = Text(self.Window,
#                              width = 20,
#                              height = 2,
#                              bg = "#17202A",
#                              fg = "#EAECEE",
#                              font = "Helvetica 14",
#                              padx = 5,
#                              pady = 5)
#         self.textCons.place(relheight = 0.745,
#                             relwidth = 1,
#                             rely = 0.08)
         
#         self.labelBottom = Label(self.Window,
#                                  bg = "#ABB2B9",
#                                  height = 80)
         
#         self.labelBottom.place(relwidth = 1,
#                                rely = 0.825)
         
#         self.entryMsg = Entry(self.labelBottom,
#                               bg = "#2C3E50",
#                               fg = "#EAECEE",
#                               font = "Helvetica 13")
#          # place the given widget
#         # into the gui window
#         self.entryMsg.place(relwidth = 0.74,
#                             relheight = 0.06,
#                             rely = 0.008,
#                             relx = 0.011)
         
#         self.entryMsg.focus()
         
#         # create a Send Button
#         self.buttonMsg = Button(self.labelBottom,
#                                 text = "Send",
#                                 font = "Helvetica 10 bold",
#                                 width = 20,
#                                 bg = "#ABB2B9",
#                                 command = lambda : self.sendButton(self.entryMsg.get()))
#         self.buttonMsg.place(relx = 0.77,
#                              rely = 0.008,
#                              relheight = 0.06,
#                              relwidth = 0.22)
         
#         self.textCons.config(cursor = "arrow")
         
#         # create a scroll bar
#         scrollbar = Scrollbar(self.textCons)
         
#         # place the scroll bar
#         # into the gui window
#         scrollbar.place(relheight = 1,
#                         relx = 0.974)
#         scrollbar.config(command = self.textCons.yview)
         
#         self.textCons.config(state = DISABLED)
 
#     # function to basically start the thread for sending messages
#     def sendButton(self, msg):
#         self.textCons.config(state = DISABLED)
#         self.msg=msg
#         self.entryMsg.delete(0, END)
#         Thread(target = self.sendMessage).start()
#   # function to receive messages
#     def receive(self):
#         while True:
#             try:
#                 message = client.recv(1024).decode(FORMAT)
                 
#                 # if the messages from the server is NAME send the client's name
#                 if message == 'NAME':
#                     client.send(self.name.encode(FORMAT))
#                 # elif 'New Client' in message:
#                 #     userNames.append(message)
#                 #     print(message)
#                 else:

#                     # insert messages to text box
#                     self.textCons.config(state = NORMAL)
#                     self.textCons.insert(END,
#                                          message+"\n\n")
                     
#                     self.textCons.config(state = DISABLED)
#                     self.textCons.see(END)
#             except:
#                 # an error will be printed on the command line or console if there's an error
#                 print("An error occured!")
#                 client.close()
#                 break
         
#     # function to send messages
#     def sendMessage(self):
#         self.textCons.config(state=DISABLED)
#         while True:
#             message = (f"{self.name}: {self.msg}")
#             client.send(message.encode(FORMAT))  
#             break  
 
# # create a GUI class object
# g = GUI()

    # def userNamesWindow(self, name):
    #     self.userNamesWindow = TK()
    #     self.userNamesWindow.withdraw()

    #     self.userNames.title("Users")
    #     counter = 0
    #     listbox = Listbox(userNamesWindow)
    #     for userName in userNames:
    #         counter = counter + 1
    #         listbox.insert(counter, userName)
    #     listbox.pack()
    #     self.userNamesWindow.mainloop()















# # import socket
# # from threading import Thread
# # from tkinter import *
# # from tkinter import font
# # from tkinter import ttk

# # # serverIp = "165.22.14.77"
# # serverIp = "192.168.0.104"
# # port = 9998
# # client = socket.socket()
# # client.connect((serverIp, port))
# # FORMAT = "utf=8"
# # class GUI:
# #     def __init__(self):
# #         # hidden window
# #         self.window = Tk()
# #         self.window.withdraw()
# #         # login window
# #         self.login = Toplevel()
# #         # login title
# #         self.login.title("Login")
# #         self.login.resizable(width = False, height = False)
# #         self.login.configure(width = 500, height = 400)
# #         # create a lable
# #         self.pls = Label(self.login, text = "Please login to continue", justify = CENTER, font = "Serif 14 bold")
# #         self.pls.place(relheight = 0.15, relx = 0.2, rely = 0.07)
# #         # create a Label
# #         self.LabelName = Label(self.login, text = "Name: ", font = "Serif 12")
# #         self.LabelName.place(relheight = 0.2, relx = 0.1, rely = 0.2)
# #         self.entryName = Entry(self.login, font = "Serif 14")
# #         self.entryName.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.2)
# #         # set the focus of the cursor
# #         self.entryName.focus()
# #         # create a Continue Button along with action
# #         self.go = Button(self.login, text = "CONTINUE", font = "Serif 14 bold", command = lambda: self.goAhead(self.entryName.get()))
# #         self.go.place(relx = 0.4, rely = 0.55)
# #         self.window.mainloop()
# #     def goAhead(self, name):
# #         self.login.destroy()
# #         self.layout(name)
# #         # Thraed to receive messages
# #         Thread(target = self.receive).start()
# #     # The main layout of the chat
# #     def layout(self, name):
# #         self.name = name
# #         self.window.deiconify()
# #         self.window.title("CHATROOM")
# #         self.window.resizable(width = False, height = False)
# #         self.window.configure(width = 470, height = 550, bg = "#38d1C4")
# #         self.labelHead = Label(self.window, bg = "#38d1C4", fg = "#021426", text = self.name, font = "Serif 13 bold", pady = 5)
# #         self.labelHead.place(relwidth = 1)
        # self.line = Label(self.window, width = 450, bg = "#6fb4f9")
        # self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
        # self.textCons = Text(self.window, width = 20, height = 2, bg = "#38d1C4", fg = "#021426", font = "Serif 14", padx = 5, pady = 5)
        # self.textCons.place(relheight = 0.745, relwidth = 1, rely = 0.08)
        # self.labelBootom = Label(self.window, bg = "6fb4f9", height = 80)
        # self.labelBootom.place(relwidth = 1, rely = 0.825)
        # self.entryMsg = Entry(self.labelBootom, bg = "#061523", fg = "#5de1ea", font = "Serif 13")
        # self.entryMsg.place(relwidth = 0.68, relheight = 0.06, rely = 0.012, relx = 0.011)
        # self.entryMsg.focus()
# #         # create a send button
# #         self.buttonMsg = Button(self.labelBootom, text = "Send", font = "Serif 10 bold", width = 20, bg = "6fb4f9", command = lambda : self.sendButton(self.entryMsg.get()))
# #         self.buttonMsg.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)
# #         self.textCons.config(cursor = "arrow")
# #         # create a scroll bar
# #         scrollbar = Scrollbar(self.textCons)
# #         # place the scroll bar into the gui window
# #         scrollbar.place(relheight = 1, relx = 0.974)
# #         scrollbar.config(command = self.textCons.yview)
# #         self.textCons.config(state = DISABLED)
# #     # function to basically start the thread for sending messages
# #     def sendButton(self, msg):
# #         self.textCons.config(state = DISABLED)
# #         self.msg=msg
# #         self.entryMsg.delete(0, END)
# #         Thread(target = self.sendMessage).start()
# #         # function to receive messages
# #     def receive(self):
# #         while True:
# #             try:
# #                 message = client.recv(1024).decode(FORMAT)
                 
# #                 # if the messages from the server is NAME send the client's name
# #                 if message == 'NAME':
# #                     client.send(self.name.encode(FORMAT))
# #                 else:
# #                     # insert messages to text box
# #                     self.textCons.config(state = NORMAL)
# #                     self.textCons.insert(END,
# #                                          message+"\n\n")
                     
# #                     self.textCons.config(state = DISABLED)
# #                     self.textCons.see(END)
# #             except:
# #                 # an error will be printed on the command line or console if there's an error
# #                 print("An error occured!")
# #                 client.close()
# #                 break
# #      # function to send messages
# #     def sendMessage(self):
# #         self.textCons.config(state=DISABLED)
# #         while True:
# #             message = (f"{self.name}: {self.msg}")
# #             client.send(message.encode(FORMAT))  
# #             break  
 
# # # create a GUI class object
# # g = GUI()


















# # GUI Client program.

# import socket
# from threading import Thread
# from tkinter import *
# from tkinter import font
# from tkinter import ttk
# # from chat import *
# # serverIp = "165.22.14.77"
# serverIp = "192.168.0.103"
# port = 9927
# client = socket.socket()
# client.connect((serverIp, port))
# FORMAT = "utf=8"
# class GUI:
#     # constructor method
#     def __init__(self):
       
#         # chat window which is currently hidden
#         self.Window = Tk()
#         self.Window.withdraw()
         
#         # login window
#         self.login = Toplevel()
#         # set the title
#         self.login.title("Login")
#         self.login.resizable(width = False,
#                              height = False)
#         self.login.configure(width = 400,
#                              height = 300)
#                               # create a Label
#         self.pls = Label(self.login,
#                        text = "Please login to continue",
#                        justify = CENTER,
#                        font = "Helvetica 14 bold")
         
#         self.pls.place(relheight = 0.15,
#                        relx = 0.2,
#                        rely = 0.07)
#         # create a Label
#         self.labelName = Label(self.login,
#                                text = "Name: ",
#                                font = "Helvetica 12")
         
#         self.labelName.place(relheight = 0.2,
#                              relx = 0.1,
#                              rely = 0.2)
#         self.entryName = Entry(self.login,
#                              font = "Helvetica 14")
         
#         self.entryName.place(relwidth = 0.4,
#                              relheight = 0.12,
#                              relx = 0.35,
#                              rely = 0.2)
         
#         # set the focus of the cursor
#         self.entryName.focus()
#          # create a Continue Button
#         # along with action
#         self.go = Button(self.login,
#                          text = "CONTINUE",
#                          font = "Helvetica 14 bold",
#                          command = lambda: self.goAhead(self.entryName.get())) #userNames = []
         
#         self.go.place(relx = 0.4,
#                       rely = 0.55)
#         self.Window.mainloop()
#     def goAhead(self, name):
#         self.login.destroy()
#         self.layout(name)
         
#         # the thread to receive messages
#         Thread(target = self.receive).start()
#         # The main layout of the chat
#     def layout(self,name):
       
#         self.name = name
#         # to show chat window
#         self.Window.deiconify()
#         self.Window.title("CHATROOM")
#         self.Window.resizable(width = False,
#                               height = False)
#         self.Window.configure(width = 470,
#                               height = 550,
#                               bg = "#17202A")
#         self.labelHead = Label(self.Window,
#                              bg = "#17202A",
#                               fg = "#EAECEE",
#                               text = self.name ,
#                                font = "Helvetica 13 bold",
#                                pady = 5)
#         self.labelHead.place(relwidth = 1)
#         self.line = Label(self.Window,
#                           width = 450,
#                           bg = "#ABB2B9")
         
#         self.line.place(relwidth = 1,
#                         rely = 0.07,
#                         relheight = 0.012)
         
#         self.textCons = Text(self.Window,
#                              width = 20,
#                              height = 2,
#                              bg = "#17202A",
#                              fg = "#EAECEE",
#                              font = "Helvetica 14",
#                              padx = 5,
#                              pady = 5)
#         self.textCons.place(relheight = 0.745,
#                             relwidth = 1,
#                             rely = 0.08)
         
#         self.labelBottom = Label(self.Window,
#                                  bg = "#ABB2B9",
#                                  height = 80)
         
#         self.labelBottom.place(relwidth = 1,
#                                rely = 0.825)
         
#         self.entryMsg = Entry(self.labelBottom,
#                               bg = "#2C3E50",
#                               fg = "#EAECEE",
#                               font = "Helvetica 13")
#          # place the given widget
#         # into the gui window
#         self.entryMsg.place(relwidth = 0.74,
#                             relheight = 0.06,
#                             rely = 0.008,
#                             relx = 0.011)
         
#         self.entryMsg.focus()
         
#         # create a Send Button
#         self.buttonMsg = Button(self.labelBottom,
#                                 text = "Send",
#                                 font = "Helvetica 10 bold",
#                                 width = 20,
#                                 bg = "#ABB2B9",
#                                 command = lambda : self.sendButton(self.entryMsg.get()))
#         self.buttonMsg.place(relx = 0.77,
#                              rely = 0.008,
#                              relheight = 0.06,
#                              relwidth = 0.22)
         
#         self.textCons.config(cursor = "arrow")
         
#         # create a scroll bar
#         scrollbar = Scrollbar(self.textCons)
         
#         # place the scroll bar
#         # into the gui window
#         scrollbar.place(relheight = 1,
#                         relx = 0.974)
#         scrollbar.config(command = self.textCons.yview)
         
#         self.textCons.config(state = DISABLED)
 
#     # function to basically start the thread for sending messages
#     def sendButton(self, msg):
#         self.textCons.config(state = DISABLED)
#         self.msg=msg
#         self.entryMsg.delete(0, END)
#         Thread(target = self.sendMessage).start()
#   # function to receive messages
#     def receive(self):
#         while True:
#             try:
#                 message = client.recv(1024).decode(FORMAT)
                 
#                 # if the messages from the server is NAME send the client's name
#                 if message == 'NAME':
#                     client.send(self.name.encode(FORMAT))
#                 else:
#                     # insert messages to text box
#                     self.textCons.config(state = NORMAL)
#                     self.textCons.insert(END,
#                                          message+"\n\n")
                     
#                     self.textCons.config(state = DISABLED)
#                     self.textCons.see(END)
#             except:
#                 # an error will be printed on the command line or console if there's an error
#                 print("An error occured!")
#                 client.close()
#                 break
         
#     # function to send messages
#     def sendMessage(self):
#         self.textCons.config(state=DISABLED)
#         while True:
#             message = (f"{self.name}: {self.msg}")
#             client.send(message.encode(FORMAT))  
#             break  
 
# # create a GUI class object
# g = GUI()