import unittest

class Node:
    def __init__(self ):
        self.children = {}
    
    def add_word(self, w):
        if w[0] not in self.children:
            self.children[w[0]] = Node()    
        if len(w) > 1:
            self.children[w[0]].add_word(w[1:])

    def find(self, c):
        if c in self.children:
            return self.children[c]
        return 

    def __repr__(self):
        return '<' + str(self.children) + '>'

def word_break(string, dictionary):
    #sort dictionary
    dicts  = Node()
    for w in dictionary:
        dicts.add_word(w + '\n')
    
    possibles  = {'':dicts}
    current = ''
    done = ''
    terms = []
    c_i = 0
    while c_i < len(string):
        c = string[c_i]
        current += c
        #print c
        index = 0
        to_delete = []
        to_add = []
        for term in possibles:
            node = possibles[term]
            next = node.find(c)
            #print "NOW:", c, "filter:", str(next) 
            if next == None:
                #print done
                to_delete.append(term)

            elif '\n' in next.children:
                #print "children:", len(next.children)
                if len(next.children) == 1:
                    #print "find 1 sure term!", current
                    done += current + ' '
                    current = ''
                    to_add.append(['', dicts])
                    for i in possibles:
                        if i != '': to_delete.append(i)
                else:
                    to_add.append([current, dicts])
                    possibles[term] = next
                    #print "find 1 possible term!", current
                

            else:
                if term != '':
                    #print "ambiguous:", term, possibles
                    done += term + ' '
                    current = c
                    to_add.append(['',  next])
                    to_delete.append(term)

                possibles[term] = next
            
        for d in to_delete:
            if d in possibles:
                del possibles[d]
        for a in to_add:
            possibles[a[0]] = a[1]

        c_i += 1
    return done.strip()

class Test(unittest.TestCase):
    def setUp(self):
        self.dictionary= ["this", "is", "a", "book", "i", "can", "fly", "ppm", "sucks", 'the', 'they', 'like',  'key']

    def testUnambiguous(self):
        string = "theylikethebook"
        self.assertEqual(word_break(string, self.dictionary), "they like the book")
    
    def testAmbigious(self):
        string = "theylikethisbook"
        self.assertEqual(word_break(string, self.dictionary), "they like this book")

if __name__ == "__main__":
    unittest.main()
