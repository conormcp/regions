from astropy.utils.data import get_pkg_data_filename, get_pkg_data_fileobj
import pytest

from .. import ShapeList


parametrize_filenames = pytest.mark.parametrize(
    'filename',
    ['../crtf/tests/data/CRTFgeneral.crtf',
     '../ds9/tests/data/ds9.color.reg',
     '../fits/tests/data/fits_region.fits',
    ])


@parametrize_filenames
def test_read_filename(filename):
    filename = get_pkg_data_filename(filename)
    result = ShapeList.read(filename)
    assert isinstance(result, ShapeList)


@parametrize_filenames
@pytest.mark.parametrize('encoding', [
    'binary',
    pytest.param(None, marks=pytest.mark.xfail),  # does not work yet
])
def test_read_fileobj(filename, encoding):
    with get_pkg_data_fileobj(filename, encoding=encoding) as fileobj:
        result = ShapeList.read(fileobj)
    assert isinstance(result, ShapeList)


@pytest.mark.parametrize('format', ['crtf', 'ds9'])
def test_write_format(format, tmpdir):
    infilename = get_pkg_data_filename('../crtf/tests/data/CRTFgeneral.crtf')
    outfilename = str(tmpdir / 'region')
    shapelist = ShapeList.read(infilename)
    shapelist.write(outfilename, format=format)