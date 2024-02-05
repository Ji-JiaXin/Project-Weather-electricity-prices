# Project-Weather-electricity-prices
Welcome to our Python project for “Data Processing in Python” (JEM207) aimed at exploring the relationship between weather conditions, especially air temperature, and electricity consumption and generation in Germany. Given that Germany's energy mix is predominantly comprised of renewables, the weather should be a significant factor influencing electricity supply and demand. We prepared a module that allows users to input temperatures from previous days. The module will analyze historical weather data and identify periods when weather conditions closely resemble the provided input. The user can also set the threshold, which enables him to regulate how strict the similarity between the weather patterns must be (scale of 1-8, the higher the number the less strict the condition -> higher number of similar weather patterns). 

The ultimate goal is to provide the user with information regarding the development of the monitored indicator during the past periods with similar weather conditions. 

Join us on this exciting journey, and let us explore together the impact of weather on electricity flow within the German energy system!

## How does the user interface work?
For your simplicity and comfortability, we have created a simple modern-looking graphical user interface (GUI). You can insert the 7 temperatures in °c, set the threshold, choose the preferred variable you want to examine, and lastly, the method you want to use.
Click on the run button and here the MAGIC happens. You should be provided with a graphical visualization of the relationship between your chosen variable and the temperature development over time. Furthermore, based on your inserted temperatures and the threshold, you can see highlighted periods in the graph which are the periods with similar weather temperature patterns as your inserted values. 
From the graph, you can further conclude, whether your chosen variable has a similar trend to weather temperature. That is pretty cool, right?

## How to run the project on your device?
1. Have installed Git on your device. You can download using the following link: https://git-scm.com/downloads. 

2. Start by cloning the project repository on your machine. Open command prompt or terminal (press the windows button on your keyboard and search for "terminal"/use "command + t" for macOS). Set your desired current working directory using this (replace "file_path" with your path in a similar form as "C:/Users/mypersonal/Desktop..." ):
<pre>
cd file_path
</pre>
Press enter to execute. To clone the repository use the following command and execute.
<pre>
git clone https://github.com/Ji-JiaXin/Project-Weather-electricity-prices.git
</pre>

3. To open the project, go to the file where you cloned the repository (it should be your "file_path" from step two) using the following command for example.
<pre>
cd Project-Weather-electricity-prices
</pre>

4. Install all required libraries that are specified in the "requirements.txt" using the following command. After this step, you should be able to run all the files without any other issues. 
<pre>
pip install -r requirements.txt
</pre>

5. To open the user interface, please run "User_interface.py" using your preferred code editor/runner (for example Virtual Studio Code - https://code.visualstudio.com/download). 

## About the data sources
The data about electricity generation from different sources (offshore wind, onshore wind, photovoltaics, pump storage, other conventional sources, and other renewables) and total electricity consumption are downloaded using API. Using the class DownloadAPI specified in the "Electricity_API_download.py" the user can download data based on his preferences. This class is very powerful as it downloads data from https://smard.de/app based on the multiple parameters that could be specified, such as region (Germany, Austria...) or frequency (quarter-hour, hour, day, week...). Therefore, you are more than welcome to reuse this module in your electricity-related project! The class DownloadAPI was inspired by the GitHub repository (https://github.com/bundesAPI/smard-api). The code was modified to ensure its proper functionality and desired features. 

The weather data is composed of various online sources, as we could not find one reliable free provider that would satisfy our data requirements. Therefore, we merged data from different sources ("Weather_base.xlsx" and "Weather_new.csv") into one final file ("All_weather_data.csv). 

For our analysis, we merged the data about electricity (from API) with the final weather data into one data frame ("final_data.csv"). Everything about the data preparation can be found in one file ("Data_preparation.py").

## Models for finding similar weather patterns
To find similar weather patterns, you can choose from two different methods. Both of them are based on differences between the input temperature values. 

The method "First difference" calculates the first difference of the values and makes a comparison with the first difference of temperature values in the dataset. Using the threshold it filters only those periods when the sum of squared differences falls below the inserted threshold. On the other hand, the second method "Direct sum of squared" directly compares the sum of squared differences between the inut temperature values and the values in the dataset, filtering out only those that fall below the threshhold.   

## Graphics
Based on the previous analysis we provide a graphical visualization for you, as sometimes a nice graphical visualization is worth more than a thousand words. There are two types of graphs you can choose from - either a graph covering the whole period or a set of more detailed subgraphs displaying each yearly development. The output dates from the model for finding similar weather patterns are also incorporated in the graph (highlighted in red).  

## Final words
We tried our best to offer you a module which would provide you with interesting insights on the relationship between weather temperature and your chosen electricity-related variable. However, due to data restrictions and other factors we were not able to ensure the quality of our weather data. Additionaly, we tried to cover all possible errors that may arise by invalid user input, but there might still be some that we have missed. Lastly, we would be delighted for your comments, feedbacks and pull requests that will allow us to make the module work better and smoother! Thank you and have fun!


