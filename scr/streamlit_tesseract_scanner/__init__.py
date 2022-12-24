import base64
from io import BytesIO
from pathlib import Path
from typing import Optional
import cv2
import numpy as np
import pytesseract
from pytesseract import Output

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called camera_input_live,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "tesseract_scanner", path=str(frontend_dir)
)


def tesseract_scanner(showimg: bool =False, 
                      lang: str = 'eng',
                      blacklist: str = None,
                      whitelist: str = None,
                      psm: str = '3',
                      hrate: float=0.2, 
                      key: Optional[str] = None
                ) -> Optional[BytesIO]:
    """
    Add a descriptive docstring
    """
    b64_data: Optional[str] = _component_func(hrate=hrate, key=key)

    if b64_data is None:
        return None

    raw_data = b64_data.split(",")[1]  # Strip the data: type prefix

    component_value = BytesIO(base64.b64decode(raw_data))

    # return component_value
    # image = cv2.imdecode(np.frombuffer(component_value, np.uint8), cv2.IMREAD_COLOR)
    
    image = base64.b64decode(raw_data)
    image = np.fromstring(image, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    if showimg:
        st.image(image)

    # blacklist = '@*|©_Ⓡ®¢§š'
    if blacklist:
        custom_config = f'''-l {lang} -c tessedit_char_blacklist={blacklist} --psm {psm}'''
    else:
        custom_config = f'''-l {lang} -c tessedit_char_whitelist={whitelist} --psm {psm}'''
    
    text = pytesseract.image_to_string(image, config=custom_config).replace('  ', ' ')
    text = text.split('\n')
    while("" in text): text.remove("")
    while(" " in text): text.remove(" ")
    text.remove("\x0c")
    
    return text


def main():
    st.write("## Example")

    blacklist='@*|©_Ⓡ®¢§š'
    data = tesseract_scanner(showimg=False, lang='vie+eng', 
                             blacklist=blacklist, psm=3)

    if data is not None:
        st.write(data)

if __name__ == "__main__":
    main()