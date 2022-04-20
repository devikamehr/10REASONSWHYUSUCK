
   
# coding: utf-8
#
# the top line, above, is important --
# it ensures that Python will be able to use this file,
# even if you paste in text with Unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
#
# Name:
#
import random
def wc(filename):
    """Word-counting function.  Opens a file named 'filename', reads
       it, and returns the number of words in the file.
       Example: wc('a.txt')
    """
    #
    # First we have to "open" the file (just like opening a book so you
    # can read it).  We ask Python to use the "latin1" encoding, because it
    # accepts more characters ASCII.  If you have a REALLY adventurous file,
    # you might need to use the "utf-8" encoding.
    #
    f = open(filename, encoding = 'latin1')

    #
    # Now read the entire contents of the file into a string named "text",
    # and then close it.  Note that this approach only works for relatively
    # small files; bigger ones should be read one line at a time by calling
    # 'f.readline()' in a loop.
    #
    text = f.read()
    f.close()

    #
    # The text of the file is one long string.  Use "split" to divide
    # it up into "words" at whitespace boundaries.
    #
    LoW = text.split()    

    #
    # LoW is a list of words, so its length is the word count.
    #
    return len(LoW)

def vc(filename):
    """Vocabulary-counting function.  Opens a file named 'filename',
       reads it, and breaks it into words.  Then, for each word,
       counts how many times it occurs.  Prints a message giving the
       number of distinct words in the file, and then returns a
       dictionary in which each word is a key and the word's frequency
       is the value.
       Example: vc('a.txt') might print 3 and return
       {'I': 2, 'love': 3, 'spam': 42}
    """
    f = open(filename, encoding = 'latin1')
    text = f.read()
    f.close()

    LoW = text.split()    
    print("There are", len(LoW), "words.")

    d = {}
    for w in LoW:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
            
    print("There are", len(d), "*distinct* words.\n")
    return d   # this way we can use the data in d later!

# function #1
#
def createDictionary(filename):
    f = open(filename, encoding = 'latin1')
    text = f.read()
    f.close()

    LoW = text.split()    
    d = {}
    pw = '$'

    for nw in LoW:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]
                    

        pw = nw
        if pw[-1] == "!" or pw[-1] == "." or pw[-1] == "?":
            pw = '$'

    return d

    # then check for whether that new pw ends in 
    # punctuation -- if it _does_ then set pw = '$



# function #2
#
def generateText(d, N):
    final = " "
    pointer = "$"
    #words = fw
    #length = len(d)
    # pointer = random.choice(d[1,length])
    for i in range(N):
        pointer = random.choice(d[pointer])
        final += " " + pointer
        #final += " " + newWord[pointer]
        nextWord = pointer[-1]
        if nextWord == "!" or nextWord == "." or nextWord == "?":
            pointer = '$'

    return final[1:]

def createPhrases():
    d = createDictionary('info.txt')
    l = generateText(d, 50).split('.')
    return l


