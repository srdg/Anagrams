from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_que = webdriver.PhantomJS(executable_path="C:\\Users\\USER\\Desktop\\CSE\\phantomjs.exe")
driver_ans = webdriver.PhantomJS(executable_path="C:\\Users\\USER\\Desktop\\CSE\\phantomjs.exe")
inp = []

def display_rules():
	pass

def get_words():
	driver_que.get("https://www.textfixer.com/tools/random-words.php")
	driver_que.find_element_by_name("numWords").send_keys("2")
	driver_que.find_element_by_name("random-words").click()
	temp = driver_que.find_elements_by_class_name("savedWords")
	ques = [item.text for item in temp]
	#print(ques)
	return ques

def get_anagrams(ques):
	driver_ans.get("https://www.wordplays.com//anagram-solver/")
	driver_ans.find_element_by_name("Word").send_keys(ques[0])
	driver_ans.find_element_by_name("search").click()
	temp = driver_ans.find_elements_by_class_name("word")
	anse = [item.text for item in temp if len(item.text)==len(ques[0])]
	#print(anse)
	return anse

def play_game():
	while(1):
		i = str(input())
		if i =='0':	break
		inp.append(i)
	return inp 

def main():
	print("Please stand by while I build my database...")
	wrd = get_words()
	ans = get_anagrams(wrd)
	input("READY TO PLAY? PRESS ENTER ")
	print("Enter all possible meaningful combinations of "+wrd[0].upper()+" you can think of.\nIf you can't think anymore, enter 0.")
	inp = play_game()
	score = len(list(set(ans).intersection(inp)))
	print("YOUR SCORE IS %.2f " % ((score/len(ans))*100))
	if score == len(ans):	print("So, CONGRATULATIONS!!! IT SEEMS YOU ARE EXCELLENT AT DECIPHERING ANAGRAMS!!")
	else: print("Looks like you need to practice more, buddy! Better luck next time!");
	print("The possible answers were...")
	print(ans)
	input("Press ENTER to finish!!")

main()