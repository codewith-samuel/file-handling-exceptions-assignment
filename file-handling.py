def process_file():
    try:
        # Prompt user for input filename
        input_filename = input("Enter the input filename: ")
        
        # Open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename by appending '_modified' to the original name
        output_filename = input_filename.rsplit('.', 1)[0] + '_modified.txt'
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"File processed successfully! Modified content written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the program
process_file()
