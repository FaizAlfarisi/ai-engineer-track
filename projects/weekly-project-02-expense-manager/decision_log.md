# Expense Manager


### commit:
##### Decision
-
##### Why 
- 
##### Alternative Considered
- 

### Init Project:
##### Decision
- Make .venv
- Install mypy
##### Why 
- 
##### Alternative Considered
- 

### Project Structure:
##### Decision
- Proposed folder structure is following the clean separation of concern (clean architecture - Go)
##### Why 
- Learn to separating the concern of each script
- Develop easily with each module has its own concern
##### Alternative Considered
- In small project (like this wp2), it is unnecessary to make it as clean as proposed. It could be written in simpler structure or even without module (use direct name.py). Because it can lead to overengineering (a single action need to access 3 to 5 module) and confusion.

### Command route:
#### first decision
##### Decision
- implementing router with dict (action: func) approach
- set the sub_action if exist, if it isn't set None instead
- dict routes with key "report" have a dict value of its type of report
##### Why 
- trying another approach and exploring dict utility
- set none to represent empty (null) data
- by using "report": dict approach i can set the delegation cleaner and inform users more clearly
##### Alternative Considered
- match-case approach for routing, but i find a struggle to set the nested match-case

```python
# old code
import sys

def seed():
    print("seed")
def add(biji):
    print(f"add {biji}")
def list_data():
    print("list")
def net_summary():
    print("net")
def report_weekly():
    print("report_weekly")
def report_monthly():
    print("report_monthly")
def report_categories():
    print("report_categories")

def main() -> None:
    args = sys.argv[1:]
    
    if not args:
        print("empty input")
        sys.exit(1)
    
    action = args[0]
    sub_action = args[1:] if len(args) > 1 else None
    
    routes = {
        "--seed": seed,
        "add": add,
        "list": list_data,
        "report": {
            "summary": net_summary,
            "monthly": report_monthly,
            "weekly": report_weekly,
            "categories": report_categories,
        }
    }

    try:
        service = routes.get(action)
        
        if service is None:
            print("unknown command")
            sys.exit(1)
        
        # if it is an instance, it would be a report family command
        # capture the first sub_action to get the desired type of report
        if isinstance(service, dict):
            if sub_action is None:
                print("no type of report provided")
                sys.exit(1)
                
            if sub_action[0] not in service:
                print("unknown report type")
                sys.exit(1)
            service[sub_action[0]]()
        else:
            print(service.__name__)
            service() if service == "list_data" else service(sub_action)

    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

#### final decision
##### Decision
- change the dict action-func approach to match-case 
- create helper function for the report action to delegate the report type requested to its function
##### Why 
- the match-case approach is cleaner for this project case since each of the action func (beside the report) can be handled specifictly for the positional argument.
- helper function to make the main match-case keep simple and clean
##### Alternative Considered
- keep dict action-func but add a conditional (`if service.__name__`) but it is need way more logical and code instead of match-case approach
- direct nested report match-case

### feat: List:
##### Decision
- create configurations/config.py to set the FILE_PATH
- set the repositories to a single file transactions_repo as the Transaction class mediator to data source (json, csv)
- use object_hook to decode json into Transaction object
- create formatter for transaction service, sort it by date by simply set the key of sorting with the value of date (without using datetime)
##### Why 
- FILE_PATH not passed through every function from main.py, instead the service can import it from configurations.config. So that the main and the service func are not passing the same file_path over and over again for each of it.
- the merge of the proposed json_repo.py and csv_repo.py is for keep the repo simple and easier for maintenance, since the action to the data source of Transactions is gathered in one place.
- set the record in transactions.json to be an object of Transaction class to get the method signed_amount for the next implementation
- create a reusable Transactions formatter and separate it from the transaction_service module to make it clean
- the result of sorted string could represent the order date by oldest
##### Alternative Considered
- FILE_PATH set in the guard block like wp1 project, but it will cost us the pass and call file_path in each func.
- Set the formatter directly in the list service since it is just use once

### feat: Add:
##### Decision
- validate data passed to add function by its lenght, unpack, parse & validate
- new utils validators to validate data, in this implementation validate date format
- serialize and encode enum before dumps json
- set the error message more verbose (not exactly following byte by byte from brief) (just add either 'bad request' or 'corrupt data' or 'unexpected error')
##### Why 
- because of the add action is strictly have the exact 4 args, it is easier to check the length first, then unpack it, and then parse & validate
- create utils because it can be reusable through the entire project, moreover it is an independent helper.
- the dataclass is need to be serialized asdict first and then encode the kind enum so its get the value, it would be raising an error if we skip this flow.
- clearer error message scope
##### Alternative Considered
- set the validation directly through service, for this scope it just used once tho. so it is unnecessary to create new utils.

### feat: Report Monthly, Report Categories:
##### Decision
- change config var, set DATA_PATH as the dir of data, change FILE_PATH to JSON_PATH
- new repo write and load csv, exclusively for Transaction model
- report formatter for monthly and categories report on Transaction domain
##### Why 
- it is more flexible reusable for the records service since its need to create new csv file 
- write and load csv reusable in Transaciton domain since it is a transaction repo
- reusable report formatter since it is used in two func 
##### Alternative Considered
- direct set the csv path in the service, but it is need from pathlib import Path which is not the scope of service, it should be on consistent on config

### feat: report weekly and summary:
##### Decision
- change utils/validators.py to utils/datetime_helper.py, add more helper related to datetime
- refactor validate_date to return converted datetime
- summary counted manualy outside the dict first before construct it to dict
##### Why 
- weekly report need datetime helper, moreover this project doesnt need more validators
- it can be reuse in weekly report service since the extract year week need the datetime object to get the desired format (year and week)
- count total net easier and build the summary dict with the expected sequence (income then expense then net)
##### Alternative Considered
- the extract_year_week can convert by itself since the recorded data has a low chance of invalid date
- dict.get method to set the summary, but it need to count net inside the loop