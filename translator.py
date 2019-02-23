#!/usr/bin/python3
"""
author: @brendanmoore42
date: Feb 23, 2019
Twitch Translator: Display live closed captions
"""
import re
import sys
import random
import speech_recognition as sr

# #instantiate Recognizer class
# r = sr.Recognizer()
# version = '1.0.6'

def speak():
    """
    Opens microphone, listens for speech then prints translated text
    """

    def send_tweet(tweet):
        """Proof of concept: Just add with tweepy with creds"""
        print('Authenticating bot...Beep Boop...')
        print(f'Sending Tweet: {tweet}')


    def make_first_capital(arg):
        """Changes first character to...a capital"""

        new_char = arg[0].title()
        new_sent = new_char + arg[1:]
        return new_sent


    def custom_functions(arg, words):
        """Executes function on speech"""

        if arg == 'party_on':
            print(random.choice(['Cowabunga dude!', "WEEEN", "Tubular", "PPMD's Coming back"]))
        if arg == 'send_tweet':
            tweet = ' '.join(words.split(' ')[1:])
            start_listening(tweet=tweet)


    def start_listening(tweet=None, retry_tweet=False):

        def check_tweet(tweet):
            """Checks tweet and uses Machine Learning to predict gas prices"""

            print(f'Tweet: {tweet}')
            print('Send tweet?')

            choice = grab_audio()

            #execute choice
            if choice == 'Yes':
                send_tweet(tweet)
            elif choice == 'No':
                print('Resuming...')
                pass
            elif choice == 'Retry':
                start_listening(retry_tweet=True)
            else:
                print('Tweet not sent...try again?')
                check_tweet(retry=True)


        def grab_audio():
            """Return translated speech"""
            try:
                print("Listening... ")
                #microphone is listening
                audio = r.listen(source, timeout=20,)
                print('Translating...')
                try:
                    words = r.recognize_google(audio)
                    words = make_first_capital(words)
                    return words
                #No speech detected, or translation error, will restart
                except (sr.UnknownValueError, sr.RequestError)as e:
                    print(f"No speech detected, restarting...")

            except:
                pass

        with sr.Microphone() as source:
            while True:
                # instantiate Recognizer class
                r = sr.Recognizer()
                version = '1.0.6'

                #testing this out
                r.energy_threshold = 400
                r.dynamic_energy_threshold = True

                if retry_tweet:
                    # get new tweet
                    tweet = grab_audio()
                    check_tweet(tweet)

                if tweet:
                    # check tweet
                    check_tweet(tweet)

                #normal fn
                words = grab_audio()

                #check for special cases
                funcs = ['party_on', 'send_tweet', 'play_song', 'send_text']

                #for complex functions, api calls, etc
                special_phrases = {'send_tweet': ['send tweet'],  # tweepy
                                   'send_text': ['send text message'],  #twilio
                                   'play_song': ['play music'],  #spotify
                                   'party_on': ['party on'],  # party on wayne
                                   }

                for k, v in special_phrases.items():
                    pattern = re.compile("(%s)" % "|".join(map(re.escape, v)))
                    words = re.sub(pattern, k, words)

                for word in words.split(' '):
                    if word in funcs:
                        print('yea man')
                        custom_functions(word, words)

                    elif words == 'Quit':
                        lets_go(run=False)


                #Print the message-->make it pop with graphics
                print(words)

    start_listening()


def lets_go(key, run=True):
    """
    Press key to trigger microphone recursively after capture
    """
    # print('Press "s" to start...')
    while run:
        try:
            # Record audio
            if key == ('s'):
                speak()
                break
            # Quit program
            if key == ('q'):
                return False
        except:
            break

        lets_go(key)


if __name__ == '__main__':
    """
    -add in ability to quit while stream is listening
    -phrase timeout afterall?
    """
    key = input("Press 's' to start")
    lets_go(key)