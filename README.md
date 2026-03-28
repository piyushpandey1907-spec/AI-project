## vityarthi project 

#  AI Sentiment Analyzer

Ever wondered how your text *feels*?  
This simple Python project analyzes your input and tells whether it is **Positive 🟢, Negative 🔴, or Neutral 🟡** — just like a mini AI assistant.

---

## Features

-  Real-time sentiment analysis  
-  Works well with chat and social media text  
-  Fast and lightweight  
-  Emoji-based output for easy understanding  
-  Continuous input until you exit  

---

##  How It Works

This project uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** from NLTK.

- It calculates a **compound score** between `-1` and `+1`
- Based on the score:
  - `>= 0.05` →   POSITIVE  
  - `<= -0.05` →   NEGATIVE  
  - Otherwise →  NEUTRAL  

---

##  Requirements

Install the required libraries using:

```bash
pip install pandas nltk


==================================================
AI SENTIMENT ANALYZER (Type 'exit' to stop)
==================================================

 Enter text to analyze: I love this project!

--------------------------------------------------
Result  :  POSITIVE
Score   : 0.6369 (Range: -1 to 1)
--------------------------------------------------
