# Project-Weather-electricity-prices
Welcome to our Python project for “Data Processing in Python” (JEM207) aimed at exploring the relationship between weather conditions, especially air temperature, and electricity consumption and generation in Germany. Given that Germany's energy mix is predominantly comprised of renewables, weather should be a significant factor influencing electricity suplly and demand. We prepared a module that allows users to input temperatures from previous days. The module will analyze historical weather data and identify timeperiods when weather conditions closely resemble the provided input. The user can also set the threshold setting the allowance for consideration of past time periods as similar, in the matter of weather situation.

The ultimate goal is to provide the user with information regarding the development of the monitored indicator during the past periods with similar weather conditions. 

Join us on this exciting journey, and let us explore together the impact of weather on electricity flow within the German energy system!

## How does the user interface work?
For your simplicity and comfortability, we have created a simple modern looking graphical user interface (GUI). You can simply insert the 7 temperatures in °c, set the treshhold, choose prefered variable you want to examine and lastly, the method you want to use.
Click on the run button and the here the MAGIC happens. You should be provided with a graphical visualisation of the relationship between your chosen variable and the temperature development over the time. Futhermore, based on your inserted temperatures and the treshhold, you can see highlighted periods in the graph which are the periods with similar weather temperature pattern as your inserted values. 
From the graph you can further conclude, whether your chosen variable has similar trend as weather temperature. That is pretty cool, right?

## How to run the project on your device?
1. Have installed Git on your device. You can downloaded using following link: https://git-scm.com/downloads. 

2. Start by cloning the project repository on your machine. Open command prompt or terminal (press windows button on your keyboard and search for "terminal"/use "command + t" for macOS). Set your desired current working directory using this (replace "file_path" with your path in the similar form as "C:/Users/mypersonal/Desktop..." ):
<pre>
cd file_path
</pre>
Press enter to execute. To clone repository simply use following command and execute.
<pre>
git clone https://github.com/Ji-JiaXin/Project-Weather-electricity-prices.git
</pre>

3. To open the project, go to the file where you cloned the repository (it should be your "file_path" from step two) using the following command for example.
<pre>
cd Project-Weather-electricity-prices
</pre>

4. Install all required libraries that are specified in the "requirements.txt" using following command. After this step you should be able to run all the files without any other issues. 
<pre>
pip install -r requirements.txt
</pre>

5. To open the user interface, please run "User_interface.py" using your prefered code editor/runner (for example Virtual Studio Code - https://code.visualstudio.com/download). 

## About the data sources
The data about electricity generation from different sources (offshore wind, onshore wind, photovoltaics, pump storage, other conventional sources, other renewables) and total electricity consumption are downloaded using API. Using the class DownloadAPI specified in the "Electricity_API_download.py" the user can download data based on his preferences. This class is very powerfull as it downloads data from https://smard.de/app based on the multiple parameters that could be specified, such as region (Germany, Austria...) or frequency (quarterhour, hour, day, week...).

The weather data is composed from various online sources, as we were not able to find one reliable free provider, which would satisfy our data requirements. Therefore, we merged data from different sources ("Weather_base.xlsx" and "Weather_new.csv") into one final file ("All_weather_data.csv). 

For our analysis we merged the data about electricity (from API) with the final weather data into one dataframe ("final_data.csv"). Everything about the data preparation can be found in one file ("data_preparation.csv").

## Models for finding similar weather patterns



## Graphics
Based on the previous analysis we provide a graphical visualisation for you, as sometimes a nice graphical visualisation is worth more than tausend words. There are two types of graphs you can choose from - either a graph covering the whole period or a set of more detailed subgraphs displaying each yearly development. The output dates from the model for finding similar weather patterns are also incorporated in the graph (highlighted in red).  


