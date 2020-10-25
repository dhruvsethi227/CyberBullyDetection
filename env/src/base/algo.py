from profanity import profanity
import sentiment_analysis

def get_sentiment(transcript):
    f1 = open("f1.txt", "w")
    f1.write(transcript)
    f1.close()
    l1 = sentiment_analysis.main(["f1.txt"])
    return l1

def do_profanity(transcript):
    startIndex = 0
    currIndex = 0
    counter = 0
    s1 = transcript[0: 4]
    for i in transcript:
        if i == '.' or i == '!' or i == '?':
            s1 = transcript[startIndex: currIndex]
            startIndex = currIndex
            if profanity.contains_profanity(s1):
                counter += 1
        currIndex += 1
    s1 = transcript[startIndex: currIndex]
    startIndex = currIndex
    if profanity.contains_profanity(s1):
        counter += 1
    return counter 

def get_final(transcript):
    l1 = get_sentiment(transcript)
    l1[0] = l1[0] - (do_profanity(transcript) * 0.005)
    return l1