from pytube import YouTube
import os



while True:
    succes = False

    cont = str(input("Do you want to exit? y/n? \n"))

    if(cont == "y"):
        break

    try:
        # kullanıcının indirmek istediği video linki
        yuLink = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))
    except:
        continue

    # sadece ses kaydının çıkarılması için
    video = yuLink.streams.filter(only_audio=True).first()

    try:
        # dosyayının indirileceği konum
        print("Enter the destination for the file location (leave blank if you want music to be downloaded to current directory)")
        destination = str(input(">> ")) or '.'
    except:
        continue

    # videoyu indir
    downloadedFile = video.download(output_path=destination)

    try:
        # dosyayı kaydetme
        base, ext = os.path.splitext(downloadedFile)
        newFile = base + '.mp3'
        os.rename(downloadedFile, newFile)
        succes = True
    except:
        print("An error occured! Please try again")

    if(succes):
        print(yuLink.title + " downloaded succesfully.")