import requests

def apply_filter(files, data):
        response = requests.post("http://localhost:5000/upload", files=files, data=data)

        if response.status_code == 200:
            return response
        else:
            print("Erro ao aplicar filtro:", response.text)

def get_images():
    response = requests.get("http://localhost:5000/list_images")
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao carregar imagens:", response.text)
        return []

def view_image(image_id):
    response = requests.get(f"http://localhost:5000/image/{image_id}")
    return response if response.status_code == 200 else None