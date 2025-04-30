from PyPDF2 import PdfReader, PdfWriter

# Load PDF
pdf_path = "B30_MC_Complete_Lab_Manual[1].pdf"
pdf_reader = PdfReader(pdf_path)

# Define experiment page ranges
experiments = {
    "B30_MC_Experiment_1": (5, 29),
    "B30_MC_Experiment_2": (30, 41),
    "B30_MC_Experiment_3": (42, 52),
    "B30_MC_Experiment_4": (53, 66),
    "B30_MC_Experiment_5": (67, 88),
    "B30_MC_Experiment_6": (89, 103),
    "B30_MC_Experiment_7": (104, 117),
    "B30_MC_Experiment_8": (118, 132),
    "B30_MC_Experiment_9": (133, 143),
    "B30_MC_Experiment_10": (144, 154),
}

# Extract and save each experiment as a PDF
for exp_name, (start, end) in experiments.items():
    pdf_writer = PdfWriter()
    
    # Add pages to the new PDF
    for page_num in range(start - 1, end):  # Adjusting for 0-based index
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    # Save the new PDF
    output_pdf_path = f"{exp_name}.pdf"
    with open(output_pdf_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

print("Experiments extracted and saved as PDFs successfully!")
