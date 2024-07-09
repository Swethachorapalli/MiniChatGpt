
import sys, time, wikipedia

def minichatgpt():
    topic = input('Hey what do you want to know about??!!: ')
    sentences = int(input('How many sentences do you want to know about??!!: '))
    result = wikipedia.summary(topic, sentences=sentences)
    
    
    words = result.split()
    
    
    for word in words:
        sys.stdout.write(word + ' ')
        sys.stdout.flush()
        time.sleep(0.2)  

minichatgpt()