def installs:
  !pip install pdfminer3
  !pip install spacy 
  
  
def imports:
  from pdfminer3.layout import LAParams, LTTextBox
  from pdfminer3.pdfpage import PDFPage
  from pdfminer3.pdfinterp import PDFResourceManager
  from pdfminer3.pdfinterp import PDFPageInterpreter
  from pdfminer3.converter import PDFPageAggregator
  from pdfminer3.converter import TextConverter
  import io
  import spacy 
  !python -m spacy download en_core_web_md
  import en_core_web_md
  nlp = en_core_web_md.load()


def process_pdf_files(list_of_file_names):
  resource_manager = PDFResourceManager()
  fake_file_handle = io.StringIO()
  converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
  page_interpreter = PDFPageInterpreter(resource_manager, converter)
  text_dictionary = {}
  for name in list_of_file_names:
    print(name)
    with open(entries / name, 'rb') as fh:
        i = 0
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            print(i)
            i += 1
            try:
              page_interpreter.process_page(page)
            except:
              print(i)

        text = fake_file_handle.getvalue()
        text_dictionary[name] = text

  # close open handles
  converter.close()
  fake_file_handle.close()
  return text_dictionary


