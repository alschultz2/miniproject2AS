# INF601 - Advanced Programming in Python
# Adam Schultz
# Mini Project #2

# (5/5 points) Initial comments with your name, class and project at the top of your .py file. #Done

# (5/5 points) Proper import of packages used. #Done

# Imported the necessary packages
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc. #Done
        # Think of some question you would like to solve such as:
        # "How many homes in the US have access to 100Mbps Internet or more?"
        # "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
        # Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data. #Done

#Get the data in from the csv file
data = pd.read_csv('All Countries.csv')
# Get a small sample of the data so it will fit nicer on a plot
MainData = data.head(10)
# Print out the data points so the user can see them easier
print(MainData)
# calculate out the average land area for refrence
AverageArea = data['land_area'].mean()
print(AverageArea)

try:
    #Create the charts folder
    Path('charts').mkdir()
except FileExistsError:
    pass

# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.

# Plot the land area for the first 10
plt.bar(MainData['country'], MainData['land_area'])
plt.title('Land Area for first 10 Countries')
# Set up the x and y axis
plt.xlabel('country')
plt.ylabel('Land Area')
# Rotate the names so they can be read
plt.xticks(rotation=45)
# Save the plot
savefile = "charts/" + "Land Area.png"
plt.savefig(savefile)
# Actually show the graph
plt.show()



plt.bar(MainData['country'], MainData['agricultural_land'])
plt.title('Agricultural land Area for first 10 Countries')
plt.xlabel('country')
plt.ylabel('Agricultural Land Area')
plt.xticks(rotation=45)
savefile = "charts/" + "Agricultural Land Area.png"
plt.savefig(savefile)
# Actually show the graph
plt.show()

# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.



# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often! #Done
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt. #Done
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations. #Done


