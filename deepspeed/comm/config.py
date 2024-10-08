# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

from deepspeed.runtime.config_utils import DeepSpeedConfigModel

from .constants import *


class CommsLoggerConfig(DeepSpeedConfigModel):
    enabled: bool = COMMS_LOGGER_ENABLED_DEFAULT
    prof_all: bool = COMMS_LOGGER_PROF_ALL_DEFAULT
    prof_ops: list = COMMS_LOGGER_PROF_OPS_DEFAULT
    verbose: bool = COMMS_LOGGER_VERBOSE_DEFAULT
    debug: bool = COMMS_LOGGER_DEBUG_DEFAULT


class DeepSpeedCommsConfig:

    def __init__(self, ds_config):
        self.comms_logger_enabled = 'comms_logger' in ds_config

        if self.comms_logger_enabled:
            self.comms_logger = CommsLoggerConfig(**ds_config['comms_logger'])
