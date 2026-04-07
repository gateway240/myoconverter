""" Contains the `FunctionBasedBushingForce` parser.

@author: Aleksi Ikkala
"""

from loguru import logger

from myoconverter.xml.parsers import IParser


class FunctionBasedBushingForce(IParser):
  """ This class parses and converts the OpenSim `FunctionBasedBushingForce` XML element to MuJoCo (not implemented
  yet). """

  def parse(self, xml):
    """ This function handles the actual parsing and converting.

    :param xml: OpenSim `FunctionBasedBushingForce` XML element
    :return: None
    """
    logger.warning(f"FunctionBasedBushingForce parser has not been implemented, skipping {xml.attrib['name']}")
