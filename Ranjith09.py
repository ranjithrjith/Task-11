from datetime import datetime
import os

def create_file_with_custom_name(custom_name):
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Define the file name with the custom name provided
    file_name = f'{custom_name}.txt'
    
    # Create and open the file in write mode
    with open(file_name, 'w') as file:
        # Write the current timestamp to the file
        file.write(timestamp)
    
    print(f"File '{file_name}(timestamp)' has been created with the current timestamp as content.")

# Call the function with your custom file name
create_file_with_custom_name("my_custom_file")