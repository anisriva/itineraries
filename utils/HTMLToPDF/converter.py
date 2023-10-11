import os
from weasyprint import HTML

def get_html_filepath():
    """Prompt the user to input a valid HTML file path repeatedly."""
    while True:
        filepath = input("Enter the path to the html: ")
        if os.path.exists(filepath) and filepath.endswith('.html'):
            return filepath
        else:
            print("Invalid HTML file path. Please try again.")

def generate_pdf_from_html(filepath):
    """Generate a PDF from the provided HTML file path."""
    # Extracting the parent folder's name from the filepath
    parent_folder_name = os.path.basename(os.path.dirname(filepath))
    # Determine the directory where the Python script is running
    current_script_folder = os.path.dirname(os.path.realpath(__file__))
    # Create the output directory if it doesn't exist
    output_dir = os.path.join(current_script_folder, 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Construct the output filepath
    outfile = os.path.join(output_dir, f"{parent_folder_name}_out.pdf")
    try:
        HTML(filename=filepath).write_pdf(outfile)
        print(f"PDF generated successfully at {outfile}")
    except Exception as e:
        print(f"Error generating PDF: {e}")


def main():
    html_filepath = get_html_filepath()
    generate_pdf_from_html(html_filepath)

if __name__ == "__main__":
    main()
