import nltk, re

from nltk.corpus import words , names
"""
corpus package automatically creates a set of corpus reader instances that can be used to access the corpora in the NLTK data package

"""
nltk.download('names', quiet=True)

listOfNume = names.words()

nltk.download('words', quiet=True)


listOfWord = words.words()



All_letter = 'abcdefghijklmnopqrstuvwxyz'

"""
Create an encrypt function that takes in a plain text phrase and a numeric shift
E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’

"""

def encrypt(text,numeric):

    charactures=text.split()

    characture_arr=[]

    for word in charactures:

        encrypt_data=''
        
        for words in word:
        
            if words.lower() != words and words.lower() in All_letter:
        
                num=(All_letter.index(words.lower())+numeric) %26
        
                encrypt_data+=(All_letter[num].upper())
        
        
            elif words.lower() == words and words.lower() in All_letter:
        
                num=(All_letter.index(words)+numeric) %26
        
                encrypt_data+=(All_letter[num])
        
            else :
        
                encrypt_data+=words
        
        characture_arr.append(encrypt_data) 
   
    return " ".join(characture_arr)



"""

Create a decrypt function that takes in encrypted text and numeric shift 
which will restore the encrypted text back to its original form when correct key is supplied.
"""    

def decrypt(encrypted_text,numeric):

    return encrypt(encrypted_text,-numeric)

"""

Create a crack function that will decode the cipher so 
that an encrypted message can be transformed into its original state WITHOUT access to the key

"""
def crack(encrypted_data):


    for word in range (1,27):


        data = decrypt(encrypted_data,word)


        percent = int(count_words(data) / len(encrypted_data.split()) * 100)


        if percent < 50:


            return data 
"""
function that called count_words that  count number of word in sentences
"""
def count_words(text):
    
     split_text = text.split()
    
     conter = 0   
    
     for obj in split_text:
    
        word = re.sub(r'[^A-Za-z]+','', obj)
    
        if word.lower() in listOfWord or word in listOfNume:
    
            conter += 1
    
        else:
    
            pass
    
     return conter

    

print(encrypt('shahd',1))
print(decrypt('shahd',1))
