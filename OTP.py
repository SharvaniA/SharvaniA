# Generating OTP using API.

import requests
import random
def getOTPAndValidate():
	OTP = random.randint(11111, 99999)
	print(OTP)
	print(requests.get('https://www.fast2sms.com/dev/bulkV2?authorization=Xu0HdbJThvVBO4jkgEcnN5zMS67ArmWDsF1wefpax3YGKCtRl9dWLvNSGwEPKhulqoCjAVJ56MDpOrg7&variables_values=' + str(OTP) + '&route=otp&numbers=7995250666'
	).text)
	userEnteredOTP = int(input("Enter your OTP: "))
	validateOTP(userEnteredOTP, OTP)

def validateOTP(userEnteredOTP, OTP):
	if userEnteredOTP == OTP:
		print(requests.get('https://www.fast2sms.com/dev/bulkV2?authorization=Xu0HdbJThvVBO4jkgEcnN5zMS67ArmWDsF1wefpax3YGKCtRl9dWLvNSGwEPKhulqoCjAVJ56MDpOrg7&message=Welcome&language=english&route=q&numbers=7995250666').text)
	else:
		print("Invalid OTP")
		quit()
# print(givenOTP1 := input(requests.get('https://www.fast2sms.com/dev/bulkV2?authorization=Xu0HdbJThvVBO4jkgEcnN5zMS67ArmWDsF1wefpax3YGKCtRl9dWLvNSGwEPKhulqoCjAVJ56MDpOrg7&message=Enter OTP&language=english&route=q&numbers=7995250666').text))