import re

def extract_emails(input_file_path, output_file_path):
    try:
        # Read the input file
        with open(input_file_path, 'r') as file:
            content = file.read()

        # Use regular expression to extract emails
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)

        # Remove duplicates and sort
        unique_emails = sorted(set(emails))

        # Write emails to the output file
        with open(output_file_path, 'w') as file:
            for email in unique_emails:
                file.write(email + '\n')

        print(f"✅ Extracted {len(unique_emails)} unique email(s) to '{output_file_path}'")

    except FileNotFoundError:
        print(f"❌ File not found: {input_file_path}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Example usage
input_file = 'sample_input.txt'
output_file = 'extracted_emails.txt'
extract_emails(input_file, output_file)
