import socket  # Importing socket library to handle network connections

# Function to scan ports on the target IP
def scan_ports(target_ip, start_port, end_port):
    open_ports = []  # List to store open ports
    print(f"\nScanning {target_ip} from port {start_port} to {end_port}...\n")

    # Loop through the given port range
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket using IPv4 and TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Set timeout to avoid long waits
                result = s.connect_ex((target_ip, port))  # Try to connect to the port
                if result == 0:  # If connection is successful, the port is open
                    print(f"Port {port} is OPEN")
                    open_ports.append(port)  # Add open port to the list
        except KeyboardInterrupt:
            print("\nScan aborted by user.")  # Handle Ctrl+C interruption
            break
        except socket.error:
            print(f"Couldn't connect to {target_ip}")  # Handle unreachable host
            break
    return open_ports  # Return the list of open ports

# Main function to interact with the user
def main():
    try:
        # Get user input for target IP and port range
        target_ip = input("Enter target IP address: ")
        start_port = int(input("Enter start port (e.g., 1): "))
        end_port = int(input("Enter end port (e.g., 1024): "))

        # Validate the port range
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 1 and 65535.")
            return

        # Perform the port scan
        open_ports = scan_ports(target_ip, start_port, end_port)

        # Print the result
        if open_ports:
            print("\nScan complete. Open ports:")
            print(", ".join(map(str, open_ports)))
        else:
            print("\nNo open ports found.")
    
    except ValueError:
        print("Please enter valid numbers for ports.")  # Handle non-integer inputs
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any other error

# Execute main function if script is run directly
if __name__ == "__main__":
    main()
