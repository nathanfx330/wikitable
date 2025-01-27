import csv
import os

def csv_to_wiki_table(csv_filename, output_filename):
    # Get the absolute path of the CSV file
    csv_filepath = os.path.join(os.getcwd(), csv_filename)
    
    with open(csv_filepath, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        
        with open(output_filename, mode='w', encoding='utf-8') as output_file:
            # Start the table with the Wiki table syntax and centering style
            output_file.write("{| class=\"wikitable\" style=\"margin-left:auto; margin-right:auto;\"\n")
            
            # If there are rows, assume the first row is for headers
            if rows:
                # Add table headers
                headers = rows[0]
                output_file.write("! " + " !! ".join(headers) + "\n")
                
                # Add table content
                for row in rows[1:]:
                    output_file.write("|-\n")  # New row
                    output_file.write("| " + " || ".join(row) + "\n")
            
            # End the table
            output_file.write("|}\n")

    print(f"Table written to {output_filename}")

# File I/O
csv_filename = './input.csv'  # Relative path to your CSV file
output_filename = 'output_table.txt'  # Path to the output text file
csv_to_wiki_table(csv_filename, output_filename)
