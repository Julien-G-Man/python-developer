"""
I was just tryring to have some fun :)
We have a list of words that can be arranged to form a meaningful sentence.
This get_random_senttence() funtion tries random combinations of words till it gets the correct arrangement of the words that gives the meaningful sentence.
The clean_sentence() function turns the list into a string
"""
import random
import statistics as stx
from statistics import mean, median, mode

words = ['George', 'man', 'polite', 'is', 'Bush', 'a'] #'young',

def get_random_sentence(words):
    sentence = []
    for word in words:
        sentence.insert(random.randint(0, len(words)), word)
    return sentence

def stringify_sentence(sentence):
    """ Turn the list into string """
    string = ""
    for i in sentence:
        string += i + " "
    sentence = string
    return sentence   

def main():
    count = 0
    max_count = 200000
    for i in range(max_count):
        sentence = get_random_sentence(words)
        # print(f"Trial {count + 1}: {sentence}")
        count += 1
        
        # if sentence[0] == 'George' and sentence[1] == 'is' and sentence[2] == 'a' and sentence[3] == 'polite' and sentence[4] == 'boy':
        #     break 'young',
        
        if sentence == ['George', 'Bush', 'is', 'a', 'polite', 'man']:
            break
        
    if count >= max_count:
        print(f"\nCould not get correct sentence after {count} trials")
        exit()
    else:
        # print(f"\nProper sentence gotten in {count} trials") 
        string_sentence = stringify_sentence(sentence)
        # print(f"'{string_sentence}'")
        return count
     
if __name__ == "__main__":
    main()        


def display_results():
    """ 
    This function gets a list of the number of trials required to get the correct sentence after a 100 iterations (rounds).
    Each of the 100 values represents the number of trials for each time a correct sentence a produced.
    """
    
    trials = []
    for i in range(100):
        trials.append(main())
    print(f"\nNumber of trials before getting correct sentence for each of the 100 rounds: \n{trials}") 
    print(f"\nMean number of trials: {stx.mean(trials)}")
    print(f"Median number of trials: {stx.median(trials)}")
    print(f"Mode: {stx.mode(trials)}")
    print(f"Highest number of trials: {max(trials)}")
    print(f"Lowest number of trials: {min(trials)}")
    
    #return mean(trials)

print(display_results())

"""
Results:
for 5 words, mean number of trials = 35297.27, highest number of trials = 165669
for 6 words, mean number of trials = 2886.87, highest number of trials = 13114
for 7 words, mean number of trials = , highest number of trials = 
"""