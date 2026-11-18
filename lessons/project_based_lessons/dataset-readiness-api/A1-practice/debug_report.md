H1
1. 
| Step | Content |
|------|---------|
| Symptom | test_h1.py::test_mixed_file_counts |
| Trigger | AssertionError: assert {'total': 3, 'ok': 3, 'invalid': 2} == {'total': 3, 'ok': 1, 'invalid': 2} |
| Hypothesis | wrong logic on 'ok' increment |
| Evidence | Differing items: {'ok': 3} != {'ok': 1} |
| Cause | increment ok first before model_validate |
| Fix | validate model first then increment the ok |
| Proof | test_h1.py::test_mixed_file_counts PASSED |

2. 
| Step | Content |
|------|---------|
| Symptom | test_h1.py::test_counts_add_up_with_empty_object_row |
| Trigger | AssertionError: assert {'total': 2, 'ok': 1, 'invalid': 0} == {'total': 2, 'ok': 1, 'invalid': 1} |
| Hypothesis | empty row not counted as invalid |
| Evidence | {'invalid': 0} != {'invalid': 1} |
| Cause | continued empty row without recording as invalid |
| Fix | add increment in empty row validation |
| Proof | test_h1.py::test_counts_add_up_with_empty_object_row PASSED |

3. 
| Step | Content |
|------|---------|
| Symptom | test_h1.py::test_binary_bytes_are_bad_upload_not_a_crash FAILED |
| Trigger | UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte |
| Hypothesis | did not catch the unicodedecodeerror |
| Evidence | check_products(b"\x89PNG\r\n") |
| Cause | exception block did not catch unicodedecodeerror |
| Fix | add new exception UnicodeDecodeError |
| Proof | test_h1.py::test_binary_bytes_are_bad_upload_not_a_crash PASSED |