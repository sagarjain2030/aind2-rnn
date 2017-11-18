import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import string


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    lastIndex = window_size
    i = 0
    count = len(series)

    while (lastIndex < count):
        X.append(series[i:lastIndex])
        y.append(series[lastIndex])
        i += 1
        lastIndex += 1

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])

    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5,input_shape=(window_size,1)))
    model.add(Dense(1))
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    Valid_Characters = string.ascii_letters
    punctuation = ['!', ',', '.', ':', ';', '?', ' ']
    uniq = ''.join(set(text))
    for c in uniq:
        if c not in punctuation and c not in Valid_Characters:
            text = text.replace(c,'')

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    lastIndex = window_size
    i = 0
    count = len(text)

    while (lastIndex < count):
        inputs.append(text[i:lastIndex])
        outputs.append(text[lastIndex])
        i += step_size
        lastIndex += step_size

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200,input_shape=(window_size,num_chars)))
    model.add(Dense(num_chars,activation='softmax'))
    return model

def main():
    odd_nums = np.array([1, 3, 5, 7, 9, 11, 13])
    X , y = window_transform_series(odd_nums,2)
    print(X)
    print(y)

    tri = "ï»¿project gutenberg's the adventures of sherlock holmes, by arthur conan doyle\n\nthis ebook is for the use of anyone anywhere at no cost and with\nalmost no restrictions whatsoever.  you may copy it, give it away or\nre-use it under the terms of the project gutenberg license included\nwith this ebook or online at www.gutenberg.net\n\n\ntitle: the adventures of sherlock holmes\n\nauthor: arthur conan doyle\n\nposting date: april 18, 2011 [ebook #1661]\nfirst posted: november 29, 2002\n\nlanguage: english\n\n\n*** start of this project gutenberg ebook the adventures of sherlock holmes ***\n\n\n\n\nproduced by an anonymous project gutenberg volunteer and jose menendez\n\n\n\n\n\n\n\n\n\nthe adventures of sherlock holmes\n\nby\n\nsir arthur conan doyle\n\n\n\n   i. a scandal in bohemia\n  ii. the red-headed league\n iii. a case of identity\n  iv. the boscombe valley mystery\n   v. the five orange pips\n  vi. the man with the twisted lip\n vii. the adventure of the blue carbuncle\nviii. the adventure of the speckled band\n  ix. the adventure of the engineer's thumb\n   x. the adventure of the noble bachelor\n  xi. the adventure of the beryl coronet\n xii. the adventure of the copper beeches\n\n\n\n\nadventure i. a scandal in bohemia\n\ni.\n\nto sherlock holmes she is always the woman. i have seldom heard\nhim mention her under any other name. in his eyes she eclipses\nand predominates the whole of her sex. it was not that he felt\nany emotion akin to love for irene adler. all emotions, and that\none particularly, were abhorrent to his cold, precise but\nadmirably balanced mind. he was, i take it, the most perfect\nreasoning and observing machine that the world has seen, but as a\nlover he would have placed himself in a false position. he never\nspoke of the softer passions, save with a gibe and a sneer. they\nwere admirable things for the observer--excellent for drawing the\nveil from men's motives and actions. but for the trained reasoner\nto admit such intrusions into his own delicate and finely\nadjusted temperament was to introduce a di"
    print(cleaned_text(tri))

if __name__ == "__main__":
    main()

