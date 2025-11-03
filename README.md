# xXAUDIOMASTERXx (xxamxx)
simple audio enshittifier. no further introduction needed

### usage
```
xxamxx input.mp3 output.mp3
```

takes an input audio file and decreases the quality to make it sound like dogshit. this supports a wide range of audio types (please refer to pydub's documentation for format support).
if you feel like these settings aren't good, then you can use these flags.
```
xxamxx input.mp3 output.mp3 -f 0.8 -g 2
```
-f and -g (--fr and --grain) are multipliers of the default framerate and grain, using ``-g 2`` doubles the amount of grain and ``-f 0.5`` doubles the quality where ``-f 2`` halves the quality (I made it confusing). Just think that the higher the number, the worse the quality.


you can also remove the extra artifacts I put in there to make it sound worse if that helps.
````
xxamxx input.mp3 output.mp3 -d
````

### requirements (for compiling)
 - Pydub
 - Audioop-lts (depending on the version of python you have)
 - Loguru
 - Pyinstaller
 - Git
 - Python 3.10 or higher
 - Ffmpeg (at path)


### compiling
```
git clone https://github.com/powerpellet1077/xXAUDIOMASTERXx.git
cd xXAUDIOMASTERXx
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --console --name "xxamxx"  "xxamxx.py"
cd dist
xxamxx
```
if you got this:
````
usage: xxamxx [-h] [-f FR] [-g GRAIN] [-d] input output
xxamxx: error: the following arguments are required: input, output
````

it should have compiled correctly.
questions or concerns can be sent to @powerpellet1077 on discord

