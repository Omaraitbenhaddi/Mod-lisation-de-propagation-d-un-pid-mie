





from pandas import *
from numpy import *
from matplotlib.pyplot import *
# Importer les données de Universite Johns Hopkins
deces = read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmer = read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
retabli = read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
etat =read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')
etat.columns
# Afficher les statistiques au niveau monde
global_data=etat.copy().drop(['Country_Region','Last_Update', 'Lat', 'Long_','Active', 'Incident_Rate', 'People_Tested',
       'People_Hospitalized', 'Mortality_Rate', 'UID', 'ISO3'],axis=1)
global_synthese=DataFrame(global_data.sum()).transpose()
global_synthese


# Afficher les statistiques au niveau Maroc


country=['Morocco']
Morocco_data=etat.copy().drop(['Active', 'Incident_Rate','People_Hospitalized',
                    'Incident_Rate', 'Mortality_Rate', 'UID', 'ISO3','Last_Update', 'Lat', 'Long_', 'People_Tested'],axis=1)
Morocco_data[Morocco_data['Country_Region'].isin(country)].transpose()