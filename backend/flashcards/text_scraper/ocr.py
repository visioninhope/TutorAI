

from spire.pdf.common import *
from spire.pdf import *
import pytesseract
from PIL import Image

import pytesseract
import pypdfium2 as pdfium
from pypdfium2 import PdfPage

import pipeline as piper


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




class OCR:
    def __init__(self, file):
        self.file = file
        self.image = None
        self.page_data = []
        
        
    def hoppelopp(self):
        """
        loops through each page of the pdf and extracts the text
        """
        
        # Create a PdfDocument object
        doc = PdfDocument()

        # Load a PDF document
        doc.LoadFromFile(self.file)

        # Get a specific page
        for page_num in range(doc.Pages.Count):
            page = doc.Pages.get_Item(page_num)
            
            
            for image in page.ExtractImages():
                    # image = Image.open(io.BytesIO(image))
                    # self.image = image
                    # self.preprocess()
                    # text = self.get_text()
                    # self.page_data.append(text)
                    self.img_dats.append(image)
            try:
                
                print("yo")
                    
                    
                # # Extract image from the page
                # images = page.extractImages()
                # if images:
                #     self.image = Image.open(io.BytesIO(images[0]))
                #     self.preprocess()
                #     text = self.get_text()
                #     self.page_data.append(text)
                # else:
                #     print(f"No images found on page {page_num}")
            except SpireException as e:
                print(f"An error occurred while extracting images from page {page_num}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        doc.Close()
            
            
        
    def preprocess(self):
        """
        preprocesses the image
        """
        pipeline: piper.Pipeline = piper.PipelineFactory(self.image).create_pipeline(1)
        pipeline.pipe()
        self.image = pipeline.get_image()
        
        

    def make_pdf_into_image_list(self, file) -> list[Image.Image]:
        """
        Converts a file into an image

        Converts a file into an image. The file can be in any format that can be converted into an image.

        Args:
            file: The file to convert into an image
        Returns:
            List of image names for the given files' pages
        """
        pdf = pdfium.PdfDocument(file)

        n_pages = len(pdf)
        pages_as_images = []
        for page_number in range(n_pages):
            page: PdfPage = pdf.get_page(page_number)
            pil_image = page.render(
                scale=300 / 72
            ).to_pil()  # Probably possible to optimize this.
            image_name = f"page_{page_number}"
            image_name = f"{image_name}.jpg"

            pages_as_images.append(pil_image)
        return pages_as_images
    
    def ocr_images(self, file):
        """
        take in pdf file, and calls a function that creates a list of images from the pdf file, then uses OCR to extract text from the images
        params: file: InMemoryUploadedFile
        """
        images: list[Image.Image] = self.make_pdf_into_image_list(file)
        
        for image in images:
            text = pytesseract.image_to_string(image)
            print(text)
            self.page_data.append(text)
        
    
    def get_page_data(self):
        return self.page_data
        
    
if __name__=="__main__":
    pdf_file = "TutorAI/backend/flashcards/text_scraper/assets/example.pdf"
    
    ocr = OCR(pdf_file)
    #ocr.hoppelopp()
    ocr.ocr_images(pdf_file)
    page_data = ocr.get_page_data()
    
    for page in page_data:
        print(page)
