# xXAUDIOMASTERXx (xxamxx)
simple audio enshittifier. no further introduction needed

### usage
```
xxamxx input.mp3 output.mp3
```

takes an input audio file and fucks up the quality and exports. this supports a wide range of audio types (please refer to pydub's documentation for format support)

### requirements
 - Pydub
 - Audioop-lts (depending on the version of python you have)
 - Loguru
 - Pyinstaller (for compiling)


### compiling
```
git clone https://github.com/powerpellet1077/xXAUDIOMASTERXx.git
cd xXAUDIOMASTERXx
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --console --name "xxamxx"  "xxamxx.py"
cd output
xxamxx
```
if you got anything other than command not found, it should have compiled correctly.
questions or concerns can be sent to @powerpellet1077 on discord

