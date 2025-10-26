import time

def health_check():
    """
    Perform a health check by simulating a delay.
    Returns True if the service is healthy.
    """
    time.sleep(1)  # Simulate some processing delay
    return True

def log(message):
    """
    Log a message to the console with a timestamp.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{timestamp}] {message}")

def main():
    """
    Main function to run the health check and log the result.
    """
    log("Day 0: Trading bot")
    if health_check():
        log("Health check passed: Service is healthy.")
    else:
        log("Health check failed: Service is unhealthy.")


if __name__ == "__main__":
    main()  