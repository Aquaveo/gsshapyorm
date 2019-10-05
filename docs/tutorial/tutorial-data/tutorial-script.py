"""
********************************************************************************
* Name: Tutorial Script
* Description: This script summarizes the steps followed in the GsshaPy tutorial
* Author: Nathan Swain
* Created On: July 30, 2014
* Copyright: (c) Brigham Young University 2013
* License: BSD 2-Clause
********************************************************************************
"""

# Create a GsshaPy PostGIS database
from gsshapyorm.lib import db_tools as dbt
from sqlalchemy.orm import create_session

sqlalchemy_url = dbt.sqlalchemy_url = dbt.init_postgresql_db(
    username='gsshapyorm',
    host='localhost',
    database='gsshapy_tutorial',
    port='5432',
    password='pass'
)

# Create SQLAlchemy session object for db interaction
session = create_session(sqlalchemy_url)

# Read Files to a Database --------------------------------------------------------------------------------------------#

# Instantiate ProjectFile file object
from gsshapyorm.orm import ProjectFile
projectFile = ProjectFile()

# Read file into database
readDirectory = '/path_to/tutorial-data'
filename = 'parkcity.prj'
projectFile.read(directory=readDirectory, filename=filename, session=session)

# Inspect supporting objects
projectCards = projectFile.projectCards

for card in projectCards:
    print(card)

for card in projectCards:
    print(card.name, card.value)

# Querying the database using the GsshaPy objects ---------------------------------------------------------------------#

# Retrieve all project cards for a given project file
from gsshapyorm.orm import ProjectCard
cards = session.query(ProjectCard).all()
for card in cards:
    print(card)

cards = session.query(ProjectCard).filter(ProjectCard.projectFile == projectFile).all()
for card in cards:
    print(card)

# Equivalently:
cards = projectFile.projectCards
for card in cards:
    print(card)

# Write File from a Database ------------------------------------------------------------------------------------------#

# Retrieve the ProjectFile object from the database
newProjectFile = session.query(ProjectFile).first()

# Define write parameters and invoke write
writeDirectory = '/path_to/tutorial-data/write'
name = 'mymodel'
newProjectFile.write(session=session, directory=writeDirectory, name=name)

# Read and Write Entire GSSHA Projects --------------------------------------------------------------------------------#

# Create new session
from gsshapyorm.lib import db_tools as dbt
sqlalchemy_url = dbt.sqlalchemy_url = dbt.init_postgresql_db(
    username='gsshapyorm',
    host='localhost',
    database='gsshapy_tutorial',
    port='5432',
    password='pass'
)
all_session = create_session(sqlalchemy_url)

# Instantiate a new ProjectFile object
from gsshapyorm.orm import ProjectFile
projectFileAll = ProjectFile()

# Invoke the readProject() method
readDirectory = '/path_to/tutorial-data'
filename = 'parkcity.prj'
projectFileAll.readProject(directory=readDirectory, projectFileName=filename, session=all_session)

# Retrieve project file from dataabase and invoke writeProject()
newProjectFileAll = all_session.query(ProjectFile).filter(ProjectFile.id == 2).one()
writeDirectory = '/path_to/tutorial-data/write'
name = 'mymodel'
newProjectFileAll.writeProject(session=all_session, directory=writeDirectory, name=name)

# Read as Spatial Objects and Generate Spatial Visualizations ---------------------------------------------------------#

# Create a new session and a project file object as before
from gsshapyorm.lib import db_tools as dbt
sqlalchemy_url = dbt.sqlalchemy_url = dbt.init_postgresql_db(
    username='gsshapyorm',
    host='localhost',
    database='gsshapy_tutorial',
    port='5432',
    password='pass'
)
spatial_session = create_session(sqlalchemy_url)
from gsshapyorm.orm import ProjectFile
spatialProjectFile = ProjectFile()

# Define variables and invoke project read method
readDirectory = '/path_to/tutorial-data'
filename = 'parkcity.prj'
spatial = True
srid = 26912
raster2pgsql_path = '/path_to/raster2pgsql'
spatialProjectFile.readProject(directory=readDirectory, projectFileName=filename, session=spatial_session,
                               spatial=spatial, spatialReferenceID=srid, raster2pgsqlPath=raster2pgsql_path)

# Read an individual file with spatial objects (using same inputs as above)
from gsshapyorm.orm import RasterMapFile
maskMap = RasterMapFile()
filename = 'parkcity.msk'
maskMap.read(directory=readDirectory, filename=filename, session=spatial_session, spatial=spatial,
             spatialReferenceID=srid, raster2pgsqlPath=raster2pgsql_path)

# Demonstrate spatial visualization methods
from gsshapyorm.orm import ProjectFile
import os
kml_path = os.path.join(writeDirectory, 'model_summary.kml')
newSpatialProjectFile = spatial_session.query(ProjectFile).filter(ProjectFile.id == 3).one()
newSpatialProjectFile.getModelSummaryAsKml(session=spatial_session, path=kml_path)
