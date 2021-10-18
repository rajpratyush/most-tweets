import operator

class Twitter:
    
    def __init__(self):
        self.user_tweets_count: list[dict] = []                                 #initialising list that store user tweet count
        self.tweet_users_map: list[dict] = []                                   #initialising list that store user tweet map
        
    def tweets(self):
        tweets_count = int(input(''))
        tweet_user_map: dict[str, str] = {}
        user_tweet_count: dict[str, str] = {}
        while (tweets_count > 0):
            try:
                tweet=(input(''))
                user,id=tweet.split(" ")
                if tweet_user_map.get(id,'')=='':                                   #check tweet already id exist or not
                    tweet_user_map[id]=user                                         #mapping tweet to corresponding user
                    user_tweet_count[user]=user_tweet_count.setdefault(user,0)+1    #increasing user tweet count
                tweets_count=tweets_count-1
            except Exception:
                print('Invalid Input. Try again')

        self.user_tweets_count.append(user_tweet_count)         #adding current user for the particular iteration 
        self.tweet_users_map.append(tweet_user_map)             #adding tweet user mapping particular iteration
    
    def evalTweets(self):
        for item in self.user_tweets_count:
            sort = {key: val for key, val in sorted(item.items(), key = lambda ele: ele[1],reverse = True)}     #Sorting user_tweets_count current iteration data based on value
            maxVal=list(sort.values())[0]                                                                       #Storing the max value
            ret_val: dict[str, str] = {}
            for key,val in sort.items():                                                                        #Loop to filter tweets
                if maxVal==val:                                                                                 #Finding tweets that match max value
                   ret_val[key]=val
            sorted_ret_val={key: val for key, val in sorted(ret_val.items(), key = lambda ele: ele[0])}         #Sorting max value tweets based on name
            for key,val in sorted_ret_val.items():
                print(key,val)                                                                                  #output in each seperate line
    
    def main(self):
        intial_count = int(input(''))
        while (intial_count > 0):
            try:
                self.tweets()
                intial_count=intial_count-1
            except Exception:
                print('Invalid Input. Try again')
        print()
        self.evalTweets()

    
twitter=Twitter()
twitter.main()
