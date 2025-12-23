votes={"A":0,"B":0,"C":0}
for _ in range(5):
    choice=input("vote(A/B/C): ").upper()
    if choice in votes:
        votes[choice]+=1
        print("Result:",votes)
