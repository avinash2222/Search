from flask import Flask, render_template, request
import PyPDF2
import re
import os
app = Flask(__name__)
  
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/', methods=['POST'])
def getvalue():
    result=request.form['search2']
    result=compute(result)
    return render_template('pass.html', s=result)
  
  
  
def compute(result):
    # import packages
    aa=""
    for foldername,subfolders,files in os.walk(r"C:/Users/Avinash/Desktop/Searching-String-in-all-PDF-file-master/Searching-String-in-all-PDF-file-master/app/"):
        for file in files:
            # open the pdf file
            object = PyPDF2.PdfFileReader(os.path.join(foldername,file))

            # get number of pages
            NumPages = object.getNumPages()

            # define keyterms
            String = 'Convolution'

            # extract text and do the search
            for i in range(0, NumPages):
                PageObj = object.getPage(i)
                Text = PageObj.extractText() 
                # print(Text)
                ResSearch = re.search(String, Text)
                if ResSearch==None :
                    continue
                else :
                    aa=aa+ '\n' + '. '+file
                    break
    return aa
  
if __name__ == '__main__':
  app.run(debug=True)