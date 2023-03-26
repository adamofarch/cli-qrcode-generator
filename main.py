import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def generator():

    qr = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_L)
    data = input("\nInput something to generate: ")
    qr.add_data(data)
    img = qr.make_image()
    nameQR = input("Name your File: ")
    inputPath = input("Enter the path(Default = current directory): ")

    try:
        if inputPath.startswith(''):
            img.save(f"{inputPath}{nameQR}.png")

        # for linux and mac users
        if '/' in inputPath:
            if inputPath.endswith('/'):
                img.save(f"{inputPath}{nameQR}.png")
            else:
                img.save(f"{inputPath}/{nameQR}.png")

        # for windows users
        if '\\' in inputPath:
            if inputPath.endswith('\\'):
                img.save(f"{inputPath}{nameQR}.png")
            else:
                img.save(f"{inputPath}\\{nameQR}.png")

        print("QR generated successfully")

    except FileNotFoundError as f:
        print("Directory doesn't exist, Enter a correct path and try again !")
        generator()

    


if __name__ == "__main__":
    print("\n*************************CLI-QR-CODE-GENERATOR*************************\n")
    print("---------------------------- By AdamOfArch ----------------------------")
    generator()

    