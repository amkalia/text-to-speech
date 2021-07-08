# Text to speech

Cross platform multilingual Text-to-Speech tool that uses Google Translate API. 


- Currently only supports translation from .txt


Example Usage (test.txt file is provided):


*Translate text in file from German to French*

./text_to_speech.py --file test.txt 

> French
Detected language is German
Translating into French
--------------------
Translated file from German to French. File is test_french.txt 

*Translate text in file from German to French mp3*

./text_to_speech.py --audio test.txt

Which language?
> French
Detected language is German
Translating into French
--------------------
Translated file from German to French. File is test_french.txt 
Converted test_french.txt to French audio. File is test_french.mp3 


Languages supported for text-to-text translation (Not all are supported for text-to-speech):

AFRIKAANS | af 
ALBANIAN | sq 
AMHARIC | am 
ARABIC | ar 
ARMENIAN | hy 
AZERBAIJANI | az 
BASQUE | eu 
BELARUSIAN | be 
BENGALI | bn 
BOSNIAN | bs 
BULGARIAN | bg 
CATALAN | ca 
CEBUANO | ceb 
CHICHEWA | ny 
CHINESE (SIMPLIFIED) | zh-cn 
CHINESE (TRADITIONAL) | zh-tw 
CORSICAN | co 
CROATIAN | hr 
CZECH | cs 
DANISH | da 
DUTCH | nl 
ENGLISH | en 
ESPERANTO | eo 
ESTONIAN | et 
FILIPINO | tl 
FINNISH | fi 
FRENCH | fr 
FRISIAN | fy 
GALICIAN | gl 
GEORGIAN | ka 
GERMAN | de 
GREEK | el 
GUJARATI | gu 
HAITIAN CREOLE | ht 
HAUSA | ha 
HAWAIIAN | haw 
HEBREW | iw 
HEBREW | he 
HINDI | hi 
HMONG | hmn 
HUNGARIAN | hu 
ICELANDIC | is 
IGBO | ig 
INDONESIAN | id 
IRISH | ga 
ITALIAN | it 
JAPANESE | ja 
JAVANESE | jw 
KANNADA | kn 
KAZAKH | kk 
KHMER | km 
KOREAN | ko 
KURDISH (KURMANJI) | ku 
KYRGYZ | ky 
LAO | lo 
LATIN | la 
LATVIAN | lv 
LITHUANIAN | lt 
LUXEMBOURGISH | lb 
MACEDONIAN | mk 
MALAGASY | mg 
MALAY | ms 
MALAYALAM | ml 
MALTESE | mt 
MAORI | mi 
MARATHI | mr 
MONGOLIAN | mn 
MYANMAR (BURMESE) | my 
NEPALI | ne 
NORWEGIAN | no 
ODIA | or 
PASHTO | ps 
PERSIAN | fa 
POLISH | pl 
PORTUGUESE | pt 
PUNJABI | pa 
ROMANIAN | ro 
RUSSIAN | ru 
SAMOAN | sm 
SCOTS GAELIC | gd 
SERBIAN | sr 
SESOTHO | st 
SHONA | sn 
SINDHI | sd 
SINHALA | si 
SLOVAK | sk 
SLOVENIAN | sl 
SOMALI | so 
SPANISH | es 
SUNDANESE | su 
SWAHILI | sw 
SWEDISH | sv 
TAJIK | tg 
TAMIL | ta 
TELUGU | te 
THAI | th 
TURKISH | tr 
UKRAINIAN | uk 
URDU | ur 
UYGHUR | ug 
UZBEK | uz 
VIETNAMESE | vi 
WELSH | cy 
XHOSA | xh 
YIDDISH | yi 
YORUBA | yo 
ZULU | zu 
