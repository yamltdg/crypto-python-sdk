# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云 - crypto-python-sdk
(BlueKing - crypto-python-sdk) available.
Copyright (C) 2017-2023 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import typing

from bkcrypto.utils import base_interceptors


class BaseAsymmetricInterceptor(base_interceptors.BaseInterceptor):
    @classmethod
    def before_sign(cls, plaintext: str, **kwargs) -> str:
        return plaintext

    @classmethod
    def after_sign(cls, signature: str, **kwargs) -> str:
        return signature

    @classmethod
    def before_verify(cls, plaintext: str, signature: str, **kwargs) -> typing.Tuple[str, str]:
        return plaintext, signature

    @classmethod
    def before_sign_b(cls, plaintext_bytes: bytes, **kwargs) -> bytes:
        return plaintext_bytes

    @classmethod
    def after_sign_b(cls, signature: bytes, **kwargs) -> bytes:
        return signature

    @classmethod
    def before_verify_b(cls, plaintext_bytes: bytes, signature_bytes: bytes, **kwargs) -> typing.Tuple[bytes, bytes]:
        return plaintext_bytes, signature_bytes
