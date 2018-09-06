class Middle:
    cards = []

    def __init__():
        pass

    @classmethod
    def place_card(cls, card):
        cls.cards.append(card)
          
        

    @classmethod
    def show_middle(cls):
        print "\n***Middle*** \n"
        count = 1
        for i in cls.cards:
            if i[-1] == "Combined" or i[-1] == "Paired":
                print "((" + str(count) + "))",
                for e in range(1, len(i) - 1):
                    if i[e][0] == 1:
                        print "Ace of", i[e][1], "|" ,
                    else:
                        print i[e][0] ,"of", i[e][1], "|" ,
                print "Needs a ", i[0],  "to Claim"
            else:
                if i[0] == 1:
                    print "((" + str(count) + "))",  "Ace of", i[1] , "|",
                else:
                    print "((" + str(count) + "))",  i[0], "of", i[1] , "|",
            print "\n"
            count +=1
        
        

    
    
        
        

