import mysql.connector as mysql

HOST = "165.22.14.77"
DATABASE = "dbSharvani"
USER = "sharvani"
PASSWORD = "pwdsharvani"
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
obj = db_connection.cursor()
obj.callproc("spGetDMartReports2")

for result in obj.stored_results():
	details = result.fetchall()

for det in details:
	print(det)
obj.close()
db_connection.close()







# print("Connected to:", db_connection.get_server_info())

# DELIMITER //
# CREATE PROCEDURE spGetDMartReports1()
# BEGIN
# 	SELECT
# 	BillNumber,
# 	(SELECT BillDate FROM BillHeader WHERE BillHeader.BillNumber = BillDetails.BillNumber) AS BillDate,
# 	ItemId,
# 	(SELECT Description FROM Item WHERE Item.ItemId = BillDetails.ItemId) AS Description,
# 	SoldQty,
# 	(SELECT UnitPrice FROM Item WHERE Item.ItemId = BillDetails.ItemId) AS UnitPrice,
# 	SoldQty * (SELECT UnitPrice FROM Item WHERE Item.ItemId = BillDetails.ItemId) AS TotalPrice
# 	FROM BillDetails;
# END //
# enter your code here!