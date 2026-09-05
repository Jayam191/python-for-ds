# Food Delivery Live Data Pipeline

## Project Overview

A console-based Food Delivery Live Data Pipeline Tool built using Python.

The project fetches mock restaurant data from a public API, manages records using Object-Oriented Programming, calculates commission using higher-order functions, and saves and loads records using JSON file handling.

## Features

1. Fetch and display top 10 restaurants from the API.
2. Add a new restaurant.
3. Calculate commission using `map()` and `filter()`.
4. Save and load records using JSON.
5. Validate numeric input.
6. Handle API errors gracefully.

## Technologies

- Python
- Requests
- JSON
- Object-Oriented Programming
- `map()`
- `filter()`
- File Handling
- Git and GitHub

## API

https://jsonplaceholder.typicode.com/posts?_limit=10

The API's `id` is used as the restaurant ID and `title` is used as the restaurant name.

## Project Structure

mini-capstone/
- src/
  - food_delivery_pipeline.py
- data/
  - raw/
  - processed/
- docs/
- tests/
- README.md

## Run the Program

From the `mini-capstone` folder:

```text
python src\food_delivery_pipeline.py