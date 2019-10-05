"""
********************************************************************************
* Name: Test Grid Template
* Author: Alan D. Snow
* Created On: September 16, 2016
* License: BSD 3-Clause
********************************************************************************
"""
from numpy import array
from numpy.testing import assert_almost_equal
import os
from osgeo import gdal
from shutil import rmtree
import unittest
from gsshapyorm.util.optional import import_optional


SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))


class TestGridTemplate(unittest.TestCase):
    # Define workspace
    readDirectory = os.path.join(SCRIPT_DIR, 'grid_standard')
    writeDirectory = os.path.join(SCRIPT_DIR, 'out')

    def _compare_files(self, original, new, raster=False, precision=7):
        """
        Compare the contents of two files
        """
        if raster:
            dsO = gdal.Open(original)
            dsN = gdal.Open(new)

            # compare data
            rO = array(dsO.ReadAsArray())
            rN = array(dsN.ReadAsArray())
            assert_almost_equal(rO, rN, decimal=precision)

            # compare geotransform
            assert_almost_equal(dsO.GetGeoTransform(), dsN.GetGeoTransform(),
                                decimal=5)

            # compare band counts
            assert dsO.RasterCount == dsN.RasterCount
            # compare nodata
            for band_id in range(1, dsO.RasterCount+1):
                assert (dsO.GetRasterBand(band_id).GetNoDataValue()
                        == dsN.GetRasterBand(band_id).GetNoDataValue())

        else:
            with open(original) as fileO:
                contentsO = fileO.read()
                linesO = contentsO.strip().split()

            with open(new) as fileN:
                contentsN = fileN.read()
                linesN = contentsN.strip().split()

            for lineO, lineN in zip(linesO, linesN):
                for valO, valN in zip(lineO.split(), lineN.split()):
                    try:
                        valO = float(valO)
                        valN = float(valN)
                        assert_almost_equal(valO, valN, precision)
                    except ValueError:
                        self.assertEqual(valO, valN)
                        pass

    def _compare_directories(self, dir1, dir2, ignore_file=None, raster=False, precision=7):
        """
        Compare the contents of the files of two directories
        """

        for afile in os.listdir(dir2):
            if not os.path.basename(afile).startswith(".")\
               and not afile == ignore_file:

                # Compare files with same name
                try:
                    self._compare_files(os.path.join(dir1, afile),
                                        os.path.join(dir2, afile),
                                        raster=raster,
                                        precision=precision)
                except AssertionError:
                    print(os.path.join(dir1, afile))
                    print(os.path.join(dir2, afile))
                    raise

    def _list_compare(self, listone, listtwo):
        for one, two in zip(listone, listtwo):
            self.assertEqual(one, two)

    def _before_teardown(self):
        """
        Method to execute at beginning of tearDown
        """
        return

    def tearDown(self):
        """
        Method to cleanup after tests
        """
        self._before_teardown()

        # Clear out directory
        fileList = os.listdir(self.writeDirectory)

        for afile in fileList:
            if not afile.endswith('.gitignore'):
                path = os.path.join(self.writeDirectory, afile)
                if os.path.isdir(path):
                    rmtree(path)
                else:
                    os.remove(path)
