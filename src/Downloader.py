"""
Youtube Downloader class. Functionality for 
video/audio downloading is located here.
"""

from pytube import YouTube
from pytube.cli import on_progress
import json
import sys
from utility import LOG


class Downloader:
	progress_bar_width = 20

	def __init__(self):
		self.current_dir = False
		self.default_naming = False
		self.current_file_size = 0
		with open("config.json") as f:
			self.data = json.load(f)


	def set_path(self, path, mode):
		if path == "$CURRENT_DIR":
			self.current_dir = True
		else:
			if mode == 1:
				self.data["dp_audio"] = path
			elif mode == 2:
				self.data["dp_video"] = path
			elif mode == 3:
				self.data["dp_audio"] = path
				self.data["dp_video"] = path
			else:
				LOG("\"mode\" argument value is not valid", "FAIL", True)

			with open("config.json", "w") as f:
				json.dump(self.data, f, indent=2)
	

	def download_video(self, url):
		video = YouTube(url, on_progress_callback = on_progress)
		elements = video.streams.filter(progressive = True)#mime_type = "video/mp4", progressive = True)

		index = 0
		print()
		for element in elements:
			index += 1
			LOG("Option ", "HEADER", False)
			LOG(index, "OKCYAN", False)
			LOG(": ", "HEADER", False)
			print(f"{element.resolution} {element.fps}fps")
		print()

		valid = False
		chosen = None
		option_num = None
		while not valid:
			try:
				LOG(f"Option number: ", "OKCYAN", False)
				option_num = input()
				if option_num == "/cancel":
					return
				else:
					option_num = int(option_num)
					if (option_num < 1 or option_num > index):
						LOG("[ERROR]: Invalid option chosen. Input is out of range", "FAIL", True)
					else:
						valid = True

			except ValueError:
				LOG("[ERROR]: Argument is not a number", "FAIL", True)
				pass

		chosen = elements[option_num-1]
		self.current_file_size = chosen.filesize

		LOG("File name: ", "OKCYAN", False)
		title = input();
		if title == "$DEFAULT":
			default_naming = True
		elif title == "/cancel":
			return

		if self.current_dir == True:
			if self.default_naming == True:
				chosen.download()
			else:
				chosen.download(filename = f"{title}.mp4")
		else:
			if self.default_naming == True:
				chosen.download(output_path = self.data["dp_video"])
			else:
				chosen.download(output_path = self.data["dp_video"], filename = f"{title}.mp4")

		LOG("Done!", "OKGREEN", True)
		self.default_naming = False
		self.current_file_size = 0


	def download_audio(self, url):
		audio = YouTube(url, on_progress_callback = on_progress)

		index = 0
		elements = audio.streams.filter(only_audio = True)
		print()
		for element in elements:
			index += 1
			LOG("Option ", "HEADER", False)
			LOG(index, "OKCYAN", False)
			LOG(": ", "HEADER", False)
			print(f"{element.mime_type} {element.abr}")
		print()

		valid = False
		chosen = None
		option_num = None
		while not valid:
			try:
				LOG(f"Option number: ", "OKCYAN", False)
				option_num = input()
				if option_num == "/cancel":
					return
				else:
					option_num = int(option_num)
					if (option_num < 1 or option_num > index):
						LOG("[ERROR]: Invalid option chosen. Input is out of range", "FAIL", True)
					else:
						valid = True

			except ValueError:
				LOG("[ERROR]: Argument is not a number", "FAIL", True)
				pass

		chosen = elements[option_num-1]
		self.current_file_size = chosen.filesize

		LOG("File name: ", "OKCYAN", False)
		title = input();
		if title == "$DEFAULT":
			default_naming = True
		elif title == "/cancel":
			return

		if self.current_dir == True:
			if self.default_naming == True:
				chosen.download()
			else:
				chosen.download(filename = f"{title}.mp3")
		else:
			if self.default_naming == True:
				chosen.download(output_path = self.data["dp_video"])
			else:
				chosen.download(output_path = self.data["dp_video"], filename = f"{title}.mp3")

		LOG("Done!", "OKGREEN", True)
		self.default_naming = False
		self.current_file_size = 0
