gcloud beta container --project "tali-multi-modal" clusters create "spot-gpu-cluster-1" --zone "us-central1-a" --no-enable-basic-auth --cluster-version "1.24.5-gke.600" --release-channel "regular" --machine-type "n2-highcpu-16" --image-type "UBUNTU_CONTAINERD" --disk-type "pd-balanced" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/cloud-platform" --max-pods-per-node "110" --spot --num-nodes "1" --logging=SYSTEM,WORKLOAD --monitoring=SYSTEM --enable-ip-alias --network "projects/tali-multi-modal/global/networks/default" --subnetwork "projects/tali-multi-modal/regions/us-central1/subnetworks/default" --enable-intra-node-visibility --default-max-pods-per-node "110" --enable-autoscaling --total-min-nodes "0" --total-max-nodes "1" --enable-dataplane-v2 --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing,NodeLocalDNS,GcePersistentDiskCsiDriver,GcpFilestoreCsiDriver --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --autoscaling-profile optimize-utilization --enable-shielded-nodes --node-locations "us-central1-a" && gcloud beta container --project "tali-multi-modal" node-pools create "gpu-a100-1g-pool" --cluster "spot-gpu-cluster-1" --zone "us-central1-a" --machine-type "a2-highgpu-1g" --accelerator "type=nvidia-tesla-a100,count=1" --image-type "UBUNTU_CONTAINERD" --disk-type "pd-balanced" --disk-size "300" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/cloud-platform" --spot --enable-autoscaling --total-min-nodes "0" --total-max-nodes "16" --enable-autoupgrade --enable-autorepair --max-surge-upgrade 16 --max-unavailable-upgrade 0 --max-pods-per-node "110" --node-locations "us-central1-a"
