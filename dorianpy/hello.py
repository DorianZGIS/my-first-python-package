from emoji import emojize

def hello(username = "anon"):
  """Write here a title of your function
  
  Write here a short description of your function.
  
  Parameters
  ----------
  username : str
    Describe here what the name parameter does.

  Returns
  -------
  str
    Describe here what the function returns.
  
  Examples
  --------
  hello(dorian)
  Hello dorian! Welcome to the best python Python package in the entire universe!
  """
  print("Hello ", username, emojize(":wave:"), "! Welcome to the best python Python package in the entire universe!", sep = "")