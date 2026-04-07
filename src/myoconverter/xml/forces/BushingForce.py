""" Contains the `CoordinateCouplerConstraint` parser.

@author: Aleksi Ikkala
"""

from loguru import logger

from myoconverter.xml.parsers import IParser


class BushingForce(IParser):
  """ This class parses and converts the OpenSim `BushingForce` XML element to MuJoCo (not implemented yet). """

  def parse(self, xml):
    """ This function handles the actual parsing and converting.

    :param xml: OpenSim `BushingForce` XML element
    :return: None
    """
    logger.warning(f"BushingForce parser has not been implemented, skipping {xml.attrib['name']}")
