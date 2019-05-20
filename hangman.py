
Dash='_'
Empty_string=''
import random
import hangman_helper

def samelength_words_patern(words_list, word_pattern, ):
    ''' A function that receives words list , word pattern and return all the words that
     have the same length of the word pattern '''
    sameLength = []
    for i in range(len(words_list)):
        if len(words_list[i]) == len(list(word_pattern)):
            sameLength.append(words_list[i])
    return sameLength

def words_sutiable_pattern(list_word,pattern):
 '''a Funcction that receives list of Word and pattern of word
 and return all the words that appropriate to this pattern'''
 words_same_pattern = []
 for i in range (len(list_word)):
     a=list(list_word[i])
     b=(list_word[i])#to save the list
     for j in range(len(list(pattern))):
      if list(pattern)[j]== Dash:
          if list(list_word[i])[j] in list(pattern):#if the letter appears in the word more once
              pass
          else:
              a[j] = Dash
     if a==list(pattern):
      words_same_pattern.append(b)

 return words_same_pattern

def no_wrong_letters(word_list, list_Wrong):
    """ A Function that receives list of words and list of wrong letters
    and return all the words in the list that doesn't contain the wrong letters"""
    no_wrong = []
    count = 0
    for i in range(len(word_list)):
        for j in range(len(list_Wrong)):
            if list_Wrong[j] not in list(word_list[i]):
                count = count + 1
        if count == len(list_Wrong):
            no_wrong.append(word_list[i])
        count = 0
    return no_wrong

def filter_words_list(words,pattern,wrong_guess_lst):
    """ A Function that receives list of words and word-pattern and list of letters that
    does not appears in the word and return  all the words that found in list of words
     that have same length of pattern , same shape of pattern,does not contain wrong letters"""
    needed_list = samelength_words_patern(words, pattern)
    needed_list=words_sutiable_pattern(needed_list,pattern)
    needed_list = no_wrong_letters(needed_list, wrong_guess_lst)
    return needed_list

def return_max(sorted_list):
    """ A Function that receives a list that sorted [letter(even),number of appearance(odd)
    ,letter,number of appearance .....]and return by random the most letters appearance"""
    list_max_numbers = []
    list_max_letters = []
    for i in range(1,len(sorted_list)+1, 2):
            list_max_numbers.append(sorted_list[i])# just take the numbers
    maxnumber=max(list_max_numbers)
    for i in range(1, len(sorted_list) + 1, 2):
        if sorted_list[i]==maxnumber:
            list_max_letters.append(sorted_list[i-1])
    return(random.choice(list_max_letters))

def choose_letter(words,pattern):
 ''' A Function that receives a list of words and patter od word ande return the most
 common letter in the words that appropriate to this pattern****
 no need to sort the list of words again i supposed that the list is appropriate to the patetrn
 because we created fillter function'''
 convert_lettrs = []
 sorted_list=[]#[letter that does not appearance at pattern,number of appearance]
 for i in range(len(words)):
  convert_lettrs+=list(words[i])
 for i in range(97,123):
    if chr(i)in list(pattern):
        pass
    else:
     sorted_list.append(chr(i))
     sorted_list.append(convert_lettrs.count(chr(i)))
 return (return_max(sorted_list))



def update_word_pattern(word,pattern,letter):
    ''' A function that receives, word ,word pattern,letter and return the update word pattern'''
    string_list_pattern = Empty_string
    list_word = list(word)
    list_pattern = list(pattern)
    for i in range(len(list_word)):
        if list_word[i] == letter:
            list_pattern[i] = letter
    for j in range(len(list_pattern)):
        string_list_pattern+=list_pattern[j]
    return string_list_pattern

def convert_to_pattern(word):
    ''' A function that convert words to patterns'''
    pattern_len = Empty_string
    for i in range(len(list(word))):
        pattern_len += Dash
    return pattern_len

def run_single_game(words_list):
    ''' A function that receives a list of word and started the game '''
    error_count = 0
    wrong_guess_lst = []
    msg =hangman_helper.DEFAULT_MSG
    ask_play = False
    random_word = hangman_helper.get_random_word(words_list)
    word_pattern = convert_to_pattern(random_word)
    list_letters = []
    for i in range(97, 123):
        list_letters.append(chr(i))

    while len(wrong_guess_lst) < hangman_helper.MAX_ERRORS and Dash in list(word_pattern):
        hangman_helper.display_state(word_pattern, error_count, wrong_guess_lst, msg, ask_play)
        letter = hangman_helper.get_input()
        if letter[1] in list_letters:

            if letter[1] in list(random_word):

                if letter[1] in word_pattern:
                    msg = hangman_helper.ALREADY_CHOSEN_MSG+letter[1]
                else:
                    word_pattern = update_word_pattern(random_word, word_pattern, letter[1])
                    msg = hangman_helper.DEFAULT_MSG

            else:
                if letter[1] not in wrong_guess_lst:
                    msg = hangman_helper.DEFAULT_MSG
                    wrong_guess_lst.append(letter[1])
                    error_count=error_count + 1
                else:
                    msg = hangman_helper.ALREADY_CHOSEN_MSG+letter[1]

        elif letter[0]==hangman_helper.HINT:
            words_list = filter_words_list(words_list, word_pattern, wrong_guess_lst)
            hintletter = choose_letter(words_list, word_pattern)
            msg = hangman_helper.HINT_MSG+hintletter
        else:
            msg = hangman_helper.NON_VALID_MSG

    if Dash not in list(word_pattern):
     msg = hangman_helper.WIN_MSG
    else:
     msg = hangman_helper.LOSS_MSG + random_word
    ask_play = True
    hangman_helper.display_state(word_pattern, error_count, wrong_guess_lst, msg, ask_play)

def main():
    list_of_all_words=hangman_helper.load_words(file='words.txt')
    run_single_game(list_of_all_words)
    ans = hangman_helper.get_input()
    while ans[0] == hangman_helper.PLAY_AGAIN and ans[1]:
        run_single_game(list_of_all_words)
        ans = hangman_helper.get_input()

if __name__ == "__main__":
 hangman_helper.start_gui_and_call_main(main)
 hangman_helper.close_gui()
