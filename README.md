# MiniProject_2_Interaction_System

This is going to be the repository for all the work done for mini project 2.

### Members:
* Daniel Vasquez Murillo
* Miguel Angel Nivia

Date: 10:00 PM - 05/09/2024

### Teacher:
* Francisco Suarez Ramirez

## Objective:
Develop a Zork-type video game, text mode using OpenAL where the video game must build an auditory world consistent with the player's actions, with 50 lines of text, being a complete story that lasts at least 5 minutes as a minimum.

## Explanation of the problem:
In order to make a Zork-style video game, it is necessary to present a code that contains the game displayed in the cmd, in which the player can choose decisions / actions to take, which may or may not affect the story, being linear or free, in addition to this, it must be taken into account that the actions carried out must have associated sounds that accompany them, giving it 3d audio effects (50 lines of text), this indicating that it can be heard behind, to the right, etc. This means that there is a spatial location of the characters, a story that must be played in a minimum of 5 minutes.

## Proposed Solution:
For the video game we propose an adventure/fiction story with characters taken from role-playing games, where you play a character from a group of mercenaries willing to leave a mysterious place, which will reveal the reason why they are there and how they got to where they are, being a linear story but with 2 paths that lead to different endings, which the player can take in each game, where some decisions will be relevant to the story.

All this to be applied in a python code, where we will use the "pyopenal" library for the reproduction of sounds at specific moments of the story, also for the use of sounds with "threads" to show sounds at the same time on screen, where these sounds will be accessed with the relative paths of "os" so that anyone who downloads the file can run it without problem, and we will use tools like youtube and y2mate to obtain the audios and then with audacity change the audio format from stereo to mono and fix it if necessary to avoid problems with the 3d audio, taking into account that they are WAV files.

## Conclusion:
In conclusion we can say that we did a pretty good job, where we corrected the errors commented by the teacher in the last class, taking into account that there is a good use of sounds and how these are located in the character's environment, for this reason the audios are heard from the perspective of the character which the player embodies, where we use 3d audios to give a sense of depth and direction, however we want to clarify that we had a couple of problems for the correct reproduction of these and there may be slight problems in these, also so that the code is not heavy the text of the story was passed in csv with information of the audios in each part so that the main is light to read, in addition to separating the main with important functionalities of the program that uses this for better space performance, and we use some structures in the program to facilitate access such as dictionaries.

## References:
* [OpenAL](https://www.openal.org)
* [Python](https://www.python.org)
* [Youtube](https://www.youtube.com)
* [Y2mate](https://www.y2mate.com/es906)
* [Audacity](https://www.audacityteam.org)
