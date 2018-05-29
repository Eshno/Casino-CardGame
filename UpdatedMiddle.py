class Middle:

    def __init__(self,cards = []):
        self.cards = []


    def Select_Card():
        return

    def show_middle(self):
        print "\n***Middle*** \n"
        count = 1
        for card in self.cards:
            if card[-1] == "Combined" or card[-1] == "Paired":
                print "((" + str(count) + "))",
                for e in range(1, len(i) - 1):
                    if card[e][0] == 1:
                        print "Ace of", card[e][1], "|" ,
                    else:
                        print card[e][0] ,"of", card[e][1], "|" ,
                print "Needs a ", card[0],  "to Claim"
            else:
                if card[0] == 1:
                    print "((" + str(count) + "))",  "Ace of", card[1] , "|",
                else:
                    print "((" + str(count) + "))",  card[0], "of", card[1] , "|",
            print "\n"
            count +=1
