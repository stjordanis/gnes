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


# A key-value map for Class to the (module)file it located in
from ..base import register_all_class

_cls2file_map = {
    'BertEncoder': 'text.bert',
    'BertEncoderWithServer': 'text.bert',
    'BertEncoderServer': 'text.bert',
    'FlairEncoder': 'text.flair',
    'PCALocalEncoder': 'numeric.pca',
    'PQEncoder': 'numeric.pq',
    'TFPQEncoder': 'numeric.tf_pq',
    'Word2VecEncoder': 'text.w2v',
    'BaseEncoder': 'base',
    'BaseBinaryEncoder': 'base',
    'BaseTextEncoder': 'base',
    'BaseVideoEncoder': 'base',
    'BaseNumericEncoder': 'base',
    'BaseAudioEncoder': 'base',
    'PipelineEncoder': 'base',
    'HashEncoder': 'numeric.hash',
    'TorchvisionEncoder': 'image.torchvision',
    'TFInceptionEncoder': 'image.inception',
    'CVAEEncoder': 'image.cvae',
    'IncepMixtureEncoder': 'video.incep_mixture',
    'VladEncoder': 'numeric.vlad',
    'MfccEncoder': 'audio.mfcc',
    'PoolingEncoder': 'numeric.pooling',
    'PyTorchTransformers': 'text.transformer',
    'VggishEncoder': 'audio.vggish',
    'YouTube8MFeatureExtractor': 'video.yt8m_feature_extractor',
    'YouTube8MEncoder': 'video.yt8m_model',
    'InceptionVideoEncoder': 'video.inception',
    'QuantizerEncoder': 'numeric.quantizer',
    'CharEmbeddingEncoder': 'text.char'
}

register_all_class(_cls2file_map, 'encoder')
