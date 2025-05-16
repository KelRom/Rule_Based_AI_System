# Rule Based AI Project
---
## Course: CAP320-O

## Part 1: Initial Project Ideas

### 1. Project Idea 1: File Organizer AI
- **Description:** Automatically move files from a target folder (e.g., Downloads) into categorized folders (e.g., Documents, Images, Videos) based on predefined rules.
- **Rule-Based Approach:**  
  -**IF** extension ends with jpg, jpeg, png, move to images folder
  -**IF** extension ends with pdf, docx, txt move to documents folder
  -**IF** extension ends with mp4, mkv, avi move to videos folder
  -**IF** extension ends with zip, rar move to archives folder

### 2. Project Idea 2: Game AI for Turn-Based Strategy
- **Description:** A simple AI that plays a deterministic board game using rules.
- **Rule-Based Approach:**  
  -**IF-THEN** rules to evaluate board positions.
  -Prioritized rule lists (e.g., block opponent > win move > center control).
  -Simple rule-engine implementation for decision-making.

### 3. Project Idea 3: Animal or Object Identifier
- **Description:** This system works like a game of 20 Questions: it asks the user yes/no questions and uses a decision tree to identify an animal or object based on their answers.
- **Rule-Based Approach:**  
  -Ask a sequence of questions.
  -Store user responses.
  -Apply rules (IF-THEN logic).
  -Provide an answer (e.g., “It is a Cat”).
  

### **Chosen Idea:** Animal or Object Identifier 
**Justification:** I chose this project because it is fun to me and has the ablity for users to add new entries if I want to use some basic learning, and I could use either the command line or tkinter for a GUI. So I improve it and use it for more learning in the future.

---

## Part 2: Rules/Logic for the Chosen System

The **Animal or Object Identifier** system will follow these rules:

### Rules
Q1: Does it have feathers?
├── Yes → Q2: Can it fly?
│     ├── Yes → Q3: Does it chirp?
│     │     ├── Yes → It is a Sparrow.
│     │     └── No → It is a Hawk.
│     └── No → It is a Penguin.
└── No → Q4: Does it have fur?
      ├── Yes → Q5: Does it bark?
      │     ├── Yes → It is a Dog.
      │     └── No → Q6: Does it meow?
      │           ├── Yes → It is a Cat.
      │           └── No → It is a Bear.
      └── No → Q7: Does it have scales?
            ├── Yes → Q8: Does it live in water?
            │     ├── Yes → It is a Fish.
            │     └── No → It is a Lizard.
            └── No → Q9: Does it have smooth skin and live near water?
                  ├── Yes → It is a Frog.
                  └── No → It is a Snake.

---

## Part 3: Rules/Logic for the Chosen System

Sample input and output: 

1. 
  __Does it have feathers (yes/no): no__
  __Does it have fur (yes/no): yes__
  __Does it bark (yes/no): no__
  __Does it meow (yes/no): no__
  **It is a Bear.**

2. 
  __Does it have feathers (yes/no): yes__
  __Can it fly (yes/no): yes__
  __Does it chirp (yes/no): no__
  **It is a Hawk.**

3. 
  __Does it have feathers (yes/no): no__
  __Does it have fur (yes/no): no__
  __Does it have scales (yes/no): no__
  __Does it have smooth skin and live near water (yes/no): no__
  **It is a Snake.**

---

## Part 4: Reflection

### Project Overview:
This project involved designing a practical, rule-based system to recommend recipes based on user inputs. The system uses logical conditions (e.g., exact and partial matches) to evaluate user-provided ingredients against recipes in the dataset.

### Challenges:
- **Handling Partial Matches:**  
  Deciding on a threshold (75%) that balances flexibility with accuracy was challenging.
- **Common Ingredients:**  
  Ensuring common ingredients like salt and water don’t skew the results. I resolved this by excluding them from the missing ingredient list.

