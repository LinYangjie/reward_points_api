# Reward Points API

## **Setup**

***Software Installation***
  - **Python:** [Link](https://www.python.org/downloads/)
  - **Flask: Python framework** [Link](https://pypi.org/project/Flask/)<br />
  Need to install pip first: `pip install pip`
     
  - **Postman:** [Link](https://www.postman.com/downloads/)

***Server setup***
  
  After finish above install, please clone this repository:

  - **step 1** : Copy below code snippet, type in terminal with desire location.
  
  &nbsp; `git clone https://github.com/LinYangjie/reward_points_api.git`

  - **step 2** : setup flask
  
  &nbsp; `set FLASK_APP=app.py`
  
  - **step 3** : run server

  &nbsp; `python app.py` 

  - **step 4** : run PostMan to test below api (run on portal 5000)
  
  &nbsp; `http://localhost:5000/<test below api>`
   
</br> 

## **API Document**

</br>

### ***Fetch transactions data***
___

  Return json data about all exists transactions,
  which means transactions detail

* **URL**

  /transactions

* **Method:**

  `GET` 
  
*  **URL Params**

   None

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**  

                  [{
                    "payer": "DANNON",
                    "points": 300, 
                    "timestamp": "2020-10-31T10:00:00Z"
                    }]  
 
* **Error Response:**


  * **Code:** 405 UNAUTHORIZED <br />
    **Content:** 
                  
                  Method Not Allowed

                  The method is not allowed for the requested URL.
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:**  Rest of the errors.



* **Sample Call:**

  `http://localhost:5000/transactions`

### ***Fetch balance***
___

  Return json data of all payer with their reward points balance

* **URL**

  /balance

* **Method:**

  `GET` 
  
*  **URL Params**

   None

   **Required:**
 
   None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**  

                  [{
                    "payer": "DANNON",
                    "points": 1100, 
                    }]  
 
* **Error Response:**


  * **Code:** 405 UNAUTHORIZED <br />
    **Content:** 
                  
                  Method Not Allowed

                  The method is not allowed for the requested URL.
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:**  Rest of the errors.



* **Sample Call:**

  `http://localhost:5000/balance`

 ### ***Add Transaction***
___
  Add transaction with given payer and points to the data and
  return json data about all the transactions

* **URL**

  /add-transaction

* **Method:**

  `POST` 
  
*  **URL Params**

   None

   **Required:**
 
   None

* **Data Params**

  Require payer and points

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**  
                
              [{"payer": "DANNON",
                "points": 300, 
                "timestamp": "2020-10-31T10:00:00Z"
               },
               {
                "payer": "JAY",
                "points": 5000, 
                "timestamp": "2021-11-31T10:00:00Z"
               }] 
      
 
* **Error Response:**


  * **Code:** 405 UNAUTHORIZED <br />
    **Content:** 
                  
                  Method Not Allowed

                  The method is not allowed for the requested URL.
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:** Rest of the errors.


* **Sample Call:**

  `http://localhost:5000/add-transaction`


 ### ***Spend Reward Points***
___
  Return json file with all payers correspond to how much reward points they spend

* **URL**

  /spend-points

* **Method:**

  `PUT` 
  
*  **URL Params**

   None

   **Required:**
 
   None

* **Data Params**
  desire points to spend

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**  
                  
                  [
                    { "payer": "DANNON", "points": -100 },
                    { "payer": "UNILEVER", "points": -200 },
                    { "payer": "MILLER COORS", "points": -4,700 }
                  ] 
 
* **Error Response:**


  * **Code:** 405 UNAUTHORIZED <br />
    **Content:** 
                  
                  Method Not Allowed

                  The method is not allowed for the requested URL.
  
  * **Code:** 400 BAD REQUEST <br />
    **Content:** 
                  
                  insufficient balance
                  



* **Sample Call:**

  `http://localhost:5000/spent-points`

