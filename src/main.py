"""Execute this file, in order for program to work"""

from utility import LOG
from Downloader import Downloader

#constants
EXIT_COMMAND = "/exit"
SET_VIDEO_PATH_COMMAND = "/setpath_v"
SET_AUDIO_PATH_COMMAND = "/setpath_a"
SET_ALL_PATH_COMMAND = "/setpath"
DOWNLOAD_VIDEO_COMMAND = "/video"
DOWNLOAD_AUDIO_COMMAND = "/audio"

d = Downloader()

def main():
	while True:
		c_polling()


def c_polling():
		LOG("$  ", "MAGENDA", False)
		user_input = input()
		command_list = user_input.split()

		if user_input == EXIT_COMMAND:
			exit()

		elif command_list[0] == SET_VIDEO_PATH_COMMAND:
			if len(command_list) <= 1:
				__ = "[ERROR]: Command \"/setpath\" has arguments"
				LOG(__, "FAIL", True)
			elif len(command_list) > 2:
				__ = "[ERROR]: Too many arguments"
				LOG(__, "FAIL", True)
			else:
				d.set_path(command_list[1], 2)	

		elif command_list[0] == SET_AUDIO_PATH_COMMAND:
			if len(command_list) <= 1:
				__ = "[ERROR]: Command \"/setpath\" has arguments"
				LOG(__, "FAIL", True)
			elif len(command_list) > 2:
				__ = "[ERROR]: Too many arguments"
				LOG(__, "FAIL", True)
			else:
				d.set_path(command_list[1], 1)	

		elif command_list[0] == SET_ALL_PATH_COMMAND:
			if len(command_list) <= 1:
				__ = "[ERROR]: Command \"/setpath\" has arguments"
				LOG(__, "FAIL", True)
			elif len(command_list) > 2:
				__ = "[ERROR]: Too many arguments"
				LOG(__, "FAIL", True)
			else:
				d.set_path(command_list[1], 3)	

		elif command_list[0] == DOWNLOAD_VIDEO_COMMAND:
			if len(command_list) <= 1:
				__ = "[ERROR]: Command \"/video\" has arguments"
				LOG(__, "FAIL", True)
			elif len(command_list) > 2:
				__ = "[ERROR]: Too many arguments"
				LOG(__, "FAIL", True)
			else:
				d.download_video(command_list[1])

		elif command_list[0] == DOWNLOAD_AUDIO_COMMAND:
			if len(command_list) <= 1:
				__ = "[ERROR]: Command \"/audio\" has arguments"
				LOG(__, "FAIL", True)
			elif len(command_list) > 2:
				__ = "[ERROR]: Too many arguments"
				LOG(__, "FAIL", True)
			else:
				d.download_audio(command_list[1])

		else:
			__ = f"[ERROR]: No such command as \"{command_list[0]}\" exists"
			LOG("[ERROR]: No such command exists", "FAIL", True)



if __name__ == "__main__":
	main()
