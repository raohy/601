# Twitter API
In this part, I used Twitter api to get tweets of public feelings about the weather in Boston in the past week. I use the key words to limit the tweets I get to boston, weather and ask it not to contain #boston tag to remove weather forecasts, pictures, links, and video. The query was encoded by the http protocal. Finally I get a total of 144 tweets Information, as shown in data.csv. And save the obtained information into txt and csv files for subsequent Google nlp processing. It is worth mentioning that error handling has been done for tweet messages when the API is not responding and encounting verification failures. If an error occurs, it will not affect the normal operation of the program. The source code is stored in the twitter_api.py file.

In test_twitter_api, I write two small tests for the connection and the retrieve part of the code. If the token is not working or the retrieve data is empty, the test would not pass. The result shows in the twitter_test.png. 
# Google NLP API
Through Google’s AutoML Natural Language service, I used the twitter information to train a network about the citizens’ emotional towards the weather. In this process, I created an emotion recognition model, and set three recognition levels: 0 means unhappiness, 1 means neutral, and 2 means pleasure. I marked the 144 tweets, of which 40 were unhappy, 77 were neutral, and 51 were pleasure and stored the established data set into the model for training. The final training results are shown below.

![](/images/precise.png)![](/images/score.png)
This is the prediction of the validation set, a total of 13 pictures. It can be found that the accuracy rate and recall rate are both maintained at about 60%, which can  recognized most of the emotions but are still not accurate enough. The main reason is that the training samples are not large enough to form a stable model which suggest us that big dataset is indispensable.

![](/images/matrix.png)
The above figure reflects the specific prediction situation of the verification set. It can be found that for neutral and positive emotional information, the prediction accuracy rate given by the model is relatively high, while the negative one is not satisfactory. It may be related to the small sample size of negative samples. But overall the result is quite satisfactory.

In the gnlp.py file, I listed a way from google to access my model and can import samples to get the training results. Unfortunately, it requires a secret key to verify.
