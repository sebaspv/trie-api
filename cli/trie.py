import fire
import requests

def available():
    available_request = requests.get('http://trie-cli.deta.dev/trie/available')
    available_words = available_request.json()['available']
    if available_words == []:
        return 'There are no words in the Trie.'
    return 'The words inside the Trie are: ' + ', '.join(available_words)
    
def add(word):
    requests.get(f'http://trie-cli.deta.dev/trie/add/{word}')
    return f"The word {word} has been added."

def prefix(prefix):
    prefix_request = requests.get(f'http://trie-cli.deta.dev/trie/prefix/{prefix}')
    prefix_words = prefix_request.json()['words']
    if prefix_words == []:
        return f'There are no words that start with {prefix}.'
    return f'The words that start with {prefix} are: ' + ', '.join(prefix_words)

def remove(word):
    requests.get(f'http://trie-cli.deta.dev/trie/delete/{word}')
    return f"The word {word} has been removed."

def display():
    trie_request = requests.get(f'http://trie-cli.deta.dev/trie')
    trie = trie_request.json()['trie']
    return f"Right now, the trie looks like this: \n{str(trie)}"

if __name__ == "__main__":
    fire.Fire()