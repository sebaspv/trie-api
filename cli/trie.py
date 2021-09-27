import fire
import requests

def available():
    available_request = requests.get('http://127.0.0.1:5000/trie/available')
    available_words = available_request.json()['available']
    if available_words == []:
        return 'There are no words available.'
    return 'The available words are: ' + ', '.join(available_words)
def add(word):
    return f"The word {word} has been added."

def remove(word):
    return f"The word {word} has been removed."

if __name__ == "__main__":
    fire.Fire()