============== Project ==============
request -> validate argv -> map action -> (each action): parse data -> load data -> action
add data: append existing data -> re-write file
remove data: search by title -> remove if exist -> re-write file
search data: search by title and author -> combine both -> show data
list data: return formatted data

decision log:
- analyze and build skeleton code:
1. main is the driver, read argv, print report (error or messages); following best practice to build pythonic project;.
2. map action, match the argv[1] to its intent passing to the matching function; match case has a simpler code to handle this condition, moreover it is readable than if else; if else block.
3. define load_json and write_json to follow DRY concept; load_json should be check if the path exist, catch error decode, so that it will cost less code if i make the function over it; direct load and write on each action function.

- feature add data:
1. main: validation length of argv, first validation to the data request, print usage information if it fails the validation. declare global variable FILE_PATH in the script guard; make sure that the data is on the right amount to get processed in the next step. the file path is used in a lot of function anyways so it is easier if i set the global var; passing the path for each function needed it, but it is has a potential inconsistent data.
2. add function: direct unpacking the title, author, and year data for the first 3 requested data, genre is handled in special block; the genre is handled in ternary operation since it just check a single condition and must have a default value; using if else classic way could be an alternative
3. load_json; check if path not exist. eafp for loading the json data, create new custom error for corrupt data (i use the idea from the exception handling lesson, implement it in simplest way); checking path so that i can return an empty list if it not exist. custom error so it is handled seamlessly without making an error traceback.
4. add function: load existing data and make comprehension set for the existing title; it is faster using set type for the check up value; alternative with dictionary comprehension, but since i just need to check only the title so it is simpler using set.
5. book library data design with key:value dictionary, custom key 'search_index' which is contain 'author | title'; it is easier to access and preserving the consistencity of the data structure. with search_index, next feature will be easier to implement;.
6. write json with indent; so the written text is more readable; no indent (moreover with separate) is simpler but hard to read.

- feature remove data:
1. refactor main args validation; the usage of each action has a different length of args;.
2. remove function: normalizing request with lower and strip, declare data_found None, loop through existing data to get the target data, lower the title, if found set the book dict to data_found; with this approach i can know if the data found or not so the system can report to user; alternative using list comprehension, but it is complicated to set the not found case.