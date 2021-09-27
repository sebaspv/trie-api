<h1 align = "center">Here are all of the CLI commands!</h1>

### Adding and removing words (add/remove)
Adding and removing words from the Trie is really simple. You only need the word and the command `(add/remove)`:
```bash
# add the word "hello" to the Trie
python3 trie.py add hello
# remove the word "hello" from the Trie
python3 trie.py remove hello
```
### See the Trie's words (available)
You can also see the words stored in the Trie with the `available` command.
```bash
# see the available words
python3 trie.py available
```
### See the available words for a given prefix (prefix)
Autocompletion is one of the main reasons you want to use a Trie. In this API, you can see the possible autocompletion words
given a certain prefix with the `prefix` command.
```bash
# add the "hello" word to the Trie
python3 trie.py add hello
# see the possible words given the "he" prefix
python3 trie.py prefix he # output: The words that start with he are: hello
```
### Verify if a word is stored in the Trie (verify)
You can also verify if a specific word is already in the Trie. In order to do this, you only need to use the `verify` command with the 
word that you want to verify.
```bash
# verify if the word "hello" is in the Trie
python3 trie.py verify hello
```
### Full Trie display
You can also display the Trie as a python dictionary to observe all of the words stored in the root. You can do this with the `display`
command.
```bash
# display the trie as a dictionary
python3 trie.py display
```