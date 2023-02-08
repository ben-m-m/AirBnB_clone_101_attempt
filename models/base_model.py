#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods for other classes"""


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel
        Args:
            *args
            **kwargs
        """
        if kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    val = datetime.strptime(value/ "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
                    continue
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

