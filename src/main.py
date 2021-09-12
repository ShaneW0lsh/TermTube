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

"""			 
		TODO:	
8. COMPLETE JSON INTEGRATION, SO PROGRAM ADDS INFO TO THE JSON (OVERALL DOWNLOAD SIZE, NUMBER OF DOWNLOADS etc.)
9. FIX ONE-WORD COMMANDS WITH WHITESPACES PROBLEM 
	
		DONE:
1. ADD PROGRESS BAR																...DONE
2. INTEGRATE JSON FOR PATH STRING SAVING 										...DONE
3. FINISH AUDIO() FUNCTION														...DONE
4. MAKE THE PROGRAM CATCH THE EXCEPTIONS BETTER 								...IN PROCESS
5. EXPERIMENT WITH COLOURS														...IN PROCESS
6. BORDER VIDEO DOWNLOAD PATH AND AUDIO DOWNLOAD PATH 							...DONE
7. JUST USING TEXTED COMMANDS WITHOUT ANOTHER FILE "GLOBAL_VARIBALES"
MIGHT BE A BETTER OPTION, RECODE THAT											....DONE			.

"""