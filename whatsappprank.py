import pywhatkit as kit
import time

def send_message(phone_number, message, delay):
    try:
        kit.sendwhatmsg_instantly(phone_number, message)
        print(f"Message sent to {phone_number}")
    except Exception as e:
        print(f"Failed to send message: {e}")

phone_number = "+91XXXXXXXXXX"  # Replace with your friend's phone number
message = "Pranked"
number_of_messages = 30
delay = 5  # Delay in seconds

for i in range(number_of_messages):
    send_message(phone_number, message, delay)
    time.sleep(delay)
