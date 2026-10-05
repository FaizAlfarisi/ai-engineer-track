import logging

def linked_child(parent_name: str, child_name: str) -> bool:
    parent_logger = logging.getLogger(parent_name)
    child_logger = logging.getLogger(child_name)
    
    return child_logger.parent is parent_logger