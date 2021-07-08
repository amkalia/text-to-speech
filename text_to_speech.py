import argparse
import ast # languages.json file loads as 'str' type. Use literal_eval to convert to dict
import json 
import os 
from pathlib import Path 

import googletrans 
from googletrans import Translator
from gtts import gTTS


translator = Translator()


def get_args():
	parser = argparse.ArgumentParser(description='Text-to-text and text-to-speech translator')
	parser.add_argument('-l', '--list', action='store_true', help='Request a list of supported languages', required=False)
	parser.add_argument('-f', '--file', help='Translates text in file to chosen language. Default is English')
	parser.add_argument('-a', '--audio', help='Translates text in file to to mp3 audio in chosen language with text file. Default is English')
	parser.add_argument('-t', '--to', help='Language to translate to')

	return parser.parse_args()


def print_languages(json_language_file='languages.json'):
	with open(json_language_file) as json_file:
		data = ast.literal_eval(json.load(json_file))
		for key, value in data.items():
			print(f"\033[1m{value.upper()} | {key} \033[0m")
	print(f"\033[1mPlease note the above languages are available for text translation only. Not all are supported with text to speech translation.\033[0m")

def return_languages(json_language_file='languages.json'):
	with open(json_language_file) as json_file:
		data = ast.literal_eval(json.load(json_file))
	return data 

def check_valid_extension(filename="test.txt"):
	if Path(filename).exists():
		file_extensions = ['doc', 'docx', 'odt', 'pages', 'pdf', 'rtf', 'txt']
		file = open(filename, 'r').read()
		if filename.split(".")[-1] not in file_extensions:
			print(f"Error: {filename} is not a valid file.") 
			print("The following file extensions are valid:")
			for ext in file_extensions:
				print(f".{ext}")
		else:
			pass
	else:
		print("Sorry file doesn't seem to exist")

def translate_to_text(filename='test.txt', new_language='english'):
	ext = 'txt'


	file = open(filename, "r").read()
	languages = return_languages('languages.json')
	detected_language = str(translator.detect(file).lang)
	print(f"Detected language is {languages[detected_language].capitalize()}")
	new_language_key = list(languages.keys())[list(languages.values()).index(new_language)]
	
	print(f"Translating into {new_language.capitalize()}")
	print("-"*20)
	

	new_file = f"{filename.split('.')[0]}_{new_language}.{ext}"
	new_text = translator.translate(file, dest=new_language_key).text
	with open(f"{new_file}", 'w') as f:
		f.write(new_text)
	print(f"Translated file from {languages[detected_language].capitalize()} to {new_language.capitalize()}. File is \033[1m{new_file}\033[0m ")

	return new_file

def translate_to_audio(filename='test.txt', new_language='english'):
	translated_file = translate_to_text(filename, new_language)
	detected_language = str(translator.detect(translated_file).lang)

	languages = return_languages('languages.json')
	new_language_key = list(languages.keys())[list(languages.values()).index(new_language)]

	converted_audio = f"{filename.split('.')[0]}_{new_language}.mp3"

	convert_file = open(translated_file, 'r').read()
	tts = gTTS(convert_file, lang=new_language_key)
	tts.save(converted_audio)
	
	print(f"Converted {translated_file} to {new_language.capitalize()} audio. File is \033[1m{converted_audio}\033[0m ")


if __name__ == '__main__':
	arguments = get_args()
	if arguments.list:
		print_languages()
	if arguments.file:
		if arguments.to:
			translate_to_text(filename=arguments.file, new_language=arguments.to.lower())
		else:
			translate_to_text(filename=arguments.file)
	if arguments.audio:
		if arguments.to:
			translate_to_audio(filename=arguments.audio, new_language=arguments.to.lower())
		else:
			translate_to_audio(filename=arguments.audio)
	else:
		print("Please select a file to translate.")
		print("Example: ./text_to_speech.py --file test.txt")
		print("")
