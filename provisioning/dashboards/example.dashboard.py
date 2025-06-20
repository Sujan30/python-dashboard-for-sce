from grafanalib.core import (
    Dashboard,
    TimeSeries,
    Target,
    Stat,
    GridPos,
)
# see https://github.com/weaveworks/grafanalib/blob/main/grafanalib/formatunits.py
from grafanalib.formatunits import (
    SECONDS,
    NUMBER_FORMAT,
    BYTES,
    BITS_SEC,
)

PROMETHEUS_DATASOURCE_NAME = 'Prometheus'

dashboard = Dashboard(
    title='Example dashboard',
    uid='example',
    description='I made this with python!',
    timezone='browser',
    panels=[
        TimeSeries(
            title='CPU Usage',
            unit=NUMBER_FORMAT,
            gridPos=GridPos(h=8, w=12, x=0, y=0),
            lineWidth=2,
            targets=[
                Target(
                    datasource=PROMETHEUS_DATASOURCE_NAME,
                    expr='rate(process_cpu_seconds_total[1m])',
                    refId='A',
                ),
            ],
        ),
        TimeSeries(
            title='Network Bytes',
            unit=BYTES,
            gridPos=GridPos(h=8, w=12, x=12, y=0),
            lineWidth=2,
            targets=[
                Target(
                    datasource=PROMETHEUS_DATASOURCE_NAME,
                    expr='process_network_transmit_bytes_total',
                    refId='A',
                ),
                Target(
                    datasource=PROMETHEUS_DATASOURCE_NAME,
                    expr='process_network_receive_bytes_total',
                    refId='B',
                ),
            ],
        ),
        Stat(
            title='Uptime',
            format=SECONDS,
            gridPos=GridPos(h=8, w=12, x=0, y=8),
            targets=[
                Target(
                    datasource=PROMETHEUS_DATASOURCE_NAME,
                    expr='time() - process_start_time_seconds',
                    refId='A',
                ),
            ],
        ),
    ],
).auto_panel_ids()