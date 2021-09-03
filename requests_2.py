import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        files_list = []
        BASE_URL = "https://cloud-api.yandex.net/"
        headers = {
            "accept": "application/json",
            "Authorization": f"OAuth {token}"
        }
        while True:
            file = input("Введите имя файла с расширением: ")
            if file == "ex":
                break
            files_list.append(file)
        for file in files_list:
            response = requests.get(BASE_URL + "v1/disk/resources/upload", params={"path": file}, headers=headers)
            upload_url = response.json()["href"]
            r = requests.put(upload_url, headers=headers, files={"file": open(file_path + "\\" + file, "rb")})
            print(f"Файл {file} успешно загружен")

if __name__ == '__main__':
    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите токен: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

