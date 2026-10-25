gb = int(input())
speed = int(input())
install_time = int(input()) * 60

download_time = (gb * 1024  * 8) // speed

def timeToFormat(time):
    min = str(time // 60)
    sec = str(time % 60)
    return min + ':' + sec

print("Время скачивания: ", timeToFormat(download_time))
print("Общее время: ", timeToFormat(install_time + download_time))