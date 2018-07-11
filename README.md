# Autocomplete

You're on a website (such as Github!) with a text field which autocompletes usernames as you type. Under the hood, there's an API call which takes in the prefix of a username and then returns all usernames which start with that prefix, lexicographically sorted and truncated at 5 results.

Your task is to use this API call to dump the entire user database, specifically:

Implement the `extract` function in `autocomplete.py`. `extract` should return the whole user database, making calls to `query` under the hood.

Notes:

- Assume all valid usernames are comprised of lowercase ASCII letters (a-z).
- Assume that queries to the API are expensive and should be minimized
