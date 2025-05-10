#!/bin/python3
import subprocess

#--------------------------------------------------------------------------------------------------#
# Python studend activity to write a script to install and remove packages
#--------------------------------------------------------------------------------------------------#

def check_distro():
    try:
        # Check for /etc/os-release file
        result = subprocess.run(['cat', '/etc/os-release'], capture_output=True, text=True)
        if 'Ubuntu' in result.stdout:
            return 'apt'
        elif 'Fedora' in result.stdout:
            return 'dnf'
        elif 'CentOS' in result.stdout or 'Red Hat' in result.stdout:
            return 'yum'
        else:
            return 'pip'
    except subprocess.CalledProcessError:
        return 'pip'  # Default to pip if can't determine distro

def install_package(package_name):
    pkg_manager = check_distro()
    try:
        if pkg_manager == 'apt':
            subprocess.run(['sudo', 'apt', 'install', '-y', package_name], check=True)
        elif pkg_manager == 'dnf':
            subprocess.run(['sudo', 'dnf', 'install', '-y', package_name], check=True)
        elif pkg_manager == 'yum':
            subprocess.run(['sudo', 'yum', 'install', '-y', package_name], check=True)
        else:
            subprocess.run(['pip', 'install', package_name], check=True)
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")

def remove_package(package_name):
    pkg_manager = check_distro()
    try:
        if pkg_manager == 'apt':
            subprocess.run(['sudo', 'apt', 'remove', '-y', package_name], check=True)
        elif pkg_manager == 'dnf':
            subprocess.run(['sudo', 'dnf', 'remove', '-y', package_name], check=True)
        elif pkg_manager == 'yum':
            subprocess.run(['sudo', 'yum', 'remove', '-y', package_name], check=True)
        else:
            subprocess.run(['pip', 'uninstall', '-y', package_name], check=True)
        print(f"Successfully removed {package_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to remove {package_name}")

def list_installed_packages():
    pkg_manager = check_distro()
    try:
        if pkg_manager == 'apt':
            result = subprocess.run(['dpkg', '--list'], capture_output=True, text=True)
        elif pkg_manager == 'dnf':
            result = subprocess.run(['dnf', 'list', 'installed'], capture_output=True, text=True)
        elif pkg_manager == 'yum':
            result = subprocess.run(['yum', 'list', 'installed'], capture_output=True, text=True)
        else:
            result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        print("Installed packages:")
        print(result.stdout)
    except subprocess.CalledProcessError:
        print("Failed to list packages")
        
def update_package_list():
    pkg_manager = check_distro()
    try:
        match pkg_manager:
            case 'apt':
                subprocess.run(['sudo', 'apt', 'update'], check=True)
            case 'dnf':
                subprocess.run(['sudo', 'dnf', 'check-update'], check=True)
            case 'yum':
                subprocess.run(['sudo', 'yum', 'check-update'], check=True)
            case _:
                subprocess.run(['pip', 'list', '--outdated'], check=True)
        print("Package list updated successfully")
    except subprocess.CalledProcessError:
        print("Failed to update package list")

def display_menu():
    print("\nPackage Manager Menu:")
    print("1. Update package list")
    print("2. Install a package")
    print("3. Remove a package")
    print("4. List installed packages")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            update_package_list()
        elif choice == '2':
            package = input("Enter package name to install: ")
            install_package(package)
        elif choice == '3':
            package = input("Enter package name to remove: ")
            remove_package(package)
        elif choice == '4':
            list_installed_packages()
        elif choice == '5':
            print("Exiting package manager...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()