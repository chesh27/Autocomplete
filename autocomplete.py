import random 
import string
from string import ascii_lowercase as alphabet #import the set of lowercase alphabets as a string ("abcdef....z")

def extract(query):
    dataset=set() # initialize an empty dataset which will store usernames 
    helper('',dataset,query,0) #call helper function to iteratively find users based on query 
    return sorted(list(dataset)) #return the lexicographically sorted list of usernames 
 
def helper(prefix,dataset,query,start_at): #helper function takes a prefix, the current dataset, the query function and the letter at which to start searching
    for i in range(start_at,26):  #iterate through letters starting from the specified letter until z
        results=query(prefix+alphabet[i]) # query prefix + letter and store results 
        if prefix+alphabet[i] in results: #edge case: if the query itself is a username
            dataset.add(prefix+alphabet[i]) # then add it to the dataset (eg. "al")
        if len(results)==5: #if query results in 5 names, that means there are potentially more
            dataset.update(results) #add names to dataset
            start_at=alphabet.index(results[4][len(prefix)+1]) #define new starting value as the next letter after the prefix in the last word of results (eg. if last word is allen when "a" is queried, new start value = "l")
            helper(prefix+alphabet[i],dataset,query,start_at) #recursively perform helper function as long as there are 5 results, with updated prefix and start value 
        else: #if there are < 5 results
            dataset.update(results) # add usernames to dataset 
    return

def test(num_words): #function to generate a dataset of random strings for testing purposes. Takes the number of strings to be generated as an argument 
    database = [] #initialize empty list of names 
    for i in range(num_words): #each iteration of the loop creates a random string  
        word = ''.join(random.choice(alphabet) for i in range(random.randint(1,20))) #a string is created by joining a random number of letters between 1 and 20
        database.append(word) # newly generated string is added to database
    database = sorted(database) #lexicographically sorted database 
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    print database
    print extract(query)
    assert extract(query) == database	

def main():
    """Runs your solution -- no need to update (except to maybe change the database)."""
    # Simple implementation of the autocomplete API
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "eve", "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
	
main()
test(20) #tests generality of solution on 20 randomly generated strings 
