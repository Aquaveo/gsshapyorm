"""
********************************************************************************
* Name: Write Tests
* Author: Nathan Swain
* Created On: May 16, 2013
* Copyright: (c) Brigham Young University 2013
* License: BSD 2-Clause
********************************************************************************
"""
import uuid
import os

from unittest import TestCase, main

from gsshapyorm.orm.file_io import MapTableFile, ProjectFileEventManager, PrecipFile, ChannelInputFile, \
    StormPipeNetworkFile, HmetFile, NwsrfsFile, OrographicGageFile, GridPipeFile, GridStreamFile, TimeSeriesFile, \
    OutputLocationFile, RasterMapFile, ProjectionFile, ReplaceParamFile, ReplaceValFile, LinkNodeDatasetFile, IndexMap
from gsshapyorm.orm import ProjectFile
from gsshapyorm.lib import db_tools as dbt


class TestWriteMethods(TestCase):
    def setUp(self):
        # Find db directory path
        here = os.path.abspath(os.path.dirname(__file__))

        self.dbName = '%s.db' % uuid.uuid4()
        self.db_path = os.path.join(here, 'db', 'standard.db')

        # Create Test DB
        sqlalchemy_url = dbt.init_sqlite_db(self.db_path)

        # Define workspace
        self.readDirectory = os.path.join(here, 'standard')
        self.writeDirectory = os.path.join(here, 'out')
        self.original = 'standard'
        self.name = 'standard'

        self.dir_list = ('run_2014_to_2017', 'run_2014_to_2017_2',
                         'run_2015_to_2017', 'run_2015_to_2017_1',
                         'run_2016_to_2017')
        for subdir in self.dir_list:
            try:
                os.mkdir(os.path.join(self.readDirectory, subdir))
            except OSError:
                pass

        # Create DB Sessions
        session_maker = dbt.get_sessionmaker(sqlalchemy_url)
        readSession = session_maker()

        # Instantiate GSSHAPY ProjectFile object
        prjR = ProjectFile()

        # Invoke read project method
        prjR.readProject(directory=self.readDirectory,
                         projectFileName='standard.prj',
                         session=readSession)

        readSession.close()

        # create write session
        self.writeSession = session_maker()

    def tearDown(self):
        self.writeSession.close()
        self._delete_extra_dirs()

        # Remove temp database
        dbt.del_sqlite_db(self.db_path)

        # Clear out directory
        fileList = os.listdir(self.writeDirectory)

        for afile in fileList:
            if afile != ".gitignore":
                path = os.path.join(self.writeDirectory, afile)
                try:
                    os.remove(path)
                except OSError:
                    pass

    def test_project_file_write(self):
        """
        Test ProjectFile write method
        """
        # Query and invoke write method
        self._query_n_write(ProjectFile)

        # Test
        self._compare_files(self.original, self.name, 'prj')

    def test_channel_input_write(self):
        """
        Test ChannelInputFile write method
        """
        # Query and invoke write method
        self._query_n_write(ChannelInputFile)

        # Test
        self._compare_files(self.original, self.name, 'cif')

    def test_map_table_file_write(self):
        """
        Test MapTableFile write method
        """
        # Query and invoke write method
        self._query_n_write(MapTableFile)

        # Test
        self._compare_files(self.original, self.name, 'cmt')

    def test_precip_file_write(self):
        """
        Test PrecipFile write method
        """
        # Query and invoke write method
        self._query_n_write(PrecipFile)

        # Test
        self._compare_files(self.original, self.name, 'gag')

    def test_grid_pipe_file_write(self):
        """
        Test GridPipeFile write method
        """
        # Query and invoke write method
        self._query_n_write(GridPipeFile)

        # Test
        self._compare_files(self.original, self.name, 'gpi')

    def test_grid_stream_file_write(self):
        """
        Test GridStreamFile write method
        """
        # Query and invoke write method
        self._query_n_write(GridStreamFile)

        # Test
        self._compare_files(self.original, self.name, 'gst')

    def test_hmet_file_write(self):
        """
        Test HmetFile write method
        """
        # Query and invoke write method
        self._query_n_write_filename(HmetFile, 'hmet_wes.hmt')

        # Test
        self._compare_files('hmet_wes', 'hmet_wes', 'hmt')

    def test_output_location_file_write(self):
        """
        Test OutputLocationFile write method
        """
        # Query and invoke write method
        self._query_n_write_multiple(OutputLocationFile, 'ihl')

        # Test
        self._compare_files(self.original, self.name, 'ihl')

    def test_link_node_dataset_file_write(self):
        """
        Test LinkNodeDatasetFile write method
        """
        # Query and invoke write method
        self._query_n_write_multiple(LinkNodeDatasetFile, 'cdp')

        # Test
        self._compare_files(self.original, self.name, 'cdp')

    def test_raster_map_file_write(self):
        """
        Test RasterMapFile write method
        """
        # Query and invoke write method
        self._query_n_write_multiple(RasterMapFile, 'msk')

        # Test
        self._compare_files(self.original, self.name, 'msk')

    def test_projection_file_write(self):
        """
        Test ProjectionFile write method
        """
        # Query and invoke write method
        self._query_n_write(ProjectionFile)

        # Test
        self._compare_files('standard_prj', 'standard_prj', 'pro')

    def test_replace_param_file_write(self):
        """
        Test ReplaceParamFile write method
        """
        # Query and invoke write method
        self._query_n_write_filename(ReplaceParamFile, 'replace_param.txt')

        # Test
        self._compare_files('replace_param', 'replace_param', 'txt')

    def test_replace_val_file_write(self):
        """
        Test ReplaceValFile write method
        """
        # Query and invoke write method
        self._query_n_write_filename(ReplaceValFile, 'replace_val.txt')

        # Test
        self._compare_files('replace_val', 'replace_val', 'txt')

    def test_nwsrfs_file_write(self):
        """
        Test NwsrfsFile write method
        """
        # Query and invoke write method
        self._query_n_write_filename(NwsrfsFile, 'nwsrfs_elev.txt')

        # Test
        self._compare_files('nwsrfs_elev', 'nwsrfs_elev', 'txt')

    def test_oro_gage_file_write(self):
        """
        Test OrographicGageFile write method
        """
        # Query and invoke write method
        self._query_n_write_filename(OrographicGageFile, 'oro_gages.txt')

        # Test
        self._compare_files('oro_gages', 'oro_gages', 'txt')

    def test_evt_yml_file_write(self):
        """
        Test ProjectFileEventManager write method
        """
        # Query and invoke write method
        self._query_n_write_filename(ProjectFileEventManager, 'testyml.yml')

        # Test
        self._compare_files('testyml', 'testyml', 'yml')

    def test_evt_yml_file_add_write(self):
        """
        Test ProjectFileEventManager add_event write method
        """
        # Retrieve ProjectFileEventManager from database
        prjEvtMng = self.writeSession.query(ProjectFileEventManager).one()

        a = prjEvtMng.add_event(name="event3", subfolder="run_2015_to_2017",
                                session=self.writeSession)
        assert a.name == "event3"
        assert a.subfolder == "run_2015_to_2017_2"

        a1 = prjEvtMng.add_event(name="event3", subfolder="run_2015_to_2017",
                                 session=self.writeSession)
        assert a1.name == "event3"
        assert a1.subfolder == "run_2015_to_2017_3"

        b = prjEvtMng.generate_event(session=self.writeSession)
        assert b.name == "event_1"
        assert b.subfolder == "event_1"

        b1 = prjEvtMng.generate_event(session=self.writeSession)
        assert b1.name == "event_2"
        assert b1.subfolder == "event_2"

        c = prjEvtMng.add_event(name="event2", subfolder="run_2014_to_2017",
                                session=self.writeSession)
        assert c.name == "event2"
        assert c.subfolder == "run_2014_to_2017_3"

        c1 = prjEvtMng.add_event(name="event2", subfolder="run_2014_to_2017",
                                 session=self.writeSession)
        assert c1.name == "event2"
        assert c1.subfolder == "run_2014_to_2017_4"

        # Query and invoke write method
        self._query_n_write_filename(ProjectFileEventManager, 'testyml2.yml')

        # Test
        self._compare_files('testyml2', 'testyml2', 'yml')

    def test_storm_pipe_network_file_write(self):
        """
        Test StormPipeNetworkFile write method
        """
        # Query and invoke write method
        self._query_n_write(StormPipeNetworkFile)

        # Test
        self._compare_files(self.original, self.name, 'spn')

    def test_time_series_file_write(self):
        """
        Test TimeSeriesFile write method
        """
        # Query and invoke write method
        self._query_n_write_multiple(TimeSeriesFile, 'ohl')

        # Test
        self._compare_files(self.original, self.name, 'ohl')

    def test_index_map_write(self):
        """
        Test IndexMap write method
        """
        # Retrieve file from database
        idx = self.writeSession.query(IndexMap).\
            filter(IndexMap.filename == 'Soil.idx').\
            one()

        # Invoke write method
        idx.write(session=self.writeSession,
                  directory=self.writeDirectory,
                  name='soil_new_name')

        # Test
        self._compare_files('Soil', 'soil_new_name', 'idx')

    def test_project_file_write_all(self):
        """
        Test ProjectFile write all method
        """
        # Retrieve ProjectFile from database
        projectFile = self.writeSession.query(ProjectFile).one()

        # Invoke write all method
        projectFile.writeProject(session=self.writeSession,
                                 directory=self.writeDirectory,
                                 name='standard')

        # Compare all files
        self._compare_directories(self.readDirectory, self.writeDirectory)

    def test_project_file_write_input(self):
        """
        Test ProjecFile write input method
        """
        # Retrieve ProjectFile from database
        projectFile = self.writeSession.query(ProjectFile).one()

        # Invoke write input method
        projectFile.writeInput(session=self.writeSession,
                               directory=self.writeDirectory,
                               name='standard')

        # Compare all files
        self._compare_directories(self.readDirectory, self.writeDirectory)

    def test_project_file_write_output(self):
        """
        Test ProjectFile write output method
        """
        # Retrieve ProjectFile from database
        projectFile = self.writeSession.query(ProjectFile).one()

        # Invoke write output method
        projectFile.writeOutput(session=self.writeSession,
                                directory=self.writeDirectory,
                                name='standard')

        # Compare all files
        self._compare_directories(self.readDirectory, self.writeDirectory)

    def _query_n_write(self, fileIO):
        """
        Query database and write file method
        """
        # Retrieve file from database
        instance = self.writeSession.query(fileIO).one()

        # Invoke write method
        instance.write(session=self.writeSession,
                       directory=self.writeDirectory,
                       name=self.name)

    def _query_n_write_filename(self, fileIO, filename):
        """
        Query database and write file method
        """
        # Retrieve file from database
        instance = self.writeSession.query(fileIO).one()

        # Invoke write method
        instance.write(session=self.writeSession,
                       directory=self.writeDirectory,
                       name=filename)

    def _query_n_write_multiple(self, fileIO, ext):
        """
        Query database and write file method for fileIO object that could have multiple extensions
        """
        # Retrieve file from database
        instance = self.writeSession.query(fileIO).\
            filter(fileIO.fileExtension == ext).\
            one()

        # Invoke write method
        instance.write(session=self.writeSession,
                       directory=self.writeDirectory,
                       name=self.name)

    def _compare_files(self, original, new, ext):
        """
        Compare the contents of two files
        """
        if ext == 'cmt':
            original = '{0}_compare'.format(original)

        filenameO = '%s.%s' % (original, ext)
        filePathO = os.path.join(self.readDirectory, filenameO)
        filenameN = '%s.%s' % (new, ext)
        filePathN = os.path.join(self.writeDirectory, filenameN)

        with open(filePathO) as fileO:
            contentsO = fileO.read()
            linesO = contentsO.strip().split()

        with open(filePathN) as fileN:
            contentsN = fileN.read()
            linesN = contentsN.strip().split()

        self.assertEqual(linesO, linesN)

    def _compare_directories(self, dir1, dir2):
        """
        Compare the contents of the files of two directories
        """
        self._delete_extra_dirs()

        fileList2 = os.listdir(dir2)

        for afile in fileList2:
            if not os.path.basename(afile).startswith("."):
                name = afile.split('.')[0]
                ext = afile.split('.')[1]

                # Compare files with same name
                self._compare_files(name, name, ext)

    def _list_compare(self, listone, listtwo):
        for one, two in zip(listone, listtwo):
            self.assertEqual(one, two)

    def _delete_extra_dirs(self):
        for subdir in self.dir_list:
            try:
                os.rmdir(os.path.join(self.readDirectory, subdir))
            except OSError:
                pass


if __name__ == '__main__':
    main()
