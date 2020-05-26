#  Tencent is pleased to support the open source community by making GNES available.
#
#  Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from .base import BaseService as BS, MessageHandler
from ..proto import gnes_pb2


class PreprocessorService(BS):
    handler = MessageHandler(BS.handler)

    def post_init(self):
        from ..preprocessor.base import BasePreprocessor
        self._model = self.load_model(BasePreprocessor)

    @handler.register(gnes_pb2.Request.TrainRequest)
    def _handler_train(self, msg: 'gnes_pb2.Message'):
        for d in msg.request.train.docs:
            self._apply(d)

    @handler.register(gnes_pb2.Request.IndexRequest)
    def _handler_index(self, msg: 'gnes_pb2.Message'):
        for d in msg.request.index.docs:
            self._apply(d)

    @handler.register(gnes_pb2.Request.QueryRequest)
    def _handler_query(self, msg: 'gnes_pb2.Message'):
        self._apply(msg.request.search.query)

    def _apply(self, d: 'gnes_pb2.Document'):
        self._model.apply(d)
        if not d.chunks:
            self.logger.warning('document (doc_id=%s) contains no chunks!' % d.doc_id)
