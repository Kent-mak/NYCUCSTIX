# NYCUCSTIX
## introduction
This is a ticket Purchasing Website. After logging in, users can select the type of ticket they want to buy on the homepage. Once they pass the ticket purchase verification, they can view their successfully purchased tickets in their personal ticket storage.

The purpose of this website is to be used in a camp to teach web scraping techniques for building a ticket-snatching bot.

## requirements
- python 3.10
  - download packages
    ```shell
    .\venv\Scripts\Activate
    pip install -r requirements.txt
    ```
- download Node.js
  - verify installation
    ```shell
    node -v
    npm -v
    ```
  - download requirements
    ```shell
    npm install axios react-markdown
    ```
## architecture
  ```
  - backend/   # a backend built using FastAPI and MongoDB
  - frontend/  # a frontend developed using React
  - Crawler/   # a crawler to crawl the website
  - manageDB/  # use to test the connection to DB
  - scoreboard-app/ # a scoreboard to show number of tickets the user purchases
  ```
## run project
  - run backend
  ```shell
  fastapi dev main.py
  ```
  
  - run frontend
  ```shell  
  npm install
  npm run dev
  ```
  - run crawler
  ```shell  
  python crawler_ans.py
  ```
## website url
http://cstix.nctucsunion.me/
