import numpy as np
import pandas as pd
import recommendation_functions as rf
import sys # can use sys to take command line arguments

class Recommender():

    def __init__(self):
        '''
        I don't have any required attributes when creating my calss
        '''

    def fit(self, user_item_pth, articles_pth):

        # Load user_item, articles data
        self.df = pd.read_csv(user_item_pth)
        self.df_content = pd.read_csv(articles_pth)
        del self.df['Unnamed: 0']
        del self.df_content['Unnamed: 0']
        
        # Drop duplicates from df_content 
        self.df_content.drop_duplicates(subset='article_id', keep='first', inplace=True)

        # Map the user email to a user_id column and remove the email column
        email_encoded = rf.email_mapper(self.df)
        del self.df['email']
        self.df['user_id'] = email_encoded
        print("email mapping is finished")

        # Create user_item_matrix
        self.user_item = rf.create_user_item_matrix(self.df)
        print("fitting is finished")
    

    def recommend(self, user_id=None, article_id=None, m=10):
        '''
        haha
        '''
        # No arguments of user_id and article_id / New user case
        if  (user_id==None and article_id==None) or (user_id not in self.df['user_id'].unique() and article_id==None) : 
            recs = rf.get_top_article_ids(m, self.df)
            rec_names = rf.get_top_articles(m, self.df)
        
        # Existed user
        elif user_id in self.df['user_id'].unique() and article_id==None:
            recs,rec_names = rf.user_user_recs(user_id, self.user_item, self.df, m=10)
        
    
        # One article given
        elif article_id != None and user_id == None:
            recs, rec_names = rf.make_content_recs(article_id, self.df_content, self.df, m)

        elif user_id != None and article_id !=None:
            print("input only user_id or article_id")
            recs = []
            rec_names =[]
            
        return recs, rec_names

    