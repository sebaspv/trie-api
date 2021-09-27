from Tree import Trie
from fastapi import FastAPI
import uvicorn

app = FastAPI()
tree = Trie()

@app.get("/trie")
async def root():
    """Displays the Trie's root as a dictionary"""
    return tree.display_trie()

@app.get("/trie/available")
async def keywords():
    """Displays a list of all available words"""
    available = tree.get_words()
    return {"available":available}

@app.get("/trie/prefix/{prefix}")
async def prefix(prefix):
    """Get words with specified prefix"""
    words = tree.get_prefixes(prefix)
    return {"words":words}

@app.get("/trie/add/{added_word}")
async def add(added_word):
    tree.add_word(added_word)
    return {"available":tree.get_words()}

@app.get("/trie/delete/{deleted_word}")
async def remove(deleted_word):
    tree.remove_word(deleted_word)
    return {"available":tree.get_words()}

@app.get("/trie/verify/{word}")
async def verify(word):
    return {"status": tree.verify_word(word)}


if __name__ == "__main__":
    uvicorn.run(app, port = 5000)