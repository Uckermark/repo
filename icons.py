import os

def add_icon_key(package_content, icon_path):
    # Add Icon key to the package content
    return f'{package_content.rstrip()}\nIcon: {icon_path}\n\n'

def update_packages_file(packages_path, updated_content):
    with open(packages_path, 'w') as packages_file:
        packages_file.write(updated_content)

def main():
    repo_path = '.'
    packages_path = os.path.join(repo_path, 'Packages')

    # Read the content of the Packages file
    with open(packages_path, 'r') as packages_file:
        packages_content = packages_file.read()

    # Iterate through all packages in the Packages file
    packages = packages_content.split('\n\n')
    updated_packages = []

    for package_content in packages:
        package_lines = package_content.split('\n')
        package_id = next((line.split(' ')[1] for line in package_lines if line.startswith('Package: ')), None)

        if package_id:
            icon_path = os.path.join(repo_path, 'icons', f'{package_id}.webp')

            # Check if the icon file exists
            if os.path.exists(icon_path):
                # Add Icon key to the package
                updated_package_content = add_icon_key(package_content, f'https://repo.uckermark.dev/icons/{package_id}.webp')
                updated_packages.append(updated_package_content)
                continue

        # If no modification is made, keep the original package content
        updated_packages.append(package_content)

    # Update the Packages file with the modified content
    updated_packages_content = '\n\n'.join(updated_packages)
    update_packages_file(packages_path, updated_packages_content)

if __name__ == "__main__":
    main()

