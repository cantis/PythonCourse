def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) //2
    print (" " * left_margin, text)


def center_text(text):
    left_margin = (80 - len(text)) //2
    print (" " * left_margin, text)


#call the function
center_text("span and eggs")
center_text("spam, spam and eggs")
center_text("spam, spam, spam and spam")