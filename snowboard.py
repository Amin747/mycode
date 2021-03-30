#!/usr/bin/env python3
ever_done = input("Welcome to my snowboard level estimator!!!\nHave you ever snowboarded before?\n Reply with y/n please.\n")
if ever_done == "n":
    print("You're a beginner. I would recommend getting a 5-day pass! Get on the slopes! If you can afford it, get a trainer, if not, YouTube is almost free! You're gonna fall many times, but a true snowboarder stands up every time and pushes again...\n#yesyoucan")
else :
    s_turn = int(input("Interesting! Ok, scale 1-10, how comfortable are you making S turns on slopes?\n"))
    if s_turn >=7 and s_turn<=10:
        jumps = input("Wow! Thats amazing! Looks like you've paid the price to become a master! Let me ask you one more question...Can you do L-XL jumps with 180s, 360s, 540s and larger rotations?\n Please reply with y/n.\n")
        if jumps == "y":
            print("You are a PRO level 10!!! Keep it rockin and let me know your number so we can set up a ride sometime! Will be happy to learn alongside/behind you! lol\n")
        else :
            print("You're an expert level 8-9! You're an excellent performer, just focus on jumps and I'll give you a PRO 10 badge!\n")
    elif s_turn>=4 and s_turn<7:
        steep_slope = input("Seems like you have done a fair bit of practice, and now honing your skills! That's where I am too! So let's get deeper to determine your level! Can you do S turns comfortably on black and diamond slopes? reply with y/n\n")
        if steep_slope == "y":
            print("Nice! Looks like you've mastered the most important chunk of it all, the S turns! All you need to focus on is now jumps and quick turns on air. You are a solid level 6-7! Keep pushing, you're on the right track!")
        else :
            print("You're a level 4-5! You are an intermediate snowboarder and that's amazing! keep working on your S turns and also try to jump when the conditions permit, chances are you will like it!")
    else:
        print("You have made great progress and with 5-10 more sessions, I see you passing the beginner level and join the cool intermediate gang! Focus on basics and watch YouTube videos on how to do it right!")
print("\nI hope this app was somewhat alright in estimating your snowboarding level. Thanks for giving it a shot!")
