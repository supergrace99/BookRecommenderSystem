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
Therefore, I've decided to combine my interest in data science with my love for books in order to build a recommender system that takes into account all books that I would like my next recommendation to be based on, regardless of genre, through collaborative filtering.
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
  From early data analysis of the book.csv data set, I found that there were books in the ratings.csv file that was not in the English language. As English books made up the vast majority of books (89%) as illustrated in the pie chart below and as I was interested in building a recommender system that recommended only English books, books that were not in English were removed from the dataset. This process can be found in Data Extraction.ipynb </p>
<p align='center'>
  <img width=350 height=300 src="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Images/Image%201.png?raw=true">
  <p align='center'>Pie Chart of Book Languages</p>
  </p>
</n>
<p align='justify'>
  At this point, the dataset to be used for the recommender system contained 5,916,166 observations, comprising of the ratings of 53424 users on 9814 books. As 5,916,166 observations is relatively large, I had concerns of memory errors when fitting models due to limitations of my computers GPU RAM. In order to avoid this issue, I removed a certain portion of users and books from the dataset.</p>
  </n>
<p align='justify'>
  As the accuracy of recommender systems built with collaborative filtering are unable to provide accurate recommendations when users and items have few ratings, I decided to remove users and books with the fewest ratings respectively. The bottom 10% of the frequency at which users rate books is less than 82 books while on average, users make 111 ratings. I decided to remove users that have made less than or equal to 80 ratings, this comprises of 5219 of the 53424 (approx 10%) of users. For books however, as there is a large difference in the frequency at which books are rated, as seen in the median number of ratings a book receives being 250 in contrast to the most infrequently rated book receiving 8 ratings and the most freqnently rated book having 22806 ratings. As such, I have deicided to remove books that have been rated fewer than 100 times, this accounts for 449 of the 9814 books (4.5%). By removing these users and books, I was able to reduce the size of the dataset by 6% to 5,563,131. This process has been documented in Data Cleaning.ipynb.
  </p>
  
<p align='justify'>
  Another thing to note is that I found that there is an inbalance in distribution of ratings, it appeares that most users tend to rate books only when they have left a favourable impression upon them. Ratings 4 and 5 tend to occur at the greatest frequency while a rating of 1 happens rather relatively infrequently. This is seen in the plot below.
  </p>
  </n>
  <p align='center'>
  <img width=350 height=300 src="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Images/Image%202.png?raw=true">
  <p align='center'>Distribution of Ratings</p>
  </p>
</n>
<h4>Model Selection </h4>
<p align='justify'>
  Due to hardware limitations, I was unable to perform the more accurate cross validation for model selection and instead split the data (DataSet.csv) into a training set (80% of data) and test set (20% of data). The training set was fitted to different models while the accuracy of each model was tested using Root Mean Square Errors (RMSE) of the fitted models on the test set, the models were compared to a baseline model which makes estimations of user ratings based on the overall average ratings made in the training set plus the bias of the user the estimation is being made for and the bias of the item to be predicted. The model that was deemed to have the lowest RMSE would be chosen as the most appropriate model for the data set.
  </p>
  </n>
<p align='justify'>
  For the recommender system, I considered both memory based and model based approaches. For the memory based approach I considered 4 types of KNN algorithms, these algorithms were used to calculate the similarities between books based on users ratings in the training set which was then used as weights to predict the rating a user would give an item in the test set. The similiarities between books was used as weights as opposed to the similarities between users in order to avoid the issue of dimensionality as there were fewer books (9365) than users (48205). 
  </p>
<p align='justify'>
  For the model based approach, I considered 2 kinds of matrix factorisation based algorithms. These algorithms reduce and compress the large matrix that comprises of the user and book data, the reduction and compression is desirable as the matrix I have is relatively sparse as users are unlikely to have rated all 9365 books. In these instances, reducing dimensionality tends to improve the performance of algorithms.
  </p>
<h4>Models Considered</h4>
  <ul>
    <li>Memory Based</li>
    </n>
    <ul>
      <li>KNNBasic</li>
      <li>KNNWithMeans</li>
      <li>KNNWithZScore</li>
      <li>KNNBaseline</li>  
    </ul>
  </n>
    <li>Model Based</li>
    <ul>
      <li>SVD</li>
      <li>NMF</li>
    </ul>
  </ul>
  <p align='justify'>Please read the Surprise documentation for each approach <a href="https://surprise.readthedocs.io/en/stable/prediction_algorithms_package.html">HERE</a> </p>
  </n>
<p align="justify"> The results of my model selection process can be found in the table below. I noted that the model that recorded the lowest RMSE was the singular value decompostion model (SVD). As a result of the pivotal role the SVD algorithm played in the popular Netflix Prize, this result did not surprise me too much particularly due to the sparsity of my matrix as mentioned earlier. In comparison to the baseline, there appears to be a 3% improvement in estimations of ratings when the SVD is used. While 3% may not seem like much, it should be noted that in past recorded attempts to build recommender systems, such as during the Netflix Prize, an 8.43% improvement in the recommender system, which required more than 2000 hours of work in order to come up with the final combination of 107 algorithms, was enough to secure the team the first Progress Prize. (<a href="https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429">source</a>). Hence, I would consider a 3% improvement from the baseline model quite impressive seeing as only a single SVD algorithm is used. This process was recorded in "Model Selecion.ipynb".

<p align='center'>
  <img width=350 height=300 src="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Images/Model%20Selection.png?raw=true">
  <p align='center'>Model Selection Results</p>
  </p>
</p>
<h4>Hyperparameter Tuning</h4>  
<p align='justify'>Once again due to harware limitations and time, I decided that I would conduct manual hyperparameter tuning in order to better improve my model. While using automated hyperparameter tuning methods such as random search or Optuna would have likely resulted in even greater improvements to the models accuracy, the time taken to conduct these methods not only took far too long but often times resulted in memory errors. </p>
</n>
<p align='justify'>For my model, I decided to tune the number of iterations of SGD (stochastic gradient descent), the learning rate and the regularization term of the model. For each of these hyperparameters, I considered a range of values that was centered aroung the default value of these hyperparameters, I then plotted RMSE of the SVD model when the hyperparameter was set to each value to decide the best value of each hyperparameter. </p>
</n>
<p align='justify'> When considering the optimal number of iterations on the SGD procedure (n_epochs) the model should take, the default number of iterations, 20 was found to produce the best results as seen in the plot below, where the RMSE of the model is at its lowest when n_epochs is 20</p>
</n>
<p align='center'>
  <img width=390 heigh=390 src="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Images/Image%203.png?raw=true">
</p>
<p align='justify'> The learning rate (lr_all) chosen was 0.006. Despite the default learning rate of 0.005 having a lower RMSE, I found that 0.006 was at the elbow of the plot as seen below. The smaller the learning rate of the model, the the smaller the steps taken by the model at each SGD iteration. As such, smaller learning rates would take a longer time to train. By selecting 0.006 which is at the elbow of the plot, I believe I am best able to balance the need for the model to train at a reasoanble pace while mainitaing the accuracy of the model. Should I have selected 0.005, I believe that the benefit of the slightly better accuracy of the model would have been offset by the far longer time it would take to train the model.</p>
</n>
<p align='center'>
  <img width=390 heigh=390 src="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Images/Image%204.png?raw=true">
</p>
<p align='justify'> 0.03 was chosen for the regularization term (reg_all) as it results in the lowest RMSE as seen in the plot below. The regularization term is used to prevent overfitting in the model, should the term be too large it results in underfitting and should it be too small it will not be able to prevent overfitting of the model.
  <p align='center'>
  <img width=390 heigh=390 src="https://github.com/supergrace99/BookRecommenderSystem/blob/main/Images/Image%205.png?raw=true">
</p>
<p align='justify'> Through parameter tuning, I was able to further improve the model such that it was now better than the baseline model by 4% from the initial 3% prior to parameter tuning. Once again, as colllaboraive filtering only uses users rating to make predictions and that historically building recommender systems do not show that great of an improvement from baseline models, a 1% improvement is condisdered good improvement to the model.


 


