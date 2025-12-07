#!/bin/bash

export AIRFLOW_HOME="/workspaces/hands-on-introduction-data-engineering-4395021/airflow"
echo "AIRFLOW_HOME is set to: $AIRFLOW_HOME"

# --- Stop API Server ---
WEBSERVER_PID=$(pgrep -f "api_server")
if [ -n "$WEBSERVER_PID" ]; then
    echo "Stopping Airflow API server (PID: $WEBSERVER_PID)"
    kill $WEBSERVER_PID
else
    echo "No Airflow API server is running"
fi

# --- Stop Scheduler ---
SCHEDULER_PID=$(pgrep -f "airflow scheduler")
if [ -n "$SCHEDULER_PID" ]; then
    echo "Stopping Airflow scheduler (PID: $SCHEDULER_PID)"
    kill $SCHEDULER_PID
else
    echo "No Airflow scheduler is running"
fi

# --- Stop Dag Processor ---
DAGPROC_PID=$(pgrep -f "airflow dag-processor")
if [ -n "$DAGPROC_PID" ]; then
    echo "Stopping Airflow DAG Processor (PID: $DAGPROC_PID)"
    kill $DAGPROC_PID
else
    echo "No Airflow dag-processor is running"
fi

echo "Airflow stopped."
