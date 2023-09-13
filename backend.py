import requests

APIkey = "b43d205a205ca641078f92ad86543ea6"
def get_data(place, days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_value = 8 * days
    filtered_data = filtered_data[:nr_value]
    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
    return(filtered_data)

if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3, kind='Sky'))
