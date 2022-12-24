# streamlit_tesseract_scanner
OCR Scanner with back camera as default  
Use tesseract engine

## Install:
pip install streamlit_tesseract_scanner  

## Example:
````
import streamlit as st  
from streamlit_tesseract_scanner import tesseract_scanner

blacklist='@*|©_Ⓡ®¢§š'  
data = tesseract_scanner(showimg=False, lang='vie+eng', blacklist=blacklist, psm=3)  

if data is not None:  
    st.write(data)
````
