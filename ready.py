# Read the input file (replace 'input.txt' with your actual file name)
input_filename = 'modified.txt'

# Create a new output file (replace 'output.txt' with your desired output file name)
output_filename = 'modified_out.txt'

# Open the input file for reading
with open(input_filename, 'r') as infile:
    # Read each line from the input file
    lines = infile.readlines()

# Add double quotes to the start and end of each line
quoted_lines = ['"' + line.strip() + '", ' for line in lines]

# Write the modified lines to the output file
with open(output_filename, 'w') as outfile:
    outfile.write('\n'.join(quoted_lines))

print(f'Double quotes added to each line. Output saved to {output_filename}')

# Read the input file (replace 'input.txt' with your actual file name)
input_filename = 'deleted.txt'

# Create a new output file (replace 'output.txt' with your desired output file name)
output_filename = 'deleted_out.txt'

# Open the input file for reading
with open(input_filename, 'r') as infile:
    # Read each line from the input file
    lines = infile.readlines()

# Add double quotes to the start and end of each line
quoted_lines = ['"' + line.strip() + '", ' for line in lines]

# Write the modified lines to the output file
with open(output_filename, 'w') as outfile:
    outfile.write('\n'.join(quoted_lines))

print(f'Double quotes added to each line. Output saved to {output_filename}')