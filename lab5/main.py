
votes = [2,6,3]
data = [["c","a","b"],["a","b","a"],["b","c","d"],["d","d","c"]]
keys = ["a","b","c","d"]
data2 = [["c","a","b","d"],["a","b","c","d"],["b","a","d","c"]]

def bords_method():
    res = {"a": 0, "b": 0, "c": 0,"d":0}
    for i,num in enumerate(data):
        for j,let in enumerate(num):
            tmp = {f"{let}": res.get(f"{let}") + votes[j] * (3-i)}
            res.update(tmp)

    winner = [max([(key,ress) for key, ress in res.items()],key=lambda elem:elem[1])]

    for key,ress in res.items():
        if key != winner[0][0] and res == winner[0][1]:
            winner.append((key,res))

    print("Borda:")
    [print(f"{key} score {ress} votes") for key,ress in res.items()]
    print("Winner ",end="")
    [print(f"{elem[0]}",end=" ")for elem in winner]
    print(f"scored {winner[0][1]} votes", end="\n\n")

def komplenda():
    win_res = dict.fromkeys(keys, 0)
    results = []

    for i, applicnt1 in enumerate(keys[:-1]):
        for applicnt2 in keys[i+1:]:
            winner = dict.fromkeys((applicnt1,applicnt2),0)
            for j,res in enumerate(data2):
                win_score = min(((key,res.index(key)) for key in (applicnt1,applicnt2)),key=lambda elem:elem[1])
                winner[win_score[0]] += votes[j]
            results.append(winner)
            aps = sorted(((key,value) for key,value in winner.items()),key=lambda elem:elem[1], reverse=True)
            win_res[aps[0][0]] += 1
            win_res[aps[1][0]] -= 1

    winners = [max([(key,ress) for key, ress in win_res.items()],key=lambda elem:elem[1])]
    for applicant,res in win_res.items():
        if applicant != winners[0][0] and res == winners[0][1]:
            winners.append((applicant,res))

    print("Komplenda:")
    [print(f"({list(d.keys())[0]},{list(d.keys())[1]}) = ({list(d.values())[0]},{list(d.values())[1]})") for d in results]
    [print(f"{applicant} scored {res} votes") for applicant,res in win_res.items()]
    print("Winners ", end="")
    [print(f"{elem[0]}",end="")for elem in winners]
    print(f" scored {winners[0][1]} votes", end="\n\n")
    print()

def relative_majority(appls,vote):
    result = dict.fromkeys(appls,0)
    for i,res in enumerate(vote):
        result[res[0]] += votes[i]

    winners = [max([(alt,res) for alt,res in result.items()], key=lambda elem:elem[1])]

    for alt,res in result.items():
        if alt != winners[0][0] and res == winners[0][1]:
            winners.append((alt,res))

    return winners[0][0]


def parallel_exeption():
    votes1 = data2.copy()
    votes_sub1 = []
    votes2 = data2.copy()
    votes_sub2 = []
    votes3 = data2.copy()
    votes_sub3 = []

    for res in votes1:
        vote = []
        for i, appl in enumerate(res):
            if appl == "a" or appl == "b":
                vote.append(res[i])
        votes_sub1.append(vote)
    for res in votes2:
        vote = []
        for i, appl in enumerate(res):
            if appl == "c" or appl == "d":
                vote.append(res[i])
        votes_sub2.append(vote)

    win = [relative_majority(keys[:-2],votes_sub1),relative_majority(keys[2:],votes_sub2)]

    for res in votes3:
        vote = []
        for i, appl in enumerate(res):
            if appl == win[0] or appl == win[1]:
                vote.append(res[i])
        votes_sub3.append(vote)

    win = relative_majority(win,votes_sub3)

    print("Parallel exception:")
    print(f"applicant {win} wins 2 rounds")


bords_method()
komplenda()
parallel_exeption()