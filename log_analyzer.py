#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json


# log_format ui_short '$remote_addr  $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';


def stdin_args():
    parser = argparse.ArgumentParser(description='Configuration file')
    parser.add_argument(
        '--config',
        default='./def_config.json',  # default configuration file
        type=str,
        help='Custom configuration file'
    )
    print(parser.parse_args().config)
    return parser.parse_args().config


def configuration_file_parse(configuration_file):
    default_config = {
        "REPORT_SIZE": 1000,
        "REPORT_DIR": "./reports",
        "LOG_DIR": "./log"
    }
    with open(configuration_file, 'r') as f:
        custom_config = json.load(f)
    config = {**default_config, **custom_config}
    return config




    pass


def get_recent_logs():
    pass


def logs_parse():
    pass


def report_generator():
    pass


def save_report():
    pass


def main():
    configuration_file = stdin_args()
    configuration = configuration_file_parse(configuration_file)
    recent_logs = get_recent_logs(configuration)
    logs_data = logs_parse(recent_logs)
    report = report_generator(logs_data)
    save_report(report, configuration)

    pass


if __name__ == "__main__":
    stdin_args()
