"""가위바위보 게임

[입력] 사용자에게 r, s, p 중 하나의 문자를 입력받는다.
r은 바위(rook), s는 가위(sissors), p는 보(papers)를 의미한다.

[출력]
컴퓨터가 r, s, p 중 랜덤으로 선택한 것을 출력한다.
사용자가 선택한 문자를 출력한다.
사용자가 이겼는지, 졌는지 비겼는지 출력한다.
"""


import random


def rsp_game(user):
	computer = random.choice(['r', 's', 'p'])

	if user == computer:
		result = "User: " + user + "\nComputer: " + computer + "\n비겼습니다."
	else:
		if user == 'r':
			if computer == 's':
				result = "User: " + user + "\nComputer: " + computer + "\n이겼습니다."
			else:
				result = "User: " + user + "\nComputer: " + computer + "\n졌습니다."
		elif user == 's':
			if computer == 'p':
				result = "User: " + user + "\nComputer: " + computer + "\n이겼습니다."
			else:
				result = "User: " + user + "\nComputer: " + computer + "\n졌습니다."
		else:
			if computer == "r":
				result = "User: " + user + "\nComputer: " + computer + "\n이겼습니다."
			else:
				result = "User: " + user + "\nComputer: " + computer + "\n졌습니다."

	return result

if __name__ == "__main__":
	user = input("r, s, p 중 하나를 입력학세요 -->>")
	print(rsp_game(user))