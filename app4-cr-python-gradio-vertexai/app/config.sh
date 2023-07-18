#!/bin/sh

project_id="gcp-experiments-349209"
region_name="us-central1-a" #us-central1 for now
artifact_repository_name="test321"

# Configure Docker
gcloud auth configure-docker ${region_name}-docker.pkg.dev

#Create Artifact Repository
gcloud artifacts repositories create ${artifact_repository_name} --location=${region_name} --repository-format=Docker

