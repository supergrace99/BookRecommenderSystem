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
<li><a href="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Data%20Extraction.ipynb"><b>Data Extraction.ipynb</b></a>: Documents the data extraction process, whereby the books.csv dataset and ratings.csv dataset were combined to work with</li>
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
<h4>Effective Data Analysis & Preprocessing</h4>


 


