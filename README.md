# File_Organizer
The script is based on 2 directories : 
- path_to_trigger_folder
- path_to_sorting_folder

"path_to_sorting_folder" is where you move files that need sorting.


After the files have been moved to the "path_to_sorting_folder" directory the "Watcher" sends an event that files have been transfered.


Before we start the sorting, we look over our "path_to_sorting_folder" directory and create sub-folders based on the current date.

The structure is as follows :

![image](https://user-images.githubusercontent.com/22921655/151804481-4ad09681-c04b-405a-88b4-209a59825aac.png)

Files are then transfered to "dd-mm-yyyy Day/" folder after which they are further divided into sub-folders based on their .extension:

![image](https://user-images.githubusercontent.com/22921655/151804628-4c013cea-5396-4ae8-bd8d-22fae37ab72a.png)
