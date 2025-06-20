from grafanalib.core import (
    Dashboard,
    TimeSeries,
    Target,
    Stat,
    GridPos,
    Threshold,
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
    title='My Second dashboard',
    uid='second',
    description='Hello everyone!!',
    timezone='browser',
    panels=[
        Stat(
            title='Uptime',
            reduceCalc='lastNotNull',
            format=SECONDS,
            gridPos=GridPos(h=8, w=12, x=0, y=0),
            thresholds=[
                Threshold('green', 0, 0.0),
            ],
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