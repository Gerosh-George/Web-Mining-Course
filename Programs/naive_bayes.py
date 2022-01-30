from enum import unique
import pandas as pd
import numpy as np
import re

all_words = []
word_size_class = {}
all_sents = []
word_frequency_label = {}

def load_data(filename):

    data = pd.read_excel(filename)
    test_index = data['Class'] == '?'
    training_data = data[-test_index]
    testing_data = data[test_index]   
    testing_data.reset_index(inplace = True, drop = True) 
    
    return (training_data,testing_data)

def find_vocab_size(training_data):

    for index,sent in enumerate(training_data['URL']):
        ext_words = re.findall(r"([a-z0-9]+)",sent)
        label = training_data['Class'][index]
        word_size_class[label] = word_size_class.get(label,0) + len(ext_words)
        all_words.extend(ext_words)
        all_sents.append(ext_words)
    
    unique_words_count = len(set(all_words))
    all_words_count = len(all_words)

    global unique_words
    unique_words = list(set(all_words))

    return (unique_words_count,all_words_count)


def find_prior_probabilties(training_data):
    
    class_prior = {}

    labels = training_data['Class'].unique()
    
    total = len(training_data)
    for l in labels:
        class_prior[l] = sum(training_data['Class'] == l) / total

    return class_prior


def find_word_frequency_class(training_data):
    
    for word in unique_words:

        for index,sent_vec in enumerate(all_sents):
            if word in sent_vec:
            
                if word not in word_frequency_label:
                    word_frequency_label[word] = {}
                label = training_data['Class'][index]

                word_frequency_label[word][label] = word_frequency_label[word].get(label,0) + sent_vec.count(word) 


def display_conditional_prob(vocab_size,labels):

    i=0
    for word in word_frequency_label:
        
        for label in labels:
            num = word_frequency_label[word].get(label,0) + 1
            denom = word_size_class[label] + vocab_size
            space = " "
            print(f"P({word}/{label}) = {num}/{denom} {space*(14-len(word))}",end="\t")

        print()   
   
def display_test_results(data,labels,vocab_size,class_prior):
    

    for i,sent in enumerate(data['URL']):
        ext_words = re.findall(r"([a-z0-9]+)",sent)
        
        probs = []
        for label in labels:
            prob = 1
            for word in ext_words:
                
                class_dict = word_frequency_label.get(word)
                
                num = 0
                denom = (word_size_class[label]+vocab_size)

                if class_dict == None:
                    num = 1
                else:                    
                    num = class_dict.get(label,0) + 1

                #print(f"{num}/{denom} ({word})  ",end=" ")
                prob *= (num/denom) 
            #print(f"{label}\n")  

            prior = class_prior[label]
            probs.append(prior*prob)
        
        probs = np.array(probs, dtype=np.float32)

        index = np.argmax(probs)
        print(f"\n{sent} ===> {labels[index]}  {probs}")
        data['Class'][i] = labels[index]
    
    print("\nFinal Result:")
    print(f"{data}\n")



def main():

    filename = "./naive_bayes_data.xlsx"
    #filename = "./test_data.xlsx"

    train_data,test_data = load_data(filename)

    print("Training Data:")
    print(train_data)
    
    labels = train_data['Class'].unique()

    class_prior = find_prior_probabilties(train_data)
    print(f"\nPrior Probabilities: {class_prior}\n")

    vocab_size, total_word_count = find_vocab_size(train_data)
    print(f"Vocab size: {vocab_size}")
    print(f"Total words in train data: {total_word_count}\n")

    find_word_frequency_class(train_data)
    print("Formed a dictionary of words with respect to their frequency and class\n")

    for key,value in word_size_class.items():
        print(f"No of words in '{key}' class: {value}")
    
    print('\nDisplaying all the conditional Probabilities:')
    display_conditional_prob(vocab_size,labels)

    print("\nDisplaying the result on test sentences:")
    display_test_results(test_data,labels,vocab_size,class_prior)






if __name__ == "__main__":
    main()

