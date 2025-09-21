<p align="center">
  <a href="https://www.linkedin.com/in/cesar-coppola-santos-a899a0153/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  
  <a href="https://github.com/cesarcoppolasantos">
    <img src="https://img.shields.io/badge/GitHub-0077B5?logo=github&logoColor=white" alt="GitHub"/>
  </a>
  
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12"/>
</p>

# 💰 Python Loans Service API

An API developed as a solution for the challenge 🔗[Desafio Backend &lt;Brasil&gt; - Loans](https://github.com/backend-br/desafios/blob/master/loans/PROBLEM.md)

This API verifies the customer's CPF, age, and location, and performs an eligibility analysis based on their salary, age, and location.

## 🛠️ Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- brutils

## ⚙️ Installation

1. Clone this repository:
```bash
git clone git@github.com:cesarcoppolasantos/python-loans-service.git
cd python-loans-service
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
```

3. Activate the virtual environment:

**Windows**
```bash
venv\Scripts\activate
```
**Linux/macOS**
```bash
source venv/bin/activate
```

4. Install the dependencies:
```bash
pip3 install -r requirements.txt
```


## 💻 Usage Examples

#### Request Example

```http
POST /customer-loans
Content-Type: application/json

{
  "age": 26,
  "cpf": "123.456.789-00",
  "name": "Cesar Santos",
  "income": 7000.00,
  "location": "SP"
}

```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `age` | `integer` | **Required**. Customer's age in years |
| `cpf` | `string` | **Required**. Customer's CPF (May include symbols - .) |
| `name` | `string` | **Required**. Customer's name |
| `income` | `float` | **Required**. Customer's monthly income |
| `location` | `string` | **Required**. Customer's location (e.g., "SP", "RJ") |

#### Response Example

```http
{
  "customer": "Cesar Santos",
  "loans": [
    {
      "type": "PERSONAL",
      "interest_rate": 4
    },
    {
      "type": "GUARANTEED",
      "interest_rate": 3
    },
    {
      "type": "CONSIGNMENT",
      "interest_rate": 2
    }
  ]
}
```


## ✏️ Author

- Developed by **Cesar Santos**  
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cesar-coppola-santos-a899a0153/)   [![GitHub](https://img.shields.io/badge/GitHub-0077B5?logo=github&logoColor=white)](https://github.com/cesarcoppolasantos)
  
