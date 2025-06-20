FROM python:3.9.6-slim-buster AS builder

RUN pip install grafanalib

COPY ./provisioning/dashboards /dashboards

RUN generate-dashboards /dashboards/*.dashboard.py

# stage 2
FROM grafana/grafana:10.2.2

# Grafana configs
COPY ./grafana.ini /etc/grafana/grafana.ini

COPY ./provisioning/datasources/ /etc/grafana/provisioning/datasources/

# force regeneration of dashboards generated from python
RUN rm -rf /etc/grafana/provisioning/dashboards/*

COPY ./provisioning/dashboards/all.yml /etc/grafana/provisioning/dashboards/all.yml

COPY --from=builder /dashboards/*.json /etc/grafana/provisioning/dashboards/