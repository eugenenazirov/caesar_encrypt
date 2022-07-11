from caesar_encrypt import caesar_encrypt_main
from pathlib import Path


path_en = Path("caesar_encrypt", "files", "EN_file.txt")
path_ru = Path("caesar_encrypt", "files", "RU_file.txt")


def main():
    caesar_encrypt_main.caesar_encrypt(path_en, 3)
    caesar_encrypt_main.caesar_encrypt(path_ru, 3)


if __name__ == '__main__':
    main()
