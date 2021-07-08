# Text to speech

 Text-to-Text and Text-to-Speech tool that uses the Google Translate API. 


- Currently only supports translation from .txt


Example Usage (test.txt file is provided):


*Translate text in file from German to French*

> ./text_to_speech.py --file test.txt <br>
> Which language? <br>
> French <br>
>Detected language is German
>Translating into French
> --------------------
> Translated file from German to French. File is test_french.txt 

*Translate text in file from German to French mp3*

> ./text_to_speech.py --audio test.txt <br>

> Which language? <br>
> French <br>
> Detected language is German <br>
> Translating into French <br>
> -------------------- <br>
> Translated file from German to French. File is test_french.txt <br>
> Converted test_french.txt to French audio. File is test_french.mp3 <br>


Languages supported for text-to-text translation (Not all are supported for text-to-speech):

AFRIKAANS | af <br>
ALBANIAN | sq <br>
AMHARIC | am <br>
ARABIC | ar <br>
ARMENIAN | hy <br>
AZERBAIJANI | az <br>
BASQUE | eu <br>
BELARUSIAN | be <br>
BENGALI | bn <br>
BOSNIAN | bs <br>
BULGARIAN | bg <br>
CATALAN | ca <br>
CEBUANO | ceb <br>
CHICHEWA | ny <br>
CHINESE (SIMPLIFIED) | zh-cn <br>
CHINESE (TRADITIONAL) | zh-tw <br>
CORSICAN | co <br>
CROATIAN | hr <br>
CZECH | cs <br>
DANISH | da <br>
DUTCH | nl <br>
ENGLISH | en <br>
ESPERANTO | eo <br>
ESTONIAN | et <br>
FILIPINO | tl <br>
FINNISH | fi <br>
FRENCH | fr <br>
FRISIAN | fy <br>
GALICIAN | gl <br>
GEORGIAN | ka <br>
GERMAN | de <br>
GREEK | el <br>
GUJARATI | gu <br>
HAITIAN CREOLE | ht <br>
HAUSA | ha <br>
HAWAIIAN | haw <br>
HEBREW | iw <br>
HEBREW | he <br>
HINDI | hi <br>
HMONG | hmn <br>
HUNGARIAN | hu <br>
ICELANDIC | is <br>
IGBO | ig <br>
INDONESIAN | id <br> 
IRISH | ga <br>
ITALIAN | it <br>
JAPANESE | ja <br>
JAVANESE | jw <br>
KANNADA | kn <br>
KAZAKH | kk <br>
KHMER | km <br>
KOREAN | ko <br>
KURDISH (KURMANJI) | ku <br>
KYRGYZ | ky <br>
LAO | lo <br>
LATIN | la <br>
LATVIAN | lv <br>
LITHUANIAN | lt <br>
LUXEMBOURGISH | lb <br>
MACEDONIAN | mk <br>
MALAGASY | mg <br>
MALAY | ms <br>
MALAYALAM | ml <br>
MALTESE | mt <br>
MAORI | mi <br>
MARATHI | mr <br>
MONGOLIAN | mn <br>
MYANMAR (BURMESE) | my <br> 
NEPALI | ne <br>
NORWEGIAN | no <br>
ODIA | or <br>
PASHTO | ps <br>
PERSIAN | fa <br>
POLISH | pl <br>
PORTUGUESE | pt <br>
PUNJABI | pa <br>
ROMANIAN | ro <br>
RUSSIAN | ru <br>
SAMOAN | sm <br>
SCOTS GAELIC | gd <br> 
SERBIAN | sr <br>
SESOTHO | st <br>
SHONA | sn <br>
SINDHI | sd <br>
SINHALA | si <br>
SLOVAK | sk <br>
SLOVENIAN | sl <br>
SOMALI | so <br>
SPANISH | es <br>
SUNDANESE | su <br>
SWAHILI | sw <br>
SWEDISH | sv <br>
TAJIK | tg <br>
TAMIL | ta <br>
TELUGU | te <br>
THAI | th <br>
TURKISH | tr <br>
UKRAINIAN | uk <br>
URDU | ur <br>
UYGHUR | ug <br>
UZBEK | uz <br>
VIETNAMESE | vi <br> 
WELSH | cy <br>
XHOSA | xh <br>
YIDDISH | yi <br>
YORUBA | yo <br>
ZULU | zu <br>
