def pdfimports():
  from pdfminer3.layout import LAParams, LTTextBox
  from pdfminer3.pdfpage import PDFPage
  from pdfminer3.pdfinterp import PDFResourceManager
  from pdfminer3.pdfinterp import PDFPageInterpreter
  from pdfminer3.converter import PDFPageAggregator
  from pdfminer3.converter import TextConverter
  import io
  return print('imports complete')

def get_data():
  from google.colab import drive
  drive.mount('/content/drive', force_remount=True)
  from pathlib import Path
  district_list = []
  entries = Path("/content/drive/My Drive/LWP")
  for entry in entries.iterdir():
    district_list.append(entry.name)
  return print(district_list, len(district_list))

def get_list():
  from pathlib import Path
  district_list = []
  entries = Path("/content/drive/My Drive/LWP")
  for entry in entries.iterdir():
      district_list.append(entry.name)
  print(len(district_list), district_list)
  alpha_district_list = sorted(district_list)
  return print(alpha_district_list)

def process_pdf_files(list_of_file_names):
  resource_manager = PDFResourceManager()
  fake_file_handle = io.StringIO()
  converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
  page_interpreter = PDFPageInterpreter(resource_manager, converter)
  text_dictionary = {}
  for name in list_of_file_names:
    if name.endswith('.pdf') or name.endswith('.PDF'):
      with open(entries / name, 'rb') as fh:
          i = 0
          for page in PDFPage.get_pages(fh,
                                        caching=True,
                                        check_extractable=True):
                # i += 1
                # print(i)
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

def get_dictionary():
  big_dictionary = {}
  from pathlib import Path
  district_list = []
  entries = Path("/content/drive/My Drive/LWP")
  for entry in entries.iterdir():
    district_list.append(entry.name)
  alpha_district_list = sorted(district_list)
      for name in alpha_district_list:
        small_dictionary = process_pdf_files([name])  #do one name at a time
        big_dictionary[name] = small_dictionary[name]
  return print(list(big_dictionary.keys()))  #should see this grow

def addv(x:list, y:list) -> list:
  assert isinstance(x, list), f"x must be a list but instead is {type(x)}"
  assert isinstance(y, list), f"y must be a list but instead is {type(y)}"
  assert len(x) == len(y), f"x and y must be the same length"

  #result = [c1 + c2 for c1, c2 in zip(x, y)]  #one-line compact version

  result = []
  for i in range(len(x)):
    c1 = x[i]
    c2 = y[i]
    result.append(c1+c2)

  return result
  
def dividev(x:list, c) -> list:
  assert isinstance(x, list), f"x must be a list but instead is {type(x)}"
  assert isinstance(c, int) or isinstance(c, float), f"c must be an int or a float but instead is {type(c)}"

  #result = [v/c for v in x]  #one-line compact version

  result = []
  for i in range(len(x)):
    v = x[i]
    result.append(v/c) #division produces a float

  return result

def meanv(matrix: list) -> list:
    assert isinstance(matrix, list), f"matrix must be a list but instead is {type(x)}"
    assert len(matrix) >= 1, f'matrix must have at least one row'

    #Python transpose: sumv = [sum(col) for col in zip(*matrix)]

    sumv = matrix[0]  #use first row as starting point in "reduction" style
    for row in matrix[1:]:   #make sure start at row index 1 and not 0
      sumv = addv(sumv, row)
    mean = dividev(sumv, len(matrix))
    return mean

def wordcounts(s:str): #definining function
  scores = [] #creating new list
  doc = nlp(s.lower())
  for token in doc: #for every item in list
    if token.pos_ == 'VERB':
      scores.append('2')
    if token.text == 'must':
      scores.append('1')
    if token.text == 'shall':
      scores.append('1')
    if token.text == 'will':
      scores.append('1')
    #add mean of vector to list 
  #  if average == []: #if not legal token 
  #   return [0.0]*300 #make a 300-element vector of zeroes 
  # policy_avg = meanv(scores) #function to calculate mean of vector
  return scores #return the complete list of vector means 
