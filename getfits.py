import pyfits

from hyperion.model import ModelOutput
from hyperion.util.constants import pc

# Open the model - we specify the name without the .rtout extension
m = ModelOutput('tutorial_model.rtout')

# Extract the image for the first inclination, and scale to 300pc. We
# have to specify group=1 as there is no image in group 0
wav, nufnu = m.get_image(group=1, inclination=0, distance=300 * pc)

# The image extracted above is a 3D array. We can write it out to FITS.
# We need to swap some of the directions around so as to be able to use
# the ds9 slider to change the wavelength of the image.
pyfits.writeto('image_cube.fits', nufnu.swapaxes(0, 2).swapaxes(1, 2), \
               clobber=True)

# We can also just output one of the wavelengths
pyfits.writeto('image_slice.fits', nufnu[:, :, 0], clobber=True)
