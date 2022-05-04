# flash-card-app
An app that helps you learn common French words. 

## Screenshot

![f1](https://user-images.githubusercontent.com/40911055/166618607-7423a414-f788-42ef-bda0-2bdeed1e41dc.png)
![f2](https://user-images.githubusercontent.com/40911055/166618612-e01966a3-1642-4211-b09d-a1838abcd4a6.png)

# How to play
- The card has a French and English side.
- Once a french word is displayed, you should guess the english translation of that word
- After 3 seconds, the card will flip and the english translation will be shown
- If you mentioned the correct answer, press the ✅ button to continue
- If you did not get it correct, press the ❌ button to continue
- Any word you get correct will be removed from the list as you play on
- The next time you run the app, it will load the remaining words.

## Features

- Saves the words that you did not get correct
- Automatically flips the card after 3 seconds to reveal the translation

## Roadmap

- [ ]  Add pronunciation of words
- [ ]  Customize flip delay
- [ ]  Customize data sets (e.g learn capital cities)
- [ ]  Add an intro screen for instructions
- [ ]  Add scores and high scores

## Dependencies

- Pandas. (https://pypi.org/project/pandas/)
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/StephenKiiyuruNganga/flash-card-app.git
```

Go to the project directory

```bash
  cd flash-card-app
```

Install dependencies

```bash
  pip install pandas
```

Start the program

```bash
  python main.py
```




