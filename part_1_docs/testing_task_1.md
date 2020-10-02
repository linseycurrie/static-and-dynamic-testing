### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

#card.value to be compared to 1 not assigned to 1 therefore '=' changed to '=='
#Semi-colon required after else
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   

#'dif' needs to be changed to 'def' to create method
#Comma required betweem card1 and card2 in the parameters
#Indentation of the 'if else' statement 
#Return 'card1' not 'card'
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

#overall indentation required to allow the function to be linked to card_game class.
#total needs to be initialised to '= 0'
#move the return function out to be in line with the for statment
#Convert total to str before concatenating to the string by str(total)
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
