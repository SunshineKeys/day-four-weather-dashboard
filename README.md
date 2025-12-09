# Weather Dashboard (Day 4)

A simple Python command-line tool that fetches current weather and a 3-day forecast for any city or location.

This project uses a public weather API (`wttr.in`) and demonstrates:

- Making HTTP requests with `requests`
- Parsing JSON data
- Handling errors and bad input
- Building a user-friendly CLI loop

## Features

- Ask the user for a city or location name
- Show:
  - Current conditions (description, temperature, feels-like, humidity)
  - A simple 3-day forecast (min/avg/max temp + description)
- Handles network errors and invalid locations gracefully
- Type `q`, `quit`, or `exit` to leave the program

## How to Run

1. Install dependencies:

   ```bash
   pip install requests
