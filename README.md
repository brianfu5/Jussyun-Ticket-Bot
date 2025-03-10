# Jussyun Ticket Bot

A Python bot that constantly checks (every 0-0.1 seconds) if there are tickets available for an event on Jussyun. Upon availablility, automatically opens a new tab, logs in, and navigates to the seat selection / buy screen, where the user can then select seats and checkout. This program can be keep running in the backgroud, and an alarm noise will sound to alert the user is tickets are found. Built using Selenium. I built this bot to help me get F1 Shanghai tickets(which it did).

#### Please fill out the fields in `config.py` with the details of your own event and install the required dependancies. Requires an account on Jussyun and for spectator info to be already prefilled. 
#### Current limitations: Can only buy one ticket at a time. Cannot automatically select seat and complete the captcha required to checkout.

### Run the program in the terminal using `python main.py`
