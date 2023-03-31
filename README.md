# Setup Prompt
```
I need you to give me instructions for automating my computer because it is hard for me to use. When I ask you a question you must answer in json format with the following command options:
  "click": [x_pos, y_pos] #Telling me to click on this exact location of the screen
  "type": "what to type" #telling me to type out this on my keyboard
  "enter": "true" #telling me to hit the enter key
  "wait": x #tells you to wait x seconds before executing the commands

I am on windows 10. When asked to open an app make sure to use the start key that is located at [0,1080]. Make sure to open the app by using enter. My computer is 1080p resolution.

Do you understand?
```

```
Here is an example question:
How do I open youtube.com in edge on a windows computer that is 1080p

Here is the example solution:
[  
  {"click": [0, 1080]},
  {"type": "Edge"},
  {"enter": "true"},
  {"type": "youtube.com", "enter", "true"},
]
```

# Prereqs
```python3```
### install deps
```
pip install -r requirements.txt
```