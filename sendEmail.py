import smtplib
import ssl
import mysql.connector as mysql
import pandas as pd
import time
HOST = "165.22.14.77"
DATABASE = "dbSharvani"
USER = "sharvani"
PASSWORD = "pwdsharvani"
connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
cursor = connection.cursor()
port = 587  
smtp_server = "smtp.gmail.com"
sender = "atchulasharvani29@gmail.com"
sender_password = ""
while(1):
	cursor.execute('''SELECT MailId FROM Supplier, OrderItems, Item WHERE OrderItems.ItemId = Item.ItemId AND Supplier.SupplierId = Item.SupplierId''')
	recipientMail = cursor.fetchall()
	print(recipientMail)
	if recipientMail != []:
		print("3")
		recipient = recipientMail[0][0]
		# recipient = "ravi_pendyala@tecnics.com"
		# recipient = "atchulasharvani29@gmail.com"
		CC = "atchulasharvani29@gmail.com"
		print("2")
		cursor.execute("SELECT Item.ItemId, OrderOty, Description FROM Item, OrderItems, Supplier WHERE OrderItems.ItemId = Item.ItemId AND Supplier.SupplierId = Item.SupplierId")
		messageRequirements = cursor.fetchall()
		Item = messageRequirements[0][0]
		OrderQty = messageRequirements[0][1]
		Description = messageRequirements[0][2]
		message = ("""CC: """ + CC + """\n\n\nSubject: Order from DMart.\n\n
This Mail is to confirm an order from DMart Warangal Branch.
We require an Order of """ + str(OrderQty) + """ Units of """ + Description + """ (""" + Item + """).
We are running out of stock. So, we request you to deliver the order as soon as possible.

Thanking You,
Yours faithfully,
Manager,
Warangal Branch,
DMart. """)
		SSL_context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
			server.starttls(context=SSL_context)
			server.login(sender, sender_password)
			server.sendmail(sender, [recipient, CC], message)
		print("Email send successfully.")
		cursor.execute("DELETE FROM OrderItems")
		connection.commit()
	time.sleep(10)
connection.close()



		# recipient = "ravi_pendyala@tecnics.com"
		# CC = "ravi_pendyala@tecnics.com"


# Subject: Order from DMart.

# This Mail is to confirm an order from DMart Warangal Branch.
# We require an Order of 500 Units of Kisam Jam (KJ576).
# We are running out of stock. So, we request you to deliver the order as soon as possible.

# Thanking You,
# Yours faithfully,
# Manager,
# Warangal Branch,
# DMart. 


# Subject: Placing an order for DMart India.

# I am writing this Mail to place an order for DMart Vizg.
# We require a regular order of 1Kg of 600 Units of Sugar of Item Id SR658. 
# Payment will be paid after the receiving of the order.
# Deliver the order as soon as possible.

# Thank You,
# Store Manager,
# DMart Vizag.











# import smtplib
# import ssl
# import mysql.connector as mysql
# import pandas as pd
# HOST = "165.22.14.77"
# DATABASE = "dbSharvani"
# USER = "sharvani"
# PASSWORD = "pwdsharvani"
# connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
# cursor = connection.cursor()
# port = 587  
# smtp_server = "smtp.gmail.com"
# sender = "atchulasharvani29@gmail.com"
# sender_password = "Sharvani$$99"
# cursor.execute('''SELECT MailId FROM Supplier, OrderItems WHERE Supplier.SupplierId = OrderItems.SupplierId''')
# recipientMail = cursor.fetchall()
# recipient = recipientMail[0][0]
# print("Email send successfully.")
# message = """Subject: Order Confirmation.
# Place an Order from DMart."""
# SSL_context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
# 	server.starttls(context=SSL_context)
# 	server.login(sender, sender_password)
# 	server.sendmail(sender, recipient, message)
# connection.close()
# "Need order of 500 for Item KJ576" 










# import smtplib
# import ssl
# import mysql.connector as mysql
# import pandas as pd
# HOST = "165.22.14.77"
# DATABASE = "dbSharvani"
# USER = "sharvani"
# PASSWORD = "pwdsharvani"
# connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
# cursor = connection.cursor()
# port = 587  
# smtp_server = "smtp.gmail.com"
# sender = "atchulasharvani29@gmail.com"
# sender_password = "Sharvani$$99"
# cursor.execute('''SELECT MailId FROM Supplier WHERE SupplierId = %s''' %('7275'))
# # connection.commit()
# recipientMail = cursor.fetchall()
# # for message in deleteMessage:
# # 	for msg in message:
# # 		print(msg)
# recipient = recipientMail[0][0]
# print(recipient)
# message = """
# Subject: This is a test message
# Sent using Python."""
# SSL_context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
# 	server.starttls(context=SSL_context)
# 	server.login(sender, sender_password)
# 	server.sendmail(sender, recipient, message)
# connection.close()
























# # Import the following module
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import os
# from tkinter import *
# class GUI:
# 	def __init__(self):
# 		self.window = Tk()
# 		self.window.withdraw()
# 		self.login = Tk()
# 		self.login.title("Login")
# 		self.login.configure(width = 400, height = 300)
# 		self.pls = Label(self.login, text = "Please login to continue", justify = CENTER, font = "Helvetica 14 bold")
# 		self.pls.place(relheight = 0.15, relx = 0.2, rely = 0.07)
# 		self.emaillabelName = Label(self.login, text = "Email: ", font = "Helvetica")
# 		self.emaillabelName.place(relheight = 0.12, relx = 0.1, rely = 0.2)
# 		self.passwordlabel = Label(self.login, text = "Password: ", font = "Helvetica")
# 		self.passwordlabel.place(relheight = 0.12, relx = 0.1, rely = 0.3)
# 		self.emailEntry = Entry(self.login, font = "Helvetica 14")
# 		self.emailEntry.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.2)
# 		self.emailEntry.focus()
# 		self.passwordEntry = Entry(self.login, font = "Helvetica 14")
# 		self.passwordEntry.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.3)
# 		self.passwordEntry.focus()
# 		self.passwordEntry.configure(show = "*")
# 		self.go  = Button(self.login, text = "SignIn", font = "Helvetica 14 bold", command = lambda: self.layout(self.emailEntry.get(), self.passwordEntry.get()))
# 		self.login.bind('<Return>', self.continueKey)
# 		self.go.place(relx = 0.4, rely = 0.55)
# 		self.window.mainloop()
# 	def continueKey(self, e):
# 		self.layout(self.emailEntry.get(), self.passwordEntry.get())
# 	def layout(self, email, password):
# 		self.login.destroy()
# 		self.window.deiconify()
# 		self.window.title("Compose")
# 		self.window.configure(width = 470, height = 550, bg = "#808080")
# 		self.fromAddr = Label(self.window, bg = "#e5e4e2", fg = "#17202A", text = "from: " + email, font = "Helvetica 13", padx = 3)
# 		self.fromAddr.place(relwidth = 1)
# 		# self.line = Label(self.Window, width = 450, bg = "#ABB2B9")
# 		# self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
# 		# self.toAddrName = Label(self.window, text = "To: ", font = "Helvetica")
# 		# self.toAddrName.place(relheight = 0.05, relx = 0.1, rely = 0.2)
# 		self.fromlabel = Label(self.window, text = "To:", font = "Helvetica")
# 		self.fromlabel.place(relheight = 0.05, relwidth = 0.1, rely = 0.05)

# 		self.toAddr = Entry(self.window, font = "Helvetica 13")
# 		self.toAddr.place(relwidth = 0.9, relheight = 0.05, rely = 0.05, relx = 0.1)
# 		self.toAddr.focus()

# 		self.cclabel = Label(self.window, text = "CC:", font = "Helvetica")
# 		self.cclabel.place(relwidth = 0.2, relheight = 0.05, rely = 0.11)

# 		self.cc = Entry(self.window, font = "Helvetica")
# 		self.cc.place(relwidth = 0.8, relheight = 0.05, rely = 0.11, relx = 0.2)
# 		self.cc.focus()
# 		# self.window.bind('<Return>', self.handler)
# 		# self.line = Label(self.window, width = 450, bg = "#ABB2B9")
# 		# self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
# 		self.subjectlabel = Label(self.window, text = "Subject:", font = "Helvetica")
# 		self.subjectlabel.place(relwidth = 0.2, relheight = 0.05, rely = 0.17)

# 		self.subject = Entry(self.window, font = "Helvetica 13")
# 		self.subject.place(relwidth = 0.8, relheight = 0.05, rely = 0.17, relx = 0.2)
# 		self.subject.focus()

# 		self.entryMsg = Text(self.window, bg = "#bccbda", fg = "#101a23", font = "Helvetica 13")
# 		self.entryMsg.place(relwidth = 1, relheight = 0.6, rely = 0.22) 
# 		self.entryMsg.focus()

# 		self.buttonMsg = Button(self.window, text = "Send", font = "Helvetica 10 bold", width = 20, bg = "#ABB2B9", 
# 			command = lambda : self.sendButton(self.entryMsg.get("1.0", END), self.toAddr.get(), email, password, self.subject.get(), self.cc.get()))
# 		self.buttonMsg.place(rely = 0.84, relheight = 0.15, relwidth = 1)

# 		self.window.bind('<Return>', self.handler)
# 		# self.window.config(cursor = "arrow")
# 		scrollbar = Scrollbar(self.window)
# 		scrollbar.place(relheight = 1, relx = 0.974)
# 		scrollbar.config(command = self.window.yview)
# 	def handler(self, e):
# 		self.sendButton(self.entryMsg.get(), self.toAddr.get(), self.emailEntry.get("1.0", END), self.passwordEntry.get(), self.subject.get(), self.cc.get())
# 	def sendButton(self, msg, receiverAddre, senderAddre, password, subject, cc):
# 		print(msg)
# 		print(receiverAddre)
# 		print(senderAddre)
# 		print(password)
# 		print(subject)
# 		print(cc)
# 		textInMail = "From: %s\r\n"%(senderAddre) + "To: %s\r\n"%(receiverAddre) + "CC: %s\r\n"%",".join([cc]) + "Subject: %s\r\n\n"%subject + "\r\n" + msg
# 		receiverAddre = [receiverAddre, cc]
# 		try:
# 		    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# 		    smtp_server.ehlo()
# 		    smtp_server.login(senderAddre, password)
# 		    smtp_server.sendmail(senderAddre, receiverAddre, textInMail)
# 		    smtp_server.close()
# 		    print ("Email sent successfully!")
# 		except Exception as ex:
# 		    print ("Something went wrong….",ex)
# 		# smtp.quit()
# g = GUI()

# # # atchulasharvani29@gmail.com
# # # Sharvani$$99































# # Import the following module
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import os
# from tkinter import *
# smtp = smtplib.SMTP('smtp.gmail.com', 587)
# smtp.ehlo()
# smtp.starttls()
# smtp.ehlo()
# # Login with your email and password
# # smtp.login('atchulasharvani29@gmail.com', 'xutveowmtjfezvhy')
    
# # send our email message 'msg' to our boss
# def message(subject="Python Notification", text="", img=None, attachment=None):
    
#     # build message contents
#     msg = MIMEMultipart()
      
#     # Add Subject
#     msg['Subject'] = subject  
      
#     # Add text contents
#     msg.attach(MIMEText(text))

# # Call the message function
# # msg = message()
  
# # Make a list of emails, where you wanna send mail
# # to = ["atchulasharvani29@gmail.com"]
  
# # Provide some data to the sendmail function!
  
#  # Finally, don't forget to close the connection
# smtp.quit()



# class GUI:
# 	def __init__(self):
# 		self.window = Tk()
# 		self.window.withdraw()
# 		self.login = Tk()
# 		self.login.title("Login")
# 		self.login.configure(width = 400, height = 300)
# 		self.pls = Label(self.login, text = "Please login to continue", justify = CENTER, font = "Helvetica 14 bold")
# 		self.pls.place(relheight = 0.15, relx = 0.2, rely = 0.07)
# 		self.emaillabelName = Label(self.login, text = "Email: ", font = "Helvetica")
# 		self.emaillabelName.place(relheight = 0.2, relx = 0.1, rely = 0.2)
# 		self.passwordlabel = Label(self.login, text = "Password: ", font = "Helvetica")
# 		self.passwordlabel.place(relheight = 0.2, relx = 0.1, rely = 0.3)
# 		self.emailEntry = Entry(self.login, font = "Helvetica 14")
# 		self.emailEntry.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.2)
# 		self.emailEntry.focus()
# 		self.passwordEntry = Entry(self.login, font = "Helvetica 14")
# 		self.passwordEntry.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.3)
# 		self.passwordEntry.focus()
# 		self.go  = Button(self.login, text = "SignIn", font = "Helvetica 14 bold", command = lambda: self.continueKey(self.emailEntry.get(), self.passwordEntry.get()))
# 		self.login.bind('<Return>', self.continueKey)
# 		self.go.place(relx = 0.4, rely = 0.55)
# 		self.window.mainloop()
# 	def continueKey(self, e):
# 		self.layout(self.emailEntry.get(), self.passwordEntry.get())
# 	# def goAhead(self, mail, password):
# 		# self.mailID.(self.emailEntry.get())
# 		# self.password.(self.passwordEntry.get())
# 		# self.layout()
# 	def layout(self, email, password):
# 		self.login.destroy()
# 		self.window.deiconify()
# 		self.window.title("Compose")
# 		self.window.configure(width = 470, height = 550, bg = "#808080")
# 		self.fromAddr = Label(self.window, bg = "#e5e4e2", fg = "#17202A", text = "from: " + self.email, font = "Helvetica 13", pady = 5)
# 		self.fromAddr.place(relwidth = 1)
# 		self.line = Label(self.Window, width = 450, bg = "#ABB2B9")
# 		self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
# 		self.toAddr = Entry(self.login, font = "Helvetica 14")
# 		self.toAddr.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.2)
# 		self.toAddr.focus()
# 		self.line = Label(self.Window, width = 450, bg = "#ABB2B9")
# 		self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012)
# 		self.entryMsg = Entry(self.window, bg = "#7ebcfa", fg = "#101a23", font = "Helvetica 13")
# 		self.entryMsg.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011) 
# 		self.entryMsg.focus()
# 		self.buttonMsg = Button(self.labelBottom, text = "Send", font = "Helvetica 10 bold", width = 20, bg = "#ABB2B9", command = lambda : self.sendButton(self.entryMsg.get()))
# 		self.buttonMsg.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)
# 		self.Window.bind('<Return>', self.handler)
# 		self.textCons.config(cursor = "arrow")
# 		scrollbar = Scrollbar(self.textCons)
# 		scrollbar.place(relheight = 1, relx = 0.974)
# 		scrollbar.config(command = self.textCons.yview)
# 	def handler(self, e):
# 		self.sendButton(self.entryMsg.get(), self.toAddr.get(), self.mailEntry.get(), self.passwordEntry.get())
# 	def sendButton(self, msg, receiverAddre, senderAddre, password):
# 		self.receiverAddre = to
# 		self.msg = msg
# 		self.senderAddre = fromMail
# 		self.password = password
# 		smtp.sendmail(from_addr=fromMail, to_addrs=to, msg=msg.as_string())
# 		msg = message(msg)
# 		smtp.login(fromMail, password)
# g = GUI()


























# # Import the following module
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import os
  
# # initialize connection to our
# # email server, we will use gmail here
# smtp = smtplib.SMTP('smtp.gmail.com', 587)
# smtp.ehlo()
# smtp.starttls()
# smtp.ehlo()
  
# # Login with your email and password
# smtp.login('atchulasharvani29@gmail.com', 'Sharvani$$99')

# # xutveowmtjfezvhy
# # send our email message 'msg' to our boss
# def message(subject="Python Notification", 
#             text="Good! " + "Hi there!", img=None,
#             attachment=None):
    
#     # build message contents
#     msg = MIMEMultipart()
      
#     # Add Subject
#     msg['Subject'] = subject  
      
#     # Add text contents
#     msg.attach(MIMEText(text))  
  
  
  
# # Call the message function
# msg = message()
  
# to = ["atchulasharvani29@gmail.com"]
  
# smtp.sendmail(from_addr="atchulasharvani29@gmail.com",
#               to_addrs=to, msg=str(msg))
#  # .as_string() 
#  # Finally, don't forget to close the connection
# smtp.quit()

















  # # Check if we have anything
    # # given in the img parameter
    # if img is not None:
          
    #     # Check whether we have the lists of images or not!
    #     if type(img) is not list:  
            
    #           # if it isn't a list, make it one
    #         img = [img] 
  
    #     # Now iterate through our list
    #     for one_img in img:
            
    #           # read the image binary data
    #         img_data = open(one_img, 'rb').read()  
    #         # Attach the image data to MIMEMultipart
    #         # using MIMEImage, we add the given filename use os.basename
    #         msg.attach(MIMEImage(img_data,
    #                              name=os.path.basename(one_img)))
  
    # # We do the same for
    # # attachments as we did for images
    # if attachment is not None:
          
    #     # Check whether we have the
    #     # lists of attachments or not!
    #     if type(attachment) is not list:
            
    #           # if it isn't a list, make it one
    #         attachment = [attachment]  
  
    #     for one_attachment in attachment:
  
    #         with open(one_attachment, 'rb') as f:
                
    #             # Read in the attachment
    #             # using MIMEApplication
    #             file = MIMEApplication(
    #                 f.read(),
    #                 name=os.path.basename(one_attachment)
    #             )
    #         file['Content-Disposition'] = f'attachment;\
    #         filename="{os.path.basename(one_attachment)}"'
              
    #         # At last, Add the attachment to our message object
    #         msg.attach(file)
    # return msg





















# import smtplib
# import ssl
# port = 587  
# smtp_server = "smtp.gmail.com"
# sender = "atchulasharvani29@gmail.com"
# recipient = "atchulasharvani29@gmail.com"
# sender_password = "Sharvani$$99"
# message = """
# Subject: This is a test message
# Sent using Python."""
# SSL_context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
# 	server.starttls(context=SSL_context)
# 	server.login(sender, sender_password)
# 	server.sendmail(sender, recipient, message)




# import smtplib

# sender = 'atchulasharvani29@gmail.com'
# receivers = 'atchulasharvani29@gmail.com'

# message = """From: From Person <from@fromdomain.com>
# To: To Person <to@todomain.com>
# Subject: SMTP e-mail test

# This is a test e-mail message.
# """

# try:
#    smtpObj = smtplib.SMTP('192.168.0.104')
#    smtpObj.sendmail(sender, receivers, message)         
#    print("Successfully sent email")
# except BaseException:
#    print("Error: unable to send email")







# import smtplib
# import ssl
# port = 587
# smtp_server = "smtp-mail.outlook.com"
# sender = "sender@outlook.com"
# recipient = "receiver@gmail.com"
# sender_password = "strongpassword"
# messag = """
# Subject:.................."""
# SSL_context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
# 	server.starttls(context=SSL_context)
# 	server.login(sender, sender_password)
# 	server.sendmail(sender, recipient, message)