class CheckBid:

    def check(self, bidders):
        highest_bid = 0
        for name in bidders:
            if bidders[name] > highest_bid:
                highest_bidder = name
                highest_bid = bidders[name]
        win_dict = {highest_bidder: highest_bid}
        for name in win_dict:
            return f"The winner is {name} with a bid of ${win_dict[name]}"