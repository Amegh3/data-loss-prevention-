from app.core.tasks import async_scan_and_alert

def main():
    print("Starting task trigger...")
    filename = "example.txt"
    content = "My credit card number is 4111 1111 1111 1111"
    user_email = "ttariyahgema@gmail.com"  # added user_email as task argument
    async_scan_and_alert.delay(user_email, filename, content)
    print("Task dispatched")

if __name__ == "__main__":
    main()
