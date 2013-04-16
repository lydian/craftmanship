import unittest

class TrieNode:
    def __init__(self ):
        self.children = {}
    
    def add_child(self, character):
        if character not in self.children:
            self.children[character] = TrieNode()

    def find(self, c):
        if self.children == None or c not in self.children:
            return 
        return self.children[c]

    def __repr__(self):
        return '<' + str(self.children) + '>'

class Dictionary:
    def __init__(self):
        self.root_node = TrieNode()

    def add_term(self,  term):
        current_node = self.root_node
        for char in term + '\n':
            current_node.add_child(char)
            current_node = current_node.children[char]

    def __repr__(self):
        return "{" + str(self.root_node)  + "}"


def update_possible_terms(possible_terms, to_delete, to_add):
    for term_to_delte in to_delete:
        if term_to_delte in possible_terms:
            del possible_terms[term_to_delte]
    for term_to_add in to_add:
        possible_terms[term_to_add] = to_add[term_to_add]
    return possible_terms


def getStatus(last_node, current_character):
    current_node = last_node.find(current_character)

    if current_node  == None:
        return "Incorrect Node"
    elif '\n' in current_node.children and len(current_node.children) == 1:
        return "Find 1 sure term"
    elif '\n' in current_node.children:
        return "Find 1 possible term, need to validate after"
    else:
        return "still possible, need to checkout after"

def createDictionary(dictionary_array):
    dictionary  = Dictionary()
    for term in dictionary_array:
        dictionary.add_term(term)
    return dictionary

def word_break(string_to_break, dictionary): 
    possible_terms  = {"":dictionary.root_node} 
    current_term = ""
    finished_parsed_string = ""

    for current_character in string_to_break:
        current_term += current_character
        add_to_possibles = {}
        not_possible = set()
        for possible_term in possible_terms:
            
            last_node_for_possible_term = possible_terms[possible_term]        
            status = getStatus(last_node_for_possible_term, current_character)
            
            if status == "Incorrect Node":
                not_possible.add(possible_term)

            elif status == "Find 1 sure term":
                finished_parsed_string += current_term + ' '
                current_term = ''
                add_to_possibles[''] =  dictionary.root_node
                not_possible.add(possible_term)
            
            elif status == "Find 1 possible term, need to validate after":
                add_to_possibles[current_term] = dictionary.root_node
                current_node_for_this_character = last_node_for_possible_term.find(current_character)
                possible_terms[possible_term] = current_node_for_this_character
            
            elif status == "still possible, need to checkout after":
                current_node_for_this_character = last_node_for_possible_term.find(current_character)
                possible_terms[possible_term] = current_node_for_this_character
                
                #validates possible terms, if there are possible terms
                if possible_term != '':
                    #print "ambiguous:", possible_term, possible_terms
                    finished_parsed_string += possible_term + ' '
                    current_term = current_character
                    current_node_for_this_character = last_node_for_possible_term.find(current_character)
                    add_to_possibles[''] = current_node_for_this_character
                    not_possible.add(possible_term)
                
        possible_terms = update_possible_terms(possible_terms, not_possible, add_to_possibles)
        

    return finished_parsed_string.strip()

class Test(unittest.TestCase):
    def setUp(self):
        self.dictionary_array= ["this", "is", "a", "book", "i", "can", "fly", 'the', 'they', 'like',  'key']
        self.dictionary = createDictionary(self.dictionary_array)
    
    def testEasy(self):
        string = "icanfly"
        self.assertEqual(word_break(string, self.dictionary), "i can fly")
    
    def testEasy2(self):
        string = "thisisabook"
        self.assertEqual(word_break(string, self.dictionary), "this is a book")

    def testUnambiguous(self):
        string = "theylikethebook"
        self.assertEqual(word_break(string, self.dictionary), "they like the book")
    
    def testAmbigious(self):
        string = "theylikethisbook"
        self.assertEqual(word_break(string, self.dictionary), "they like this book")

if __name__ == "__main__":
    unittest.main()
