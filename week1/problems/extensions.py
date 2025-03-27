def main():
    f_name = input("Enter file name: ")
    f_name = f_name.strip().lower()
    f_ext = f_name.split(".")[1]
    f_type = file_type(f_ext)
    print("File type:", f_type)

def file_type(ext):
    match ext:
        case "gif" | "jpg" | "jpeg" | "png":
            return "image/jpeg" if ext == "jpg" else f"image/{ext}"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "Not an expected file type."

main()