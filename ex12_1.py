import requests

def random_joke():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url)

    if response.status_code == 200:
        joke_data = response.json()
        return joke_data.get('value')
    else:
        return None

def main():
    joke = random_joke()

    if joke:
        print("The Chuck Norris Joke is:")
        print(joke)
    else:
        print("Sorry, failed to fetch data.")

if __name__ == "__main__":
    main()
