from zou.app.models.file_status import FileStatus
from zou.app.resources.data.base import BaseModelResource, BaseModelsResource


class FileStatusesResource(BaseModelsResource):

    def __init__(self):
        BaseModelsResource.__init__(self, FileStatus)


class FileStatusResource(BaseModelResource):

    def __init__(self):
        BaseModelResource.__init__(self, FileStatus)