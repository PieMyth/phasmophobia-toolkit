# Phasmophobia Toolkit
Application that uses pyttsx3 and outputs the sayings to get interactions from the ghost.


## Building
Currently tested and working with python 3.6.8, but it shouldn't have a problem running on other versions.

### Windows
If desired to create a virtual environment, please do so now. See [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for help on installing virtualenv

```
virtualenv env
.\env\Scripts\activate
pip install -r .\requirements.txt
```

### Linux
The building steps is very similar to Windows with a few key differences. You will need to install a tts engine on your install if one is not already installed espeak or something similar, otherwise a voice will not play.
```
virtualenv env
source env/bin/activate
pip install -r .\requirements.txt
```
**NOTE: This does build and run on linux, however speech recoginition currently does not work with the game**

## Running
To run simply make sure that the virtualenv is activate and run python with ```main.py```. It is perfered to run the toolkit with an external speaker or laptop that can be picked up by the mic used for the game. In order to achieve this, one can go into the sound settings and select the toolkit to the other audio source.

**NOTE: Sometimes it will not immediately go to that dedicated output. To fix this go into sounds and switch the primary sound device to the other output and back again.**

### Using the tool
Currently the toolkit only spits out sayings that are put into the ```sayings.json``` file. There is another set of sayings that can make the ghost mad and cause hunts more often shown [here](https://steamcommunity.com/sharedfiles/filedetails/?id=2250732804) and would be very easy to add to ```sayings.json``` if desired.

# To-Do
- [ ] Make gui look nice
- [ ] Manually select audio source
- [ ] Ghost helper aid
    - [ ] Determine the type of ghost given the evidence
    - [ ] Give list of possible ghosts, indicating what piece of evidence is needed
        - [ ] Possible keyboard listening to eliminating tabbing out