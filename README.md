<h1 align='center'>Book Recommender System</h1>

<p align="center">
  <img width="800" height="300" src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/old-books-arranged-on-shelf-royalty-free-image-1572384534.jpg">
</p>

I Built a recommender system for books with collaborative filtering using a data set found via <a href="https://www.kaggle.com/alexanderfrosati/goodbooks-10k-updated">Kaggle</a> that will recommend a total of 20 books to its user based on their past ratings of books on a scale of 1-5.

<h3> Why Did I Build This? </h3>
<p align='justify'>
My decision to build a recommender system for books stemmed from my love of reading books. Over the course of this pandemic, I've had A LOT of time to read, having read a book a week since the start of 2021. In order to feed my reading habits, I've spent hours scowering the internet looking for book recommendations, however I've noticed that these recommendations tend to be based on the genre of the last book I've read, which would be fine should I be interested in reading a similiar book to what I've just read, but rarely do these recommendations take into account the fact that I enjoy books from a variety of different genres.
</p>
</n>
<p align='justify'>
Therefore, I've decided to combine my interest in data science with my love for books in order to build a recommender system that takes into account books that I would like my next recommendation to be based on, regardless of genre, through collaborative filtering.
</p>
</n>
<p align='justify'>
 P.S. I am aware that getting a GoodReads account would probably solve my problem, but I think building this would be way more fun!
</p>

<h3> File Descriptions </h3>
<details>
  <summary>Show/Hide</summary>
<ol>
  <li><a href="https://github.com/supergrace99/BookRecommenderSystem/tree/main/Data"><b>Data</b></a>: Folder contains all datasets created or required for recommender system to work</li>
  <ul>
    <li><b>ratings.csv.zip</b>: Contains ratings of 53434 different users on a variety of diiferent books</li>
    <li><b>books.csv</b>: Has metadata for each book (goodreads IDs, authors, title, average rating, etc.)</li>
    <li><b>DataSet.csv.zip</b>:The final dataset used for model selection, parameter tuning and for the recommender system itself </li>
    <li><b>book_list.csv</b>: Dataset required for the recommender system itself</li>
  </ul>
<li><a href="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Data%20Extraction.ipynb"><b>Data Extraction.ipynb</b></a>: Documents data preprocessing, whereby subsets of the books.csv dataset and ratings.csv dataset were combined to work with</li>
<li><a href="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Data%20Cleaning.ipynb"><b>Data Cleaning.ipynb</b></a>: Contains jupyter notebook documenting the data cleaning process, primarily removing certain pieces of data to avoid memory errors</li>
<li><a href="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Model%20Selection.ipynb"><b>Model Selection.ipynb</b></a>: Models considered for the recommendation system </li>
<li><a href="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Parameter%20Tuning.ipynb"><b>Parameter Tuning.ipynb</b></a>: Documents the manual paramter tuning conducted for model improvement</li>
<li><a href="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Recommender.py"><b>Recommender.py</b></a>: Contains all functions required for user to use the final recommender system</li>
<li><a href="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Interface.ipynb"><b>Interface.ipynb</b></a>: The final recommender system for users</li>
</ol>
</details>
</n>
<h3>Technologies Used</h3>
<details>
  <summary>Show/Hide</summary>
  <ul>
    <li><b>Pandas</b>: software library written for the Python programming language for data manipulation and analysis</li>
    <li><b>Matplotlib</b>: a plotting library for the Python programming language and its numerical mathematics extension NumPy</li>
    <li><b>Seaborn</b>: data visualization library based on matplotlib</li>
    <li><b>Surprise</b>: a Python <b>scikit</b> for building and testing recommender systems</li>
  </ul>
</details>
</n>
<h3>Executive Summary</h3>
<h4>Data Preprocessing </h4>
<p align='justify'>
  In order to build a recommendation system via collaborative filetering, a data set that contains a way of identify a user (user_id), the book they are rating (book_id) and their actual rating (rating) of the book must be created. To do this, the datasets books.csv and ratings.csv were used. While the ratings.csv dataset, contained all relevant information required to build the recommendation system, the books.csv was needed to identify the books from their book id as the dataset contains important information such as the title, authors and language of the book along with their respective book ID (book_id).</p>
  </n>
 <p align='justify'>
  From early data analysis of the book.csv data set, we found that there were books in the ratings.csv file that were not in the English language. As English books made up the vast majority books (89%) as illustrated in the pie chart below and as I was interested in building a recommender system that recommended only English books, books that were not in english were removed from the dataset. This process can be found in Data Extraction.ipynb </p>
<p align='center'>
  <img width=350 height=300 src="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Images/Image%201.png?raw=true">
  <p align='center'>Pie Chart of Book Languages</p>
  </p>
</n>
<p align='justify'>
  At this point the dataset to be used for the recommender system contained 5,916,166 observations, comprising of the ratings of 53424 users on 9814 books. As 5,916,166 observations is relatively large, I had concerns of causing memory errors when fitting models due to limitations of my computers GPU RAM. In order to avoid this issue, I removed a certain portion of users and books from the dataset.</p>
  </n>
<p align='justify'>
  As the accuracy of recommender systems built with collaborative filtering are unable to provide accurate recommendations when users and items have few ratings, I decided to remove users and books with the fewest ratings respectively. The bottom 10% of the frequency at which users rate books have rated less than 82 books while on average, users make 111 ratings. I decided to remove users that have made less than or equal to 80 ratings, which comprises of 5219 of the 53424 (approx 10%) of users. For books however, as there is a large difference in the frequency at which books are rated, as seen in the median number of ratings a book receives being 250 but the most infrequently rated book receiving 8 ratings while the most freqnently rated book receiving 22806 ratings. As such, I have deicided to remove books that have been rated fewer than 100 times, this accounts for 449 of the 9814 books (4.5%). By removing these users and books, I was able to reduce the size of the dataset by 6% to 5,563,131. This process has been documented in Data Cleaning.ipynb.
  </p>
  
<p align='justify'>
  Another thing to note is that I found that there is an inbalance in distribution of ratings, it appeares that most users tend to rate books only when they have left a favourable impression upon them. Ratings 4 and 5 tend to occur at the greatest frequency while a rating of 1 happens rather relatively infrequently. This is seen in the plot below.
  </p>
       
  
  
  
  


 


