import os

# Define the base path where your application directories are located
base_path = os.path.expanduser('~/projects/InvoicePlane-CI4/app/')
directories_to_process = ['Libraries', 'Models']

# Function to add namespaces to PHP files and count changes
def add_namespace_to_file(file_path, namespace):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if namespace is already added
    namespace_already_added = any(line.startswith('namespace') for line in lines)
    if namespace_already_added:
        print(f"Namespace already exists in: {file_path}")
        return False

    # Insert the namespace and use statements at the beginning of the file
    new_lines = [f'<?php\n\nnamespace {namespace};\n\n'] + lines
    with open(file_path, 'w') as file:
        file.writelines(new_lines)
    
    return True

# Counter for the number of changes made
changes_count = 0

# Iterate over each directory in the list
for directory in directories_to_process:
    current_path = os.path.join(base_path, directory)
    
    # Iterate over all directories and files in the current directory
    for root, dirs, files in os.walk(current_path):
        for file in files:
            if file.endswith('.php'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, base_path)
                namespace = 'App\\' + '\\'.join(os.path.dirname(relative_path).split(os.sep))

                # Correct namespace for directories
                if directory == 'Libraries':
                    namespace = namespace.replace('Libraries', 'Libraries')
                elif directory == 'Models':
                    namespace = namespace.replace('Models', 'Models')

                print(f"Processing file: {file_path} with namespace: {namespace}")
                if add_namespace_to_file(file_path, namespace):
                    changes_count += 1
                    print(f"Added namespace to: {file_path}")

print(f"Total changes made: {changes_count}")

