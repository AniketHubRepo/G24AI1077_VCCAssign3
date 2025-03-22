#!/bin/bash
gcloud compute instance-groups managed set-target-pools web-auto-scale   --target-pools web-target-pool   --zone us-central1-a
