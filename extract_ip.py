from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import parameters
from selenium.webdriver.common.keys import Keys
import boto3

ec2_client = boto3.client('ec2',
                          aws_access_key_id='AKIAS4JV6BICBQYZD7WM',
                          aws_secret_access_key='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',
                          region_name='us-east-1')

instance_id = 'i-02b5cde04e15ef477'
response = ec2_client.describe_instances(InstanceIds=[instance_id])


public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']

driver = webdriver.Chrome()
driver.maximize_window()
sleep(0.5)

driver.get("https://scrapeops.io/app/login")
sleep(3)

username_input = driver.find_element(By.NAME, "email")
username_input.send_keys(parameters.username)
sleep(0.5)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(parameters.password)
sleep(0.5)

# click on the sign in button
driver.find_element(By.ID, "login-btn").click()
sleep(1)

driver.get("https://scrapeops.io/app/servers")
sleep(2)

driver.find_element(By.CLASS_NAME, "server-name").click()
sleep(1)
driver.find_element(By.CLASS_NAME, "outline-button").click()
sleep(0.5)

ip_input = driver.find_element(By.NAME, "server_ip_address")
ip_input.clear()
ip_input.send_keys(public_ip)
driver.find_element(By.XPATH, "//*[@class='mat-focus-indicator mat-raised-button mat-button-base']").click()
sleep(0.5)

driver.close()