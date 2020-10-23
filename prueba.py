from selenium import webdriver
from getpass import getpass

firstName  = input("Teclee un nombre: ")
nameInitial  = input("Teclee su segundo nombre: ")
lastName = input("Teclee su apellido: ")
email = input("Ponga su direccion email: ")
password = getpass("Teclee una contraseña: ")
confirmPassword  = getpass("Confirme su contraseña: ")

driver = webdriver.Chrome("C:\\Dev\\WebDrivers\\chromedriver.exe")
driver.get("http://demo-store.seleniumacademy.com/customer/account/create/")

firstName_text = driver.find_element_by_id("firstname")
firstName_text.send_keys(firstName)

nameInitial_text = driver.find_element_by_id("middlename")
nameInitial_text.send_keys(nameInitial)

lastName_text = driver.find_element_by_id("lastname")
lastName_text.send_keys(lastName)

email_text = driver.find_element_by_id("email_address")
email_text.send_keys(email)

password_text = driver.find_element_by_id("password")
password_text.send_keys(password)

confirmPassword_text = driver.find_element_by_id("confirmation")
confirmPassword_text.send_keys(confirmPassword)

#register_Button = driver.find_element_by_css_selector("button[ type=\"submit\"  ]").click()
#register_Button = driver.find_element_by_class_name("button")
#register_Button = driver.find_element_by_xpath("//*[@id="form-validate"]/div[2]/button")
register_Button = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button")
register_Button.submit()