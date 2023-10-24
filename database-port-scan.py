
import subprocess

def run_nmap(target):
    try:
        nmap_command = f'nmap -p 3306,5432,1433,1521,1526,27017,6379,5984,9042,9160,50000 -T2 -v -Pn {target}'
        subprocess.run(nmap_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    target = input("Enter the target IP address or hostname: ")
    run_nmap(target)
