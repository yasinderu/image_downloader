import os
import requests

def get_extention(image_url: str) -> str | None:
    extentions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']

    for ext in extentions:
        if ext in image_url:
            return ext
        
def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extention(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extention is not recognized')
    
    if os.path.isfile(image_name):
        raise Exception('Image already exist...')
    
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully')
    except Exception as e:
        print(f'Error :{e}')

if __name__ == '__main__':
    img_url: str = input('Enter a Image URL: ')
    img_name: str = input('What would you want to name the image: ')
    print('Downloading...')
    download_image(img_url, name=img_name, folder='images')