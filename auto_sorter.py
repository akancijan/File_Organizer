import os
import time
import datetime
import shutil

from logging import Handler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os import listdir


# Path to your downloads folder
path_to_download_folder = "C:/Users/aljos/Documents/Testing Folder"
# Path to folder where you want your files sorted
path_to_sorting_folder = "C:/Users/aljos/Documents/Sorted Downloads"

# Current time
now = datetime.datetime.now()
# Current date
curr_date = datetime.date(now.year, now.month, now.day)
# Day value for folder name
current_day_folder = (curr_date.strftime("%A"))
# Month value for folder name
current_month_folder = curr_date.strftime("%B")
# Year value for folder name
current_year_folder = now.year


print(curr_date)
print(current_day_folder)
print(current_month_folder)
print(current_year_folder)

print(path_to_download_folder)
print(listdir(path_to_download_folder))

# Tracks any actions that happen in the folder which will trigger file sorting
class Watcher:
    DIRECTORY_TO_WATCH = path_to_download_folder

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    def on_any_event(self, event):
        # Set a delay when files are being copied over to avoid permission collision
        if event.event_type == 'created':
            time.sleep(3)
        # Check whether the specified path to YEAR folder exists or not
        year_folder_path = path_to_sorting_folder + "/" + str(current_year_folder)
        year_folder_present = os.path.exists(year_folder_path)

        if not year_folder_present:
            # Create a new directory because it does not exist
            os.makedirs(year_folder_path)
            print("The new YEAR directory is created!")

        # Check whether the specified path to MONTH folder exists or not
        month_folder_path = year_folder_path + "/" + str(current_month_folder)
        month_folder_exists = os.path.exists(month_folder_path)

        if not month_folder_exists:
            # Create a new directory because it does not exist
            os.makedirs(month_folder_path)
            print("The new MONTH directory is created!")

        # Check whether the specified path to DAY folder exists or not
        day_folder_path = month_folder_path + "/" + now.strftime("%d") + "-" + now.strftime("%m") + "-" + now.strftime("%Y") + " " + str(current_day_folder)
        day_folder_exists = os.path.exists(day_folder_path)

        if not day_folder_exists:
            # Create a new directory because it does not exist
            os.makedirs(day_folder_path)
            print("The new DAY directory is created!")

        # Iterate over all files and transfer them to current days directory
        for filename in os.listdir(path_to_download_folder):
            src_dir = path_to_download_folder + "/" + filename

            while not os.path.exists(src_dir):
                print('cekam')
                time.sleep(1)

            new_destination = day_folder_path + "/" + filename
            shutil.move(src_dir, new_destination)

        # After the files have been transferred , sort them by their extension
        # NOTE!! folders will be transferred as is without their contents being sorted
        for file_ in os.listdir(day_folder_path):
            name, ext = os.path.splitext(file_)
            # This is going to store the extension type
            ext = ext[1:]
            # This forces the next iteration,
            # if it is the directory
            if ext == '':
                continue
            # This will move the file to the directory
            # where the name 'ext' already exists
            if os.path.exists(day_folder_path + '/' + ext):
                shutil.move(day_folder_path + '/' + file_, day_folder_path + '/' + ext + '/' + file_)
            # This will create a new directory,
            # if the directory does not already exist
            else:
                os.makedirs(day_folder_path + '/' + ext)
                shutil.move(day_folder_path + '/' + file_, day_folder_path + '/' + ext + '/' + file_)


if __name__ == '__main__':
    w = Watcher()
    w.run()
