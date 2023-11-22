# SnapGameGUI

# Installation
To be able to play Snap Game you need to install external libraries - Tkinter and Pillow. 

**Tkinter is the standard GUI (Graphical User Interface) toolkit that comes with Python. It provides tools for creating desktop applications with graphical interfaces.**

**Pillow is a powerful image-processing library for Python.**

Both libraries require Python; if you don't already have it, you can download from [python.org](https://www.python.org/).  It's recommended to run the latest Python version, 
because it's usually faster and has better features than the older ones.

Step-by-step installation:
- [1] Install the following project -> [SnapGameGUI.zip](https://github.com/AndrewLukashchuk202/SnapGame_AndrewLukashchuk.py/archive/refs/heads/main.zip)
- [2] Important note! Make sure that the folder with the playing card images is installed in the same location on the disk where the game itself is located
- [3] Install external libraries. The best way to install them is to use the pip tool (which is what python uses to install packages). If you have the latest version of Python, which is Python 3, provide the next command in the terminal: ```pip3 install Tkinter``` and ```pip3 install Pillow```
- [4] The last step is: using Windows/Linux commands in your terminal go to the location where you store the installed project and run the following command using Python: ```python3 Play.py``` to play the simulation version of s Snap Game or ```python3 SnapGameGUI.py``` to play an interactive version of a Snap Game

# An Interactive Game of Snap - Description
The essence of the game is that at the beginning of the round, the game's participants evenly deal with each other cards from a deck consisting of 52 cards. 
In each round, the participants of the game take turns putting cards on the table, on top of each other, face down so that you can see the card, if the card number of the 
participant who just put the card matches the card number of the previous participant, the game says - Snap and takes all the cards. The game continues until one player takes 
all the cards from the other players

# How to Play:
Snap game includes 52 playing cards, 12 of each suit, not including jokers. The game can be played in two ways, through the console and through the interactive design. 
To play the first way, run this file; to play the second way, run that file. In the first option, the minimum number of players is 2, and the maximum is 52, in the second option,
the minimum and maximum number of players is 2. In the first option, the game is carried out using the simulation method by printing output to the console, in the second 
option, by pressing the button - "Next round"

# License:
```Tkinter License Statement

This project includes Tkinter, a GUI library for Python, which is part of the Python Software Foundation's distribution.

Tkinter is subject to the Python Software Foundation License.

License details for Tkinter:

The Python Software Foundation License
=======================================

1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"), and the Individual or Organization ("Licensee") accessing and otherwise using this software ("Python") in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, PSF hereby grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce, analyze, test, perform and/or display publicly, prepare derivative works, distribute, and otherwise use Python alone or in any derivative version, provided, however, that PSF's License Agreement and PSF's notice of copyright, i.e., "Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020 Python Software Foundation; All Rights Reserved" are retained in Python alone or in any derivative version prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on or incorporates Python or any part thereof, and wants to make the derivative work available to others as provided herein, then Licensee hereby agrees to include in any such work a brief summary of the changes made to Python.

4. PSF is making Python available to Licensee on an "AS IS" basis. PSF MAKES NO REPRESENTATION OR WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON, OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any relationship of agency, partnership, or joint venture between PSF and Licensee. This License Agreement does not grant permission to use PSF trademarks or trade name in a trademark sense to endorse or promote products or services of Licensee, or any third party.

8. By copying, installing or otherwise using Python, Licensee agrees to be bound by the terms and conditions of this License Agreement.

More details: https://docs.python.org/3/license.html
```
```Pillow License Statement

This project includes Pillow, an imaging library for Python.

Pillow is subject to the following license:

PIL Software License
====================

The Python Imaging Library (PIL) is

   Copyright (c) 1995-2011 by Secret Labs AB
   Copyright (c) 1997-2011 by Fredrik Lundh

By obtaining, using, and/or copying this software and/or its associated documentation, you agree that you have read, understood, and will comply with the following terms and conditions:

Permission to use, copy, modify, and distribute this software and its associated documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Secret Labs AB or the author not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```
# Credits & Aknowledgment:
All materials used are freeware

Made with Tkinter and Pillow modules: [https://docs.python.org/3/library/tkinter.html], [https://pillow.readthedocs.io/en/stable/]

Images of 52 playing cards you can download from - [tekeye.uk](https://tekeye.uk/playing_cards/svg-playing-cards)

Author: Daniel S. Fowler [https://boardgames.stackexchange.com/users/34841/daniel-s-fowler]








