"""
I was just tryring to have some fun :)
We have a list of words that can be arranged to form a meaningful sentence.
This get_random_senttence() funtion tries random combinations of words till it gets the correct arrangement of the words that gives the meaningful sentence.
The clean_sentence() function turns the list into a string
"""

import random
import statistics as stx
from statistics import mean, median, mode

words = ['George', 'boy', 'polite', 'is', 'a']

def get_random_sentence(words):
    sentence = []
    for word in words:
        sentence.insert(random.randint(0, len(words)), word)
    return sentence

def clean_sentence(sentence):
    """ Turn the list into string """
    string = ""
    for i in sentence:
        string += i + " "
    sentence = string
    return sentence   

def main():
    count = 0
    for i in range(10000):
        sentence = get_random_sentence(words)
        print(f"Trial {count + 1}: {sentence}")
        count += 1
        
        # if sentence[0] == 'George' and sentence[1] == 'is' and sentence[2] == 'a' and sentence[3] == 'polite' and sentence[4] == 'boy':
        #     break 
        
        if sentence == ['George', 'is', 'a', 'polite', 'boy']:
            break
        
    if count >= 10000:
        print(f"\nCould not get correct sentence after {count} trials")
        exit()
    else:
        print(f"\nProper sentence gotten in {count} trials") 
        cleaned_sentence = clean_sentence(sentence)
        print(f"'{cleaned_sentence}'\n")
        return count
     
if __name__ == "__main__":
    main()        


def list_results():
    """ 
    This function gets a list of the number of trials required to get the correct sentence after a 100 iterations.
    Each of the 100 values represents the number of trials for each time a correct sentence a produced.
    """
    
    trials = []
    for i in range(100):
        trials.append(main())  
    print(f"\nNumber of trials before getting correct sentence for the 100 trials: \n{trials}") 
    print(f"\nMean number of trials: {stx.mean(trials)}")
    print(f"Median number of trials: {stx.median(trials)}")
    print(f"Mode: {stx.mode(trials)}")
    print(f"Highest number of trials: {max(trials)}")
    print(f"Lowest number of trials: {min(trials)}")
    
    return mean(trials)

print(list_results())