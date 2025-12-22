## Music-Separation-as-a-Service (MSaaS)
It harnesses  source separation through Demucs to precisely isolate vocals and instruments from audio tracks. Building on techniques used by Spotify and Apple Music, it delivers enterprise-grade audio processing through a scalable, Kubernetes architecture. This enables streaming services, music production studios, and digital platforms to offer enhanced experiences like professional-quality karaoke, remixing tools, and interactive music features. By bringing advanced audio manipulation to the cloud, it equips businesses to meet rising demand for AI-driven audio innovation.

# Music Separation

This repository implements Music-Separation-as-a-Service (MSaaS), a Kubernetes-based system for waveform source separation. MSaaS provides a REST API for automatic music separation, enabling users to upload MP3 files, process them into separate tracks (vocals, bass, drums, etc.), and retrieve the results.

# Overview
The project leverages Kubernetes to deploy and manage a microservices architecture that includes:

- REST API service (rest): Handles API requests for music analysis and communicates with workers via a Redis queue.
- Worker service (worker): Processes MP3 files using Facebook's Demucs, a waveform source separation tool, and stores results in Min.io object storage.
- Redis service (redis): Provides a lightweight database for queuing work requests and logging messages.
- The system relies on Min.io for object storage to store uploaded MP3 files and output tracks.

# Architecture
The MSaaS system comprises the following components:

- Redis: Handles the queuing of tasks and logging via lpush/blpop operations.
- REST API (rest): Provides endpoints for uploading MP3 files, initiating music separation, and retrieving results.
- Worker: Executes the computationally expensive music separation tasks using Demucs.
- Min.io: Stores MP3 files and separated tracks in "queue" and "output" buckets.

# Prerequisites
Before starting, ensure you have the following:

- Kubernetes Cluster: You can use a local Kubernetes installation or a cloud provider like GKE. For local development, Minikube or Docker Desktop is recommended.
- Min.io: Set up Min.io locally or as a Kubernetes service using the Kubernetes tutorial instructions.
- Redis: Deployed via Kubernetes as a service.
- Docker: Installed locally to build and manage container images.
- Python 3.8+: For running test scripts and interacting with the REST API.

# Deployment
1. Clone Repository
- git clone https://github.com/Madhumitha-Somasundaram/Music-separation-as-a-service.git
- cd Music-separation-as-a-service

3. Set Up Min.io
Deploy Min.io locally or on Kubernetes by following the Min.io Kubernetes tutorial. Ensure Min.io is accessible and credentials are correctly configured.

4. Deploy Redis

4. Build and Push Docker Images

5. Deploy Services on Kubernetes

6. Port Forwarding (Optional for Local Development)


# Testing the System
1. REST API Endpoints
The REST API accepts requests for:

- Uploading MP3s
- Processing MP3s
- Retrieving separated tracks


2. Sample Data

3. Logs
Monitor logs using the logging service provided in the logs/ directory. Deploy the logs service on Kubernetes or run it locally to view debug messages from the Redis logging queue.

# Development Workflow
- Redis Deployment: Use deploy-local-dev.sh to deploy Redis with port-forwarding enabled.
- REST Server: Develop and test the REST API locally by connecting to Redis and Min.io via localhost.
- Worker Node: Test the worker service locally by connecting to the port-forwarded Redis queue and Min.io.
- Debugging: Use the logging pod to debug issues during development.


# Monitor Kubernetes resource usage with:
- kubectl describe node <node-name>  
- Use versioned Docker images for better deployment tracking.

