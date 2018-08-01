# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Secret(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'data': 'dict(str, str)',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'string_data': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'data': 'data',
        'kind': 'kind',
        'metadata': 'metadata',
        'string_data': 'stringData',
        'type': 'type'
    }

    def __init__(self, api_version=None, data=None, kind=None, metadata=None, string_data=None, type=None):
        """
        V1Secret - a model defined in Swagger
        """

        self._api_version = None
        self._data = None
        self._kind = None
        self._metadata = None
        self._string_data = None
        self._type = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        if data is not None:
          self.data = data
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata
        if string_data is not None:
          self.string_data = string_data
        if type is not None:
          self.type = type

    @property
    def api_version(self):
        """
        Gets the api_version of this V1Secret.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1Secret.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1Secret.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1Secret.
        :type: str
        """

        self._api_version = api_version

    @property
    def data(self):
        """
        Gets the data of this V1Secret.
        Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4

        :return: The data of this V1Secret.
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this V1Secret.
        Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4

        :param data: The data of this V1Secret.
        :type: dict(str, str)
        """

        self._data = data

    @property
    def kind(self):
        """
        Gets the kind of this V1Secret.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1Secret.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1Secret.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1Secret.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1Secret.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :return: The metadata of this V1Secret.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1Secret.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1Secret.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def string_data(self):
        """
        Gets the string_data of this V1Secret.
        stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.

        :return: The string_data of this V1Secret.
        :rtype: dict(str, str)
        """
        return self._string_data

    @string_data.setter
    def string_data(self, string_data):
        """
        Sets the string_data of this V1Secret.
        stringData allows specifying non-binary secret data in string form. It is provided as a write-only convenience method. All keys and values are merged into the data field on write, overwriting any existing values. It is never output when reading from the API.

        :param string_data: The string_data of this V1Secret.
        :type: dict(str, str)
        """

        self._string_data = string_data

    @property
    def type(self):
        """
        Gets the type of this V1Secret.
        Used to facilitate programmatic handling of secret data.

        :return: The type of this V1Secret.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1Secret.
        Used to facilitate programmatic handling of secret data.

        :param type: The type of this V1Secret.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1Secret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
