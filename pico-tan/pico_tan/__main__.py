#!/usr/bin/env python3

"""
the entry point, this parses command line input and provides some basic commands
"""
import sys, os
from random import shuffle


from scraping import *

#import PIL
#import requests
#import urllib
#import beautifulscraper

#keyed by command name, value is arguments, used by process_argv()
valid_commands={
    "ud" : 1,
    "help" : 0,
    "8ball" : 0,
}

def eight_ball():
    
    addages = ["It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely",
    "You may rely on it", "As I see it, yes", "Most Likely", "Outlook good", "Yes", "Signs point to yes",
    "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
    "Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    shuffle(addages)
    print(addages[0])

def hello():
    print("I LIVE")

def help():
    """
    called with <pico help>
    prints list of all available commands and a stereotype
    """
    print("8ball: \t | <pico 8ball> \t | prints an 8ball addage\n")
    print("help: \t | <pico help> \t | prints commands(you probably already knew that)\n")
    print("ud: \t | <pico ud [term]> \t | searches urban dictionary for the definition of your term(replace spaces with +)")


def process_argv():
    """
    function processes argv
    returns: tuple (command, [arguments])
    """
    if(sys.argv[1] is None):
        return ("help","")
    if(sys.argv[1] in valid_commands):
        #check to make sure the right number of arguments were entered
        if(len(sys.argv) == 2 + valid_commands[sys.argv[1]]):
            return (sys.argv[1], sys.argv[2:])
        else:
            print("invalid number of arguments for that command, expected: " + valid_commands[sys.argv[1]])
    else:
        print("unrecognized command")



def main():
    """
    def main()
    
    calls the correct function after receiving processed data from process_argv()
    """
    active_command = process_argv()

    if(active_command[0] == "help"):
        help()
    elif(active_command[0] == "8ball"):
        eight_ball()
    elif(active_command[0] == "ud"):
        urban_dict(active_command[1][0])
    

if __name__ == "__main__":
    main()