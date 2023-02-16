import read_cv
import population
import chart

def country_dict():
    name_country = input("Write the name of the country: ").capitalize()
    #Data
    data = read_cv.read_csv('./data/data.csv')
    country = list(filter(lambda item:item['Country/Territory'] == name_country, data))

    #countries with the largest population
    filt = list(filter(lambda item:float(item['World Population Percentage']) > 2,data))
    percentages = list(map(lambda item:item['World Population Percentage'],filt))
    percentages_country = list(map(lambda item:item['Country/Territory'],filt))
    




    return country[0], name_country, percentages, percentages_country




if __name__ =='__main__':
    #country filter
    country, name, percentages, percentages_country = country_dict()
    #population
    labels, values = population.get_population(country)
    #bar graph
    chart.generate_bar_chart(labels, values, name)
    chart.generate_pie_chart(percentages_country,percentages)


    
    
