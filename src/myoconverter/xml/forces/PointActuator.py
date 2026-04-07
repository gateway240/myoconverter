""" Contains the `PointActuator` parser.

@author: Aleksi Ikkala
"""

from loguru import logger

from myoconverter.xml.parsers import IParser


class PointActuator(IParser):
  """ This class parses and converts the OpenSim `PointActuator` XML element to MuJoCo (not implemented yet). """

  def parse(self, xml):
    """ This function handles the actual parsing and converting.

    :param xml: OpenSim `PointActuator` XML element
    :return: None
    """
    logger.warning(f"PointActuator parser has not been implemented, skipping {xml.attrib['name']}")
