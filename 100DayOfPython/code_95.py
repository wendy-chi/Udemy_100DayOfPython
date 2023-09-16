
#HINT: You can call clear() to clear the output in the console.



record_dic = {}

another_bid_exist = True

def find_highest_score(bidding_record):
    highest_score = 0
    bidder = ""
    winner = {}
    for bidder in bidding_record:
        bidding_amount = int(bidding_record[bidder])
        if bidding_amount > highest_score:
            highest_score = bidding_amount
    winner[bidder] = highest_score
    print(winner)
    print(f"the winner is {bidder} with bidding ${highest_score}")

while another_bid_exist:
    name = input("Please enter the name: \n")
    bid = input("please enter the bid: \n")
    more_bid = input("Any other bidder? yes or no.").lower()
    if more_bid == "yes":
        record_dic[name] = bid

    else:
        record_dic[name] = bid
        another_bid_exist = False

print(record_dic)
find_highest_score(record_dic)
# max[name] = record_dic[name]
# max[bid] = max(record_dic[bid])

