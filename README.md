# Wiki Game Player
This project is a solver for the [Wiki Game](https://www.thewikigame.com/group), built with OpenAI's embeddings. The objective of the wiki game is to navigate to a selected page in Wikipedia from a random page, 
using only internal wikipedia links. The wiki game is rather well known as it is often used as an example
to show the interrelatedness of different concepts. It's the internet version of "6 degrees of separation".
The game is a test of trivia knowledge and creativity in finding links between topics.

## Algorithm
The inputs are two links to wikipedia pages. The output is a path between the two pages. 
My algorithm queries OpenAI's embeddings API to generate an embedding for the start and end pages.
It then scrapes the start page for internal wiki links. For each link, it computes an embedding of the text
in the link, then selects the link that is closest to the end page.  
**Q: Wouldn't breadth first search be more effective?**  
A: Yes. In fact, there is already [Six Degrees Of Wikipedia](https://www.sixdegreesofwikipedia.com/), which will certainly find better solutions. The purpose of this project is not to find the best path, but to demonstrate how embeddings represent connections between words.  

## Set Up
This project is for a Django API. For just the code, checkout the repository, then copy /wikisite/wiki_game_api/game_src. You may want to simplify the import statements to allow running code within the same directory. 
You will also need to create a paid OpenAI account and get an API key. Run
    export OPENAI_API_KEY={YOUR KEY}
Also run
    pip install numpy, openai, beautifulsoup4
You can directly run wiki_game.py. Input links should be formatted /wiki/{Topic}

## Interesting Discoveries
- The solver is very bad at fictional characters. Try finding a route to Darth Vader or Spock. This indicates the embedding model may not be sufficiently trained on them.
- The solver also has difficulty with names in general because it tries to find people with similar names. An attempt to find "Douglas Adams" will often go through "John Adams" and other people with Adams surnames. This indicates that the embedding still preserves a lot of information about the individual words in its input, even though the combined term may mean something very different.
- The algorithm tends to select specific topics that are close to the person. For example, if going to Barack Obama, it may find other presidents until it hits Obama. This is inefficient since it is better to get to a list of presidents, I have thus prioritized list articles to speed up the search.

## Potential Improvements
It will be more efficient if the algorithm selects topics with many links. I could train a neural network to predict topics that have a lot of wikipedia links and integrate that into the solution. 
