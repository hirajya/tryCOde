import qrcode
import os
import re

def generate_qrcode(links):

    folder_path = r"C:\Users\angel\Desktop\tryCOde\QRCodeGen\QRpics"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for idx, link in enumerate(links):
        qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border=4
        ) 

        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        domain_name = extract_keyword(link)
        img.save(os.path.join(folder_path, f"qrcode_{domain_name}.png"))

def extract_keyword(url):
    pattern = r'(?:https?:\/\/)?([^\/]+)\/?$'
    
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    else:
        return None  

links = [
    "https://python.ph/", 
    "https://reactjs.org.ph/", 
    "https://devcon.ph/"
]


generate_qrcode(links)