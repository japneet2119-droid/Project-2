2016 BC HOUSING AFFORDABILITY AND RENTAL SUBSIDIES DATA ANALYSIS PROJECT

DESCRIPTION:-

This project surveys housing prices and rental subsidies among the major regions of British Columbia using platforms
like python, panda and matplotlib. The main aim of this project is to analyse the rental trends and compare the 
housing costs among different regions using various data representation models.

The program demonstrates basic concepts in Python graphics, including:

- Plotting data on graphs and charts (matplotlib).
- using functions to modularize code.
- analysis of the data of rent and housing using panda platform.
- plotting the analysed data using data visualization methods like graphs and charts using matplotlib platform.

 CODE OVERVIEW:-
 The project is structured around reusable functions:
 - matplotlib.pyplot -> used to create charts
 - df = pd.read_csv("BC census 2016 data.csv") -> converts the given file into a table format.
 - plt.bar(high_rent["chsa"], high_rent["shelt_rent_30plus_rate"]) -> draws a bar chart (histogram) of the given data.
 - plt.pie(
    avg_region,
    colors=colors,
    explode=explode,
    labels= avg_region.index,
    autopct='%2.2f%%',
    startangle=150,
    shadow=True,
    wedgeprops={'edgecolor': 'red'}

) -> creates a pie chart of the analysed data with the mentioned attributes.

The result of the overall code provides us with a bar chart and a pie chart of the analysed data which helps us to
determine the housing and affordability costs of the regions among British Columbia and helps us to decide 
which region is more costly to reside. 

HOW TO RUN

1. Clone or download this repository.
2. Open the project file Project2_Japneet.py in your python IDE or text editor.
3. Along with the project file, make sure to open the  BC Census 2016 data.csv file in the same folder.
4. Run the program.
5. A window will open showing the bar chart and the pie chart of the data from the CSV file to be analysed.

License

This project is open-source and free to use for educational purposes.



  
