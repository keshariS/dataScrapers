Please see below:

This is a flowchart of how the project was done:

<img src="https://github.com/keshariS/dataScrapers/blob/main/allScraper_Twitter/tw.png" width="240">

The use of every python file/python notebook is mentioned in the first line as a comment.

# Topic Modelling iterations

1. iter1_preprocess_model_save.ipynb contains the first iteration of topic modelling which automatically loads the data and runs some preprocessing
when run from the OCI instance. (Setting up and accessing the OCI instance and the data it contains can be found in the dataScrapers/README.md file)

2. Similarly iter2_prepro_eng_esp_model.ipynb contains the 2nd iteration of topic modelling with language detectino and geolocation code added.

3. iter3_4_enesTopicModel_removedTopics.ipynb contains the 3rd and 4th iteration with removal of irrelevant keywords.


# Folders:

<h1 style="font-size:30px;">classifier/</h1> contains data used by Prof. Dobbs in their paper. Can be used to replicate results (not completed yet, but the paper pdf is included)

<h1 style="font-size:30px;">data_16k_tweets/</h1> contains the first iteration done in twitter scraping before the spritzer stream for the VAMoS project (we had scraped 16k tweets for the hashtags)

<h1 style="font-size:30px;">misc_codes/</h1> contains python files for scraping data using the twarc 2 API

<h1 style="font-size:30px;">spritzer2categories/</h1> contains code for querying the 465M spritzer stream data aand convert into categories as needed for the VAMoS project

<h1 style="font-size:30px;">topicModels/</h1> contains the topic modeling results per iteration

