import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gdownmain'))
import gdown

folderPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Trendyol Resimler')
url = "https://drive.google.com/drive/folders/18KOfnD5IHf15oTRl15f7cDgZmcoHIoc7?usp=sharing"
if url.split('/')[-1] == '?usp=sharing':
    url= url.replace('?usp=sharing','')

dest = gdown.download_folder(url,remaining_ok=True,output=folderPath)
print("Linkteki klasör indirildi")
