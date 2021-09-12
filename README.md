# TermTube

A simple tool used to download YouTube video/audio using terminal.

## Installation
All you need to do is download the source code and run main.py file.
When starting script for the first time, you need to run "/setpath $download_path$" command:

![setpath](https://user-images.githubusercontent.com/70367786/132988196-a7075018-d726-416b-a4dc-f92fd5d60fd5.png)

## Usage
You can separate paths for video and audio. For audio only path setting use "/setpath_a" and for video "/setpath_v".
You don't have to do this every time you start the script, using command described above, program saves path string to 
JSON file, in order to use this info in future.
Use "/video <link>" command to download video and "/audio <link> to download audio.
![work_representation](https://user-images.githubusercontent.com/70367786/132987913-cbfe49b6-611f-44c5-b7af-6e7246f6fa83.png)

## Error Handling
Also, this program has some basic error handling.
![error_handling](https://user-images.githubusercontent.com/70367786/132987973-906599c3-da34-45df-b3d4-f7550c232cb3.png) 

## Authors

- [@ShaneW0lsh](https://github.com/ShaneW0lsh)
