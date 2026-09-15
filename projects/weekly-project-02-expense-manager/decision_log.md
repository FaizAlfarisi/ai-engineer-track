# Expense Manager


### Commit:
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
- 
##### Why 
- the match-case approach is cleaner for this project case since each of the action func (beside the report) can be handled specifictly for the positional argument.
- helper function to make the main match-case keep simple and clean
##### Alternative Considered
- keep dict action-func but add a conditional (`if service.__name__`) but it is need way more logical and code instead of match-case approach
- direct nested report match-case
