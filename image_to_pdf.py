import img2pdf
import os

def images_to_pdf(directory, output_pdf):
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
    image_files = []

    for filename in os.listdir(directory):
        ext = os.path.splitext(filename)[1].lower()
        if ext in image_extensions:
            image_files.append(os.path.join(directory, filename))

    image_files.sort()

    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(image_files))

directory = '/XXX/XXX/XXX'  # Path to your image directory

output_pdf_directory = '/XXX/XXXX/XXX'  # Path to your output directory

output_pdf_filename = 'output.pdf'

os.makedirs(output_pdf_directory, exist_ok=True)

output_pdf = os.path.join(output_pdf_directory, output_pdf_filename)

images_to_pdf(directory, output_pdf)
