"""
********************************************************************************
* Name: base.py
* Author: Nathan Swain
* Created On:October 5, 2019
* Copyright: (c) Aquaveo, LLC 2019
* License: BSD 2-Clause
********************************************************************************
"""
from sqlalchemy.ext.declarative import declarative_base
# Base class for all of model classes
DeclarativeBase = declarative_base()

# Global metadata. This is used to
# Initialize a database with the
# Appropriate tables. See db_tools
metadata = DeclarativeBase.metadata
