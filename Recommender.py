#This file will contain all the functions I want to use for the user interface :)


import pandas as pd
import numpy as np

#Prepare data for models
from surprise import Dataset, Reader

#Seperate data into train and test set
from surprise.model_selection.split import train_test_split




#Fucntion to search Book_id of books required to input users data
def book_search(book_list):
    books_up = book_list.apply(lambda x: x.astype(str).str.upper())
    print("Do you have the title of the book? Type T if true!")
    print("T / F ?")
    input1 = input()
    if input1 == "T":
        print("What is the title of this author?")
        title = input()
        title = title.upper()
        dataframe = books_up[books_up['title'].astype(str).str.contains(title)]
        dataframe = dataframe.reset_index(drop=True, inplace=False)
    else:
        print("Do you know the author of this book? ")
        author = input()
        author = author.upper()
        dataframe = books_up[books_up['authors'].astype(str).str.contains(author)]
        dataframe = dataframe.reset_index(drop=True, inplace=False)
    
    return dataframe



#Function to input users data
def your_profile(books, profile): #dataframe is book_list

    lists = []

    userid = 106058 # unique user id (this was selected arbitrarily)
    lists.append(userid)

    print("Please input the book id of the book to be rated\n")
    bookid = input()
    bookid = int(bookid)
    lists.append(bookid)

    print("Please rate the book on a scale of 1-5\n")
    rating = input() #Please stay within scale of 1-5
    rating = int(rating)
    while rating < 0 or rating > 5:
        print("Sorry, please make a rating within the range of 1-5\n")
        rating = input()
        rating = int(rating)
    lists.append(rating)   

    print("This is the book that you are rating: ")
    print(books.loc[books["book_id"]==bookid, 'title'].item())
    print("This is the rating you gave the book: " + str(rating))
    
    profile.append(lists)

    print("\nShould this be incorrect please use the delete function! \n")
    print("If you have more books to add, re-run this function")




#Should the last input of user be incorrect, run this function to remove the last input
def clear_last(profile):
    del profile[-1]




#Run this function to clear all inputs 
def clear_all(profile):
    profile.clear()





#This function will recommend 20 books based on users past preferences
def recommender(profile, dataframe, book_list, algorithm):
    data = dataframe.append(pd.DataFrame(profile, columns=["user_id", "book_id", "rating"]), ignore_index=True)

    reader = Reader(rating_scale=(1,5))
    data_read = Dataset.load_from_df(data, reader)
    data_train = data_read.build_full_trainset()

    algorithm.fit(data_train)

    list_books = list(set(book_list['book_id']))

    book_title = []
    author = []
    rating_est = []

    for i in list_books:
        prediction = algorithm.predict(106058, i)
        rating_est.append(prediction.est)
        book_title.append(book_list.loc[book_list["book_id"]== i, "title"].item())
        author.append(book_list.loc[book_list["book_id"]==i, 'authors'].item())

    recommendations = pd.DataFrame([book_title, author, rating_est])
    recommendations = recommendations.transpose()
    recommendations.columns = ["Title", "Authors", "Est_Rating"]

    return recommendations.sort_values(by=["Est_Rating"], ascending=False).head(n=20)




#Show user their ratings of books and the title of the book
def profile_show(profile, book_list):

    book_name = []
    book_author = []
    rating = []

    for i in profile:
        book_name.append(book_list.loc[book_list["book_id"]== i[1], "title"].item())
        book_author.append(book_list.loc[book_list["book_id"]== i[1], "authors"].item())
        rating.append(i[2])
    
    profile_df = pd.DataFrame([book_name,book_author,rating])
    profile_df = profile_df.transpose()
    profile_df.columns = ["Title", "Authors", "Rating"]

    return profile_df

    
    
    