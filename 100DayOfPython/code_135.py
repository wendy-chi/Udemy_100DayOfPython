#随机显示出两条数据
from code_135_data import data
import random

user_correct = True
user_score = 0


a = random.choice(data)
#a = data[0]
a_followers = a['follower_count']
while user_correct:
    #data.remove(a)
    b = random.choice(data)
    #b = data[1]
    b_followers = b['follower_count']

    if a == b:
        b = random.choice(data)

    print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
    print(f"Against B: {b['name']}, {b['description']}, {b['country']}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    #比较两个人的follower数量

    if a_followers > b_followers:
        if user_choice == 'A':
            #user_get_score(user_correct)
            user_score += 1
            print(f"You are right. Current score: {user_score}")
            user_correct = True
            a = b
            a_followers = b_followers
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            user_correct = False   #游戏结束
    else:  #a_followers < b_followers
        if user_choice == 'A':
            print(f"Sorry, that's wrong. Final score: {user_score}")
            user_correct = False  # 游戏结束
        else:
            user_score += 1
            print(f"You are right. Current score: {user_score}")
            user_correct = True
            a = b
            a_followers = b_followers
