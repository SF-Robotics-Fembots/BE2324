import datetime
import time

def check_wifi_connection():
    return True  # Change to your actual WiFi check logic

def report_current_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current time:", current_time)

def main():
    while True:
        if check_wifi_connection():
            report_current_time()
            # Wait for a certain interval before checking again
            time.sleep(60)  # Wait for 60 seconds (1 minute) before checking again
        else:
            print("WiFi not connected. Waiting to reconnect...")
            # Wait for a certain interval before checking again
            time.sleep(10)  # Wait for 10 seconds before checking WiFi again

if __name__ == "__main__":
    main()