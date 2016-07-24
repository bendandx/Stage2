# IPND Stage 2 Final Project

blanks=['___0___', '___1___', '___2___', '___3___', '___4___', '___5___']

prompt1 = '''Survivor is a long-running game show hosted by Jeff ___0___. In it, contestants are stranded in a remote location for 39 days. The contestants are split into two to four ___1___. Every three days, they must vote off one of their own in tribal ___2___.  When there are two to three contestants left, the rules change in the final tribal ___2___. The last seven to nine people voted out are put on the ___3___, and must decide which of the remaining contestants is most deserving of winning one ___4___ dollars by interrogating them, and then casting a vote for who they thing should win.\n'''
key1=['probst', 'tribes', 'council', 'jury', 'million']

prompt2 = '''Many strategies are viable in Survivor. Some players focus on their ___0___ game, building relationships to ensure that they are not voted out, and hopefully end up with friends on the jury. Others focus on their strategic game, forming utilitarian ___1___ and turning Survivor into a numbers game against opposing ___1___. Other still focus on their physicality, aiming to win ___2___ challenges, which make them safe at the next tribal council. To take home the million dollars, some amount of all three are necessary - usually, someone with no ___0___ game is taken to the end as a sacrificial ___3___, ensuring that whoever they are up against wins the jury vote. Someone with no strategic game, however, might not even make it that far.\n'''
key2=['social', 'alliances', 'immunity', 'goat']

prompt3 = '''The first season is known as Survivor:___0___. The eventual winner, Richard ___1___, formed the first alliance, known as the ___2___ alliance based on their tribe name. The other tribe, ___3___, are remembered for their systematic elimination once the tribes merged, as they had neglected to form any sort of voting bloc themselves. To this day, one tribe being eliminated one after another postmerge is referred to as "___3___ing". The endgame of ___0___ revolved around Rudy, ___1___'s loyal ally, Sue, a member of the ___2___ alliance who was wary of ___1___, and Kelly, Sue's best friend on the island, who was also close to the ___3___s. In the end, Kelly betrayed Sue and ___1___ managed to vote Rudy off without losing his friendship. The final two consisted of Kelly and Rich; Sue gave the infamous, incendiary "Snakes and ___4___" speech, criticizing ___1___ for his predatory game and Kelly for her dishonesty. In the end, Kelly was seen as feckless for downplaying(and at some points outright denying) her role in the ___2___ alliance. The jury narrowly awarded the win to ___1___ in a 4-3 vote. ___1___ is seen as the founder of modern Survivor strategy, and one of the best players ever.\n'''
key3 = ['borneo', 'hatch', 'tagi', 'pagong', 'rats']

def difficultySelector():
    """Returns chosen difficulty"""
    difficulty=''
    while difficulty!='hard' and difficulty!='medium' and difficulty!='easy':
        difficulty=raw_input("Easy, Medium, or Hard? ").lower()
    return difficulty

def failState(strikes):
    """checks if player has used allotted strikes"""
    if strikes>=3:
        return True
    return False

def checkAnswer(answer, blank, key):
    """returns True if given answer matches blank"""
    if answer in key and key.index(answer)==blanks.index(blank):
        return True
    else:
        return False

def blankTranslator(blank):
    """accepts int, outputs formatted str"""
    stringBlank='___%d___'%blank
    return stringBlank

def playAgain():
    yn=''
    while yn!='y' and yn!='n':
        yn=raw_input("Play Again? y/n").lower()
    if yn=='n':
        return False
    return True

def quizzer(prompt, key):
    """presents prompt and accepts answers, returns True if player is successful, otherwise False"""
    strike, blank=0, 0
    for i in key:
        print prompt
        answer=raw_input("Your answer: ").lower()
        while checkAnswer(answer, blankTranslator(blank), key)==False:
            strike+=1
            print "strike %d!" %strike
            if failState(strike)==True:
                return False
            print prompt
            answer=raw_input("Your answer: ").lower()
        prompt=prompt.replace(blankTranslator(blank), answer)
        blank+=1
        strike=0
    print prompt.replace(blankTranslator(blank), answer)
    return True

tryAgain=True
while tryAgain==True:
    print "you have three chances per answer."
    difficulty=difficultySelector()
    if difficulty=='easy':
        success=quizzer(prompt1, key1)
    if difficulty=='medium':
        success=quizzer(prompt2, key2)
    if difficulty=='hard':
        success=quizzer(prompt3, key3)
    if success==True:
        print 'Congratulations!'
        tryAgain=playAgain()
    if success==False:
        print 'Game Over!'
        tryAgain=playAgain()
